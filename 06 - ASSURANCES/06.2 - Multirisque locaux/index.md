---
schema: classement-documents/3.0
id: "06.2"
parent: "06"
niveau: sous-dossier
titre: 06.2 - Multirisque locaux
usage: >-
  L'assurance des locaux et de leur contenu (incendie, dégât des eaux, vol, bris de machine, RC
  occupant), souvent exigée par le bailleur.
classement: par-contrat
sensibilite: normale
documents:
  - type: contrat-multirisque-locaux
    libelle: Contrat multirisque des locaux
    description: "Conditions particulières et générales de la multirisque professionnelle (incendie, dégât des eaux, vol, bris de machine, RC occupant) et ses avenants de surface ou de capitaux assurés."
    indices: [multirisque professionnelle, incendie, degat des eaux, vol, bris de machine, rc occupant]
    champs: [date-effet, assureur, numero-contrat, adresse, surface, montant, plafond-garantie, franchise]
    nommage: "{date}_Contrat-multirisque_{assureur}_{numero-contrat}"
    conservation:
      legale: 2a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code des assurances art. L.124-5
      sort-final: C
    registre: { fichier: Registre-des-assurances.csv, cle: numero-contrat }
  - type: attestation-multirisque
    libelle: "Attestation d'assurance multirisque"
    description: "Attestation annuelle de la multirisque des locaux, à transmettre au bailleur (copie dans 02.4)."
    indices: [attestation multirisque, attestation pour le bailleur, assurance du local, attestation annuelle]
    champs: [exercice, assureur, numero-contrat, bailleur, adresse]
    nommage: "{exercice}_Attestation-multirisque_{assureur}_{adresse}"
    conservation:
      legale: 2a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code des assurances art. L.124-5
      sort-final: D
    registre: null
  - type: inventaire-biens-assures
    libelle: Inventaire des biens assurés
    description: "Inventaire du matériel assuré et photos des locaux, mis à jour chaque année — pièce décisive en cas de sinistre."
    indices: [inventaire du materiel assure, photos des locaux, capitaux assures, valeur a neuf, mise a jour annuelle]
    champs: [date, assureur, numero-contrat, montant, adresse]
    nommage: "{date}_Inventaire-biens-assures_{adresse}"
    conservation:
      legale: 2a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code des assurances art. L.124-5
      sort-final: T
    registre: null
  - type: quittance-multirisque
    libelle: Quittance de prime multirisque
    description: "Quittance ou appel de prime de la multirisque des locaux, avis d'échéance et courriers de l'assureur."
    indices: [quittance multirisque, appel de prime, "avis d'echeance", "courrier de l'assureur", indexation]
    champs: [periode, assureur, numero-contrat, montant]
    nommage: "{periode}_Quittance-multirisque_{assureur}"
    conservation:
      legale: 2a
      recommandee: 10a
      declencheur: date-document
      base: Code des assurances art. L.114-1
      sort-final: D
    registre: null
va-ailleurs:
  - motif: Bail et états des lieux
    vers: "02.4"
---

# 06.2 - Multirisque locaux

> Chemin : `06 - ASSURANCES/06.2 - Multirisque locaux`

## À quoi sert ce dossier

L'assurance des locaux et de leur contenu (incendie, dégât des eaux, vol, bris de machine, RC occupant), souvent exigée par le bailleur.

## Documents à y ranger

- Conditions particulières et générales, avenants (surface, capitaux assurés, activités)
- Inventaire du matériel assuré et photos des locaux (mise à jour annuelle) — utile en cas de sinistre
- Attestation annuelle (à transmettre au bailleur, copie dans `02.4`)
- Quittances, courriers

## Ne pas ranger ici

- Bail et états des lieux → `02.4`

## Méthode de classement

**Un sous-dossier par contrat** `Assureur - N° contrat`, puis `Contrat`, `Attestations/AAAA`, `Quittances/AAAA`, `Courriers`. En cas de changement d'assureur, garder l'ancien contrat dans son propre sous-dossier (ne pas fusionner).

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | 2 ans après la fin du contrat. |
| **Recommandé** | 10 ans après la fin du contrat (dommages différés, litiges avec le bailleur). |

Base : Code des assurances art. L.114-1, L.124-5.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
