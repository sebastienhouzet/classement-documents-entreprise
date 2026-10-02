---
schema: classement-documents/3.0
id: "01.5"
parent: "01"
niveau: sous-dossier
titre: "01.5 - Dirigeants & mandats"
usage: >-
  Tout ce qui concerne les mandataires sociaux (président, directeur général, gérant) :
  nomination, statut, rémunération, pouvoirs délégués et fin de mandat.
classement: par-tiers
sensibilite: confidentielle
documents:
  - type: decision-nomination-dirigeant
    libelle: Décision de nomination ou de cessation de mandat
    description: "Décision de nomination, de renouvellement, de révocation ou de démission d'un mandataire social (copie du PV original)."
    indices: [nomination du dirigeant, revocation, demission, mandat social, renouvellement de mandat]
    champs: [date, dirigeant, date-effet, objet]
    nommage: "{date}_Decision-nomination-dirigeant_{dirigeant}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: fin-mandat
      base: Code civil art. 2224
      sort-final: C
    registre: null
  - type: convention-reglementee-dirigeant
    libelle: Convention réglementée avec le dirigeant
    description: "Convention conclue entre la société et un dirigeant, et rapport spécial présenté à l'assemblée."
    indices: [convention reglementee, rapport special, convention avec le dirigeant, remuneration exceptionnelle]
    champs: [date-signature, dirigeant, montant, objet]
    nommage: "{date}_Convention-reglementee_{dirigeant}_{objet}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: fin-mandat
      base: Code de commerce art. L.227-10
      sort-final: C
    registre: null
  - type: decision-remuneration-dirigeant
    libelle: Décision de rémunération du dirigeant
    description: "Décision fixant la rémunération du dirigeant et ses avantages (véhicule, mutuelle, remboursements)."
    indices: [remuneration du dirigeant, avantages en nature, vehicule de fonction, decision de remuneration]
    champs: [date, dirigeant, montant, exercice]
    nommage: "{date}_Decision-remuneration-dirigeant_{dirigeant}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: fin-mandat
      base: Code civil art. 2224
      sort-final: C
    registre: null
  - type: delegation-pouvoir-signature
    libelle: Délégation de pouvoir ou de signature
    description: "Délégation de pouvoir ou de signature consentie par le dirigeant (banque, RH, engagements commerciaux)."
    indices: [delegation de pouvoir, delegation de signature, pouvoir bancaire, subdelegation, perimetre de delegation]
    champs: [date, dirigeant, objet, date-fin]
    nommage: "{date}_Delegation-de-pouvoir_{dirigeant}_{objet}"
    conservation:
      legale: 5a
      recommandee: 5a
      declencheur: fin-mandat
      base: Code civil art. 2224
      sort-final: D
    registre: null
  - type: kyc-dirigeant
    libelle: "Pièces d'identité du dirigeant (KYC)"
    description: "Pièce d'identité et justificatif de domicile du dirigeant, demandés par les banques et les plateformes."
    indices: ["piece d'identite du dirigeant", justificatif de domicile, kyc, vigilance bancaire]
    champs: [date, dirigeant, echeance, adresse]
    nommage: "{date}_KYC-dirigeant_{dirigeant}"
    conservation:
      legale: aucune
      recommandee: aucune
      declencheur: aucun
      base: Code civil art. 2224
      sort-final: D
    registre: null
va-ailleurs:
  - motif: Assurance RC des mandataires sociaux
    vers: "06.6"
  - motif: Bulletins de paie du dirigeant assimilé salarié
    vers: "03.3"
---

# 01.5 - Dirigeants & mandats

> Chemin : `01 - JURIDIQUE & GOUVERNANCE/01.5 - Dirigeants & mandats`

## À quoi sert ce dossier

Tout ce qui concerne les mandataires sociaux (président, directeur général, gérant) : nomination, statut, rémunération, pouvoirs délégués et fin de mandat.

## Documents à y ranger

- PV ou décision de nomination, de renouvellement, de révocation ou de démission (copie — original dans `01.3`)
- Décisions fixant la rémunération du dirigeant et ses avantages (véhicule, mutuelle…)
- Conventions réglementées entre la société et le dirigeant (contrat, rapport spécial)
- Délégations de pouvoir et de signature (banque, RH, signature des devis…)
- Contrat de travail cumulé avec le mandat, le cas échéant
- Affiliation du dirigeant aux organismes sociaux (SSI/URSSAF TNS ou régime assimilé salarié)
- Pièce d'identité et justificatif de domicile du dirigeant (pour les KYC des banques et plateformes)

## Ne pas ranger ici

- Assurance RC des mandataires sociaux → `06.6`
- Bulletins de paie du dirigeant assimilé salarié → `03.3`

## Méthode de classement

Un sous-dossier par dirigeant `NOM Prénom`, puis à l'intérieur : `Mandat`, `Rémunération`, `Délégations`, `KYC`. Ajouter un fichier `Historique-des-mandats.md` à la racine (dates de début/fin par personne).

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Durée du mandat + 5 ans (prescription de droit commun). |
| **Recommandé** | Permanent pour les nominations et conventions réglementées ; pièces d'identité à renouveler à expiration et anciennes versions supprimées. |

Base : Code civil art. 2224 ; Code de commerce art. L.227-10 (conventions réglementées SAS).

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
