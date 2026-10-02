---
schema: classement-documents/3.0
id: "06.7"
parent: "06"
niveau: sous-dossier
titre: 06.7 - Sinistres
usage: >-
  Chaque sinistre déclaré, quel que soit le contrat concerné : dégât des eaux, vol de matériel,
  accident de véhicule, réclamation d'un client, incident cyber.
classement: par-operation
sensibilite: confidentielle
documents:
  - type: declaration-sinistre
    libelle: Déclaration de sinistre
    description: "Déclaration du sinistre à l'assureur avec la preuve d'envoi dans le délai (2 jours ouvrés pour un vol, 5 pour les autres) et la synthèse du dossier."
    indices: [declaration de sinistre, delai de declaration, "preuve d'envoi", numero de sinistre, circonstances]
    champs: [date, assureur, numero-sinistre, numero-contrat, montant, objet, franchise]
    nommage: "{date}_Declaration-de-sinistre_{assureur}_{objet}"
    conservation:
      legale: 2a
      recommandee: 10a
      declencheur: date-document
      base: Code des assurances art. L113-2
      sort-final: D
    registre: null
  - type: rapport-expertise-sinistre
    libelle: Expertise et pièces de constat
    description: "Constats, photos, plaintes, témoignages, rapports d'intervention, rapport d'expertise et contre-expertise, échanges avec l'expert et le courtier."
    indices: [constat amiable, "rapport d'expertise", contre-expertise, photos du sinistre, plainte, temoignage]
    champs: [date, assureur, numero-sinistre, montant, objet]
    nommage: "{date}_Rapport-d-expertise_{assureur}_{numero-sinistre}"
    conservation:
      legale: 2a
      recommandee: 10a
      declencheur: date-document
      base: Code des assurances art. L114-1
      sort-final: D
    registre: null
  - type: decompte-indemnisation-sinistre
    libelle: "Décompte d'indemnisation"
    description: "Lettre d'acceptation, décompte d'indemnisation, franchise appliquée, avis de règlement et clôture du dossier de sinistre."
    indices: ["decompte d'indemnite", avis de reglement, "lettre d'acceptation", franchise appliquee, cloture du sinistre]
    champs: [date, assureur, numero-sinistre, montant, statut, franchise]
    nommage: "{date}_Decompte-d-indemnisation_{assureur}_{numero-sinistre}"
    conservation:
      legale: 2a
      recommandee: 10a
      declencheur: reglement-sinistre
      base: Code des assurances art. L114-2
      sort-final: D
    registre: null
  - type: dossier-sinistre-dommage-corporel
    libelle: Dossier de sinistre avec dommage corporel
    description: "Dossier d'un sinistre ayant causé un dommage corporel — pièces médicales de consolidation, évaluation du préjudice et offre d'indemnisation. Le délai court dix ans à compter de la consolidation du dommage, souvent bien après le règlement."
    indices: [dommage corporel, consolidation du dommage, prejudice corporel, victime, "offre d'indemnisation"]
    champs: [date, assureur, numero-sinistre, tiers, montant]
    nommage: "{date}_Dossier-sinistre-corporel_{numero-sinistre}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: consolidation-dommage
      base: Code civil art. 2226
      sort-final: D
    registre: null
  - type: recours-contre-tiers-sinistre
    libelle: Recours contre un tiers
    description: "Recours exercé contre un tiers responsable, ou réclamation reçue d'un tiers, à l'occasion d'un sinistre — dix ans pour une réclamation d'un tiers."
    indices: [recours contre un tiers, "reclamation d'un tiers", tiers responsable, "subrogation de l'assureur"]
    champs: [date, tiers, numero-sinistre, montant, objet]
    nommage: "{date}_Recours-contre-tiers_{tiers}_{numero-sinistre}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: date-document
      base: Code des assurances art. L114-1
      sort-final: D
    registre: null
va-ailleurs:
  - motif: Litige judiciaire qui en découle
    vers: "01.9"
---

# 06.7 - Sinistres

> Chemin : `06 - ASSURANCES/06.7 - Sinistres`

## À quoi sert ce dossier

Chaque sinistre déclaré, quel que soit le contrat concerné : dégât des eaux, vol de matériel, accident de véhicule, réclamation d'un client, incident cyber. Le dossier suit la déclaration jusqu'à l'indemnisation et la clôture.

## Documents à y ranger

- `Synthese.md` : date, contrat concerné, n° de sinistre, circonstances, montant, interlocuteurs, étapes, statut
- Déclaration de sinistre (avec preuve d'envoi dans le délai : 2 jours ouvrés pour un vol, 5 pour les autres)
- Constats, photos, plaintes, témoignages, rapports d'intervention
- Échanges avec l'assureur, le courtier, l'expert ; rapport d'expertise, contre-expertise
- Devis et factures de réparation ou de remplacement (copie — originaux dans `04.3`)
- Lettre d'acceptation, décompte d'indemnisation, avis de règlement
- Recours contre un tiers, franchise appliquée, clôture

## Ne pas ranger ici

- Litige judiciaire qui en découle → `01.9` (avec un renvoi croisé)

## Méthode de classement

**Un sous-dossier par sinistre** : `AAAA-MM-JJ - Contrat - Objet` (ex. `2026-01-14 - Multirisque - Degat des eaux bureau`). À l'intérieur, classement chronologique. Une fois clos, ajouter `[CLOS]` au nom du dossier.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | 2 ans à compter de l'événement (prescription biennale de l'assurance, interrompue par chaque échange). **Dommage corporel : 10 ans à compter de la consolidation du dommage.** 10 ans pour une réclamation d'un tiers. |
| **Recommandé** | 10 ans après le règlement définitif ; pour un sinistre corporel, 10 ans après la consolidation, ce qui peut être bien plus tardif que le règlement. |

Base : Code des assurances art. L113-2 (délais de déclaration), L114-1 et L114-2 (prescription biennale) ; Code civil art. 2226 (dommage corporel, 10 ans à compter de la consolidation).

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
