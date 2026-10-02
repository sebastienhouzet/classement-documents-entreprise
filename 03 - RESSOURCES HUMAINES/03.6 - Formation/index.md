---
schema: classement-documents/3.0
id: "03.6"
parent: "03"
niveau: sous-dossier
titre: 03.6 - Formation
usage: >-
  Les actions de formation des salariés et du dirigeant : plan de développement des compétences,
  conventions, convocations, attestations, prises en charge OPCO.
classement: chronologique
sensibilite: rh
documents:
  - type: convention-de-formation
    libelle: Convention de formation
    description: "Convention signée avec l'organisme de formation, son programme et le devis accepté."
    indices: [convention de formation, organisme de formation, programme, devis accepté, convocation]
    champs: [date, organisme-formation, objet, montant, date-debut, date-fin]
    nommage: "{date}_Convention-de-formation_{organisme-formation}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: date-document
      base: Code du travail L6321-1
      sort-final: D
    registre: null
  - type: attestation-formation
    libelle: Attestation de fin de formation
    description: "Attestation de présence, de fin de formation ou certificat individuel, avec une copie au dossier du salarié."
    indices: [attestation de formation, certificat de formation, émargement, présence, certificat]
    champs: [date, salarie, organisme-formation, objet]
    nommage: "{date}_Attestation-de-formation_{salarie}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: depart-salarie
      base: Code du travail L6321-1
      sort-final: D
    registre: null
  - type: attestation-formation-securite
    libelle: Attestation de formation sécurité
    description: "SST, habilitation électrique, incendie : attestation et date de recyclage."
    indices: [sst, habilitation électrique, incendie, recyclage, formation obligatoire]
    champs: [date, salarie, organisme-formation, objet, echeance]
    nommage: "{date}_Attestation-securite_{salarie}_{objet}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: depart-salarie
      base: Code du travail L6321-1
      sort-final: C
    registre: null
  - type: prise-en-charge-opco
    libelle: Prise en charge OPCO
    description: "Demande et accord de prise en charge par l'OPCO, et le remboursement correspondant."
    indices: [opco, prise en charge, remboursement, financement, dossier]
    champs: [date, organisme, numero-dossier, montant]
    nommage: "{date}_Prise-en-charge-OPCO_{organisme}_{numero-dossier}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: date-document
      base: Code du travail L6321-1
      sort-final: D
    registre: null
  - type: plan-developpement-competences
    libelle: Plan de développement des compétences
    description: Plan annuel de formation et sa consultation du CSE le cas échéant.
    indices: [plan de développement des compétences, plan de formation, entretien professionnel, consultation, annuel]
    champs: [exercice, objet, effectif, montant]
    nommage: "{exercice}_Plan-de-developpement-des-competences"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: date-document
      base: Code du travail L6321-1
      sort-final: D
    registre: null
va-ailleurs:
  - motif: Factures de formation
    vers: "04.3"
  - motif: "Certification Qualiopi de l'entreprise (si elle est elle-même organisme de formation)"
    vers: "07.5"
---

# 03.6 - Formation

> Chemin : `03 - RESSOURCES HUMAINES/03.6 - Formation`

## À quoi sert ce dossier

Les actions de formation des salariés et du dirigeant : plan de développement des compétences, conventions, convocations, attestations, prises en charge OPCO. Ces pièces justifient les financements obtenus et prouvent que l'employeur respecte son obligation d'adaptation des salariés.

## Documents à y ranger

- Plan de développement des compétences annuel (et consultation du CSE si ≥ 50)
- Conventions de formation, programmes, devis acceptés
- Convocations, feuilles d'émargement, attestations de présence et de fin de formation, certificats
- Demandes et accords de prise en charge OPCO, remboursements
- Entretiens professionnels : trame, calendrier (les comptes rendus individuels → `03.2`)
- Formations obligatoires sécurité (SST, habilitation électrique, incendie) : attestations et dates de recyclage

## Ne pas ranger ici

- Factures de formation → `04.3`
- Certification Qualiopi de l'entreprise (si elle est elle-même organisme de formation) → `07.5`

## Méthode de classement

**Par année, puis par action** : `AAAA/AAAA-MM - Intitulé - Organisme/`. Une copie de chaque attestation individuelle est aussi rangée dans le dossier du salarié (`03.2/02 Vie du contrat`).

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | 5 ans (contrôle de l'OPCO et de l'URSSAF) ; attestations individuelles : durée du contrat + 5 ans. |
| **Recommandé** | 10 ans (aligné sur les factures) ; permanent pour les attestations de formation sécurité. |

Base : Code du travail art. L.6321-1 (obligation de formation), L.6315-1 (entretien professionnel) ; Code de commerce art. L.123-22.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
