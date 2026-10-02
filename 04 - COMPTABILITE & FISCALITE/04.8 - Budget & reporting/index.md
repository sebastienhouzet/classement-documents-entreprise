---
schema: classement-documents/3.0
id: "04.8"
parent: "04"
niveau: sous-dossier
titre: "04.8 - Budget & reporting"
usage: >-
  Les documents de pilotage financier, sans valeur légale mais essentiels pour diriger : budget
  annuel, plan de trésorerie, tableaux de bord, prévisionnels transmis aux banques et
  investisseurs.
classement: chronologique
sensibilite: confidentielle
documents:
  - type: budget-annuel
    libelle: Budget annuel
    description: "Budget de l'exercice, ses hypothèses, la version validée et ses révisions. Sans valeur légale."
    indices: [budget, prévisionnel, hypothèses, révision, pilotage]
    champs: [exercice, date, objet, montant]
    nommage: "{exercice}_Budget"
    conservation:
      legale: aucune
      recommandee: 5a
      declencheur: cloture-exercice
      sort-final: D
    registre: null
  - type: plan-de-tresorerie
    libelle: Plan de trésorerie
    description: Export mensuel daté du plan de trésorerie glissant.
    indices: [plan de trésorerie, trésorerie, glissant, export, encaissements]
    champs: [periode, date, montant]
    nommage: "{periode}_Plan-de-tresorerie"
    conservation:
      legale: aucune
      recommandee: 5a
      declencheur: cloture-exercice
      sort-final: D
    registre: null
  - type: tableau-de-bord-financier
    libelle: Tableau de bord financier
    description: "Tableau de bord mensuel ou trimestriel (CA, marge, trésorerie, encours clients) et balance âgée."
    indices: [tableau de bord, reporting interne, marge, balance âgée, encours]
    champs: [periode, objet, montant-ht, taux]
    nommage: "{periode}_Tableau-de-bord"
    conservation:
      legale: aucune
      recommandee: 5a
      declencheur: cloture-exercice
      sort-final: D
    registre: null
  - type: business-plan-previsionnel
    libelle: Business plan et prévisionnel transmis
    description: "Business plan ou prévisionnel financier, dans la version transmise à une banque, un financeur ou un investisseur."
    indices: [business plan, prévisionnel, seuil de rentabilité, financeur, investisseur]
    champs: [date, destinataire, objet, duree, montant]
    nommage: "{date}_Business-plan_{destinataire}"
    conservation:
      legale: aucune
      recommandee: 5a
      declencheur: date-document
      sort-final: D
    registre: null
---

# 04.8 - Budget & reporting

> Chemin : `04 - COMPTABILITE & FISCALITE/04.8 - Budget & reporting`

## À quoi sert ce dossier

Les documents de pilotage financier, sans valeur légale mais essentiels pour diriger : budget annuel, plan de trésorerie, tableaux de bord, prévisionnels transmis aux banques et investisseurs.

## Documents à y ranger

- Budget annuel (hypothèses, version validée) et révisions
- Plan de trésorerie glissant (exports mensuels datés)
- Tableaux de bord mensuels / trimestriels (CA, marge, trésorerie, encours clients)
- Business plan et prévisionnels financiers (copie de la version transmise à un tiers : banque, BPI, investisseur)
- Analyses ponctuelles : rentabilité par client, par offre, seuil de rentabilité
- Suivi des encours et balance âgée clients / fournisseurs (exports)

## Méthode de classement

**Par année** : `AAAA/Budget`, `AAAA/Tresorerie`, `AAAA/Tableaux de bord`. Les prévisionnels transmis à un financeur sont aussi copiés dans le dossier de financement correspondant (`05.2`, `05.3`, `05.4`).

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Aucune obligation. |
| **Recommandé** | 5 ans (pour les comparaisons pluriannuelles) ; la version d'un prévisionnel transmis à un financeur suit la durée du dossier de financement. |

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
