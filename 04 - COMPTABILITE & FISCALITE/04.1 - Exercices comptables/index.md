---
schema: classement-documents/3.0
id: "04.1"
parent: "04"
niveau: sous-dossier
titre: 04.1 - Exercices comptables
usage: >-
  Les états de synthèse et les livres comptables de chaque exercice, tels que produits à la
  clôture. Un exercice = un sous-dossier, figé une fois les comptes approuvés.
classement: chronologique
sensibilite: confidentielle
documents:
  - type: comptes-annuels
    libelle: Comptes annuels
    description: "Bilan, compte de résultat et annexe de l'exercice, tels que produits par l'expert-comptable."
    indices: [bilan, compte de résultat, annexe, plaquette, comptes annuels]
    champs: [exercice, date, emetteur, montant]
    nommage: "{exercice}_Comptes-annuels"
    conservation:
      legale: 10a
      recommandee: permanent
      declencheur: cloture-exercice
      base: Code de commerce L123-22
      sort-final: C
    registre: null
  - type: liasse-fiscale
    libelle: Liasse fiscale
    description: "Liasse 2065 et ses tableaux (2050 à 2059 ou 2033), avec l'accusé de télétransmission."
    indices: [liasse fiscale, "2065", "2050", "2033", télétransmission, accusé]
    champs: [exercice, date, numero, montant, organisme]
    nommage: "{exercice}_Liasse-fiscale"
    conservation:
      legale: 10a
      recommandee: permanent
      declencheur: cloture-exercice
      base: LPF L102 B
      sort-final: C
    registre: null
  - type: grand-livre
    libelle: "Grand livre, balance et journaux"
    description: "Livres comptables de l'exercice : grand livre, balance générale, journaux de ventes, achats, banque, OD et paie."
    indices: [grand livre, balance générale, journal comptable, journaux, livres comptables]
    champs: [exercice, date-debut, date-fin, montant]
    nommage: "{exercice}_Grand-livre"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: Code de commerce L123-22
      sort-final: D
    registre: null
  - type: fichier-ecritures-comptables
    libelle: Fichier des écritures comptables (FEC)
    description: "FEC de l'exercice, obligatoire en cas de contrôle fiscal."
    indices: [fec, fichier des écritures comptables, contrôle, export, écritures]
    champs: [exercice, date, numero, quantite]
    nommage: "{exercice}_FEC"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: LPF L47 A
      sort-final: D
    registre: null
  - type: inventaire-de-cloture
    libelle: Inventaire et rapprochement de clôture
    description: "Inventaire des stocks et des immobilisations, et état de rapprochement bancaire de clôture."
    indices: [inventaire, stocks, rapprochement bancaire, clôture, situation intermédiaire]
    champs: [exercice, date, designation, quantite, montant]
    nommage: "{exercice}_Inventaire"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: Code de commerce L123-22
      sort-final: D
    registre: null
---

# 04.1 - Exercices comptables

> Chemin : `04 - COMPTABILITE & FISCALITE/04.1 - Exercices comptables`

## À quoi sert ce dossier

Les états de synthèse et les livres comptables de chaque exercice, tels que produits à la clôture. Un exercice = un sous-dossier, figé une fois les comptes approuvés.

## Documents à y ranger

- Bilan, compte de résultat, annexe (plaquette de l'expert-comptable)
- Liasse fiscale (2065 + 2050 à 2059 ou 2033) et accusé de télétransmission
- Grand livre, balance générale, journaux (ventes, achats, banque, OD, paie)
- Fichier des écritures comptables (FEC) de l'exercice — obligatoire en cas de contrôle
- Inventaire (stocks, immobilisations) et état de rapprochement bancaire de clôture
- Rapport de gestion (copie — original dans `01.3`), rapport du CAC
- Lettre d'affirmation, questionnaire de clôture, ajustements
- Situations intermédiaires (si établies)
- Récépissé de dépôt des comptes au greffe (copie — original dans `01.3`)

## Méthode de classement

**Un sous-dossier par exercice** : `2025` (ou `2025-07_2026-06` si décalé). À l'intérieur : `Etats financiers`, `Livres et FEC`, `Liasse`, `Cloture` (échanges et justificatifs de clôture).

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | 10 ans à compter de la clôture de l'exercice. |
| **Recommandé** | Permanent pour bilans, comptes de résultat et liasses ; 10 ans pour les livres, journaux et FEC. |

Base : Code de commerce art. L.123-22 ; LPF art. L.47 A (FEC) et L.102 B.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
