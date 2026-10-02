---
schema: classement-documents/3.0
id: "08.2"
parent: "08"
niveau: sous-dossier
titre: 08.2 - Placements bancaires
usage: >-
  Les placements sans risque en capital logés chez une banque : comptes à terme (CAT / DAT),
  comptes sur livret, bons de caisse, comptes courants rémunérés.
classement: par-contrat
sensibilite: confidentielle
documents:
  - type: contrat-compte-a-terme
    libelle: Contrat de compte à terme ou de livret
    description: "Contrat d'ouverture d'un compte à terme, d'un dépôt à terme, d'un compte sur livret ou d'un bon de caisse — rémunération, durée, pénalité de sortie anticipée, conditions de renouvellement."
    indices: [compte a terme, cat, dat, depot a terme, compte sur livret, bon de caisse, penalite de sortie anticipee]
    champs: [date-signature, banque, numero-compte, designation, montant, taux, echeance]
    nommage: "{date}_Contrat-compte-a-terme_{banque}_{designation}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code de commerce art. L.110-4
      sort-final: D
    registre: { fichier: Registre-des-placements.csv, cle: designation }
  - type: avis-souscription-placement-bancaire
    libelle: "Avis de souscription d'un placement bancaire"
    description: "Avis d'opéré ou confirmation de souscription d'un placement bancaire — montant, date de valeur, taux, échéance — et avenants, renouvellements et modifications de taux."
    indices: [confirmation de souscription, "avis d'opere bancaire", date de valeur, renouvellement tacite, modification de taux]
    champs: [date, banque, numero-compte, designation, montant, taux, echeance]
    nommage: "{date}_Avis-de-souscription_{banque}_{designation}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: { fichier: Registre-des-placements.csv, cle: designation }
  - type: releve-placement-bancaire
    libelle: "Relevé et avis d'échéance d'un placement bancaire"
    description: "Relevés périodiques, avis d'échéance et décomptes d'intérêts versés d'un compte à terme ou d'un livret."
    indices: [releve periodique, "avis d'echeance", interets verses, "decompte d'interets", releve bancaire]
    champs: [date, banque, numero-compte, periode, montant]
    nommage: "{date}_Releve-placement-bancaire_{banque}_{periode}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: date-document
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: null
  - type: attestation-valorisation-placement-bancaire
    libelle: Attestation de valorisation au 31/12
    description: "Attestation de valorisation au 31/12 et détail des intérêts courus non échus, pièce de clôture d'un placement bancaire. Les intérêts d'un CAT se rattachent à l'exercice au prorata."
    indices: [attestation de valorisation, interets courus non echus, icne, piece de cloture, valorisation au 31/12]
    champs: [date, banque, numero-compte, exercice, montant]
    nommage: "{date}_Attestation-de-valorisation_{banque}_{exercice}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: null
  - type: denouement-placement-bancaire
    libelle: "Dénouement d'un placement bancaire"
    description: "Instruction de sortie anticipée, décompte de pénalité, avis de clôture et virement de restitution d'un compte à terme ou d'un livret."
    indices: [denouement, sortie anticipee, avis de cloture, virement de restitution, decompte de penalite]
    champs: [date, banque, numero-compte, designation, montant, motif]
    nommage: "{date}_Denouement-placement_{banque}_{designation}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: { fichier: Registre-des-placements.csv, cle: designation }
va-ailleurs:
  - motif: "Comptes courants d'exploitation"
    vers: "05.1"
  - motif: Contrat de prêt garanti par le CAT
    vers: "05.2"
---

# 08.2 - Placements bancaires

> Chemin : `08 - PLACEMENTS & PARTICIPATIONS/08.2 - Placements bancaires`

## À quoi sert ce dossier

Les placements sans risque en capital logés chez une banque : comptes à terme (CAT / DAT), comptes sur livret, bons de caisse, comptes courants rémunérés. Peu de documents par ligne, mais des échéances et des renouvellements tacites à surveiller de près.

## Documents à y ranger

- Contrat d'ouverture du compte à terme ou du livret : rémunération, durée, barème de pénalité en cas de sortie anticipée, conditions de renouvellement
- Avis d'opéré / confirmation de souscription (montant, date de valeur, taux, échéance)
- Avenants, renouvellements, modifications de taux
- Relevés périodiques et avis d'échéance
- **Attestation de valorisation au 31/12** et détail des intérêts courus non échus (pièce de clôture)
- Décompte des intérêts versés
- Instruction de sortie anticipée et décompte de pénalité
- Dénouement : avis de clôture, virement de restitution
- Nantissement du CAT en garantie d'un prêt (copie — original dans `05.6`)

## Ne pas ranger ici

- Comptes courants d'exploitation → `05.1`
- Contrat de prêt garanti par le CAT → `05.2` ; la garantie elle-même → `05.6`

## Méthode de classement

**Un sous-dossier par ligne** : `AAAA - Banque - Support - Montant - Échéance` (ex. `2026 - Banque Alpha - CAT 12 mois - 50k - 2027-03`). À l'intérieur : `Contrat`, `Releves/AAAA`, `Cloture`. L'attestation d'intérêts courus au 31/12 se range dans `Releves/AAAA` avec le mot `Valorisation` dans le nom du fichier.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Relevés et documents bancaires : 5 ans. Contrat : durée + 5 ans. En tant que pièce comptable : 10 ans après la clôture de l'exercice. |
| **Recommandé** | 10 ans après le dénouement. |

Base : Code de commerce art. L.110-4 et L.123-22 ; Code civil art. 2224.

## Conseils

- Noter l'échéance **et** la date limite de dénonciation dans le `Registre-des-placements.csv` dès la souscription : beaucoup de comptes à terme se renouvellent tacitement à un taux inférieur.
- Les intérêts d'un CAT se rattachent à l'exercice au prorata, même s'ils ne sont versés qu'à l'échéance : l'attestation au 31/12 est une pièce de clôture à part entière.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
