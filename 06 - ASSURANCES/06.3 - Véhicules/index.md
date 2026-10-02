---
schema: classement-documents/3.0
id: "06.3"
parent: "06"
niveau: sous-dossier
titre: 06.3 - Véhicules
usage: >-
  L'assurance des véhicules de l'entreprise (flotte ou véhicule isolé) et, le cas échéant,
  l'assurance « mission » des véhicules personnels utilisés pour le travail.
classement: par-contrat
sensibilite: normale
documents:
  - type: contrat-flotte-automobile
    libelle: "Contrat d'assurance automobile"
    description: "Contrat d'assurance de la flotte ou du véhicule isolé, conditions et avenants d'ajout ou de retrait de véhicule et de conducteur désigné."
    indices: [assurance automobile, flotte, vehicule assure, conducteur designe, avenant de vehicule]
    champs: [date-effet, assureur, numero-contrat, immatriculation, montant, plafond-garantie, franchise]
    nommage: "{date}_Contrat-assurance-automobile_{assureur}_{numero-contrat}"
    conservation:
      legale: 2a
      recommandee: 5a
      declencheur: fin-contrat
      base: Code des assurances art. L.124-5
      sort-final: C
    registre: { fichier: Registre-des-assurances.csv, cle: numero-contrat }
  - type: carte-verte-vehicule
    libelle: Carte verte ou mémo véhicule assuré
    description: "Carte verte, mémo véhicule assuré et vignette de l'année en cours pour un véhicule de l'entreprise."
    indices: [carte verte, memo vehicule assure, vignette, "attestation d'assurance du vehicule"]
    champs: [exercice, assureur, numero-contrat, immatriculation, echeance]
    nommage: "{exercice}_Carte-verte_{assureur}_{immatriculation}"
    conservation:
      legale: 2a
      recommandee: 5a
      declencheur: fin-contrat
      base: Code des assurances art. L.124-5
      sort-final: D
    registre: null
  - type: releve-information-bonus-malus
    libelle: "Relevé d'information (bonus-malus)"
    description: "Relevé d'information de l'assureur portant le coefficient de bonus-malus et l'historique des sinistres du véhicule — il suit la flotte."
    indices: ["releve d'information", bonus-malus, coefficient de reduction majoration, historique de sinistralite]
    champs: [date, assureur, numero-contrat, immatriculation, coefficient]
    nommage: "{date}_Releve-d-information_{assureur}_{immatriculation}"
    conservation:
      legale: 2a
      recommandee: permanent
      declencheur: fin-contrat
      base: Code des assurances art. L.114-1
      sort-final: C
    registre: null
  - type: contrat-assurance-mission
    libelle: "Contrat d'assurance mission"
    description: "Contrat d'assurance « mission » couvrant l'usage professionnel des véhicules personnels des salariés."
    indices: [assurance mission, vehicule personnel du salarie, usage professionnel, deplacement professionnel]
    champs: [date-effet, assureur, numero-contrat, effectif, montant]
    nommage: "{date}_Contrat-assurance-mission_{assureur}_{numero-contrat}"
    conservation:
      legale: 2a
      recommandee: 5a
      declencheur: fin-contrat
      base: Code des assurances art. L.124-5
      sort-final: C
    registre: { fichier: Registre-des-assurances.csv, cle: numero-contrat }
  - type: quittance-assurance-vehicule
    libelle: "Quittance de prime d'assurance automobile"
    description: "Quittance ou appel de prime de l'assurance automobile, avis d'échéance et courriers de l'assureur."
    indices: [quittance automobile, appel de prime, "avis d'echeance", "courrier de l'assureur", resiliation]
    champs: [periode, assureur, numero-contrat, montant, immatriculation]
    nommage: "{periode}_Quittance-assurance-automobile_{assureur}"
    conservation:
      legale: 2a
      recommandee: 5a
      declencheur: date-document
      base: Code des assurances art. L.114-1
      sort-final: D
    registre: null
va-ailleurs:
  - motif: "Carte grise, entretien, contrôle technique, PV"
    vers: "07.4"
  - motif: Constats et sinistres
    vers: "06.7"
---

# 06.3 - Véhicules

> Chemin : `06 - ASSURANCES/06.3 - Véhicules`

## À quoi sert ce dossier

L'assurance des véhicules de l'entreprise (flotte ou véhicule isolé) et, le cas échéant, l'assurance « mission » des véhicules personnels utilisés pour le travail.

## Documents à y ranger

- Contrat, conditions, avenants (ajout / retrait de véhicule, conducteurs désignés)
- Carte verte / mémo véhicule assuré (attestation), vignettes
- Relevé d'information (bonus-malus), historique
- Contrat d'assurance mission (usage des véhicules personnels des salariés)
- Quittances, courriers

## Ne pas ranger ici

- Carte grise, entretien, contrôle technique, PV → `07.4`
- Constats et sinistres → `06.7`

## Méthode de classement

**Un sous-dossier par contrat** `Assureur - N° contrat`, puis `Contrat`, `Attestations/AAAA`, `Quittances/AAAA`, `Courriers`. En cas de changement d'assureur, garder l'ancien contrat dans son propre sous-dossier (ne pas fusionner).

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | 2 ans après la fin du contrat. |
| **Recommandé** | 5 ans après la fin du contrat ; le relevé d'information est à garder de façon permanente (il suit la flotte). |

Base : Code des assurances art. L.114-1, L.124-5.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
