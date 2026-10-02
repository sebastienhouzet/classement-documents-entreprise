#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ajoute l'en-tête YAML 3.0 aux index.md d'une copie personnalisée du gabarit.

    python3 scripts/migrer-frontmatter.py <votre-arborescence> [options]

À quoi ça sert
--------------
Les index.md du dépôt sont produits par le générateur : ils portent déjà leur
en-tête. Ce script est pour celles et ceux qui ont **repris le gabarit et
réécrit les corps Markdown** : il pose l'en-tête normalisé au-dessus de chaque
index.md sans toucher une ligne du corps.

L'en-tête est pris dans `referentiel/dossiers.json` de cette version du dépôt
(produit par `scripts/compiler.py`), et apparié par l'identifiant lu en tête du
nom de dossier : « 04.9 - Ma facturation à moi » reçoit l'en-tête de 04.9.

Options
-------
    --reference <fichier>  autre dossiers.json que celui du dépôt
    --ecrire               applique les modifications (sans cette option, le
                           script n'affiche que ce qu'il ferait)
    --remplacer            remplace un en-tête 3.x déjà présent
                           (par défaut, un index.md déjà migré est laissé seul)

Le corps Markdown n'est jamais réécrit. Les fichiers sont sauvegardés en
`index.md.avant-3.0` avant toute écriture.
"""
import json
import os
import re
import shutil
import sys

SEP = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.S)
ID = re.compile(r"^(\d{2}(?:\.\d{1,2})?)\b")
ORDRE = ["schema", "id", "parent", "niveau", "titre", "usage",
         "classement", "sensibilite", "documents", "va-ailleurs"]


# ---------------------------------------------------------------------------
# Écriture YAML : même rendu que le générateur, pour que les diffs restent nuls
# ---------------------------------------------------------------------------
_SIMPLE = re.compile(r"^[A-Za-zÀ-ÿ0-9][^:#\n\"'{}\[\],&*?|<>=!%@`]*$")
_AMBIGU = re.compile(r"""^(
      [-+]?[0-9][0-9_]*(\.[0-9]*)?([eE][-+]?[0-9]+)?
    | [-+]?\.[0-9]+
    | 0[xXbBoO][0-9a-fA-F_]+
    | (?i:true|false|yes|no|on|off|null|~)
    | [0-9]{4}-[0-9]{2}-[0-9]{2}.*
)$""", re.X)


def sc(v):
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v)
    if s == "":
        return '""'
    if _SIMPLE.match(s) and not s.endswith(" ") and ": " not in s \
            and not _AMBIGU.match(s):
        return s
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def pli(texte, indent="  ", largeur=96):
    mots, lignes, cur = texte.split(), [], ""
    for m in mots:
        if cur and len(indent) + len(cur) + 1 + len(m) > largeur:
            lignes.append(indent + cur)
            cur = m
        else:
            cur = (cur + " " + m).strip()
    if cur:
        lignes.append(indent + cur)
    return lignes


def rend(d):
    L = ["---", "schema: %s" % d["schema"], "id: %s" % sc(d["id"]),
         "parent: %s" % sc(d.get("parent")), "niveau: %s" % d["niveau"],
         "titre: %s" % sc(d["titre"]), "usage: >-"]
    L += pli(d["usage"])
    L += ["classement: %s" % d["classement"], "sensibilite: %s" % d["sensibilite"]]
    docs = d.get("documents") or []
    if not docs:
        L.append("documents: []")
    else:
        L.append("documents:")
        for x in docs:
            L.append("  - type: %s" % sc(x["type"]))
            L.append("    libelle: %s" % sc(x["libelle"]))
            if x.get("description"):
                L.append("    description: %s" % sc(x["description"]))
            if x.get("indices"):
                L.append("    indices: [%s]" % ", ".join(sc(i) for i in x["indices"]))
            L.append("    champs: [%s]" % ", ".join(sc(c) for c in x["champs"]))
            L.append("    nommage: %s" % sc(x["nommage"]))
            L.append("    conservation:")
            c = x["conservation"]
            for k in ("legale", "recommandee", "declencheur", "base", "sort-final"):
                if c.get(k) is not None:
                    L.append("      %s: %s" % (k, sc(c[k])))
            r = x.get("registre")
            L.append("    registre: " + ("{ fichier: %s, cle: %s }"
                                         % (sc(r["fichier"]), sc(r["cle"]))
                                         if r else "null"))
    if d.get("va-ailleurs"):
        L.append("va-ailleurs:")
        for v in d["va-ailleurs"]:
            L.append("  - motif: %s" % sc(v["motif"]))
            L.append("    vers: %s" % sc(v.get("vers")))
    L.append("---")
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------------------
def main():
    a = sys.argv[1:]
    if not a or a[0].startswith("-"):
        sys.exit(__doc__)
    cible = os.path.abspath(a[0])
    ecrire = "--ecrire" in a
    remplacer = "--remplacer" in a
    ref = (a[a.index("--reference") + 1] if "--reference" in a
           else os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.pardir, "referentiel", "dossiers.json"))
    if not os.path.exists(ref):
        sys.exit("référence introuvable : %s\nLancez d'abord scripts/compiler.py."
                 % ref)
    par_id = {d["id"]: d for d in json.load(open(ref, encoding="utf-8"))["dossiers"]}

    poses, remplaces, intacts, orphelins = [], [], [], []
    for base, dirs, fichiers in os.walk(cible):
        dirs[:] = [d for d in dirs
                   if d not in (".git", ".github", "scripts", "referentiel")]
        if "index.md" not in fichiers or os.path.abspath(base) == cible:
            continue
        chemin = os.path.join(base, "index.md")
        rel = os.path.relpath(chemin, cible)
        m = ID.match(os.path.basename(base))
        ident = m.group(1) if m else ("97.1" if os.path.basename(base).lower()
                                      .startswith("kit administratif") else None)
        if ident is None or ident not in par_id:
            orphelins.append(rel)
            continue

        txt = open(chemin, encoding="utf-8").read()
        deja = SEP.match(txt)
        if deja and not remplacer:
            intacts.append(rel)
            continue
        corps = txt[deja.end():] if deja else txt
        neuf = rend(par_id[ident]) + "\n" + corps.lstrip("\n")
        (remplaces if deja else poses).append(rel)
        if ecrire:
            shutil.copy2(chemin, chemin + ".avant-3.0")
            open(chemin, "w", encoding="utf-8").write(neuf)

    for nom, L in (("en-tête posé", poses), ("en-tête remplacé", remplaces),
                   ("déjà migré, laissé tel quel", intacts),
                   ("identifiant inconnu, ignoré", orphelins)):
        if L:
            print("%s (%d) :" % (nom, len(L)))
            for x in sorted(L):
                print("   %s" % x)
    if not ecrire:
        print("\nEssai à blanc — rien n'a été écrit. Relancez avec --ecrire.")
    else:
        print("\n%d fichiers modifiés, sauvegardes en *.avant-3.0"
              % (len(poses) + len(remplaces)))


if __name__ == "__main__":
    main()
