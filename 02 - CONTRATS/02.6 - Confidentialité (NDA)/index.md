---
schema: classement-documents/3.0
id: "02.6"
parent: "02"
niveau: sous-dossier
titre: 02.6 - Confidentialité (NDA)
usage: >-
  Les accords de confidentialité signés avec des prospects, partenaires, candidats,
  investisseurs ou prestataires, en dehors de tout autre contrat.
classement: par-tiers
sensibilite: confidentielle
documents:
  - type: nda-mutuel
    libelle: NDA mutuel
    description: Accord de confidentialité réciproque signé en dehors de tout autre contrat.
    indices: [nda mutuel, accord de confidentialite reciproque, confidentialite, echanges prealables]
    champs: [date-signature, tiers, numero, duree, objet, confidentiel]
    nommage: "{date}_NDA-mutuel_{tiers}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: dernier-contact
      base: Code civil art. 2224
      sort-final: D
    registre: { fichier: Registre-des-contrats.csv, cle: numero }
  - type: nda-unilateral
    libelle: NDA unilatéral
    description: "Engagement de confidentialité unilatéral signé par un prospect, un candidat, un investisseur ou un prestataire."
    indices: [nda, accord de confidentialite, engagement de confidentialite, data room, "appel d'offres"]
    champs: [date-signature, tiers, numero, duree, objet]
    nommage: "{date}_NDA-unilateral_{tiers}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: dernier-contact
      base: Code civil art. 2224
      sort-final: D
    registre: { fichier: Registre-des-contrats.csv, cle: numero }
  - type: levee-de-confidentialite
    libelle: Lettre de levée de confidentialité
    description: "Lettre libérant une partie de son obligation de confidentialité, totalement ou pour un usage donné."
    indices: [levee de confidentialite, mainlevee de confidentialite, autorisation de divulgation, "fin d'engagement"]
    champs: [date, tiers, numero, objet, date-effet]
    nommage: "{date}_Levee-de-confidentialite_{tiers}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: dernier-contact
      base: Code civil art. 2224
      sort-final: D
    registre: { fichier: Registre-des-contrats.csv, cle: numero }
va-ailleurs:
  - motif: NDA inclus dans un contrat client ou fournisseur
    vers: "02.1"
---

# 02.6 - Confidentialité (NDA)

> Chemin : `02 - CONTRATS/02.6 - Confidentialité (NDA)`

## À quoi sert ce dossier

Les accords de confidentialité signés avec des prospects, partenaires, candidats, investisseurs ou prestataires, en dehors de tout autre contrat. Quand un NDA est intégré dans un contrat plus large, il reste avec ce contrat.

## Documents à y ranger

- NDA unilatéraux et mutuels signés
- Engagements de confidentialité ponctuels (data room, appel d'offres)
- Lettres de levée de confidentialité

## Ne pas ranger ici

- NDA inclus dans un contrat client ou fournisseur → avec ce contrat (`02.1`, `02.2`)

## Méthode de classement

**Un sous-dossier par contrepartie** si elle a plusieurs accords, sinon à plat : `AAAA-MM-JJ_NDA_Contrepartie_Objet.pdf`. Noter dans le nom si l'accord est mutuel (`NDA-mutuel`).

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Durée de l'obligation de confidentialité (souvent 2 à 5 ans après la fin des échanges) + 5 ans de prescription. |
| **Recommandé** | 10 ans après la signature. |

Base : Code civil art. 2224.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
