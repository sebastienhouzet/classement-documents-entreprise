---
schema: classement-documents/3.0
id: "08.9"
parent: "08"
niveau: sous-dossier
titre: "08.9 - Valorisations & états annuels"
usage: >-
  Le dossier de clôture des placements : une fois par an, on réunit ici l'état complet de ce que
  l'entreprise détient, sa valeur et les calculs qui alimentent les comptes.
classement: chronologique
sensibilite: confidentielle
documents:
  - type: etat-recapitulatif-placements
    libelle: État récapitulatif des placements au 31/12
    description: "État récapitulatif de tous les placements au 31/12 — ligne, nature, date d'acquisition, prix de revient, valeur à la clôture, plus ou moins-value latente. Export du registre des placements."
    indices: [etat recapitulatif, placements au 31/12, prix de revient, plus-value latente, export du registre]
    champs: [date, exercice, designation, montant, cours]
    nommage: "{exercice}_Etat-recapitulatif-placements"
    conservation:
      legale: 10a
      recommandee: permanent
      declencheur: cloture-exercice
      base: Code de commerce art. L.123-22
      sort-final: C
    registre: null
  - type: attestation-valorisation-annuelle
    libelle: "Attestation de valorisation d'un établissement"
    description: Copie des attestations et relevés de valorisation au 31/12 de chaque établissement. Les originaux restent dans la ligne de placement concernée.
    indices: [attestation de valorisation, releve de valorisation, valorisation au 31/12, "copie de l'etablissement"]
    champs: [date, exercice, banque, designation, montant]
    nommage: "{date}_Attestation-de-valorisation-annuelle_{banque}_{exercice}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: null
  - type: calcul-plus-values-exercice
    libelle: "Calcul des plus et moins-values de l'exercice"
    description: "Calcul des plus et moins-values réalisées dans l'exercice, avec la méthode appliquée, et détail des intérêts courus non échus et autres produits à recevoir."
    indices: [plus-value realisee, moins-value, methode appliquee, interets courus non echus, produits a recevoir]
    champs: [date, exercice, designation, montant, methode-valorisation]
    nommage: "{date}_Calcul-plus-values-exercice_{exercice}_{designation}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: null
  - type: calcul-provision-depreciation
    libelle: Calcul des provisions pour dépréciation
    description: "Calcul des provisions pour dépréciation des placements et justification de la valeur retenue, y compris les cours et sources retenus pour les actifs valorisés au marché, avec horodatage."
    indices: [provision pour depreciation, justification de la valeur, cours retenu, source du cours, horodatage]
    champs: [date, exercice, designation, montant, motif, methode-valorisation]
    nommage: "{date}_Calcul-provision-depreciation_{exercice}_{designation}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: null
  - type: elements-annexe-placements
    libelle: "Éléments destinés à l'annexe"
    description: "Éléments des placements destinés à l'annexe des comptes — méthodes de valorisation, tableau des filiales et participations, engagements donnés (titres nantis, appels de capitaux restant à verser) — et échanges avec l'expert-comptable."
    indices: [annexe des comptes, methode de valorisation, tableau des filiales, engagements donnes, titres nantis]
    champs: [date, exercice, designation, montant, objet]
    nommage: "{date}_Elements-annexe-placements_{exercice}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: Code de commerce art. L.123-22
      sort-final: T
    registre: null
va-ailleurs:
  - motif: "Bilan, liasse fiscale et grand livre"
    vers: "04.1"
  - motif: Déclarations fiscales
    vers: "04.6"
---

# 08.9 - Valorisations & états annuels

> Chemin : `08 - PLACEMENTS & PARTICIPATIONS/08.9 - Valorisations & états annuels`

## À quoi sert ce dossier

Le dossier de clôture des placements : une fois par an, on réunit ici l'état complet de ce que l'entreprise détient, sa valeur et les calculs qui alimentent les comptes. C'est le paquet que l'expert-comptable réclame et que personne n'a envie de reconstituer ligne par ligne.

## Documents à y ranger

- État récapitulatif de tous les placements au 31/12 : ligne, nature, date d'acquisition, prix de revient, valeur à la clôture, plus ou moins-value latente (export du `Registre-des-placements.csv`)
- Attestations et relevés de valorisation au 31/12 de chaque établissement (copies — les originaux restent dans chaque ligne)
- Calcul des plus et moins-values réalisées dans l'exercice, avec la méthode appliquée
- Calcul des provisions pour dépréciation et leur justification
- Intérêts courus non échus (comptes à terme, obligations) et autres produits à recevoir
- Cours et sources retenus pour les actifs valorisés au marché, crypto-actifs compris, avec horodatage
- Éléments destinés à l'annexe : méthodes de valorisation, tableau des filiales et participations, engagements donnés (titres nantis, appels de capitaux restant à verser)
- Échanges avec l'expert-comptable sur le traitement des placements pour l'exercice

## Ne pas ranger ici

- Bilan, liasse fiscale et grand livre → `04.1`
- Déclarations fiscales → `04.6`

## Méthode de classement

**Un sous-dossier par exercice** : `2026/`. À l'intérieur, un fichier par nature de calcul, nommé `AAAA_Valorisation_Nature.xlsx` ou `.pdf`. Ce dossier ne contient que des copies et des calculs : les originaux restent dans la ligne de placement concernée.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Pièces comptables : 10 ans à compter de la clôture de l'exercice. Documents fiscaux : 10 ans. |
| **Recommandé** | 10 ans ; permanent pour l'état récapitulatif annuel, qui permet de reconstituer l'historique du portefeuille avec un seul fichier par année. |

Base : Code de commerce art. L.123-22 ; PCG (règlement ANC 2014-03), articles 221-1 et s. sur l'évaluation des actifs financiers.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
