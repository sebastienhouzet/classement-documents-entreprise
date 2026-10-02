---
schema: classement-documents/3.0
id: "05.1"
parent: "05"
niveau: sous-dossier
titre: 05.1 - Comptes bancaires
usage: >-
  Chaque compte bancaire de l'entreprise (compte courant, compte d'épargne, compte en devises,
  néobanque) : son contrat, ses relevés mensuels et la correspondance avec la banque.
classement: par-tiers
sensibilite: confidentielle
documents:
  - type: releve-compte-bancaire
    libelle: Relevé de compte bancaire
    description: "Relevé mensuel d'un compte de l'entreprise (compte courant, compte en devises, néobanque), pièce du rapprochement bancaire."
    indices: [releve bancaire, releve de compte, solde, operations, iban]
    champs: [periode, banque, numero-compte, montant]
    nommage: "{periode}_Releve_{banque}_{numero-compte}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: date-document
      base: Code de commerce art. L.110-4
      sort-final: D
    registre: null
  - type: convention-compte-bancaire
    libelle: Convention de compte et conditions tarifaires
    description: "Convention d'ouverture de compte, conditions tarifaires de chaque version, avenants et RIB/IBAN du compte."
    indices: [convention de compte, conditions tarifaires, rib, iban, ouverture de compte]
    champs: [date-signature, banque, numero-compte, iban]
    nommage: "{date}_Convention-de-compte_{banque}_{numero-compte}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: fin-contrat
      base: Code monétaire et financier art. L.312-1-1
      sort-final: C
    registre: null
  - type: procuration-bancaire
    libelle: Procuration et habilitation bancaire
    description: "Procurations et mandats de signature sur le compte (titulaires, plafonds) et habilitations à la banque en ligne."
    indices: [procuration bancaire, mandat de signature, habilitation, plafond, banque en ligne, kyc bancaire]
    champs: [date-signature, banque, numero-compte, beneficiaire, date-fin]
    nommage: "{date}_Procuration-bancaire_{banque}_{beneficiaire}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code monétaire et financier art. L.312-1-1
      sort-final: D
    registre: null
  - type: attestation-cloture-compte
    libelle: Attestation de clôture de compte
    description: Courrier de clôture du compte et attestation de clôture délivrée par la banque.
    indices: [cloture de compte, attestation de cloture, fermeture de compte, courrier de la banque]
    champs: [date, banque, numero-compte, montant]
    nommage: "{date}_Attestation-de-cloture_{banque}_{numero-compte}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: fin-contrat
      base: Code monétaire et financier art. L.312-1-1
      sort-final: C
    registre: null
  - type: avis-agios-frais-bancaires
    libelle: "Échelle d'intérêts, agios et attestation de solde"
    description: "Échelles d'intérêts, décomptes d'agios, relevés annuels de frais et attestation de solde au 31/12 demandée pour la clôture."
    indices: [agios, "echelle d'interets", frais bancaires, attestation de solde, releve annuel de frais]
    champs: [exercice, banque, numero-compte, montant, taux]
    nommage: "{exercice}_Attestation-de-solde_{banque}_{numero-compte}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: date-document
      base: Code de commerce art. L.110-4
      sort-final: D
    registre: null
  - type: rib-entreprise
    libelle: "Relevé d'identité bancaire de l'entreprise"
    description: "RIB d'un compte de l'entreprise — IBAN, BIC, titulaire. Pièce d'identité du compte, diffusée aux clients et aux organismes. Chaque version émise est conservée."
    indices: [rib, "releve d'identite bancaire", iban, bic, coordonnees bancaires, domiciliation]
    champs: [date, banque, titulaire, iban, bic, numero-compte]
    nommage: "{date}_RIB_{banque}_{numero-compte}"
    conservation:
      legale: aucune
      recommandee: 5a
      declencheur: fin-contrat
      base: Code civil art. 2224
      sort-final: D
    registre: null
va-ailleurs:
  - motif: Relevés des prestataires de paiement en ligne
    vers: "05.5"
  - motif: "Comptes à terme, livrets et autres supports de placement"
    vers: "08.2"
  - motif: "Le RIB d'un tiers n'est jamais rangé ici. Celui d'un fournisseur ou d'un prestataire, avec la preuve de vérification de ses coordonnées"
    vers: "02.2"
  - motif: "Le RIB d'un salarié"
    vers: "03.2"
---

# 05.1 - Comptes bancaires

> Chemin : `05 - BANQUE & FINANCEMENT/05.1 - Comptes bancaires`

## À quoi sert ce dossier

Chaque compte bancaire de l'entreprise (compte courant, compte d'épargne, compte en devises, néobanque) : son contrat, ses relevés mensuels et la correspondance avec la banque.

## Documents à y ranger

- Convention de compte, conditions tarifaires (chaque version), avenants
- Relevé d'identité bancaire (RIB) de chaque compte : IBAN, BIC, titulaire. Garder chaque version émise, pas seulement la dernière — c'est elle qui prouve quel compte était désigné à une date donnée
- Procurations et mandats (qui peut signer, plafonds), habilitations à la banque en ligne
- Relevés de compte mensuels (PDF), relevés annuels de frais
- Réponses aux demandes KYC de la banque (justificatifs fournis, avec la date)
- Courriers : ouverture, changements de conditions, incidents, clôture, attestation de clôture
- Échelles d'intérêts, agios, attestation de solde au 31/12

## Ne pas ranger ici

- Relevés des prestataires de paiement en ligne → `05.5`
- Comptes à terme, livrets et autres supports de placement → `08.2`
- **Le RIB d'un tiers n'est jamais rangé ici.** Celui d'un fournisseur ou d'un prestataire, avec la preuve de vérification de ses coordonnées → `02.2`
- Le RIB d'un salarié → `03.2` (dossier individuel)

## Méthode de classement

**Un sous-dossier par compte** `Banque - Type de compte` (ex. `Banque Alpha - Compte courant`). À l'intérieur : `Convention et mandats`, `Releves/AAAA/AAAA-MM_Releve.pdf`, `Courriers/AAAA`, `KYC`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Relevés bancaires et talons de chèques : 5 ans. Convention : durée du compte + 5 ans. |
| **Recommandé** | 10 ans pour les relevés (justificatifs du rapprochement bancaire) ; permanent pour les conventions et attestations de clôture. |

Base : Code de commerce art. L.110-4 ; Code monétaire et financier art. L.312-1-1.

## Conseils

- Un RIB ne se conserve pas comme une pièce comptable mais comme une pièce d'identité du compte : on garde chaque version, et on ne purge qu'après la clôture du compte.
- **Changement de RIB d'un fournisseur : ne jamais modifier les coordonnées de paiement sur la foi d'un courriel ou d'un document joint.** Rappeler le fournisseur sur le numéro déjà connu — jamais celui qui figure sur la demande — et ranger la trace de cette vérification avec le nouveau RIB dans `02.2`. C'est la fraude la plus courante et la plus coûteuse pour une petite structure.
- Le RIB diffusé à l'extérieur est celui du Kit administratif (`97.1`), qui ne garde que la version du moment ; l'historique reste ici.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
