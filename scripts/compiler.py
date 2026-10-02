#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compile les en-têtes YAML des index.md en un seul fichier exploitable.

    python3 scripts/compiler.py [racine] [-o referentiel/dossiers.json]

Le fichier produit évite à une application — ou à un agent — de parcourir
l'arborescence et d'analyser 78 fichiers Markdown : tout l'en-tête 3.0 y est,
plus deux index de recherche directe.

    {
      "schema":      "classement-documents/3.0",
      "genere_le":   "2026-10-02",
      "champs":      { "date": {…}, … },        le catalogue, tel quel
      "dossiers":    [ { id, parent, niveau, titre, chemin, usage,
                         classement, sensibilite, documents, va-ailleurs } ],
      "index_types": { "facture-client": "04.2", … },
      "index_chemins": { "04.2": "04 - COMPTABILITE…/04.2 - Factures clients" }
    }

`index_types` donne le dossier de destination d'un type documentaire en une
lecture : c'est ce qui permet à un agent de classer sans relire le gabarit.
"""
import datetime
import json
import os
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML est requis : pip install pyyaml")

SEP = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.S)
CHAMP_ORDRE = ["schema", "id", "parent", "niveau", "titre", "chemin", "usage",
               "classement", "sensibilite", "documents", "va-ailleurs"]


def entetes(racine):
    out = []
    for base, dirs, fichiers in os.walk(racine):
        dirs[:] = [d for d in dirs
                   if d not in (".git", ".github", "scripts", "referentiel")]
        if "index.md" not in fichiers or os.path.abspath(base) == os.path.abspath(racine):
            continue
        chemin = os.path.join(base, "index.md")
        m = SEP.match(open(chemin, encoding="utf-8").read())
        if not m:
            print("ignoré, sans en-tête : %s" % os.path.relpath(chemin, racine),
                  file=sys.stderr)
            continue
        d = yaml.safe_load(m.group(1))
        d["chemin"] = os.path.relpath(base, racine)
        out.append({k: d[k] for k in CHAMP_ORDRE if k in d})
    return sorted(out, key=lambda x: (len(x["id"]), x["id"]))


def main():
    args = [a for a in sys.argv[1:] if a != "-o"]
    racine = os.path.abspath(args[0] if args and not args[0].endswith(".json") else ".")
    sortie = next((a for a in args if a.endswith(".json")),
                  os.path.join(racine, "referentiel", "dossiers.json"))

    dossiers = entetes(racine)
    if not dossiers:
        sys.exit("aucun en-tête trouvé sous %s" % racine)

    champs = {}
    p = os.path.join(racine, "97 - REFERENTIEL", "champs.yaml")
    if os.path.exists(p):
        champs = (yaml.safe_load(open(p, encoding="utf-8")) or {}).get("champs", {})

    index_types, collisions = {}, []
    for d in dossiers:
        for doc in d.get("documents") or []:
            t = doc.get("type")
            if t in index_types:
                collisions.append(t)
            index_types[t] = d["id"]
    if collisions:
        sys.exit("types en collision, lancez scripts/lint.py : %s"
                 % ", ".join(sorted(set(collisions))))

    data = {
        "schema": dossiers[0].get("schema", "classement-documents/3.0"),
        "genere_le": datetime.date.today().isoformat(),
        "champs": champs,
        "dossiers": dossiers,
        "index_types": dict(sorted(index_types.items())),
        "index_chemins": {d["id"]: d["chemin"] for d in dossiers},
    }

    os.makedirs(os.path.dirname(os.path.abspath(sortie)), exist_ok=True)
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1, sort_keys=False)
        f.write("\n")
    print("%d dossiers, %d types, %d champs → %s"
          % (len(dossiers), len(index_types), len(champs),
             os.path.relpath(sortie, racine)))


if __name__ == "__main__":
    main()
