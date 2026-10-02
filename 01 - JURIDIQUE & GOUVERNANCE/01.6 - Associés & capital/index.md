---
schema: classement-documents/3.0
id: "01.6"
parent: "01"
niveau: sous-dossier
titre: "01.6 - Associés & capital"
usage: >-
  La structure du capital et les relations entre associés : qui détient quoi, à quelles
  conditions, et l'historique de tous les mouvements de titres.
classement: par-operation
sensibilite: confidentielle
documents:
  - type: pacte-associes
    libelle: "Pacte d'associés"
    description: "Pacte d'associés ou d'actionnaires de la société et ses avenants."
    indices: ["pacte d'associes", "pacte d'actionnaires", avenant au pacte, droit de preemption, agrement]
    champs: [date-signature, associe, objet, duree]
    nommage: "{date}_Pacte-associes_{objet}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: fin-contrat
      base: Code civil art. 2224
      sort-final: C
    registre: null
  - type: acte-cession-titres
    libelle: "Acte de cession de parts ou d'actions"
    description: "Acte de cession de titres, agrément préalable et justificatif d'enregistrement aux impôts."
    indices: [cession de parts, "cession d'actions", agrement, enregistrement aux impots, prix de cession]
    champs: [date-signature, associe, quantite, montant, nature]
    nommage: "{date}_Acte-de-cession-titres_{associe}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: date-document
      base: Code civil art. 2224
      sort-final: C
    registre: null
  - type: operation-sur-capital
    libelle: Opération sur le capital
    description: "Augmentation ou réduction de capital — bulletins de souscription, attestation de dépôt des fonds, table de capitalisation datée."
    indices: [augmentation de capital, reduction de capital, bulletin de souscription, attestation de depot des fonds, table de capitalisation]
    champs: [date, montant, quantite, associe, objet]
    nommage: "{date}_Operation-sur-capital_{objet}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: date-document
      base: Code de commerce art. L.228-1
      sort-final: C
    registre: null
  - type: attribution-bspce-bsa
    libelle: "Attribution de BSPCE, BSA ou actions gratuites"
    description: "Plan d'attribution, décision d'attribution, lettre au bénéficiaire et exercice des bons."
    indices: [bspce, bsa, action gratuite, "plan d'attribution", "lettre d'attribution", exercice de bons]
    champs: [date, salarie, quantite, cours, echeance]
    nommage: "{date}_Attribution-BSPCE_{salarie}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: date-document
      base: Code de commerce art. L.228-1
      sort-final: C
    registre: null
  - type: convention-compte-courant-associe
    libelle: "Convention de compte courant d'associé"
    description: "Convention d'avance en compte courant d'associé et convention de blocage éventuelle."
    indices: ["compte courant d'associe", convention de blocage, avance en compte courant, "taux d'interet", remboursement]
    champs: [date-signature, associe, montant, taux, echeance]
    nommage: "{date}_Convention-compte-courant_{associe}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: fin-contrat
      base: Code civil art. 2224
      sort-final: C
    registre: null
va-ailleurs:
  - motif: "Documents de levée de fonds (term sheet, contrat d'investissement)"
    vers: "05.4"
  - motif: "Titres que votre société détient dans d'autres sociétés"
    vers: "08.8"
---

# 01.6 - Associés & capital

> Chemin : `01 - JURIDIQUE & GOUVERNANCE/01.6 - Associés & capital`

## À quoi sert ce dossier

La structure du capital et les relations entre associés : qui détient quoi, à quelles conditions, et l'historique de tous les mouvements de titres.

## Documents à y ranger

- Pacte d'associés / d'actionnaires et ses avenants
- Table de capitalisation (fichier vivant + une version PDF datée à chaque mouvement)
- Actes de cession de parts ou d'actions, ordres de mouvement, agréments, enregistrement aux impôts
- Augmentations et réductions de capital : bulletins de souscription, attestation de dépôt des fonds, rapport CAC le cas échéant
- BSPCE / BSA / actions gratuites : plan, décisions d'attribution, bulletins, lettres d'attribution, exercices
- Comptes courants d'associés : conventions de compte courant, conventions de blocage
- Correspondance officielle avec les associés (information annuelle, droit de préemption…)

## Ne pas ranger ici

- Documents de levée de fonds (term sheet, contrat d'investissement) → `05.4` (le pacte signé reste ici)
- Titres que **votre** société détient dans d'autres sociétés → `08.8` (ici, il s'agit uniquement de votre propre capital)

## Méthode de classement

Sous-dossiers thématiques : `Pacte`, `Capitalisation`, `Cessions et mouvements` (un sous-dossier par opération `AAAA-MM-JJ - Objet`), `BSPCE-BSA` (un sous-dossier par bénéficiaire), `Comptes courants`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Actes de cession : 5 ans. Registres : 5 ans après fin d'utilisation. |
| **Recommandé** | Permanent — la chaîne de propriété des titres doit pouvoir être reconstituée à tout moment (due diligence, cession de la société). |

Base : Code civil art. 2224 ; Code de commerce art. L.228-1 et s.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
