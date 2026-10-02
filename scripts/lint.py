#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contrôle les en-têtes YAML des index.md — gabarit classement-documents 3.0.

    python3 scripts/lint.py [racine]

Sort en code 1 dès la première erreur bloquante, 0 s'il ne reste que des
avertissements. C'est ce script que la CI exécute à chaque push.

Ce qui est vérifié
------------------
  1. un en-tête YAML présent et analysable dans chaque index.md de dossier ;
  2. sa conformité au JSON Schema `97 - REFERENTIEL/schema-index.json` ;
  3. l'unicité des `id` et leur cohérence avec le chemin du dossier ;
  4. l'existence du `parent` déclaré ;
  5. l'unicité de chaque clé `documents[].type` dans tout le gabarit ;
  6. l'appartenance de chaque `champs` au catalogue `champs.yaml` ;
  7. la présence, dans `champs`, de tout variable utilisée par `nommage` ;
  8. l'existence du registre visé et la présence de sa clé dans `champs` ;
  9. l'existence du dossier visé par chaque `va-ailleurs[].vers` ;
 10. la concordance des `sort-final` avec `Tableau-de-gestion.csv` (avertissement) ;
 11. la cohérence `legale` <= `recommandee` (avertissement).
"""
import csv
import json
import os
import re
import sys


try:
    import yaml
except ImportError:
    sys.exit("PyYAML est requis : pip install pyyaml")

RACINE = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
REF = os.path.join(RACINE, "97 - REFERENTIEL")
TEMPS = {"date", "periode", "exercice"}

ERREURS, AVERTIS = [], []


def err(ou, msg):
    ERREURS.append("%s : %s" % (ou, msg))


def avert(ou, msg):
    AVERTIS.append("%s : %s" % (ou, msg))


# ---------------------------------------------------------------------------
# Lecture
# ---------------------------------------------------------------------------
SEP = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.S)


def entete(chemin):
    """Renvoie (dict, None) ou (None, message d'erreur)."""
    txt = open(chemin, encoding="utf-8").read()
    m = SEP.match(txt)
    if not m:
        return None, "pas d'en-tête YAML délimité par --- en tête de fichier"
    try:
        d = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        return None, "YAML illisible — %s" % str(e).replace("\n", " ")[:200]
    if not isinstance(d, dict):
        return None, "l'en-tête n'est pas un mapping"
    return d, None


def index_md():
    """Tous les index.md de dossier, hors index.md de la racine."""
    out = []
    for base, dirs, fichiers in os.walk(RACINE):
        dirs[:] = [d for d in dirs
                   if d not in (".git", ".github", "scripts", "referentiel")]
        if "index.md" in fichiers and os.path.abspath(base) != RACINE:
            out.append(os.path.join(base, "index.md"))
    return sorted(out)


# ---------------------------------------------------------------------------
# Référentiels
# ---------------------------------------------------------------------------
def charge_champs():
    p = os.path.join(REF, "champs.yaml")
    if not os.path.exists(p):
        err("97 - REFERENTIEL", "champs.yaml absent")
        return set()
    return set((yaml.safe_load(open(p, encoding="utf-8")) or {}).get("champs", {}))


def charge_schema():
    p = os.path.join(REF, "schema-index.json")
    if not os.path.exists(p):
        err("97 - REFERENTIEL", "schema-index.json absent")
        return None
    return json.load(open(p, encoding="utf-8"))


def charge_tableau():
    """Lignes du tableau de gestion portant une clé de type exploitable."""
    p = os.path.join(REF, "Tableau-de-gestion.csv")
    out = []
    if not os.path.exists(p):
        avert("97 - REFERENTIEL", "Tableau-de-gestion.csv absent, contrôle 10 ignoré")
        return out
    # utf-8-sig : les registres portent une BOM pour s'ouvrir dans Excel.
    with open(p, encoding="utf-8-sig") as f:
        lecteur = csv.DictReader(f, delimiter=";")
        if "Clé de type" not in (lecteur.fieldnames or []):
            err("97 - REFERENTIEL/Tableau-de-gestion.csv",
                "colonne « Clé de type » absente : la table n'est plus joignable "
                "aux en-têtes YAML")
            return out
        for r in lecteur:
            cle = (r.get("Clé de type") or "").strip()
            if not cle:                       # ligne décrivant un dossier d'affaire
                continue
            out.append({
                "dossier": (r.get("Dossier") or "").strip(),
                "typologie": (r.get("Typologie documentaire") or "").strip(),
                "sort": (r.get("Sort final (C/D/T)") or "").strip(),
                "dua": annees_texte(r.get("DUA (durée d'utilité administrative)")),
                "cle": cle,
            })
    return out


_AN = re.compile(r"^(\d{1,2})a$")
_AN_TXT = re.compile(r"^(\d{1,2})\s*an", re.I)


def annees(d):
    """« 10a » -> 10 ; « permanent », « aucune », None -> None."""
    m = _AN.match(d or "")
    return int(m.group(1)) if m else None


def annees_texte(d):
    """« 40 ans » -> 40."""
    m = _AN_TXT.match((d or "").strip())
    return int(m.group(1)) if m else None


# ---------------------------------------------------------------------------
# Contrôles
# ---------------------------------------------------------------------------
def main():
    CHAMPS = charge_champs()
    SCHEMA = charge_schema()
    TABLEAU = charge_tableau()

    fichiers = index_md()
    if not fichiers:
        err(".", "aucun index.md de dossier trouvé sous %s" % RACINE)

    valideur = None
    if SCHEMA:
        try:
            import jsonschema
            valideur = jsonschema.Draft202012Validator(SCHEMA)
        except ImportError:
            avert(".", "jsonschema absent, contrôle 2 ignoré "
                       "(pip install jsonschema)")
        except AttributeError:
            # Les versions antérieures à 4.0 ne connaissent pas le draft 2020-12.
            # C'est le cas du Python système de macOS : on continue sans ce
            # contrôle plutôt que de s'arrêter, les dix autres restent utiles.
            avert(".", "jsonschema %s est trop ancien pour le draft 2020-12, "
                       "contrôle 2 ignoré (pip install --upgrade 'jsonschema>=4')"
                  % getattr(jsonschema, "__version__", "?"))

    entetes, types = {}, {}

    for f in fichiers:
        rel = os.path.relpath(f, RACINE)
        d, pb = entete(f)
        if pb:
            err(rel, pb)
            continue

        # 2. schéma
        if valideur:
            for e in sorted(valideur.iter_errors(d), key=lambda x: list(x.path)):
                chemin = "/".join(str(x) for x in e.path) or "(racine)"
                err(rel, "schéma, %s — %s" % (chemin, e.message[:200]))

        ident = d.get("id")
        if not isinstance(ident, str):
            err(rel, "`id` absent ou non textuel (il doit être entre guillemets)")
            continue

        # 3. unicité et cohérence avec le chemin
        if ident in entetes:
            err(rel, "`id` %s déjà porté par %s" % (ident, entetes[ident]["_rel"]))
        prefixe = re.match(r"^(\d{2}(?:\.\d{1,2})?)", os.path.basename(os.path.dirname(f)))
        if prefixe and prefixe.group(1) != ident:
            err(rel, "`id` %s alors que le dossier s'appelle %s"
                % (ident, prefixe.group(1)))
        d["_rel"] = rel
        entetes[ident] = d

        for i, doc in enumerate(d.get("documents") or []):
            if not isinstance(doc, dict):
                continue
            t = doc.get("type")
            ou = "%s, documents[%d]" % (rel, i)

            # 5. unicité du type
            if t in types:
                err(ou, "type `%s` déjà déclaré dans %s" % (t, types[t]))
            else:
                types[t] = rel

            # 6. champs du catalogue
            ch = doc.get("champs") or []
            for c in ch:
                if CHAMPS and c not in CHAMPS:
                    err(ou, "champ `%s` absent de champs.yaml" % c)

            # 7. variables du nommage
            for v in re.findall(r"\{([a-z0-9-]+)\}", doc.get("nommage") or ""):
                if v not in ch and v not in TEMPS:
                    err(ou, "`nommage` utilise {%s}, qui n'est ni dans `champs` "
                            "ni une variable de temps" % v)

            # 8. registre
            r = doc.get("registre")
            if isinstance(r, dict):
                if r.get("fichier") not in registres(RACINE):
                    err(ou, "registre `%s` introuvable dans l'arborescence"
                        % r.get("fichier"))
                if r.get("cle") not in ch:
                    err(ou, "clé de registre `%s` absente de `champs`" % r.get("cle"))

            # 11. cohérence des durées
            c = doc.get("conservation") or {}
            a, b = annees(c.get("legale")), annees(c.get("recommandee"))
            if a is not None and b is not None and a > b:
                avert(ou, "minimum légal (%s) supérieur à la durée recommandée (%s)"
                      % (c["legale"], c["recommandee"]))

    # 4. parent, 9. va-ailleurs
    for ident, d in entetes.items():
        rel = d["_rel"]
        p = d.get("parent")
        if p and p not in entetes:
            err(rel, "`parent` %s ne correspond à aucun dossier" % p)
        if not p and d.get("niveau") == "sous-dossier":
            err(rel, "un sous-dossier doit déclarer un `parent`")
        for i, v in enumerate(d.get("va-ailleurs") or []):
            cible = v.get("vers")
            if cible and cible not in entetes:
                err("%s, va-ailleurs[%d]" % (rel, i),
                    "`vers` pointe sur %s, qui n'existe pas" % cible)

    # 10. concordance avec le tableau de gestion, par jointure exacte
    for L in TABLEAU:
        d = entetes.get(L["dossier"])
        ou = "97 - REFERENTIEL/Tableau-de-gestion.csv, « %s »" % L["typologie"]
        if not d:
            err(ou, "rattachée au dossier %s, qui n'existe pas" % L["dossier"])
            continue
        doc = next((x for x in (d.get("documents") or [])
                    if x.get("type") == L["cle"]), None)
        if doc is None:
            err(ou, "clé de type `%s` introuvable dans l'en-tête de %s"
                % (L["cle"], L["dossier"]))
            continue
        c = doc.get("conservation") or {}
        if c.get("sort-final") != L["sort"]:
            err(ou, "sort final %s, alors que `%s` déclare %s"
                % (L["sort"], L["cle"], c.get("sort-final")))
        dua, lg, rec = L["dua"], annees(c.get("legale")), annees(c.get("recommandee"))
        if dua is not None:
            if lg is not None and dua < lg:
                avert(ou, "DUA de %d ans inférieure au minimum légal de `%s` (%s)"
                      % (dua, L["cle"], c.get("legale")))
            if rec is not None and dua > rec:
                avert(ou, "DUA de %d ans supérieure à la durée recommandée de "
                          "`%s` (%s)" % (dua, L["cle"], c.get("recommandee")))

    # ---------------------------------------------------------------- bilan --
    for a in AVERTIS:
        print("avertissement  %s" % a)
    for e in ERREURS:
        print("ERREUR         %s" % e)
    print("\n%d dossiers, %d types documentaires, %d erreur(s), %d avertissement(s)"
          % (len(entetes), len(types), len(ERREURS), len(AVERTIS)))
    return 1 if ERREURS else 0


_REG = None


def registres(racine):
    """Noms de fichiers des registres CSV réellement présents."""
    global _REG
    if _REG is None:
        _REG = set()
        for base, dirs, fichiers in os.walk(racine):
            dirs[:] = [d for d in dirs if d not in (".git", ".github")]
            for f in fichiers:
                if f.lower().endswith(".csv"):
                    _REG.add(f)
    return _REG


if __name__ == "__main__":
    sys.exit(main())
