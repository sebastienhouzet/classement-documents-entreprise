---
schema: classement-documents/3.0
id: "02.7"
parent: "02"
niveau: sous-dossier
titre: 02.7 - Modèles de contrats
usage: >-
  La bibliothèque des modèles vierges validés (par un avocat ou par l'usage) que l'entreprise
  réutilise. On y garde la version en cours et les versions précédentes, car un contrat signé
  sur un ancien modèle doit pouvoir être relu avec le modèle de l'époque.
classement: alphabetique
sensibilite: normale
documents:
  - type: modele-contrat-prestation
    libelle: Modèle de contrat de prestation
    description: "Modèle vierge de contrat de prestation ou de sous-traitance, versionné par date."
    indices: [modele de contrat, contrat type, trame, version en vigueur, anciennes versions]
    champs: [date, reference, objet, statut]
    nommage: "{date}_Modele-contrat-prestation_{reference}"
    conservation:
      legale: aucune
      recommandee: 10a
      declencheur: fin-contrat
      sort-final: T
    registre: null
  - type: modele-devis-commercial
    libelle: Modèle de devis ou de proposition
    description: "Modèle vierge de devis, de proposition commerciale ou de bon de commande."
    indices: [modele de devis, modele de proposition commerciale, bon de commande type, trame commerciale]
    champs: [date, reference, objet]
    nommage: "{date}_Modele-devis_{reference}"
    conservation:
      legale: aucune
      recommandee: 10a
      declencheur: fin-contrat
      sort-final: T
    registre: null
  - type: modele-nda-dpa
    libelle: Modèle de NDA ou de DPA
    description: "Modèle vierge d'accord de confidentialité, d'accord de traitement des données ou d'apport d'affaires."
    indices: [modele de nda, modele de dpa, "modele d'apport d'affaires", trame de confidentialite]
    champs: [date, reference, objet]
    nommage: "{date}_Modele-NDA_{reference}"
    conservation:
      legale: aucune
      recommandee: 10a
      declencheur: fin-contrat
      sort-final: T
    registre: null
  - type: modele-courrier-juridique
    libelle: Modèle de courrier juridique
    description: "Modèle vierge de mise en demeure, de résiliation ou de relance, avec son historique de versions."
    indices: [modele de mise en demeure, modele de resiliation, modele de relance, courrier type]
    champs: [date, reference, objet]
    nommage: "{date}_Modele-courrier-juridique_{reference}"
    conservation:
      legale: aucune
      recommandee: 10a
      declencheur: fin-contrat
      sort-final: T
    registre: null
va-ailleurs:
  - motif: "Modèles RH (contrat de travail, avenant, rupture)"
    vers: "03.1"
---

# 02.7 - Modèles de contrats

> Chemin : `02 - CONTRATS/02.7 - Modèles de contrats`

## À quoi sert ce dossier

La bibliothèque des modèles vierges validés (par un avocat ou par l'usage) que l'entreprise réutilise. On y garde la version en cours et les versions précédentes, car un contrat signé sur un ancien modèle doit pouvoir être relu avec le modèle de l'époque.

## Documents à y ranger

- Modèles de contrat de prestation, de devis / proposition commerciale, de bon de commande
- Modèles de NDA, de DPA, de contrat de sous-traitance, d'apport d'affaires
- Modèles de CGV / CGU (la version publiée est dans `01.8`)
- Modèles de courriers juridiques : mise en demeure, résiliation, relance
- `CHANGELOG.md` : quelle version, quelle date, ce qui a changé et pourquoi

## Ne pas ranger ici

- Modèles RH (contrat de travail, avenant, rupture) → `03.1`

## Méthode de classement

**Un sous-dossier par type de modèle**. Fichiers versionnés par date : `Modele_Contrat-prestation_v2026-01.docx`. Ne garder à la racine du sous-dossier que la version en vigueur ; les anciennes dans un sous-dossier `Anciennes versions`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Aucune obligation. |
| **Recommandé** | Garder une version tant qu'un contrat signé sur cette version est en vigueur ou dans sa période de conservation. |

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
