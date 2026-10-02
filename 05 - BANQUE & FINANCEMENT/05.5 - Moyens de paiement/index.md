---
schema: classement-documents/3.0
id: "05.5"
parent: "05"
niveau: sous-dossier
titre: 05.5 - Moyens de paiement
usage: >-
  Les outils d'encaissement et de décaissement : cartes bancaires, terminaux de paiement,
  prestataires de paiement en ligne, prélèvements SEPA, chéquiers.
classement: par-tiers
sensibilite: confidentielle
documents:
  - type: releve-prestataire-paiement
    libelle: Relevé de prestataire de paiement
    description: "Relevé ou payout mensuel d'un prestataire de paiement en ligne et son export annuel, pièce comptable au même titre qu'un relevé bancaire."
    indices: [prestataire de paiement, psp, payout, releve mensuel, export annuel, commissions]
    champs: [periode, plateforme, numero-compte, montant]
    nommage: "{periode}_Releve-PSP_{plateforme}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: date-document
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: null
  - type: mandat-prelevement-sepa
    libelle: Mandat de prélèvement SEPA
    description: "Mandat de prélèvement SEPA signé par un client, avec sa RUM et l'identifiant créancier, et sa révocation éventuelle."
    indices: [mandat sepa, prelevement, rum, ics, identifiant creancier, revocation de mandat]
    champs: [date-signature, client, rum, iban]
    nommage: "{date}_Mandat-SEPA_{client}_{rum}"
    conservation:
      legale: 14m
      recommandee: 10a
      declencheur: derniere-operation
      base: Règles SEPA (EPC)
      sort-final: D
    registre: null
  - type: contrat-monetique-tpe
    libelle: "Contrat monétique, TPE ou prestataire de paiement"
    description: "Contrat de terminal de paiement, contrat monétique ou conditions acceptées d'un prestataire de paiement, avec sa grille de commissions."
    indices: [tpe, terminal de paiement, monetique, contrat psp, commissions, conditions acceptees]
    champs: [date-signature, prestataire, numero-contrat, taux, montant]
    nommage: "{date}_Contrat-monetique_{prestataire}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code monétaire et financier art. L.133-1
      sort-final: D
    registre: null
  - type: contrat-carte-bancaire-pro
    libelle: Contrat de carte bancaire professionnelle
    description: "Contrat de carte bancaire professionnelle, titulaire et plafonds, opposition et renouvellement ; talons et oppositions de chéquier."
    indices: [carte bancaire professionnelle, titulaire de carte, plafond de paiement, opposition, chequier, remise de cheques]
    champs: [date, banque, numero-contrat, titulaire, montant]
    nommage: "{date}_Contrat-carte-bancaire_{banque}_{titulaire}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code monétaire et financier art. L.133-1
      sort-final: D
    registre: null
  - type: contestation-chargeback
    libelle: Contestation de paiement ou chargeback
    description: "Contestation d'une opération, chargeback, déclaration de fraude et suites données par la banque ou le prestataire."
    indices: [chargeback, contestation de paiement, fraude, impaye, rejet de prelevement, declaration de fraude]
    champs: [date, plateforme, reference, montant, motif]
    nommage: "{date}_Contestation-de-paiement_{plateforme}_{reference}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: date-document
      base: Code monétaire et financier art. L.133-1
      sort-final: D
    registre: null
va-ailleurs:
  - motif: Relevés de compte bancaire
    vers: "05.1"
---

# 05.5 - Moyens de paiement

> Chemin : `05 - BANQUE & FINANCEMENT/05.5 - Moyens de paiement`

## À quoi sert ce dossier

Les outils d'encaissement et de décaissement : cartes bancaires, terminaux de paiement, prestataires de paiement en ligne, prélèvements SEPA, chéquiers. Les relevés des prestataires de paiement sont des pièces comptables au même titre que les relevés bancaires.

## Documents à y ranger

- Cartes bancaires : contrats, titulaires, plafonds, oppositions
- Contrat monétique / TPE, conditions de commissions
- Prestataires de paiement (PSP) : contrats et conditions acceptées, KYC fourni, relevés / payouts mensuels, exports annuels
- Prélèvements SEPA : identifiant créancier SEPA (ICS), mandats signés par les clients (un par client, avec la RUM), révocations
- Chéquiers : talons, oppositions ; remises de chèques
- Virements : justificatifs d'ordres importants, listes de bénéficiaires validés
- Incidents : contestations, chargebacks, fraudes (déclarations)

## Ne pas ranger ici

- Relevés de compte bancaire → `05.1`

## Méthode de classement

**Un sous-dossier par moyen ou prestataire** (`Cartes`, `TPE`, `PSP Alpha`, `PSP Beta`, `Prelevements SEPA`, `Cheques`). Relevés en `Releves/AAAA/AAAA-MM_Releve.pdf` ; mandats SEPA un fichier par client `Mandat-SEPA_Client_RUM.pdf`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Relevés : 5 ans. Mandats SEPA : 14 mois après le dernier prélèvement (règlement SEPA) ; 5 ans en cas de litige. Contrats : durée + 5 ans. |
| **Recommandé** | 10 ans pour les relevés (pièces comptables) et les mandats SEPA ; contrats : 10 ans après résiliation. |

Base : Code de commerce art. L.110-4 et L.123-22 ; règles SEPA (EPC) ; Code monétaire et financier art. L.133-1 et s.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
