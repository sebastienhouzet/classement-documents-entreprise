---
schema: classement-documents/3.0
id: "06.6"
parent: "06"
niveau: sous-dossier
titre: "06.6 - Homme-clé & RC des dirigeants"
usage: >-
  Les assurances qui protègent l'entreprise et ses dirigeants en tant que personnes :
  responsabilité civile des mandataires sociaux (RCMS / D&O), assurance homme-clé (décès ou
  incapacité du dirigeant), protection juridique.
classement: par-contrat
sensibilite: confidentielle
documents:
  - type: contrat-rcms-dirigeants
    libelle: Contrat de RC des mandataires sociaux
    description: "Contrat RCMS / D&O — conditions, déclarations annuelles et attestation — il fonctionne souvent en base réclamation."
    indices: [rcms, "d&o", rc des mandataires sociaux, base reclamation, declaration annuelle]
    champs: [date-effet, assureur, numero-contrat, dirigeant, montant, plafond-garantie, franchise]
    nommage: "{date}_Contrat-RCMS_{assureur}_{numero-contrat}"
    conservation:
      legale: 2a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code des assurances art. L.124-5
      sort-final: C
    registre: { fichier: Registre-des-assurances.csv, cle: numero-contrat }
  - type: contrat-homme-cle
    libelle: Contrat homme-clé
    description: "Contrat homme-clé (décès ou incapacité du dirigeant), bénéficiaire désigné et questionnaire médical — pièce sensible, accès restreint."
    indices: [homme-cle, personne-cle, questionnaire medical, beneficiaire designe, incapacite du dirigeant]
    champs: [date-effet, assureur, numero-contrat, dirigeant, beneficiaire, confidentiel, plafond-garantie]
    nommage: "{date}_Contrat-homme-cle_{assureur}_{dirigeant}"
    conservation:
      legale: 2a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code des assurances art. L.114-1
      sort-final: C
    registre: { fichier: Registre-des-assurances.csv, cle: numero-contrat }
  - type: contrat-protection-juridique
    libelle: Contrat de protection juridique professionnelle
    description: "Contrat de protection juridique professionnelle — conditions, domaines couverts et seuils d'intervention."
    indices: [protection juridique, "seuil d'intervention", prise en charge des honoraires, assistance juridique]
    champs: [date-effet, assureur, numero-contrat, montant, objet, plafond-garantie, franchise]
    nommage: "{date}_Contrat-protection-juridique_{assureur}_{numero-contrat}"
    conservation:
      legale: 2a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code des assurances art. L.124-5
      sort-final: C
    registre: { fichier: Registre-des-assurances.csv, cle: numero-contrat }
  - type: quittance-assurance-dirigeant
    libelle: Quittance de prime des assurances du dirigeant
    description: "Quittance ou appel de prime des contrats RCMS, homme-clé et protection juridique, et courriers de l'assureur."
    indices: [quittance rcms, appel de prime, quittance homme-cle, "avis d'echeance", "courrier de l'assureur"]
    champs: [periode, assureur, numero-contrat, montant, dirigeant]
    nommage: "{periode}_Quittance-assurance-dirigeant_{assureur}"
    conservation:
      legale: 2a
      recommandee: 10a
      declencheur: date-document
      base: Code des assurances art. L.114-1
      sort-final: D
    registre: null
va-ailleurs:
  - motif: Mandats et nominations des dirigeants
    vers: "01.5"
---

# 06.6 - Homme-clé & RC des dirigeants

> Chemin : `06 - ASSURANCES/06.6 - Homme-clé & RC des dirigeants`

## À quoi sert ce dossier

Les assurances qui protègent l'entreprise et ses dirigeants en tant que personnes : responsabilité civile des mandataires sociaux (RCMS / D&O), assurance homme-clé (décès ou incapacité du dirigeant), protection juridique.

## Documents à y ranger

- RC des mandataires sociaux : contrat, conditions, déclarations annuelles, attestation
- Homme-clé : contrat, questionnaire médical (pièce sensible — accès restreint), bénéficiaire désigné
- Protection juridique professionnelle : contrat, conditions, seuils d'intervention
- Quittances, courriers

## Ne pas ranger ici

- Mandats et nominations des dirigeants → `01.5`

## Méthode de classement

**Un sous-dossier par contrat** `Assureur - N° contrat`, puis `Contrat`, `Attestations/AAAA`, `Quittances/AAAA`, `Courriers`. En cas de changement d'assureur, garder l'ancien contrat dans son propre sous-dossier (ne pas fusionner).

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | 2 ans après la fin du contrat. |
| **Recommandé** | 10 ans après la fin du contrat (la RCMS fonctionne souvent en « base réclamation » : les faits anciens peuvent être invoqués). |

Base : Code des assurances art. L.114-1, L.124-5.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
