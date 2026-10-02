---
schema: classement-documents/3.0
id: "07.5"
parent: "07"
niveau: sous-dossier
titre: "07.5 - Certifications & labels"
usage: >-
  Les certifications, labels, agréments et référencements de l'entreprise : Qualiopi, ISO 9001 /
  27001, label RSE, référencements achats de grands comptes, agrément CIR, French Tech… Un
  dossier par certification, avec l'historique des audits qui permet de préparer le suivant.
classement: par-tiers
sensibilite: normale
documents:
  - type: certificat-certification
    libelle: Certificat de certification ou de label
    description: "Certificat en cours de validité et certificats précédents délivrés par l'organisme certificateur (Qualiopi, ISO 9001, ISO 27001, label RSE)."
    indices: [qualiopi, iso 9001, iso 27001, certificat de conformite, label, agrement]
    champs: [date, organisme, designation, echeance, reference]
    nommage: "{date}_Certificat-de-certification_{organisme}_{designation}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: fin-validite
      base: Code du travail art. L6316-1
      sort-final: C
    registre: null
  - type: rapport-audit-certification
    libelle: "Rapport d'audit de certification"
    description: "Rapport d'audit initial, de surveillance ou de renouvellement établi par l'organisme certificateur, avec les non-conformités relevées."
    indices: [audit de certification, audit de surveillance, audit de renouvellement, non-conformite, "rapport d'audit"]
    champs: [date, organisme, designation, objet, statut]
    nommage: "{date}_Rapport-d-audit_{organisme}_{designation}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: fin-utilisation
      base: Code du travail art. L6316-1
      sort-final: C
    registre: null
  - type: preuve-audit-certification
    libelle: "Preuve fournie à l'audit"
    description: "Copie ou index des preuves documentaires remises à l'audit, y compris le référentiel applicable dans sa version auditée."
    indices: ["preuve d'audit", referentiel applicable, indicateur de resultat, effectivite du distanciel, "piece justificative d'audit"]
    champs: [date, reference, designation, objet]
    nommage: "{date}_Preuve-d-audit_{designation}_{reference}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-utilisation
      base: Code du travail art. L6316-1
      sort-final: D
    registre: null
  - type: plan-actions-non-conformite
    libelle: "Plan d'actions sur non-conformité"
    description: "Plan d'actions correctives répondant aux non-conformités d'un audit, et suivi de sa mise en œuvre jusqu'à la levée."
    indices: ["plan d'actions", non-conformite, action corrective, levee de non-conformite, "suivi d'audit"]
    champs: [date, organisme, objet, echeance, statut]
    nommage: "{date}_Plan-d-actions_{organisme}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-utilisation
      base: Code du travail art. L6316-1
      sort-final: T
    registre: null
  - type: declaration-activite-formation
    libelle: "Déclaration d'activité de formation et BPF"
    description: "Déclaration d'activité de formation avec son numéro, et bilan pédagogique et financier déposé chaque année avant le 31 mai — sa non-transmission rend la déclaration caduque."
    indices: ["declaration d'activite de formation", "numero de declaration d'activite", bilan pedagogique et financier, bpf, caducite]
    champs: [date, organisme, numero, exercice]
    nommage: "{date}_Declaration-activite-formation_{organisme}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: fin-validite
      base: Code du travail art. L6351-1
      sort-final: C
    registre: null
va-ailleurs:
  - motif: Formations suivies par les salariés
    vers: "03.6"
  - motif: "Contrat avec l'organisme certificateur"
    vers: "02.2"
---

# 07.5 - Certifications & labels

> Chemin : `07 - ADMINISTRATIF & ORGANISMES/07.5 - Certifications & labels`

## À quoi sert ce dossier

Les certifications, labels, agréments et référencements de l'entreprise : Qualiopi, ISO 9001 / 27001, label RSE, référencements achats de grands comptes, agrément CIR, French Tech… Un dossier par certification, avec l'historique des audits qui permet de préparer le suivant.

## Documents à y ranger

- Référentiel applicable (copie de la version auditée)
- Dossier de candidature / demande initiale, devis et contrat de l'organisme certificateur
- Preuves fournies à l'audit (copies ou index pointant vers les dossiers d'origine)
- Rapports d'audit (initial, de surveillance, de renouvellement), non-conformités et plans d'actions
- Certificat en cours de validité (copie dans `97/Kit administratif` si demandé par les clients) et certificats précédents
- Correspondance avec l'organisme, calendrier des audits
- Référencements clients : questionnaires fournisseur remplis, chartes signées, scoring reçus
- **Activités déclarées ou réglementées** : déclaration d'activité de formation (numéro de déclaration d'activité), **bilan pédagogique et financier** déposé chaque année avant le 31 mai — sa non-transmission rend la déclaration caduque —, carte professionnelle, agrément, garantie financière selon l'activité

## Ne pas ranger ici

- Formations suivies par les salariés → `03.6`
- Contrat avec l'organisme certificateur → copie ici, original dans `02.2`

## Méthode de classement

**Un sous-dossier par certification ou label**, puis `Referentiel`, `Cycle AAAA-AAAA` (un par cycle de certification : `Audit`, `Preuves`, `Plan d'actions`, `Certificat`), `Correspondance`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Durée de validité + 5 ans ; certaines certifications imposent de garder les preuves du cycle précédent (Qualiopi : cycle de 3 ans). |
| **Recommandé** | Permanent pour les certificats et rapports d'audit ; 10 ans pour les preuves. |

Base : Référentiel de chaque certification ; Code du travail art. L6316-1 (Qualiopi) et L6351-1 (déclaration d'activité).

## Conseils

- Pour un organisme de formation, la **caducité de la déclaration d'activité** faute de bilan pédagogique et financier est l'accident administratif classique : l'échéance du 31 mai mérite une ligne dans le registre des contrats.
- Le référentiel Qualiopi a été renforcé par un décret du 1er août 2026, applicable aux audits à compter du 1er novembre 2026 : de nouvelles preuves documentaires sont attendues, notamment sur la méthode de calcul des indicateurs de résultats, l'effectivité du distanciel et la formalisation contractuelle de la sous-traitance.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
