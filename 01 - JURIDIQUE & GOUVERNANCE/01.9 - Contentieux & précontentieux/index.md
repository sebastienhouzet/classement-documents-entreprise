---
schema: classement-documents/3.0
id: "01.9"
parent: "01"
niveau: sous-dossier
titre: "01.9 - Contentieux & précontentieux"
usage: >-
  Les litiges, avérés ou en germe : impayés en recouvrement contentieux, mises en demeure reçues
  ou envoyées, procédures judiciaires, transactions.
classement: par-operation
sensibilite: confidentielle
documents:
  - type: mise-en-demeure-contentieux
    libelle: Mise en demeure
    description: "Mise en demeure envoyée ou reçue, avec sa preuve de dépôt LRAR et l'accusé de réception."
    indices: [mise en demeure, lrar, sommation, preuve de depot, injonction amiable]
    champs: [date, destinataire, montant, objet, numero-dossier, tiers, numero-recommande]
    nommage: "{date}_Mise-en-demeure_{destinataire}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: derniere-operation
      base: Code civil art. 2224
      sort-final: T
    registre: null
  - type: acte-de-procedure
    libelle: Acte de procédure
    description: "Assignation, conclusions et pièces communiquées dans une instance judiciaire."
    indices: [assignation, conclusions, pieces communiquees, audience, procedure judiciaire]
    champs: [date, numero-dossier, tiers, objet]
    nommage: "{date}_Acte-de-procedure_{tiers}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: derniere-operation
      base: Code civil art. 2224
      sort-final: T
    registre: null
  - type: jugement-ordonnance
    libelle: "Jugement, ordonnance ou injonction"
    description: "Décision de justice rendue dans une affaire — jugement, ordonnance, injonction de payer — et preuves d'exécution."
    indices: [jugement, ordonnance, injonction de payer, decision definitive, saisie, mainlevee]
    champs: [date, numero-dossier, tiers, objet, montant]
    nommage: "{date}_Jugement_{tiers}_{objet}"
    conservation:
      legale: 10a
      recommandee: permanent
      declencheur: derniere-operation
      base: "Code des procédures civiles d'exécution art. L.111-4"
      sort-final: C
    registre: null
  - type: protocole-transactionnel
    libelle: Protocole transactionnel
    description: Protocole transactionnel ou accord de médiation mettant fin au litige.
    indices: [protocole transactionnel, transaction, accord de mediation, mediation, desistement]
    champs: [date-signature, tiers, montant, objet, numero-dossier]
    nommage: "{date}_Protocole-transactionnel_{tiers}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: derniere-operation
      base: Code civil art. 2224
      sort-final: C
    registre: null
  - type: convention-honoraires-avocat
    libelle: "Convention d'honoraires"
    description: "Convention d'honoraires de l'avocat ou du commissaire de justice chargé de l'affaire."
    indices: [avocat, "convention d'honoraires", huissier, commissaire de justice, provision sur honoraires]
    champs: [date-signature, tiers, montant, taux, numero-dossier]
    nommage: "{date}_Convention-honoraires_{tiers}_{numero-dossier}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-mandat
      base: Code civil art. 2224
      sort-final: D
    registre: null
va-ailleurs:
  - motif: Relances amiables de factures
    vers: "04.2"
  - motif: Sinistres assurance
    vers: "06.7"
---

# 01.9 - Contentieux & précontentieux

> Chemin : `01 - JURIDIQUE & GOUVERNANCE/01.9 - Contentieux & précontentieux`

## À quoi sert ce dossier

Les litiges, avérés ou en germe : impayés en recouvrement contentieux, mises en demeure reçues ou envoyées, procédures judiciaires, transactions. Chaque affaire a son dossier, et chaque dossier commence par une note de synthèse.

## Documents à y ranger

- `Synthese.md` à la racine de chaque affaire : parties, objet, montant, avocat, étapes, statut
- Mises en demeure envoyées / reçues (avec preuve de dépôt LRAR et accusé de réception)
- Échanges avec avocats, huissiers (commissaires de justice), médiateurs
- Actes de procédure : assignation, conclusions, pièces, jugements, ordonnances, injonctions de payer
- Protocoles transactionnels, accords de médiation
- Preuves d'exécution (paiement, saisie, mainlevée)
- Conventions d'honoraires (factures → `04.3`)

## Ne pas ranger ici

- Relances amiables de factures → avec la facture dans `04.2`
- Sinistres assurance → `06.7`

## Méthode de classement

**Un sous-dossier par affaire** : `AAAA - Partie adverse - Objet` (ex. `2026 - Client Beta - Impaye facture F2025-0087`). À l'intérieur, classement chronologique `AAAA-MM-JJ_Type_Objet.pdf`. Un dossier `Clos` pour les affaires terminées, avant transfert vers `98 - ARCHIVES`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | 5 ans après la décision définitive ou l'exécution (prescription de droit commun) ; 10 ans pour l'exécution d'un jugement ; dossier d'avocat : 5 ans après la fin du mandat. |
| **Recommandé** | 10 ans après la clôture de l'affaire ; permanent pour les jugements. |

Base : Code civil art. 2224 ; Code des procédures civiles d'exécution art. L.111-4.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
