---
schema: classement-documents/3.0
id: "05.4"
parent: "05"
niveau: sous-dossier
titre: "05.4 - Investisseurs & levées de fonds"
usage: >-
  Chaque opération d'apport de fonds propres ou quasi-fonds propres : love money, BSA-AIR, seed,
  série A, entrée d'un associé industriel, ainsi que le reporting régulier dû aux investisseurs.
classement: par-operation
sensibilite: confidentielle
documents:
  - type: term-sheet-levee
    libelle: "Term sheet et lettre d'intention"
    description: "Term sheet, lettre d'intention et accord d'exclusivité signés avec un investisseur avant le closing."
    indices: [term sheet, "lettre d'intention", loi, exclusivite, valorisation pre-money]
    champs: [date-signature, tiers, montant, objet, echeance]
    nommage: "{date}_Term-sheet_{tiers}_{objet}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: date-document
      base: Code civil art. 2224
      sort-final: T
    registre: null
  - type: due-diligence-levee
    libelle: "Due diligence et data room de l'opération"
    description: "Deck et documents de présentation transmis, index et export de la data room, questions-réponses et rapports de due diligence."
    indices: [due diligence, data room, deck investisseurs, questions reponses, "rapport d'audit d'acquisition"]
    champs: [date, tiers, objet, confidentiel]
    nommage: "{date}_Due-diligence_{tiers}_{objet}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: date-document
      base: Code civil art. 2224
      sort-final: T
    registre: null
  - type: contrat-investissement
    libelle: "Contrat d'investissement, BSA-AIR ou obligation convertible"
    description: "Contrat d'investissement signé, BSA-AIR ou contrat d'émission d'obligations convertibles de l'opération."
    indices: ["contrat d'investissement", bsa-air, obligation convertible, closing, seed, serie a]
    champs: [date-signature, tiers, numero, montant, quantite]
    nommage: "{date}_Contrat-investissement_{tiers}_{numero}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: date-document
      base: Code de commerce art. L.225-127
      sort-final: C
    registre: null
  - type: bulletin-souscription-levee
    libelle: Bulletin de souscription et dépôt des fonds
    description: "Bulletins de souscription de nos titres, attestation bancaire de dépôt des fonds et rapport du commissaire aux apports."
    indices: [bulletin de souscription, attestation de depot des fonds, commissaire aux apports, liberation des apports, rapport cac]
    champs: [date, associe, quantite, montant, banque]
    nommage: "{date}_Bulletin-de-souscription_{associe}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: date-document
      base: Code de commerce art. L.225-127
      sort-final: C
    registre: null
  - type: reporting-investisseurs
    libelle: Reporting investisseurs
    description: "Reporting mensuel ou trimestriel adressé aux investisseurs, et comptes rendus de board ou de comité stratégique."
    indices: [reporting investisseurs, compte rendu de board, comite strategique, kpi mensuels, reporting trimestriel]
    champs: [periode, destinataire, objet, montant]
    nommage: "{periode}_Reporting-investisseurs_{destinataire}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: date-document
      base: Code civil art. 2224
      sort-final: D
    registre: null
va-ailleurs:
  - motif: Subventions et aides publiques
    vers: "05.3"
  - motif: "Comptes courants d'associés"
    vers: "01.6"
---

# 05.4 - Investisseurs & levées de fonds

> Chemin : `05 - BANQUE & FINANCEMENT/05.4 - Investisseurs & levées de fonds`

## À quoi sert ce dossier

Chaque opération d'apport de fonds propres ou quasi-fonds propres : love money, BSA-AIR, seed, série A, entrée d'un associé industriel, ainsi que le reporting régulier dû aux investisseurs. Les pièces juridiques définitives (pacte, registre des titres) vivent dans `01.6` ; ici, le dossier de l'opération.

## Documents à y ranger

- Deck et documents de présentation transmis, data room (index et export)
- Term sheet / lettre d'intention, accords d'exclusivité
- Due diligence : questions/réponses, rapports
- Contrats d'investissement, BSA-AIR, contrats d'émission d'obligations convertibles
- Bulletins de souscription, attestation de dépôt des fonds, rapport CAC / commissaire aux apports
- Pacte d'associés signé (copie — original dans `01.6`), PV d'AGE (copie — original dans `01.3`)
- Formalités post-opération : Kbis mis à jour, statuts (copie), déclaration des bénéficiaires effectifs
- Reporting investisseurs (mensuel / trimestriel), comptes rendus de board ou de comité stratégique

## Ne pas ranger ici

- Subventions et aides publiques → `05.3`
- Comptes courants d'associés → `01.6`

## Méthode de classement

**Un sous-dossier par opération** : `AAAA - Nom de l'opération` (ex. `2026 - Seed 500k`). À l'intérieur : `Preparation`, `Negociation`, `Closing`, `Post-closing`. Un sous-dossier `Reporting/AAAA` à la racine pour le reporting régulier.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | 5 ans après l'opération (prescription) ; les titres et le pacte : permanent. |
| **Recommandé** | Permanent. |

Base : Code civil art. 2224 ; Code de commerce art. L.225-127 et s.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
