---
schema: classement-documents/3.0
id: "06.1"
parent: "06"
niveau: sous-dossier
titre: 06.1 - Responsabilité civile professionnelle
usage: >-
  La RC Pro (et RC exploitation) couvre les dommages causés aux clients et aux tiers dans le
  cadre de l'activité. C'est l'attestation la plus demandée par les clients et les donneurs
  d'ordre.
classement: par-contrat
sensibilite: normale
documents:
  - type: contrat-rc-pro
    libelle: Contrat de responsabilité civile professionnelle
    description: "Conditions particulières et générales de la RC professionnelle et de la RC exploitation, et leurs avenants."
    indices: [rc professionnelle, rc pro, rc exploitation, conditions particulieres, avenant, responsabilite civile professionnelle]
    champs: [date-effet, assureur, numero-contrat, montant, objet, plafond-garantie, franchise]
    nommage: "{date}_Contrat-RC-pro_{assureur}_{numero-contrat}"
    conservation:
      legale: 2a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code des assurances art. L.124-5
      sort-final: C
    registre: { fichier: Registre-des-assurances.csv, cle: numero-contrat }
  - type: questionnaire-souscription-rc-pro
    libelle: Questionnaire de souscription RC Pro
    description: "Questionnaire de souscription et déclarations annuelles d'activité (activités couvertes, chiffre d'affaires déclaré) — elles conditionnent la garantie."
    indices: [questionnaire de souscription, "declaration d'activite", activites couvertes, "chiffre d'affaires declare"]
    champs: [exercice, assureur, numero-contrat, montant, objet]
    nommage: "{exercice}_Questionnaire-souscription-RC-pro_{assureur}"
    conservation:
      legale: 2a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code des assurances art. L.114-1
      sort-final: C
    registre: null
  - type: attestation-rc-pro
    libelle: Attestation de RC professionnelle
    description: "Attestation annuelle d'assurance RC Pro, la plus demandée par les clients et les donneurs d'ordre (copie de l'année en cours dans 97/Kit administratif)."
    indices: [attestation rc pro, "attestation d'assurance", "donneur d'ordre", kit administratif, annee en cours]
    champs: [exercice, assureur, numero-contrat, echeance]
    nommage: "{exercice}_Attestation-RC-pro_{assureur}"
    conservation:
      legale: 2a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code des assurances art. L.124-5
      sort-final: D
    registre: null
  - type: quittance-rc-pro
    libelle: Quittance de prime RC Pro
    description: "Quittance ou appel de prime de la RC professionnelle, avis d'échéance et courriers de l'assureur ou du courtier (la facture va en 04.3)."
    indices: [quittance, appel de prime, "avis d'echeance", "courrier de l'assureur", courtier, resiliation]
    champs: [periode, assureur, numero-contrat, montant]
    nommage: "{periode}_Quittance-RC-pro_{assureur}"
    conservation:
      legale: 2a
      recommandee: 10a
      declencheur: date-document
      base: Code des assurances art. L.114-1
      sort-final: D
    registre: null
va-ailleurs:
  - motif: "Déclaration d'un sinistre"
    vers: "06.7"
---

# 06.1 - Responsabilité civile professionnelle

> Chemin : `06 - ASSURANCES/06.1 - Responsabilité civile professionnelle`

## À quoi sert ce dossier

La RC Pro (et RC exploitation) couvre les dommages causés aux clients et aux tiers dans le cadre de l'activité. C'est l'attestation la plus demandée par les clients et les donneurs d'ordre.

## Documents à y ranger

- Conditions particulières, conditions générales (de la version applicable), avenants
- Questionnaire de souscription et déclarations d'activité (activités couvertes, chiffre d'affaires déclaré chaque année)
- Attestations annuelles d'assurance (copie de l'année en cours dans `97/Kit administratif`)
- Quittances / appels de prime (factures → `04.3`)
- Courriers de l'assureur ou du courtier, avis d'échéance, résiliation

## Ne pas ranger ici

- Déclaration d'un sinistre → `06.7`

## Méthode de classement

**Un sous-dossier par contrat** `Assureur - N° contrat`, puis `Contrat`, `Attestations/AAAA`, `Quittances/AAAA`, `Courriers`. En cas de changement d'assureur, garder l'ancien contrat dans son propre sous-dossier (ne pas fusionner).

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | 2 ans après la fin du contrat (prescription) ; en pratique la garantie subséquente et les réclamations tardives imposent plus. |
| **Recommandé** | 10 ans après la fin du contrat — permanent si des prestations à risque (conseil, développement, hébergement) ont été réalisées. |

Base : Code des assurances art. L.114-1, L.124-5.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
