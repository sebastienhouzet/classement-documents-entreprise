---
schema: classement-documents/3.0
id: "05.3"
parent: "05"
niveau: sous-dossier
titre: "05.3 - Aides & subventions"
usage: >-
  Les financements publics et assimilés : subventions (conseil régional, Bpifrance, ADEME, fonds
  européens), aides à l'embauche, crédit d'impôt recherche / innovation (CIR / CII), statut JEI,
  exonérations.
classement: par-operation
sensibilite: confidentielle
documents:
  - type: convention-subvention
    libelle: "Convention de subvention et décision d'attribution"
    description: "Décision d'attribution, notification et convention de subvention signée avec l'organisme financeur, avec ses avenants."
    indices: [convention de subvention, "decision d'attribution", notification, bpifrance, ademe, conseil regional, fonds europeens]
    champs: [date-signature, organisme, numero-dossier, montant, objet]
    nommage: "{date}_Convention-de-subvention_{organisme}_{objet}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: derniere-operation
      base: Convention de chaque dispositif
      sort-final: C
    registre: null
  - type: dossier-demande-subvention
    libelle: "Dossier de demande d'aide"
    description: "Dossier de demande tel que déposé — formulaire, budget du projet, annexes et pièces fournies à l'organisme."
    indices: [dossier de demande, formulaire de demande, budget du projet, pieces fournies, depot de dossier]
    champs: [date, organisme, numero-dossier, montant, objet]
    nommage: "{date}_Dossier-de-demande_{organisme}_{objet}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: derniere-operation
      base: Convention de chaque dispositif
      sort-final: D
    registre: null
  - type: justificatif-depenses-eligibles
    libelle: Justificatifs des dépenses éligibles
    description: "Copies des factures, feuilles de temps et bulletins des personnes affectées au projet, constituant la preuve des dépenses éligibles."
    indices: [depenses eligibles, feuille de temps, justificatif de depense, personnel affecte, copie de facture]
    champs: [exercice, organisme, numero-dossier, montant, effectif]
    nommage: "{exercice}_Justificatifs-depenses_{organisme}_{numero-dossier}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: derniere-operation
      base: LPF art. L.169
      sort-final: D
    registre: null
  - type: dossier-cir-cii
    libelle: "Dossier justificatif CIR, CII ou JEI"
    description: "Dossier justificatif technique et financier du CIR ou du CII pour une année, formulaire 2069-A, rescrit et attestations d'éligibilité JEI."
    indices: [cir, cii, jei, 2069-a, rescrit, dossier justificatif technique, "credit d'impot recherche"]
    champs: [exercice, montant, effectif, objet, numero-dossier]
    nommage: "{exercice}_Dossier-CIR_{objet}"
    conservation:
      legale: 3a
      recommandee: 10a
      declencheur: cloture-exercice
      base: CGI art. 244 quater B
      sort-final: T
    registre: null
  - type: demande-versement-subvention
    libelle: "Demande de versement et rapport d'avancement"
    description: "Rapports d'avancement et rapport final, demandes de versement et avis de paiement de l'organisme."
    indices: [demande de versement, "rapport d'avancement", rapport final, avis de paiement, solde de subvention]
    champs: [date, organisme, numero-dossier, montant, periode]
    nommage: "{date}_Demande-de-versement_{organisme}_{numero-dossier}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: derniere-operation
      base: Convention de chaque dispositif
      sort-final: D
    registre: null
va-ailleurs:
  - motif: Levée de fonds privée
    vers: "05.4"
  - motif: "Prêts d'honneur et prêts Bpifrance (à rembourser)"
    vers: "05.2"
---

# 05.3 - Aides & subventions

> Chemin : `05 - BANQUE & FINANCEMENT/05.3 - Aides & subventions`

## À quoi sert ce dossier

Les financements publics et assimilés : subventions (conseil régional, Bpifrance, ADEME, fonds européens), aides à l'embauche, crédit d'impôt recherche / innovation (CIR / CII), statut JEI, exonérations. Ces dossiers doivent pouvoir être rejoués intégralement en cas de contrôle, souvent longtemps après.

## Documents à y ranger

- Dossier de demande complet tel que déposé (formulaire, budget, annexes, pièces)
- Décision d'attribution, convention de subvention, notification
- Justificatifs des dépenses éligibles (copies des factures, feuilles de temps, bulletins des personnes affectées au projet)
- Rapports d'avancement et rapport final, demandes de versement, avis de paiement
- CIR / CII : dossier justificatif technique et financier de chaque année, formulaire 2069-A, rescrit, expertise éventuelle
- JEI : rescrit, attestations annuelles d'éligibilité, calcul des exonérations
- Aides à l'embauche (ASP, France Travail) : demande, décision, attestations
- Contrôles : demandes de l'organisme, réponses, conclusions

## Ne pas ranger ici

- Levée de fonds privée → `05.4`
- Prêts d'honneur et prêts Bpifrance (à rembourser) → `05.2`

## Méthode de classement

**Un sous-dossier par dispositif et par année d'obtention** : `AAAA - Organisme - Dispositif` (ex. `2025 - Bpifrance - Bourse French Tech`, `2025 - CIR`). À l'intérieur : `Demande`, `Convention`, `Justificatifs`, `Rapports et versements`, `Controle`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Durée fixée par la convention (souvent 10 ans après le dernier versement ; fonds européens : 10 ans). CIR/CII : jusqu'à la fin du délai de reprise (3 ans après l'année de dépôt) — mais le dossier technique doit rester consultable. |
| **Recommandé** | 10 ans après le dernier versement pour tout. |

Base : Convention de chaque dispositif ; CGI art. 244 quater B (CIR) ; LPF art. L.169.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
