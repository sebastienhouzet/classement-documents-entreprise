---
schema: classement-documents/3.0
id: "01.1"
parent: "01"
niveau: sous-dossier
titre: 01.1 - Constitution
usage: >-
  Les pièces d'origine de la société, produites une seule fois lors de sa création. Elles ne
  changent jamais ; les évolutions ultérieures vont dans 01.2 (statuts) et 01.3 (décisions).
classement: alphabetique
sensibilite: normale
documents:
  - type: statuts-constitutifs
    libelle: Statuts constitutifs
    description: "Statuts signés et paraphés lors de la création de la société, version d'origine."
    indices: [statuts, statuts constitutifs, constitution, paraphe, souscripteurs]
    champs: [date-signature, signataire, objet]
    nommage: "{date}_Statuts_Constitution_{objet}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: radiation-societe
      base: Code civil art. 2224
      sort-final: C
    registre: null
  - type: attestation-depot-capital
    libelle: Attestation de dépôt du capital
    description: "Attestation bancaire ou notariale de dépôt des apports en numéraire, avec la liste des souscripteurs."
    indices: [depot de capital, souscripteurs, liberation des apports, attestation de depot, commissaire aux apports]
    champs: [date, banque, montant, signataire]
    nommage: "{date}_Attestation-depot-capital_{banque}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: radiation-societe
      base: Code de commerce art. L.123-22
      sort-final: C
    registre: null
  - type: recepisse-immatriculation
    libelle: "Récépissé d'immatriculation et premier Kbis"
    description: "Récépissé de dépôt du dossier de création, premier extrait Kbis et attestation de parution de l'annonce légale de constitution."
    indices: [immatriculation, kbis, recepisse, guichet unique, greffe, annonce legale de constitution]
    champs: [date, organisme, siren, objet]
    nommage: "{date}_Recepisse-immatriculation_{organisme}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: radiation-societe
      base: Code de commerce art. L.123-22
      sort-final: C
    registre: null
  - type: formulaire-creation-m0
    libelle: Formulaire de création M0 et options fiscales
    description: "Déclaration de création de la société et options fiscales prises à la création, avec la première déclaration des bénéficiaires effectifs."
    indices: [m0, declaration de creation, options fiscales, "regime d'imposition", premiere dbe]
    champs: [date, organisme, siren, nature]
    nommage: "{date}_Formulaire-M0_{organisme}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: radiation-societe
      base: Code de commerce art. L.123-22
      sort-final: C
    registre: null
  - type: declaration-non-condamnation
    libelle: Déclaration de non-condamnation et filiation
    description: Déclaration de non-condamnation du dirigeant et attestation de filiation exigées à la création.
    indices: [non-condamnation, attestation de filiation, "declaration sur l'honneur", dirigeant fondateur]
    champs: [date, dirigeant, lieu]
    nommage: "{date}_Declaration-non-condamnation_{dirigeant}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: radiation-societe
      base: Code civil art. 2224
      sort-final: C
    registre: null
va-ailleurs:
  - motif: Statuts modifiés
    vers: "01.2"
  - motif: Kbis récents
    vers: "97.1"
---

# 01.1 - Constitution

> Chemin : `01 - JURIDIQUE & GOUVERNANCE/01.1 - Constitution`

## À quoi sert ce dossier

Les pièces d'origine de la société, produites une seule fois lors de sa création. Elles ne changent jamais ; les évolutions ultérieures vont dans `01.2` (statuts) et `01.3` (décisions).

## Documents à y ranger

- Statuts constitutifs signés (version d'origine, datée et paraphée)
- Attestation de dépôt du capital (banque ou notaire) et liste des souscripteurs
- Rapport du commissaire aux apports (si apports en nature)
- Attestation de parution de l'annonce légale de constitution
- Récépissé de dépôt / immatriculation (guichet unique INPI, greffe)
- Premier extrait Kbis
- Déclaration initiale des bénéficiaires effectifs (DBE) et récépissé
- Déclaration de non-condamnation et attestation de filiation du dirigeant
- Justificatif de domiciliation du siège (bail, contrat de domiciliation, attestation)
- Options fiscales prises à la création (régime d'IS/IR, TVA) et formulaire M0 / déclaration de création

## Ne pas ranger ici

- Statuts modifiés → `01.2`
- Kbis récents → `Kit administratif` (copie) et `07.1` (courriers greffe)

## Méthode de classement

À plat, sans sous-dossier. Nommage : `AAAA-MM-JJ_Type_Objet.pdf` (ex. `2019-03-12_Statuts_Constitution-signes.pdf`).

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Statuts : 5 ans à compter de la perte de la personnalité morale (radiation). |
| **Recommandé** | Permanent — ce dossier ne se purge jamais. |

Base : Code de commerce, art. L.123-22 et suivants ; art. 2224 du Code civil (prescription de droit commun 5 ans).

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
