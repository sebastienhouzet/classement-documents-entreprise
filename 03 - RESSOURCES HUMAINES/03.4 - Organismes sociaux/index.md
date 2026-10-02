---
schema: classement-documents/3.0
id: "03.4"
parent: "03"
niveau: sous-dossier
titre: 03.4 - Organismes sociaux
usage: >-
  La relation avec chaque organisme social : immatriculations, attestations, courriers,
  contrôles, échéanciers, adhésions.
classement: par-tiers
sensibilite: rh
documents:
  - type: attestation-vigilance-entreprise
    libelle: Notre attestation de vigilance URSSAF
    description: "Attestation de vigilance délivrée à l'entreprise par l'URSSAF, remise à ses clients et donneurs d'ordre."
    indices: [attestation de vigilance, urssaf, vigilance, régularité sociale, "donneur d'ordre"]
    champs: [date, organisme, numero, date-fin]
    nommage: "{date}_Attestation-vigilance_{organisme}"
    conservation:
      legale: 6a
      recommandee: 10a
      declencheur: date-document
      base: Code du travail L8222-1
      sort-final: D
    registre: null
  - type: controle-urssaf
    libelle: Dossier de contrôle URSSAF
    description: "Avis de contrôle, lettre d'observations, réponses de l'entreprise et mise en recouvrement."
    indices: [contrôle urssaf, "lettre d'observations", mise en demeure, rescrit social, redressement]
    champs: [date, organisme, numero-dossier, objet, montant]
    nommage: "{date}_Controle_{organisme}_{numero-dossier}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: date-document
      base: Code de la sécurité sociale L243-7
      sort-final: C
    registre: null
  - type: due-regime-social
    libelle: DUE ou accord mettant en place un régime social
    description: "Décision unilatérale de l'employeur ou accord instituant la prévoyance et la mutuelle, et les notices d'information remises aux salariés."
    indices: [due, décision unilatérale, mutuelle obligatoire, prévoyance, "notice d'information"]
    champs: [date, organisme, assureur, objet, date-effet]
    nommage: "{date}_DUE_{objet}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: fin-contrat
      base: Code de la sécurité sociale L243-16
      sort-final: C
    registre: null
  - type: adhesion-organisme-social
    libelle: Adhésion ou immatriculation à un organisme social
    description: "Immatriculation URSSAF, adhésion AGIRC-ARRCO, SPST, OPCO, affiliation SSI du dirigeant."
    indices: [adhésion, immatriculation, agirc-arrco, opco, spst, médecine du travail, ssi]
    champs: [date, organisme, numero, reference, date-effet]
    nommage: "{date}_Adhesion_{organisme}"
    conservation:
      legale: 6a
      recommandee: permanent
      declencheur: date-document
      base: Code de la sécurité sociale L243-16
      sort-final: C
    registre: null
va-ailleurs:
  - motif: Bordereaux mensuels de cotisations
    vers: "03.3"
  - motif: "Contrats d'assurance mutuelle et prévoyance"
    vers: "06.4"
---

# 03.4 - Organismes sociaux

> Chemin : `03 - RESSOURCES HUMAINES/03.4 - Organismes sociaux`

## À quoi sert ce dossier

La relation avec chaque organisme social : immatriculations, attestations, courriers, contrôles, échéanciers, adhésions. Concerne aussi bien les organismes des salariés que ceux du dirigeant (SSI, URSSAF TNS).

## Documents à y ranger

- **URSSAF** : immatriculation, attestations de vigilance (par date), échéanciers, courriers, mises en demeure, contrôles (avis, lettre d'observations, réponses), rescrits sociaux
- **Retraite complémentaire (AGIRC-ARRCO)** : adhésion, courriers
- **Prévoyance et mutuelle** : décision unilatérale de l'employeur (DUE) ou accord mettant en place le régime, notices d'information remises aux salariés, bulletins d'affiliation, attestations, courriers (le contrat d'assurance lui-même → `06.4`)
- **Médecine du travail (SPST)** : adhésion, appels de cotisation, fiche d'entreprise
- **OPCO** : adhésion, attestations de versement
- **Dirigeant TNS** : affiliation SSI/URSSAF, déclarations de revenus (DSI / volet social), attestations
- **France Travail, CPAM, CAF** : courriers employeur

## Ne pas ranger ici

- Bordereaux mensuels de cotisations → `03.3`
- Contrats d'assurance mutuelle et prévoyance → `06.4`

## Méthode de classement

**Un sous-dossier par organisme**. À l'intérieur : `Adhesion`, `Attestations` (par date), `Courriers/AAAA`, `Controles` (un sous-dossier par contrôle).

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Documents nécessaires au contrôle des cotisations : 6 ans. Contrôle URSSAF : 5 ans après (délai de reprise 3 ans, 5 en cas de travail dissimulé). DUE et notices : durée du régime + 5 ans. |
| **Recommandé** | 10 ans. Permanent pour les adhésions, DUE et dossiers de contrôle. |

Base : Code de la sécurité sociale art. L243-16 (conservation pour le contrôle, 6 ans), L244-3 (prescription du recouvrement, 3 ans) et L243-7 ; Code du travail art. L8222-1.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
