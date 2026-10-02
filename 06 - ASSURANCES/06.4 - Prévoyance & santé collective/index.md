---
schema: classement-documents/3.0
id: "06.4"
parent: "06"
niveau: sous-dossier
titre: "06.4 - Prévoyance & santé collective"
usage: >-
  Les contrats collectifs au bénéfice des salariés (mutuelle obligatoire, prévoyance : décès,
  incapacité, invalidité) et les contrats du dirigeant (prévoyance TNS, Madelin, GSC / assurance
  perte d'emploi).
classement: par-contrat
sensibilite: rh
documents:
  - type: contrat-prevoyance-collective
    libelle: Contrat collectif de prévoyance ou de santé
    description: "Contrat collectif de mutuelle obligatoire ou de prévoyance (décès, incapacité, invalidité) — conditions, tableaux de garanties et avenants. La DUE et les notices restent en 03.4."
    indices: [mutuelle obligatoire, complementaire sante, prevoyance collective, tableau de garanties, deces incapacite invalidite]
    champs: [date-effet, assureur, numero-contrat, effectif, montant, plafond-garantie]
    nommage: "{date}_Contrat-prevoyance-collective_{assureur}_{numero-contrat}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: fin-contrat
      base: Code des assurances art. L.114-1
      sort-final: C
    registre: { fichier: Registre-des-assurances.csv, cle: numero-contrat }
  - type: contrat-prevoyance-dirigeant
    libelle: Contrat de prévoyance du dirigeant
    description: "Contrats individuels du dirigeant — prévoyance TNS, retraite Madelin, GSC (perte d'emploi), PER entreprise."
    indices: [prevoyance tns, madelin, gsc, "perte d'emploi du dirigeant", per entreprise, retraite supplementaire]
    champs: [date-effet, assureur, numero-contrat, dirigeant, montant, plafond-garantie]
    nommage: "{date}_Contrat-prevoyance-dirigeant_{assureur}_{dirigeant}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: fin-contrat
      base: Code des assurances art. L.114-1
      sort-final: C
    registre: { fichier: Registre-des-assurances.csv, cle: numero-contrat }
  - type: attestation-contrat-responsable
    libelle: Attestation annuelle et certificat de contrat responsable
    description: Attestation annuelle du contrat collectif et certificat de conformité « contrat responsable ».
    indices: [attestation annuelle, contrat responsable, certificat de conformite, attestation mutuelle]
    champs: [exercice, assureur, numero-contrat, effectif]
    nommage: "{exercice}_Attestation-contrat-responsable_{assureur}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: fin-contrat
      base: Code des assurances art. L.114-1
      sort-final: D
    registre: null
  - type: quittance-prevoyance-sante
    libelle: Quittance de prime prévoyance et santé
    description: "Quittance ou appel de prime des contrats collectifs et du dirigeant, courriers d'indexation et de changement de garanties."
    indices: [quittance mutuelle, appel de prime, indexation, changement de garanties, resiliation du contrat collectif]
    champs: [periode, assureur, numero-contrat, montant, effectif]
    nommage: "{periode}_Quittance-prevoyance-sante_{assureur}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: date-document
      base: Code des assurances art. L.114-1
      sort-final: D
    registre: null
va-ailleurs:
  - motif: "DUE, notices d'information, affiliations et dispenses des salariés"
    vers: "03.4"
---

# 06.4 - Prévoyance & santé collective

> Chemin : `06 - ASSURANCES/06.4 - Prévoyance & santé collective`

## À quoi sert ce dossier

Les contrats collectifs au bénéfice des salariés (mutuelle obligatoire, prévoyance : décès, incapacité, invalidité) et les contrats du dirigeant (prévoyance TNS, Madelin, GSC / assurance perte d'emploi). Les documents de mise en place du régime (DUE, notices, affiliations) sont dans `03.4`.

## Documents à y ranger

- Contrats collectifs (mutuelle, prévoyance) : conditions particulières et générales, tableaux de garanties, avenants
- Contrats individuels du dirigeant : prévoyance TNS, retraite Madelin, GSC
- Attestations annuelles, certificats de conformité (contrat responsable), quittances
- Courriers de l'assureur : indexation, changement de garanties, résiliation
- Contrat de retraite supplémentaire (PER entreprise) le cas échéant

## Ne pas ranger ici

- DUE, notices d'information, affiliations et dispenses des salariés → `03.4` et `03.2`

## Méthode de classement

**Un sous-dossier par contrat** `Assureur - N° contrat`, puis `Contrat`, `Attestations/AAAA`, `Quittances/AAAA`, `Courriers`. En cas de changement d'assureur, garder l'ancien contrat dans son propre sous-dossier (ne pas fusionner).

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Durée du contrat + 5 ans (contentieux salariés) ; prescription assurance 2 ans (10 ans pour les bénéficiaires en cas de décès). |
| **Recommandé** | Permanent — les droits ouverts (invalidité, rente de conjoint) peuvent être invoqués des décennies plus tard. |

Base : Code des assurances art. L.114-1, L.124-5.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
