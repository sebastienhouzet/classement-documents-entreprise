# -*- coding: utf-8 -*-
"""Régénère la documentation à partir des index.md du gabarit.

Usage, depuis la racine du dossier :   python3 tools/gendoc.py .

À relancer après toute modification d'un index.md, ou après l'ajout d'un dossier
(déclarer alors sa destination dans tools/routage.py).

Sorties :
  documentation.html                        page utilisateur autonome
  97 - REFERENTIEL/AGENT-ROUTAGE.md         table compacte pour un agent d'ingestion
  97 - REFERENTIEL/routage.json             mêmes données, exploitables par du code
"""
import os, re, sys, json, html, unicodedata
from routage import R as ROUTAGE

SRC = sys.argv[1] if len(sys.argv) > 1 else "out"

# --------------------------------------------------------------- parsing ---
def parse(path):
    t = open(path, encoding="utf-8").read()
    d = {}
    d["titre"] = re.search(r"^# (.+)$", t, re.M).group(1).strip()
    m = re.search(r"^> Chemin : `(.+?)`", t, re.M)
    d["chemin"] = m.group(1) if m else ""

    def section(nom):
        m = re.search(rf"^## {re.escape(nom)}\n\n(.*?)(?=\n## |\n---\n)", t, re.S | re.M)
        return m.group(1).strip() if m else ""

    d["role"] = section("À quoi sert ce dossier")
    d["docs"] = [l[2:].strip() for l in section("Documents à y ranger").split("\n") if l.startswith("- ")]
    d["exclus"] = [l[2:].strip() for l in section("Ne pas ranger ici").split("\n") if l.startswith("- ")]
    d["classement"] = section("Méthode de classement")
    d["conseils"] = [l[2:].strip() for l in section("Conseils").split("\n") if l.startswith("- ")]
    cons = section("Durée de conservation")
    d["legal"] = (re.search(r"\| \*\*Minimum légal\*\* \| (.+?) \|", cons) or [None, ""])[1]
    d["reco"] = (re.search(r"\| \*\*Recommandé\*\* \| (.+?) \|", cons) or [None, ""])[1]
    d["base"] = (re.search(r"^Base : (.+)$", cons, re.M) or [None, ""])[1]
    return d

def code_de(chemin):
    """01 - JURIDIQUE.../01.3 - Assemblées  ->  01.3   ;   97 - REFERENTIEL -> 97"""
    parts = chemin.split("/")
    last = parts[-1]
    m = re.match(r"^(\d\d(?:\.\d+)?)", last)
    if m:
        return m.group(1)
    m = re.match(r"^(\d\d)", parts[0])          # Kit administratif
    return m.group(1) if m else ""

fiches = []
for d, _, fs in os.walk(SRC):
    if "index.md" not in fs:
        continue
    rel = os.path.relpath(d, SRC)
    if rel == ".":
        continue
    f = parse(os.path.join(d, "index.md"))
    f["rel"] = rel
    f["code"] = code_de(rel)
    f["domaine"] = rel.split("/")[0]
    f["niveau"] = 1 if "/" not in rel else 2
    fiches.append(f)

ORDRE = {"00": 0, "01": 1, "02": 2, "03": 3, "04": 4, "05": 5,
         "06": 6, "07": 7, "08": 8, "97": 97, "98": 98, "99": 99}
def tri(f):
    dom = re.match(r"^(\d\d)", f["domaine"]).group(1)
    sub = f["code"].split(".")
    return (ORDRE.get(dom, 50), f["niveau"], int(sub[1]) if len(sub) > 1 else 0, f["rel"])
fiches.sort(key=tri)

# ------------------------------------------------------------ markdown ---
def inline(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    s = s.replace("→", "<span class='ar'>→</span>")
    return s

def paras(s):
    return "".join(f"<p>{inline(p.strip())}</p>" for p in s.split("\n\n") if p.strip())

def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def cherchable(f):
    txt = " ".join([f["titre"], f["role"], " ".join(f["docs"]), " ".join(f["exclus"]),
                    f["classement"], ROUTAGE.get(f["code"], ("",))[0]])
    txt = unicodedata.normalize("NFKD", txt).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9 ]+", " ", txt)

# ------------------------------------------------------------------ CSS ---
CSS = """
/* Plan de classement : colonne de navigation fixe à gauche, fiches empilées à droite.
   La cote (04.3) est l'objet typographique central, en mono tabulaire. */
:root{
  --papier:#f6f8f6; --surface:#ffffff; --encre:#1a1f1d; --encre-2:#586460;
  --filet:#d7ded9; --filet-2:#eaefeb; --accent:#2f6b5c; --accent-doux:#e8f1ed;
  --garde:#8c3f2f; --garde-doux:#f7eae7; --ombre:0 1px 2px rgba(26,31,29,.05);
  --t-titre:'Archivo','Helvetica Neue',Arial,sans-serif;
  --t-texte:'Source Serif 4',Georgia,'Times New Roman',serif;
  --t-data:'IBM Plex Mono','SFMono-Regular',Consolas,monospace;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --papier:#121614; --surface:#1a201d; --encre:#e7ebe8; --encre-2:#9ca7a1;
  --filet:#2b332f; --filet-2:#232a27; --accent:#78bda9; --accent-doux:#1d2a26;
  --garde:#d98e7c; --garde-doux:#2a211f; --ombre:none; color-scheme:dark;
}}
:root[data-theme="dark"]{
  --papier:#121614; --surface:#1a201d; --encre:#e7ebe8; --encre-2:#9ca7a1;
  --filet:#2b332f; --filet-2:#232a27; --accent:#78bda9; --accent-doux:#1d2a26;
  --garde:#d98e7c; --garde-doux:#2a211f; --ombre:none; color-scheme:dark;
}
*{box-sizing:border-box}
body{background:var(--papier);color:var(--encre);font-family:var(--t-texte);
     font-size:15px;line-height:1.6;margin:0}
h1,h2,h3,h4{font-family:var(--t-titre);text-wrap:balance;margin:0}
code{font-family:var(--t-data);font-size:.86em;background:var(--filet-2);
     padding:.1em .34em;border-radius:3px;overflow-wrap:anywhere}
.ar{color:var(--accent);font-family:var(--t-data);padding:0 .15em}

.enveloppe{display:grid;grid-template-columns:260px minmax(0,1fr);gap:40px;
     max-width:1180px;margin:0 auto;padding:0 20px}

/* ---- bandeau ---- */
.bandeau{border-bottom:1px solid var(--filet);background:var(--surface)}
.bandeau .enveloppe{padding-block:28px 24px;gap:40px}
.marque{grid-column:1/-1;display:flex;flex-wrap:wrap;align-items:flex-end;
     justify-content:space-between;gap:16px 32px}
.marque h1{font-size:clamp(22px,3.4vw,31px);font-weight:620;letter-spacing:-.015em}
.marque p{margin:6px 0 0;color:var(--encre-2);max-width:62ch;font-size:14.5px}
.compteurs{display:flex;gap:26px;font-family:var(--t-data);font-size:12px;
     color:var(--encre-2);text-transform:uppercase;letter-spacing:.07em}
.compteurs b{display:block;font-family:var(--t-titre);font-size:25px;
     color:var(--accent);letter-spacing:-.02em;font-variant-numeric:tabular-nums}

/* ---- cycle de vie ---- */
.cycle{grid-column:1/-1;display:flex;flex-wrap:wrap;align-items:stretch;gap:8px;
     margin-top:26px;font-family:var(--t-data);font-size:11.5px}
.cycle div{flex:1 1 150px;min-width:0;border:1px solid var(--filet);
     border-radius:4px;padding:9px 11px;background:var(--papier)}
.cycle div b{display:block;font-family:var(--t-titre);font-size:13px;
     letter-spacing:.01em;margin-bottom:2px}
.cycle div span{color:var(--encre-2)}
.cycle .etape-sas{border-color:var(--accent);background:var(--accent-doux)}
.cycle .etape-fin{border-style:dashed}

/* ---- navigation ---- */
.plan{position:sticky;top:env(safe-area-inset-top,0px);align-self:start;
     max-height:100vh;overflow-y:auto;padding-block:28px 40px;font-size:13.5px}
.recherche{width:100%;font:inherit;font-family:var(--t-data);font-size:12.5px;
     padding:9px 11px;border:1px solid var(--filet);border-radius:5px;
     background:var(--surface);color:var(--encre);margin-bottom:18px}
.recherche:focus{outline:2px solid var(--accent);outline-offset:1px;border-color:var(--accent)}
.plan ol{list-style:none;margin:0;padding:0}
.plan .dom{margin-bottom:14px}
.plan .dom>a{display:block;font-family:var(--t-titre);font-weight:600;font-size:13px;
     text-transform:uppercase;letter-spacing:.05em;color:var(--encre);
     text-decoration:none;padding:3px 0}
.plan .dom>a:hover{color:var(--accent)}
.plan .dom ol a{display:flex;gap:8px;color:var(--encre-2);text-decoration:none;
     padding:2.5px 0 2.5px 2px;line-height:1.35}
.plan .dom ol a:hover{color:var(--accent)}
.plan .dom ol a i{font-family:var(--t-data);font-size:11.5px;font-style:normal;
     color:var(--accent);flex:0 0 32px;font-variant-numeric:tabular-nums}
.plan a.off{display:none}
.plan .dom.off{display:none}

/* ---- fiches ---- */
main{padding-block:34px 72px;min-width:0}
.rien{display:none;color:var(--encre-2);font-style:italic;padding:28px 0}
.rien.on{display:block}
.domaine{margin:0 0 10px;padding-top:22px}
.domaine h2{font-size:clamp(17px,2.4vw,20px);font-weight:620;letter-spacing:-.01em;
     padding-bottom:9px;border-bottom:2px solid var(--encre)}
.domaine.off,.fiche.off{display:none}

.fiche{background:var(--surface);border:1px solid var(--filet);border-radius:6px;
     padding:22px 24px;margin:16px 0;box-shadow:var(--ombre);scroll-margin-top:16px}
.fiche.est-domaine{background:var(--accent-doux);border-color:var(--accent)}
.tete{display:flex;align-items:baseline;gap:13px;flex-wrap:wrap;margin-bottom:11px}
.cote{font-family:var(--t-data);font-size:13px;font-weight:600;color:var(--accent);
     background:var(--papier);border:1px solid var(--filet);border-radius:4px;
     padding:3px 8px;font-variant-numeric:tabular-nums}
.fiche.est-domaine .cote{background:var(--surface)}
.tete h3{font-size:17.5px;font-weight:600;letter-spacing:-.01em;min-width:0}
.role p{margin:0 0 10px;max-width:68ch}
.role p:last-child{margin-bottom:0}

.colonnes{display:grid;grid-template-columns:repeat(auto-fit,minmax(265px,1fr));
     gap:18px 26px;margin-top:18px}
.bloc{min-width:0}
.bloc h4{font-family:var(--t-titre);font-size:10.5px;font-weight:700;
     text-transform:uppercase;letter-spacing:.1em;color:var(--encre-2);
     margin-bottom:7px;padding-bottom:5px;border-bottom:1px solid var(--filet-2)}
.bloc.garde h4{color:var(--garde);border-color:var(--garde)}
.bloc ul{margin:0;padding-left:17px}
.bloc li{margin-bottom:5px;font-size:14.2px}
.bloc li::marker{color:var(--filet)}
.bloc.garde li::marker{color:var(--garde)}

.rangee{display:grid;grid-template-columns:repeat(auto-fit,minmax(265px,1fr));
     gap:14px 26px;margin-top:18px;padding-top:16px;border-top:1px solid var(--filet-2)}
.donnee{min-width:0}
.donnee dt{font-family:var(--t-titre);font-size:10.5px;font-weight:700;
     text-transform:uppercase;letter-spacing:.1em;color:var(--encre-2);margin-bottom:4px}
.donnee dd{margin:0;font-size:14.2px}
.donnee dd.mono{font-family:var(--t-data);font-size:12.5px;line-height:1.55;
     overflow-wrap:anywhere}
.base{margin-top:14px;padding-top:12px;border-top:1px solid var(--filet-2);
     font-size:12.5px;color:var(--encre-2)}
.conseils{margin-top:16px;padding:14px 16px;background:var(--papier);
     border-left:2px solid var(--accent);border-radius:0 4px 4px 0}
.fiche.est-domaine .conseils{background:var(--surface)}
.conseils h4{font-family:var(--t-titre);font-size:10.5px;font-weight:700;
     text-transform:uppercase;letter-spacing:.1em;color:var(--accent);margin-bottom:7px}
.conseils ul{margin:0;padding-left:17px}
.conseils li{margin-bottom:6px;font-size:14.2px}
.conseils li:last-child{margin-bottom:0}

.pied{border-top:1px solid var(--filet);margin-top:40px;background:var(--surface)}
.pied .enveloppe{padding-block:26px 40px}
.pied p{grid-column:1/-1;margin:0 0 8px;font-size:13px;color:var(--encre-2);max-width:80ch}

@media (max-width:860px){
  .enveloppe{grid-template-columns:minmax(0,1fr);gap:0}
  .plan{position:static;max-height:none;overflow:visible;padding-block:20px 8px;
        border-bottom:1px solid var(--filet)}
  .plan ol.arbre{display:none}
  .plan.ouvert ol.arbre{display:block}
  .bascule{display:block;width:100%;font:inherit;font-family:var(--t-data);font-size:12px;
        padding:8px;background:none;border:1px dashed var(--filet);border-radius:5px;
        color:var(--encre-2);cursor:pointer}
  main{padding-block:22px 56px}
  .fiche{padding:18px 16px;border-radius:5px}
}
@media (min-width:861px){.bascule{display:none}}
@media (prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
"""

JS = """
(function(){
  var champ=document.getElementById('q'), fiches=[].slice.call(document.querySelectorAll('.fiche')),
      liens=[].slice.call(document.querySelectorAll('.plan .dom ol a')),
      groupes=[].slice.call(document.querySelectorAll('.plan .dom')),
      titres=[].slice.call(document.querySelectorAll('.domaine')),
      rien=document.getElementById('rien'), bascule=document.querySelector('.bascule'),
      plan=document.querySelector('.plan');
  function sansAccent(s){return s.normalize('NFKD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase();}
  function filtrer(){
    var q=sansAccent(champ.value.trim()), mots=q?q.split(/\\s+/):[], n=0, vus={};
    fiches.forEach(function(el){
      var t=el.dataset.k, ok=mots.every(function(m){return t.indexOf(m)>-1;});
      el.classList.toggle('off',!ok);
      if(ok){n++;vus[el.dataset.dom]=1;}
    });
    titres.forEach(function(el){el.classList.toggle('off',!vus[el.dataset.dom]);});
    liens.forEach(function(a){
      var c=document.getElementById(a.getAttribute('href').slice(1));
      a.classList.toggle('off', !c || c.classList.contains('off'));
    });
    groupes.forEach(function(g){
      g.classList.toggle('off', mots.length>0 && !g.querySelectorAll('ol a:not(.off)').length);
    });
    rien.classList.toggle('on', n===0);
  }
  champ.addEventListener('input',filtrer);
  champ.addEventListener('keydown',function(e){if(e.key==='Escape'){champ.value='';filtrer();}});
  if(bascule){bascule.addEventListener('click',function(){
    var o=plan.classList.toggle('ouvert');
    bascule.setAttribute('aria-expanded',o?'true':'false');
    bascule.textContent=(o?'▴':'▾')+'  Plan de classement';
  });}
})();
"""

# ----------------------------------------------------------------- HTML ---
def fiche_html(f):
    rt = ROUTAGE.get(f["code"])
    parts = [f'<article class="fiche{" est-domaine" if f["niveau"]==1 else ""}'
             f'" id="{slug(f["rel"])}" data-dom="{html.escape(f["domaine"])}" '
             f'data-k="{html.escape(cherchable(f))}">']
    parts.append('<div class="tete">'
                 f'<span class="cote">{html.escape(f["code"] or "—")}</span>'
                 f'<h3>{inline(re.sub(r"^[0-9.]+ - ", "", f["titre"]))}</h3></div>')
    parts.append(f'<div class="role">{paras(f["role"])}</div>')

    cols = []
    if f["docs"]:
        cols.append('<div class="bloc"><h4>Documents à y ranger</h4><ul>'
                    + "".join(f"<li>{inline(x)}</li>" for x in f["docs"]) + "</ul></div>")
    if f["exclus"]:
        cols.append('<div class="bloc garde"><h4>Ne pas ranger ici</h4><ul>'
                    + "".join(f"<li>{inline(x)}</li>" for x in f["exclus"]) + "</ul></div>")
    if cols:
        parts.append('<div class="colonnes">' + "".join(cols) + "</div>")

    rang = ['<div class="donnee"><dt>Méthode de classement</dt><dd>'
            + paras(f["classement"]) + "</dd></div>"]
    rang.append('<div class="donnee"><dt>Conservation</dt>'
                f'<dd><strong>Minimum légal.</strong> {inline(f["legal"])}<br>'
                f'<strong>Recommandé.</strong> {inline(f["reco"])}</dd></div>')
    if rt:
        rang.append('<div class="donnee"><dt>Repères de tri</dt>'
                    f'<dd class="mono">{inline(rt[1])}</dd></div>')
    parts.append('<dl class="rangee">' + "".join(rang) + "</dl>")

    if f["base"]:
        parts.append(f'<p class="base">Base : {inline(f["base"])}</p>')
    if f["conseils"]:
        parts.append('<div class="conseils"><h4>À savoir</h4><ul>'
                     + "".join(f"<li>{inline(x)}</li>" for x in f["conseils"]) + "</ul></div>")
    parts.append("</article>")
    return "".join(parts)

def corps():
    n_dom = sum(1 for f in fiches if f["niveau"] == 1)
    n_sous = sum(1 for f in fiches if f["niveau"] == 2)

    nav = []
    for d in [f for f in fiches if f["niveau"] == 1]:
        enfants = [f for f in fiches if f["niveau"] == 2 and f["domaine"] == d["domaine"]]
        nav.append(f'<li class="dom"><a href="#{slug(d["rel"])}">'
                   f'{html.escape(re.sub(r"^[0-9]+ - ", lambda m: m.group(0), d["domaine"]))}</a>')
        if enfants:
            nav.append("<ol>" + "".join(
                f'<li><a href="#{slug(e["rel"])}"><i>{html.escape(e["code"])}</i>'
                f'<span>{html.escape(re.sub(r"^[0-9.]+ - ", "", e["titre"]))}</span></a></li>'
                for e in enfants) + "</ol>")
        nav.append("</li>")

    corps_fiches = []
    dom_courant = None
    for f in fiches:
        if f["domaine"] != dom_courant:
            dom_courant = f["domaine"]
            corps_fiches.append(f'<div class="domaine" data-dom="{html.escape(dom_courant)}">'
                                f'<h2>{html.escape(dom_courant)}</h2></div>')
        corps_fiches.append(fiche_html(f))

    return f"""<header class="bandeau"><div class="enveloppe"><div class="marque">
<div><h1>Plan de classement des documents de gestion</h1>
<p>Où ranger chaque document d'une entreprise française, comment le nommer, et combien de temps
le conserver. Une fiche par dossier, reprise des fichiers <code>index.md</code> du gabarit.</p></div>
<div class="compteurs">
<span><b>{n_dom}</b>dossiers de tête</span>
<span><b>{n_sous}</b>sous-dossiers</span>
</div></div>
<div class="cycle">
<div class="etape-sas"><b>00 — Inbox</b><span>Tout document reçu entre ici. Zéro document de plus de 30 jours.</span></div>
<div><b>01 à 08 — Domaines</b><span>Le document est nommé, rangé, et son échéance reportée dans un registre.</span></div>
<div><b>98 — Archives</b><span>Le dossier est clos : il attend sa date de destruction.</span></div>
<div class="etape-fin"><b>99 — Suppression</b><span>Un lot est proposé, une autre personne valide, puis on détruit.</span></div>
</div></div></header>

<div class="enveloppe">
<nav class="plan" aria-label="Plan de classement">
<label for="q" class="sr">Rechercher</label>
<input id="q" class="recherche" type="search" placeholder="Rechercher : facture, DUERP, bail…"
       autocomplete="off" spellcheck="false">
<button class="bascule" type="button" aria-expanded="false">▾  Plan de classement</button>
<ol class="arbre">{''.join(nav)}</ol>
</nav>
<main>
<p class="rien" id="rien">Aucun dossier ne correspond. Essayez un terme plus court,
ou le type de document : « facture », « contrat », « salarié ».</p>
{''.join(corps_fiches)}
</main></div>

<footer class="pied"><div class="enveloppe">
<p>Cette page est générée depuis les fichiers <code>index.md</code> du gabarit : elle ne peut pas
divulguer d'information qui ne s'y trouve pas, et elle se régénère après chaque modification.</p>
<p>Les durées de conservation correspondent aux textes en vigueur en septembre 2026 et sont
indicatives. Le fichier <code>97 - REFERENTIEL/AGENT-ROUTAGE.md</code> contient la même information
sous une forme compacte, destinée à un agent d'ingestion automatique.</p>
</div></footer>"""

TITRE = "Plan de classement des documents de gestion"
POLICES = ('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
           '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
           'family=Archivo:wght@500;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400'
           '&family=IBM+Plex+Mono:wght@400;600&display=swap">')
SR = ".sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}"

def ecrire(chemin, contenu):
    os.makedirs(os.path.dirname(chemin), exist_ok=True) if os.path.dirname(chemin) else None
    open(chemin, "w", encoding="utf-8").write(contenu)

B = corps()
ecrire(os.path.join(SRC, "documentation.html"),
       f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{TITRE}</title>{POLICES}
<style>html{{color-scheme:light}}img{{max-width:100%}}[hidden]{{display:none!important}}
{CSS}{SR}</style></head><body>{B}<script>{JS}</script></body></html>""")

# -------------------------------------------------- pack pour un agent ---
AIGUILLAGE = [
 ("00", "Document non identifié, illisible, ou scan multi-documents. Destination de repli."),
 ("01", "Existence légale et gouvernance : statuts, assemblées, registres, dirigeants, associés, propriété intellectuelle, conformité, contentieux."),
 ("02", "Engagements contractuels, hors travail, banque et assurance : clients, fournisseurs, sous-traitance, baux, abonnements, NDA."),
 ("03", "Les personnes qui travaillent pour l'entreprise : registres, dossiers individuels, paie, organismes sociaux, recrutement, formation, absences, santé-sécurité, CSE."),
 ("04", "Ce qui justifie une écriture comptable ou une déclaration : exercices, factures, notes de frais, immobilisations, impôts, facturation électronique."),
 ("05", "L'argent qui ENTRE : comptes bancaires, emprunts, aides, investisseurs, moyens de paiement, garanties."),
 ("06", "Assurances et sinistres, y compris la décennale et les garanties de construction."),
 ("07", "Administrations, courrier, locaux, véhicules, certifications, matériel, marchés publics."),
 ("08", "L'argent qui est PLACÉ : comptes à terme, titres, capitalisation, crypto-actifs, immobilier de placement, fonds, participations."),
 ("97", "Référentiel et kit administratif : copies à jour des attestations courantes. Ne contient pas d'original."),
 ("98", "Dossiers clos dont la durée de conservation court encore."),
 ("99", "Lots proposés à la suppression, en attente de validation."),
]

NOM_DOM = {re.match(r"^(\d\d)", f["domaine"]).group(1): f["domaine"]
           for f in fiches if f["niveau"] == 1}

_vus = set()
def ligne(f):
    rt = ROUTAGE.get(f["code"])
    if not rt:
        return None
    if f["niveau"] == 1 and f["code"] not in ("00", "98", "99"):
        return None          # 97 : c'est « Kit administratif » qui est la destination
    if f["code"] in _vus:
        return None
    _vus.add(f["code"])
    cles, motif, cons, reg, arb = rt
    nom = re.sub(r"^[0-9.]+ - ", "", f["titre"])
    return f"{f['code']}|{nom}|{cles}|{motif}|{cons}|{reg or '-'}|{arb or '-'}"

blocs, lignes = [], []
for dom_code in sorted(NOM_DOM, key=lambda c: ORDRE.get(c, 50)):
    dedans = [l for l in (ligne(f) for f in fiches
              if re.match(r"^(\d\d)", f["domaine"]).group(1) == dom_code) if l]
    if not dedans:
        continue
    lignes += dedans
    blocs.append(f"### {NOM_DOM[dom_code]}\n\n```\n" + "\n".join(dedans) + "\n```")

AGENT = f"""# Routage d'un document entrant — référence pour agent

Table de décision pour un agent qui doit classer un document dans ce plan de classement :
{len(lignes)} destinations, leurs déclencheurs et leurs arbitrages.

**Deux façons de l'utiliser.** Soit charger ce fichier en entier, une fois, en préfixe stable du
prompt — c'est le plus simple et le cache de prompt absorbe le coût après le premier appel. Soit
procéder en deux temps : ne charger que les sections « Procédure », « Aiguillage » et « Sortie
attendue », puis, le domaine choisi, ne charger que le bloc de ce domaine dans la section « Table ».
Le second mode divise le coût par environ six, au prix d'un aller-retour.

Ne lire le `index.md` d'un dossier que si la table ne suffit pas à trancher. C'est l'exception.

## Procédure

1. **Identifier le type de document**, pas son sujet. Une facture d'avocat est une facture (`04.3`),
   pas un document juridique. Un relevé de compte à terme est un placement (`08.2`), pas un document
   bancaire courant.
2. **Aiguiller vers un domaine** avec la table d'aiguillage ci-dessous.
3. **Chercher les déclencheurs** dans la colonne `cles` des destinations de ce domaine.
4. **Appliquer les arbitrages** de la colonne `arb` quand plusieurs destinations matchent. Ils sont
   écrits pour trancher exactement ces cas. La section « Pièges » couvre les confusions coûteuses.
5. **Construire le chemin** : `<dossier de tête>/<code> - <nom>/` + le motif de la colonne `chemin`,
   en remplaçant les variables par ce que dit le document (tiers, année, mois, objet).
   **Si une variable du motif est absente du document**, écrire `_INCONNU` à sa place, plafonner la
   confiance à 0,65 et router en `00` avec le motif `variable de chemin manquante : <nom>`. Ne jamais
   inventer un nom de tiers, de banque ou d'assureur qui n'est pas écrit sur le document : c'est
   ainsi qu'un même assureur finit sous trois orthographes.
6. **Nommer le fichier** : `AAAA-MM-JJ_Type_Tiers_Objet.ext`, quatre segments, pas d'accent ni de
   caractère spécial, pas de point hors extension. Suffixes utiles : `_signe`, `_copie`, `_projet`.
   **Si le document ne porte pas de date propre**, utiliser la date de l'événement qu'il atteste
   (réception, période couverte, début de validité) ; à défaut seulement, la date de réception
   préfixée `r` (`r2026-10-02_...`). La date du scan n'est jamais la date du document, sauf en `00`
   où elle est la seule disponible.
7. **Si la confiance est inférieure à 0,7, router vers `00`** avec le motif du doute. Un document mal
   classé coûte plus cher qu'un document resté dans le sas.

### Barème de confiance

| Valeur | Situation |
|---|---|
| 0,95 | Déclencheur littéral, une seule destination possible, toutes les variables du chemin lues |
| 0,85 | Déclencheur littéral et un arbitrage écrit qui tranche |
| 0,70 | Déclencheur reconnu par synonyme, ou type certain mais une variable de chemin manquante |
| < 0,70 | Deux destinations plausibles sans arbitrage écrit, ou type de document non reconnu |

## Règles invariantes

- Un document n'a qu'**une seule place**. S'il est utile ailleurs, l'original va à sa place et une
  copie suffixée `_copie` va dans l'autre dossier.
- Un fichier = un document. Un scan qui contient plusieurs documents distincts va en `00`, à
  découper avant classement.
- Les sous-dossiers par tiers, par année ou par opération se **créent à la demande** : si le
  sous-dossier cible n'existe pas, le créer selon le motif.
- **Un avenant, une résiliation, un renouvellement, une mainlevée ou un ordre de mouvement va dans
  le dossier du document qu'il modifie**, jamais dans un dossier à lui.
- **Une attestation, une pièce de vigilance ou un certificat fourni par un tiers va dans le dossier
  de ce tiers**, à la destination où son contrat est classé. Nos propres attestations suivent la
  règle inverse : l'original dans son domaine, une copie à jour dans `97`.
- La colonne `reg` dit quel registre *peut* être concerné ; ne le renseigner que si le document
  **crée ou modifie un engagement** (contrat, avenant, souscription, résiliation, garantie). Une
  simple attestation ou un relevé ne crée rien. Les registres existants : `contrats`, `assurances`,
  `immobilisations`, `matériel`, `placements`, `recommandés` (global : tout envoi ou réception
  recommandé y est inscrit, quel que soit le dossier de classement), `archives`, `tableau de
  gestion`.
- Dans la colonne `chemin`, `|` sépare des sous-dossiers frères entre lesquels il faut choisir, et
  `<...>` marque une variable à lire dans le document. Pour `00` : `A classer` = type reconnu mais
  destination indécidable, `A traiter` = incomplet ou en attente d'une information, `Scans bruts` =
  à découper ou illisible.
- La règle « pas d'accent ni de caractère spécial » vise les **noms de fichiers**. Les noms de
  dossiers de niveau 1 et 2 sont fixes et gardent leurs accents ; les sous-dossiers créés à la
  demande suivent le motif tel qu'il est écrit.
- **Jamais dans l'arborescence** : mot de passe, clé privée, phrase de récupération, code
  d'authentification. Ni dans `08.5`, ni ailleurs. Un document qui en contient va en `00` avec
  l'alerte.

## Aiguillage

```
{chr(10).join(f"{c}|{d}" for c, d in AIGUILLAGE)}
```

## Table

Colonnes : `code|nom|cles|chemin|cons|reg|arb`

`chemin` = motif du sous-chemin sous le dossier · `cons` = conservation (a = années, j = jours) ·
`reg` = registre à mettre à jour, `-` si aucun · `arb` = arbitrages, `-` si aucun

{chr(10).join(chr(10).join([b, ""]) for b in blocs)}
## Pièges fréquents

- **Facture ou contrat ?** Le contrat va en `02`, la facture qu'il génère en `04.2` ou `04.3`. Les
  deux existent presque toujours pour le même tiers.
- **Facture ou note de frais ?** Au nom de l'entreprise → `04.3`. Avancée par une personne et
  remboursée → `04.4`.
- **Mon capital ou celui des autres ?** Pacte d'associés et BSPCE de votre société → `01.6`. Titres
  détenus dans une autre société → `08.8`.
- **Argent qui entre ou argent placé ?** Compte courant, emprunt, subvention, levée de fonds → `05`.
  Compte à terme, titres, crypto, SCPI, participation → `08`.
- **Local occupé ou immeuble de placement ?** Bail des bureaux → `02.4`. SCPI et immeuble de
  rapport → `08.6`.
- **Immobilisation corporelle ou financière ?** Matériel et véhicules → `04.5`. Titres et
  participations → `08`.
- **Bulletin de paie ou dossier salarié ?** Les bulletins sont classés par mois pour toute
  l'entreprise en `03.3`, jamais dans le dossier individuel `03.2`.
- **Assurance : contrat ou sinistre ?** Le contrat et ses attestations dans son dossier `06.x`. La
  déclaration et l'expertise en `06.7`, quel que soit le contrat concerné.
- **Courrier recommandé.** S'il concerne un dossier existant, il va dans ce dossier. `07.2` ne
  reçoit que le courrier général et le registre des recommandés.
- **Attestation en cours de validité.** L'original va dans son domaine (`03.4` pour l'URSSAF, `06.1`
  pour la RC Pro) ; une copie va dans `97`, qui ne garde que la version du moment.
- **Avis d'opéré de titres.** Conservé tant que la ligne est détenue : c'est lui qui porte le prix de
  revient. Ne jamais le proposer à la suppression.
- **Document dont la durée est écoulée.** Il ne part pas directement en `99` : il passe par `98`
  quand son dossier est clos, puis `99` propose le lot à validation.

## Sortie attendue

Cas simple, une facture reçue :

```json
{{
  "dossier": "04.3",
  "chemin": "04 - COMPTABILITE & FISCALITE/04.3 - Factures fournisseurs/2026/2026-03",
  "nom_fichier": "2026-03-04_Facture_Hebergeur-Alpha_Hebergement-mars-2026.pdf",
  "confiance": 0.95,
  "motif": "mentions TVA et numero de facture, emetteur tiers, a notre nom",
  "conservation": "10a",
  "registre": null,
  "echeances": [],
  "copies": [],
  "actions": []
}}
```

Cas avec copie obligatoire, une attestation que nous recevons de notre assureur :

```json
{{
  "dossier": "06.1",
  "chemin": "06 - ASSURANCES/06.1 - Responsabilite civile professionnelle/<Assureur> - <N contrat>",
  "nom_fichier": "2026-01-15_Attestation_Assureur-Alpha_RC-Pro-2026.pdf",
  "confiance": 0.70,
  "motif": "attestation RC Pro ; assureur et numero de contrat absents du document",
  "conservation": "10a apres fin",
  "registre": null,
  "echeances": [{{"type": "validite", "date": "2026-12-31"}}],
  "copies": [{{"dossier": "97", "chemin": "97 - REFERENTIEL/Kit administratif"}}],
  "actions": ["variable de chemin manquante"]
}}
```

Cas de repli, un scan multi-documents :

```json
{{
  "dossier": "00",
  "chemin": "00 - INBOX/Scans bruts",
  "nom_fichier": "r2026-10-02_Scan_Interne_38-pages-a-decouper.pdf",
  "confiance": 0.98,
  "motif": "contient une facture, deux releves bancaires et un courrier : un fichier = un document",
  "conservation": "sas, 30j max",
  "registre": null,
  "echeances": [],
  "copies": [],
  "actions": ["a_decouper"]
}}
```

`conservation` reprend la valeur de la colonne `cons`, ou celle qu'un arbitrage impose en exception.
`registre` ne porte un nom que si le document crée ou modifie un engagement, sinon `null`.
`echeances` est une liste, car un même document peut en porter plusieurs ; `type` est pris dans
`contrat`, `preavis`, `placement`, `validite`, `paiement`, `garantie`, `retention`, `purge`.
`copies` liste les destinations où une copie suffixée `_copie` doit être déposée.
`actions` est prise dans `a_decouper`, `a_renommer`, `variable de chemin manquante`,
`alerte_secret` (le document contient un mot de passe ou une clé : ne pas le classer).
"""
def _est(x):
    """Estimation du nombre de tokens pour du français dense (±10 %)."""
    mots = len(re.findall(r"[A-Za-zÀ-ÿ]+", x))
    chiffres = len(re.findall(r"\d+", x))
    ponct = len(re.findall(r"[^\w\s]", x))
    return int(mots * 1.45 + chiffres * 1.2 + ponct * 0.9)

_tbl = AGENT[AGENT.index("## Table"):AGENT.index("## Pièges")]
_noyau = _est(AGENT) - _est(_tbl)
_bloc_max = max(_est(b) for b in blocs)
COUT = f"""
## Coût en tokens

Mesuré sur ce fichier, estimation à 10 % près.

| Ce qu'on charge | Tokens |
|---|---|
| Le fichier entier | ~{_est(AGENT)} |
| Tout sauf la table (procédure, règles, aiguillage, pièges, sortie) | ~{_noyau} |
| La table entière | ~{_est(_tbl)} |
| Le plus gros bloc de domaine | ~{_bloc_max} |
| **Mode deux temps : tout sauf la table, puis un bloc** | **~{_noyau + _bloc_max} au pire** |

En préfixe stable d'un prompt, le fichier entier est mis en cache : le coût réel après le premier
appel tombe à une fraction de ces chiffres. Le mode deux temps n'a d'intérêt que sans cache, ou
quand le document à classer est lui-même très volumineux.
"""
AGENT = AGENT.replace("\n## Sortie attendue", COUT + "\n## Sortie attendue")

ecrire(os.path.join(SRC, "97 - REFERENTIEL", "AGENT-ROUTAGE.md"), AGENT)

J = {"version": "2.2.0", "convention_nom": "AAAA-MM-JJ_Type_Tiers_Objet.ext",
     "repli": "00", "seuil_confiance": 0.7, "destinations": []}
for f in fiches:
    rt = ROUTAGE.get(f["code"])
    if not rt or (f["niveau"] == 1 and f["code"] not in ("00", "97", "98", "99")):
        continue
    J["destinations"].append({
        "code": f["code"],
        "nom": re.sub(r"^[0-9.]+ - ", "", f["titre"]),
        "chemin_dossier": f["rel"],
        "cles": [c.strip() for c in rt[0].split(",")],
        "motif_sous_chemin": rt[1],
        "conservation": rt[2],
        "registre": rt[3] or None,
        "arbitrages": rt[4] if rt[4] != "-" else None,
    })
ecrire(os.path.join(SRC, "97 - REFERENTIEL", "routage.json"),
       json.dumps(J, ensure_ascii=False, indent=1))

ko = [f["code"] for f in fiches if f["niveau"] == 2 and f["code"] not in ROUTAGE]
print(f"{len(fiches)} fiches · {len(lignes)} destinations de routage")
print(f"documentation.html : {os.path.getsize(os.path.join(SRC,'documentation.html'))//1024} Ko")
print(f"AGENT-ROUTAGE.md   : {len(AGENT)} caractères")
if ko:
    print("SANS MÉTADONNÉES DE ROUTAGE :", ko)
