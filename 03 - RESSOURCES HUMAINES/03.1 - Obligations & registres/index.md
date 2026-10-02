---
schema: classement-documents/3.0
id: "03.1"
parent: "03"
niveau: sous-dossier
titre: "03.1 - Obligations & registres"
usage: >-
  Les documents que l'inspection du travail ou l'URSSAF peuvent demander à tout moment, et les
  textes collectifs qui s'appliquent à tous les salariés.
classement: alphabetique
sensibilite: rh
documents:
  - type: registre-unique-personnel
    libelle: Registre unique du personnel
    description: "Registre obligatoire dès le premier salarié, fichier vivant et ses exports datés."
    indices: [registre unique, registre du personnel, personnel, effectif, doeth, index égalité]
    champs: [date, effectif, objet]
    nommage: "{date}_Registre-du-personnel_{objet}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: depart-salarie
      base: Code du travail R1221-26
      sort-final: C
    registre: null
  - type: duerp
    libelle: DUERP et ses versions successives
    description: "Document unique d'évaluation des risques professionnels, chaque version datée et la preuve de sa mise à disposition."
    indices: [duerp, document unique, papripact, risques professionnels, prévention]
    champs: [date, reference, objet, effectif, signataire]
    nommage: "{date}_DUERP_{reference}"
    conservation:
      legale: 40a
      recommandee: permanent
      declencheur: date-document
      base: Code du travail L4121-3-1 et R4121-4
      sort-final: C
    registre: null
  - type: rapport-verification-electrique
    libelle: Rapport de vérification des installations électriques
    description: "Rapport de l'organisme accrédité et registre des vérifications périodiques des installations électriques."
    indices: [vérification électrique, registre de sécurité du personnel, organisme accrédité, installations, contrôle périodique]
    champs: [date, emetteur, objet, lieu]
    nommage: "{date}_Verification-electrique_{emetteur}"
    conservation:
      legale: 5a
      recommandee: 5a
      declencheur: date-document
      base: Code du travail R4226-19 et D4711-3
      sort-final: D
    registre: null
  - type: accord-collectif-et-reglement-interieur
    libelle: "Accord d'entreprise, DUE et règlement intérieur"
    description: "Textes collectifs applicables à tous les salariés, avec leur dépôt sur TéléAccords et les chartes annexées."
    indices: ["accord d'entreprise", téléaccords, règlement intérieur, convention collective, idcc, décision unilatérale]
    champs: [date, objet, date-effet, duree, signataire]
    nommage: "{date}_Accord-entreprise_{objet}"
    conservation:
      legale: 5a
      recommandee: 5a
      declencheur: fin-contrat
      base: Code du travail L1311-2
      sort-final: C
    registre: null
---

# 03.1 - Obligations & registres

> Chemin : `03 - RESSOURCES HUMAINES/03.1 - Obligations & registres`

## À quoi sert ce dossier

Les documents que l'inspection du travail ou l'URSSAF peuvent demander à tout moment, et les textes collectifs qui s'appliquent à tous les salariés. Certains sont obligatoires dès le premier salarié (registre unique du personnel, DUERP, affichages), d'autres à partir de seuils d'effectif.

## Documents à y ranger

- Registre unique du personnel (fichier vivant + exports datés) — dès le 1er salarié
- Document unique d'évaluation des risques professionnels (DUERP) et ses versions successives — dès le 1er salarié. Mise à jour **annuelle obligatoire à partir de 11 salariés** ; en dessous, à chaque changement des conditions de travail ou nouvelle information sur un risque
- Preuve de mise à disposition du DUERP au CSE, aux salariés et aux anciens salariés
- PAPRIPACT — programme annuel de prévention (≥ 50 salariés) ; en dessous, simple liste d'actions de prévention consignée dans le DUERP
- **Registre des vérifications des installations électriques** et rapports des organismes accrédités — obligatoire dans toute entreprise disposant d'installations électriques
- **Registre des dangers graves et imminents** et **registre des alertes en matière de santé publique et d'environnement** — dès l'existence d'un CSE, pages numérotées et sceau du CSE
- **Registre spécial du repos hebdomadaire** si le repos n'est pas pris le même jour par tous, et **tableau du travail en équipes** en cas de relais ou de roulement
- Registre de comptabilité des travailleurs à domicile, le cas échéant
- Affichages obligatoires (copies : convention collective, inspection du travail, médecine du travail, égalité, harcèlement, horaires, consignes incendie)
- Convention collective applicable (copie ou référence IDCC) et accords de branche utiles
- Règlement intérieur (obligatoire ≥ 50 salariés), chartes annexées
- Accords d'entreprise, décisions unilatérales de l'employeur (télétravail, temps de travail, intéressement), avec dépôt sur TéléAccords
- Déclarations obligatoires liées à l'effectif (DOETH ≥ 20 salariés, index égalité ≥ 50…)
- Modèles RH validés : contrat de travail, avenant, promesse d'embauche, rupture conventionnelle, courriers disciplinaires
- Courriers et observations de l'inspection du travail

## Méthode de classement

**Un sous-dossier par document ou famille** (`Registre du personnel`, `DUERP`, `Affichages`, `Accords et DUE`, `Modeles RH`, `Inspection du travail`). Fichiers versionnés par date : `DUERP_2026-01-15.pdf`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Registre du personnel : 5 ans après le départ du salarié. DUERP : 40 ans (toutes les versions). Rapports de vérification : 5 ans, et au minimum les deux derniers. Accords : durée + 5 ans. Observations de l'inspection : 5 ans. |
| **Recommandé** | Permanent pour les versions du DUERP et du registre du personnel (les exports datés ne pèsent rien). |

Base : Code du travail art. L1221-13 et R1221-26 (registre unique), L4121-3-1 et R4121-4 (DUERP, 40 ans), R4226-19 (vérifications électriques), D4132-1 (dangers graves), D4133-1 (alertes), R3135-2 et R3172-2 (repos hebdomadaire), D3171-7 (travail en équipes), D4711-3 (conservation des vérifications), L1311-2 (règlement intérieur), L4711-5 (regroupement des registres).

## Conseils

- **Le DUERP est devenu l'élément le plus exposé de tout le classement.** L'article 48 de la loi n° 2026-534 du 25 juin 2026 a instauré des sanctions administratives applicables depuis cette date : avertissement ou amende jusqu'à **4 000 € par travailleur concerné**, prononcée par l'inspection du travail et doublée en cas de récidive dans les deux ans. Elles s'ajoutent aux sanctions pénales existantes. Tracer chaque version datée et la preuve de sa mise à disposition.
- Le seuil qui change la périodicité du DUERP est **11 salariés**, pas 50 : c'est à partir de 11 que la mise à jour annuelle devient obligatoire.
- L'article L4711-5 du Code du travail autorise expressément à **regrouper plusieurs registres obligatoires en un registre unique** dès lors que cela en facilite la tenue et la consultation. Pour une petite structure, un « registre unique de sécurité » consolidé est souvent plus tenable que six registres séparés — et c'est légal.
- Le registre des questions du CSE (11 à 49 salariés) est le seul registre consultable par **les salariés eux-mêmes** : il est rangé en `03.10` mais son absence est un délit d'entrave.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
