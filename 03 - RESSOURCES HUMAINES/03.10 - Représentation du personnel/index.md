---
schema: classement-documents/3.0
id: "03.10"
parent: "03"
niveau: sous-dossier
titre: 03.10 - Représentation du personnel
usage: >-
  Les institutions représentatives du personnel : élections du CSE (obligatoires dès 11 salariés
  pendant 12 mois consécutifs), réunions, consultations, accords.
classement: par-operation
sensibilite: rh
documents:
  - type: pv-election-cse
    libelle: "PV d'élection du CSE"
    description: "Procès-verbal d'élection (Cerfa) transmis au CTEP, avec les listes électorales et les candidatures."
    indices: ["pv d'élection", élection professionnelle, cse, liste électorale, ctep, protocole préélectoral]
    champs: [date, effectif, objet]
    nommage: "{date}_PV-election-CSE_{objet}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: date-document
      base: Code du travail L2314-4
      sort-final: C
    registre: null
  - type: pv-carence-cse
    libelle: PV de carence
    description: "Procès-verbal constatant l'absence de candidat alors que le seuil de onze salariés est atteint."
    indices: [pv de carence, carence, absence de candidat, seuil 11, cse]
    champs: [date, effectif, objet]
    nommage: "{date}_PV-carence-CSE"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: date-document
      base: Code du travail L2314-4
      sort-final: C
    registre: null
  - type: pv-reunion-cse
    libelle: PV de réunion du CSE
    description: "Convocation, ordre du jour et procès-verbal d'une réunion du CSE, avec les avis rendus."
    indices: [réunion du cse, convocation, ordre du jour, procès-verbal, avis, heures de délégation]
    champs: [date, numero, objet, effectif]
    nommage: "{date}_PV-reunion-CSE_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: date-document
      base: Code du travail L2315-1
      sort-final: D
    registre: null
  - type: consultation-cse
    libelle: Consultation obligatoire du CSE
    description: "Dossier d'une consultation obligatoire (orientations stratégiques, situation économique, politique sociale) et la BDESE."
    indices: [consultation du cse, orientations stratégiques, politique sociale, bdese, registre des questions du cse]
    champs: [date, objet, exercice, nature]
    nommage: "{date}_Consultation-CSE_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: date-document
      base: Code du travail L2315-1
      sort-final: D
    registre: null
---

# 03.10 - Représentation du personnel

> Chemin : `03 - RESSOURCES HUMAINES/03.10 - Représentation du personnel`

## À quoi sert ce dossier

Les institutions représentatives du personnel : élections du CSE (obligatoires dès 11 salariés pendant 12 mois consécutifs), réunions, consultations, accords. Si l'entreprise a moins de 11 salariés, le dossier reste vide ; si elle en a 11 ou plus mais qu'aucun candidat ne s'est présenté, le **PV de carence** doit y être conservé.

## Documents à y ranger

- Élections : protocole d'accord préélectoral, listes électorales, candidatures, PV d'élection (Cerfa, transmis au CTEP), PV de carence
- Réunions du CSE : convocations, ordres du jour, procès-verbaux, avis rendus
- **Registre des questions du CSE** (entreprises de 11 à 49 salariés) : questions écrites transmises par le CSE et réponses argumentées de l'employeur — consultable par les salariés eux-mêmes et par l'inspection du travail
- Consultations obligatoires (orientations stratégiques, situation économique, politique sociale), BDESE (≥ 50)
- Heures de délégation, formation des élus, budget de fonctionnement et des ASC (≥ 50)
- Accords d'entreprise signés avec le CSE ou les délégués syndicaux (dépôt TéléAccords) — copie, l'original dans `03.1`
- Procédures de licenciement de salariés protégés (autorisations de l'inspection du travail)

## Méthode de classement

**Un sous-dossier par mandature** (`2024-2028`), puis `Elections`, `Reunions/AAAA`, `Consultations`, `Accords`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | PV d'élection et de carence : 5 ans minimum. PV de réunion et documents de consultation : 5 ans. |
| **Recommandé** | Permanent pour les PV d'élection et de carence (ils conditionnent la validité d'accords et de licenciements) ; 10 ans pour le reste. |

Base : Code du travail art. L.2311-2 (seuil 11), L.2314-4 et s. (élections), L.2315-1 et s. (fonctionnement).

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
