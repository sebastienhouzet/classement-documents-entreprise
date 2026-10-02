---
schema: classement-documents/3.0
id: "01.4"
parent: "01"
niveau: sous-dossier
titre: 01.4 - Registres légaux
usage: >-
  Les registres obligatoires de la société, tenus de façon continue. Ils peuvent être tenus sous
  forme papier (cotés et paraphés) ou dématérialisée (avec horodatage) ; dans les deux cas, on
  garde ici une version PDF figée à chaque mise à jour.
classement: alphabetique
sensibilite: confidentielle
documents:
  - type: registre-mouvements-titres
    libelle: Registre des mouvements de titres
    description: "Registre des mouvements de titres et comptes individuels d'associés, exporté en PDF figé à chaque mise à jour."
    indices: [registre des mouvements de titres, "compte d'actionnaire", "compte individuel d'associe", registre cote et paraphe, export date]
    champs: [date, associe, quantite, numero]
    nommage: "{date}_Registre-mouvements-titres_{numero}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: fin-utilisation
      base: Code de commerce art. R228-8
      sort-final: C
    registre: null
  - type: ordre-mouvement-titres
    libelle: Ordre de mouvement de titres
    description: "Ordre de mouvement signé constatant l'inscription d'un transfert de titres au registre."
    indices: [ordre de mouvement, transfert de titres, inscription en compte, signature du cedant]
    champs: [date, associe, quantite, numero, signataire]
    nommage: "{date}_Ordre-de-mouvement_{associe}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: fin-utilisation
      base: Code de commerce art. L228-1
      sort-final: C
    registre: null
  - type: registre-des-decisions-sociales
    libelle: Registre des décisions et délibérations
    description: "Registre des décisions des associés ou des délibérations du conseil, en feuilles numérotées ou en export horodaté."
    indices: [registre des decisions, registre des proces-verbaux, feuilles numerotees, deliberations du conseil, horodatage]
    champs: [date, objet, signataire, numero]
    nommage: "{date}_Registre-des-decisions_{numero}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: fin-utilisation
      base: Code de commerce art. L228-1
      sort-final: C
    registre: null
  - type: declaration-beneficiaires-effectifs
    libelle: Déclaration des bénéficiaires effectifs
    description: Déclarations successives des bénéficiaires effectifs et récépissés du greffe correspondants.
    indices: [beneficiaires effectifs, dbe, registre des beneficiaires effectifs, recepisse du greffe, changement de detention]
    champs: [date, organisme, associe, taux]
    nommage: "{date}_Declaration-beneficiaires-effectifs_{organisme}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: fin-utilisation
      base: Code de commerce art. L561-46
      sort-final: C
    registre: null
va-ailleurs:
  - motif: "Conventions réglementées : il n'existe pas de registre légal à ce nom en SAS ni en SARL. L'obligation est le rapport sur les conventions réglementées présenté à l'assemblée d'approbation des comptes"
    vers: "01.3"
  - motif: Registre unique du personnel
    vers: "03.1"
---

# 01.4 - Registres légaux

> Chemin : `01 - JURIDIQUE & GOUVERNANCE/01.4 - Registres légaux`

## À quoi sert ce dossier

Les registres obligatoires de la société, tenus de façon continue. Ils peuvent être tenus sous forme papier (cotés et paraphés) ou dématérialisée (avec horodatage) ; dans les deux cas, on garde ici une version PDF figée à chaque mise à jour.

## Documents à y ranger

- Registre des mouvements de titres (SAS/SA) et comptes individuels d'associés / d'actionnaires
- Ordres de mouvement de titres signés
- Registre des décisions / des procès-verbaux d'assemblée (feuilles numérotées)
- Registre des bénéficiaires effectifs : déclarations successives (DBE) et récépissés du greffe
- Registre des délibérations du conseil (SA, ou SAS si prévu par les statuts)

## Ne pas ranger ici

- **Conventions réglementées : il n'existe pas de registre légal à ce nom** en SAS ni en SARL. L'obligation est le *rapport* sur les conventions réglementées présenté à l'assemblée d'approbation des comptes → `01.3` ; les conventions elles-mêmes → `01.5` pour un dirigeant, `01.6` pour un associé
- Registre unique du personnel → `03.1`

## Méthode de classement

Un sous-dossier par registre. Pour chaque registre : un fichier « vivant » (le registre tenu à jour) + un export PDF daté à chaque mise à jour (`Registre-mouvements-titres_2026-03-15.pdf`). Ne jamais écraser un export.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | 5 ans à compter de la fin de l'utilisation du registre. |
| **Recommandé** | Permanent. |

Base : Code de commerce, art. L228-1, R228-8 (mouvements de titres), L561-46 (bénéficiaires effectifs).

## Conseils

- Mettre à jour le registre des bénéficiaires effectifs dans les 30 jours de tout changement (cession, augmentation de capital, changement de dirigeant). Les sanctions ont été renforcées : jusqu'à 200 000 € pour le dirigeant, 1 000 000 € pour la société, et le greffier peut prononcer la radiation d'office du RCS.
- En SARL et EURL, il n'y a pas de registre des mouvements de titres : les parts sont nominatives dans les statuts et se cèdent par acte. Le sous-dossier reste vide.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
