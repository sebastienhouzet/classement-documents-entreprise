---
schema: classement-documents/3.0
id: "04.3"
parent: "04"
niveau: sous-dossier
titre: 04.3 - Factures fournisseurs
usage: >-
  Toutes les factures reçues : achats, prestations, abonnements, loyers, honoraires, télécom,
  énergie. Chaque facture doit être au nom de l'entreprise (mentions obligatoires, TVA) pour
  être déductible.
classement: chronologique
sensibilite: confidentielle
documents:
  - type: facture-fournisseur
    libelle: Facture fournisseur
    description: "Facture reçue d'un fournisseur, au nom de l'entreprise."
    indices: [facture, avoir, honoraires, tva, siret]
    champs: [date, emetteur, numero, montant-ht, montant-tva, montant-ttc, echeance]
    nommage: "{date}_Facture_{emetteur}_{numero}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: Code de commerce L123-22
      sort-final: D
    registre: null
  - type: avoir-fournisseur
    libelle: Avoir fournisseur
    description: "Avoir reçu d'un fournisseur, rattaché à la facture qu'il corrige."
    indices: [avoir fournisseur, note de crédit, remboursement, rectification, facture reçue]
    champs: [date, fournisseur, numero, reference, montant-ht, montant-tva, montant-ttc]
    nommage: "{date}_Avoir_{fournisseur}_{numero}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: CGI art. 289
      sort-final: D
    registre: null
  - type: ticket-caisse-achat
    libelle: "Reçu ou ticket d'achat"
    description: "Petit achat sans facture, inférieur à 150 € HT, dont le ticket mentionne la TVA."
    indices: [ticket de caisse, reçu, petit achat, tva déductible, justificatif]
    champs: [date, fournisseur, objet, montant-tva, montant-ttc]
    nommage: "{date}_Ticket_{fournisseur}_{objet}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: CGI art. 271
      sort-final: D
    registre: null
  - type: journal-des-achats
    libelle: Journal des achats
    description: Export mensuel du journal des achats.
    indices: [journal des achats, export, mensuel, fournisseurs, comptabilité]
    champs: [periode, montant-ht, montant-tva, montant-ttc]
    nommage: "{periode}_Journal-des-achats"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: Code de commerce L123-22
      sort-final: D
    registre: null
va-ailleurs:
  - motif: "Facture d'un bien immobilisé (> 500 € HT amorti) : original ici + copie dans 04.5"
    vers: null
  - motif: Contrats fournisseurs
    vers: "02.2"
  - motif: Notes de frais (dépenses avancées par une personne)
    vers: "04.4"
---

# 04.3 - Factures fournisseurs

> Chemin : `04 - COMPTABILITE & FISCALITE/04.3 - Factures fournisseurs`

## À quoi sert ce dossier

Toutes les factures reçues : achats, prestations, abonnements, loyers, honoraires, télécom, énergie. Chaque facture doit être au nom de l'entreprise (mentions obligatoires, TVA) pour être déductible.

## Documents à y ranger

- Factures fournisseurs (PDF reçu ou scan du papier), y compris les factures d'abonnement récurrentes
- Avoirs fournisseurs
- Reçus et tickets pour les petits achats sans facture (< 150 € HT : ticket avec TVA accepté)
- Factures d'honoraires (expert-comptable, avocat, freelances)
- Quittances de loyer et appels de charges (si utilisés comme pièces comptables)
- Journal des achats mensuel

## Ne pas ranger ici

- Facture d'un bien immobilisé (> 500 € HT amorti) : original ici + copie dans `04.5`
- Contrats fournisseurs → `02.2` / `02.5`
- Notes de frais (dépenses avancées par une personne) → `04.4`

## Méthode de classement

**Par année, puis par mois de la date de facture** : `AAAA/AAAA-MM/`. Nommage : `AAAA-MM-JJ_Fournisseur_Objet_MontantTTC.pdf` (ex. `2026-03-04_Hebergeur-Alpha_Hebergement-mars_35.88.pdf`). Un sous-dossier `AAAA/A traiter` peut servir de boîte d'entrée avant classement.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | 10 ans à compter de la clôture de l'exercice ; 6 ans au titre fiscal (TVA déductible). |
| **Recommandé** | 10 ans. |

Base : Code de commerce art. L.123-22 ; CGI art. 289 et 271 ; LPF art. L.102 B.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
