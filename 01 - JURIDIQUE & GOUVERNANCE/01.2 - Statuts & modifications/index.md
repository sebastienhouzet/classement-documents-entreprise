---
schema: classement-documents/3.0
id: "01.2"
parent: "01"
niveau: sous-dossier
titre: "01.2 - Statuts & modifications"
usage: >-
  L'historique complet des statuts : chaque version consolidée, et pour chaque modification, la
  décision et les formalités qui l'accompagnent (annonce légale, dépôt au greffe, Kbis mis à
  jour).
classement: par-operation
sensibilite: normale
documents:
  - type: statuts-a-jour
    libelle: Statuts mis à jour
    description: "Version consolidée des statuts après une modification, certifiée conforme par le dirigeant."
    indices: [statuts a jour, statuts modifies, version consolidee, certifie conforme, statuts en vigueur]
    champs: [date, objet, signataire, date-effet]
    nommage: "{date}_Statuts-a-jour_{objet}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: radiation-societe
      base: Code de commerce art. L.123-22
      sort-final: C
    registre: null
  - type: formalite-modification-greffe
    libelle: Formalité de modification au greffe
    description: "Formulaire de modification (M2 ou guichet unique), récépissé du greffe et Kbis postérieur à la modification."
    indices: [m2, guichet unique, recepisse greffe, kbis apres modification, transfert de siege, changement de denomination, transformation]
    champs: [date, organisme, objet, nature, siren]
    nommage: "{date}_Formalite-modification_{organisme}_{objet}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: radiation-societe
      base: Code de commerce art. L.123-22
      sort-final: C
    registre: null
  - type: annonce-legale-modification
    libelle: Annonce légale de modification
    description: "Avis publié au journal d'annonces légales pour une modification statutaire, et attestation de parution."
    indices: [annonce legale de modification, "journal d'annonces legales", attestation de parution, publicite legale, "changement d'objet"]
    champs: [date, emetteur, objet, montant]
    nommage: "{date}_Annonce-legale_{emetteur}_{objet}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: radiation-societe
      base: Code civil art. 2224
      sort-final: C
    registre: null
va-ailleurs:
  - motif: "PV d'AG originaux"
    vers: "01.3"
  - motif: Registre des décisions
    vers: "01.4"
---

# 01.2 - Statuts & modifications

> Chemin : `01 - JURIDIQUE & GOUVERNANCE/01.2 - Statuts & modifications`

## À quoi sert ce dossier

L'historique complet des statuts : chaque version consolidée, et pour chaque modification, la décision et les formalités qui l'accompagnent (annonce légale, dépôt au greffe, Kbis mis à jour).

## Documents à y ranger

- **À la racine :** `Statuts-en-vigueur.pdf` (toujours la dernière version consolidée, certifiée conforme par le dirigeant)
- Pour chaque modification : statuts mis à jour, PV de la décision (copie — l'original est dans `01.3`), formulaire de modification (M2 / guichet unique), annonce légale, récépissé du greffe, Kbis après modification
- Exemples de modifications : transfert de siège, changement de dénomination, augmentation ou réduction de capital, changement de dirigeant, modification de l'objet social, transformation de forme juridique

## Ne pas ranger ici

- PV d'AG originaux → `01.3`
- Registre des décisions → `01.4`

## Méthode de classement

Un sous-dossier par modification : `AAAA-MM-JJ - Objet de la modification` (ex. `2024-06-30 - Transfert de siege`). À l'intérieur, fichiers nommés par type. La racine ne contient que les statuts en vigueur.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | 5 ans à compter de la radiation de la société. |
| **Recommandé** | Permanent — toutes les versions, jamais de purge. |

Base : Code de commerce, art. L.123-22 ; Code civil art. 2224.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
