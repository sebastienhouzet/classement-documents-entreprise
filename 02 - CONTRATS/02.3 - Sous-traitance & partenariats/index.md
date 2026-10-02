---
schema: classement-documents/3.0
id: "02.3"
parent: "02"
niveau: sous-dossier
titre: "02.3 - Sous-traitance & partenariats"
usage: >-
  Les contrats dans lesquels l'entreprise confie une partie d'une mission client à un tiers
  (sous-traitance), ou s'associe avec un tiers pour vendre ou produire (partenariat, apport
  d'affaires, distribution, groupement).
classement: par-tiers
sensibilite: normale
documents:
  - type: contrat-sous-traitance
    libelle: Contrat de sous-traitance
    description: "Contrat confiant à un tiers une partie d'une mission client, avec la référence au contrat principal."
    indices: [sous-traitance, contrat de sous-traitance, "donneur d'ordre", client principal, loi de 1975]
    champs: [date-signature, fournisseur, numero, montant-ht, client]
    nommage: "{date}_Contrat-sous-traitance_{fournisseur}_{client}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Loi du 31 décembre 1975 sur la sous-traitance
      sort-final: D
    registre: { fichier: Registre-des-contrats.csv, cle: numero }
  - type: attestation-vigilance-sous-traitant
    libelle: "Attestation de vigilance d'un sous-traitant"
    description: "Attestation de vigilance URSSAF et Kbis du sous-traitant, à renouveler tous les six mois."
    indices: [attestation de vigilance du sous-traitant, urssaf, kbis, renouvellement semestriel, vigilance]
    champs: [date, fournisseur, echeance, siren]
    nommage: "{date}_Attestation-vigilance-sous-traitant_{fournisseur}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: date-document
      base: Code du travail art. L.8222-1
      sort-final: D
    registre: null
  - type: contrat-partenariat
    libelle: Contrat de partenariat
    description: "Contrat de partenariat, d'apport d'affaires, de distribution, de revente ou de marque blanche, avec sa grille de commissionnement."
    indices: [partenariat, "apport d'affaires", distribution, revente, marque blanche, commissionnement, co-developpement]
    champs: [date-signature, tiers, numero, taux, objet]
    nommage: "{date}_Contrat-partenariat_{tiers}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code de commerce art. L.110-4
      sort-final: D
    registre: { fichier: Registre-des-contrats.csv, cle: numero }
  - type: convention-groupement-consortium
    libelle: Convention de groupement ou de consortium
    description: "Convention de groupement momentané d'entreprises ou de consortium constituée pour répondre à une consultation."
    indices: [groupement, consortium, convention de groupement, mandataire du groupement, "appel d'offres"]
    champs: [date-signature, tiers, numero, objet, acheteur-public]
    nommage: "{date}_Convention-de-groupement_{tiers}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code de commerce art. L.110-4
      sort-final: D
    registre: { fichier: Registre-des-contrats.csv, cle: numero }
va-ailleurs:
  - motif: Prestataire simple (aucun lien avec un client)
    vers: "02.2"
---

# 02.3 - Sous-traitance & partenariats

> Chemin : `02 - CONTRATS/02.3 - Sous-traitance & partenariats`

## À quoi sert ce dossier

Les contrats dans lesquels l'entreprise **confie** une partie d'une mission client à un tiers (sous-traitance), ou s'associe avec un tiers pour vendre ou produire (partenariat, apport d'affaires, distribution, groupement).

## Documents à y ranger

- Contrats de sous-traitance (avec la référence au contrat client principal dans `02.1`)
- Contrats de partenariat, d'apport d'affaires, de distribution, de revente
- Conventions de groupement / consortium pour répondre à des appels d'offres
- Accords de co-développement, de marque blanche
- Pièces de vigilance du sous-traitant (attestation URSSAF, Kbis — tous les 6 mois)
- Grilles de commissionnement, relevés de commissions (factures → `04`)

## Ne pas ranger ici

- Prestataire simple (aucun lien avec un client) → `02.2`

## Méthode de classement

**Un sous-dossier par partenaire ou sous-traitant**. Quand un contrat de sous-traitance est lié à un client précis, nommer le fichier avec le client : `2026-02-01_Sous-traitance_Agence-X_pour_Client-Y.pdf`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | 5 ans après la fin du contrat. |
| **Recommandé** | 10 ans après la fin du contrat. |

Base : Code de commerce art. L.110-4 ; loi du 31 décembre 1975 sur la sous-traitance ; Code du travail art. L.8222-1.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
