---
schema: classement-documents/3.0
id: "04.7"
parent: "04"
niveau: sous-dossier
titre: "04.7 - Expert-comptable & CAC"
usage: >-
  La relation avec les professionnels du chiffre : lettre de mission, mandats, échanges de
  clôture, rapports. Un sous-dossier par intervenant, puis par exercice.
classement: par-tiers
sensibilite: confidentielle
documents:
  - type: lettre-mission-expert-comptable
    libelle: "Lettre de mission de l'expert-comptable"
    description: "Lettre de mission, ses avenants, les conditions générales et la grille tarifaire du cabinet."
    indices: [lettre de mission, expert-comptable, cabinet, conditions générales, grille tarifaire]
    champs: [date, fournisseur, objet, montant-ht, date-debut, duree]
    nommage: "{date}_Lettre-de-mission_{fournisseur}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Ordonnance du 19 septembre 1945
      sort-final: C
    registre: null
  - type: mandat-teledeclaration
    libelle: Mandat de télédéclaration
    description: "Mandat donné au cabinet pour les télédéclarations (EDI-TVA, EDI-TDFC, DSN) ou l'accès bancaire en lecture."
    indices: [mandat edi, edi-tdfc, télédéclaration, dsn, accès bancaire]
    champs: [date, fournisseur, organisme, objet, date-effet]
    nommage: "{date}_Mandat-EDI_{fournisseur}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code civil art. 2224
      sort-final: D
    registre: null
  - type: rapport-commissaire-aux-comptes
    libelle: Rapport du commissaire aux comptes
    description: "Rapport général, rapport spécial sur les conventions réglementées, lettre d'indépendance et recommandations du CAC."
    indices: [commissaire aux comptes, cac, rapport général, rapport spécial, indépendance, recommandations]
    champs: [exercice, date, emetteur, objet, montant]
    nommage: "{exercice}_Rapport-CAC_{emetteur}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-mandat
      base: Code de commerce L823-1
      sort-final: C
    registre: null
  - type: echange-de-cloture
    libelle: Échanges de clôture
    description: "Liste des pièces demandées, questions et réponses, points en suspens, questionnaire de clôture et validation des comptes."
    indices: [questionnaire de clôture, pièces demandées, points en suspens, validation des comptes, "lettre d'affirmation"]
    champs: [exercice, date, fournisseur, objet]
    nommage: "{exercice}_Echanges-de-cloture_{fournisseur}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code civil art. 2224
      sort-final: D
    registre: null
va-ailleurs:
  - motif: Honoraires (factures)
    vers: "04.3"
---

# 04.7 - Expert-comptable & CAC

> Chemin : `04 - COMPTABILITE & FISCALITE/04.7 - Expert-comptable & CAC`

## À quoi sert ce dossier

La relation avec les professionnels du chiffre : lettre de mission, mandats, échanges de clôture, rapports. Un sous-dossier par intervenant, puis par exercice.

## Documents à y ranger

- Lettre de mission de l'expert-comptable et ses avenants, conditions générales, grille tarifaire
- Mandats donnés (télédéclarations EDI-TVA, EDI-TDFC, DSN, accès bancaire en lecture)
- Échanges de clôture : liste des pièces demandées, questions/réponses, points en suspens, validation des comptes
- Lettre d'affirmation (copie — original dans `04.1`)
- Commissaire aux comptes : lettre de mission, désignation (PV → `01.3`), lettre d'indépendance, rapports (général, spécial sur les conventions réglementées), lettres de recommandations
- Changement de cabinet : reprise de dossier, transfert des archives

## Ne pas ranger ici

- Honoraires (factures) → `04.3`

## Méthode de classement

**Deux sous-dossiers** `Expert-comptable` et `Commissaire aux comptes` (et un par cabinet en cas de changement : `Expert-comptable/Cabinet X (2019-2024)`), puis `Mission` et `Exercices/AAAA`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Durée de la mission + 5 ans. |
| **Recommandé** | 10 ans après la fin de la mission. |

Base : Code civil art. 2224 ; ordonnance du 19 septembre 1945 (expertise comptable) ; Code de commerce art. L.823-1 et s. (CAC).

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
