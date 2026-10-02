---
schema: classement-documents/3.0
id: "04.4"
parent: "04"
niveau: sous-dossier
titre: 04.4 - Notes de frais
usage: >-
  Les dépenses avancées par le dirigeant ou les salariés et remboursées par l'entreprise :
  déplacements, repas, hébergement, petits achats, indemnités kilométriques.
classement: chronologique
sensibilite: rh
documents:
  - type: note-de-frais
    libelle: Note de frais
    description: "Note de frais mensuelle signée d'une personne, regroupant ses justificatifs de dépenses avancées."
    indices: [note de frais, frais de déplacement, "repas d'affaires", hôtel, péage, train]
    champs: [periode, salarie, numero, montant-tva, montant-ttc]
    nommage: "{periode}_Note-de-frais_{salarie}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: Code de commerce L123-22
      sort-final: D
    registre: null
  - type: releve-indemnites-kilometriques
    libelle: "Relevé d'indemnités kilométriques"
    description: "Relevé des trajets (date, motif, distance), barème appliqué et copie de la carte grise du véhicule utilisé."
    indices: [indemnité kilométrique, barème kilométrique, trajets, carburant remboursé, carte grise]
    champs: [periode, salarie, immatriculation, quantite, taux, montant]
    nommage: "{periode}_Indemnites-kilometriques_{salarie}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: Arrêté du 20 décembre 2002
      sort-final: D
    registre: null
  - type: politique-frais-professionnels
    libelle: "Politique de frais de l'entreprise"
    description: Version datée des plafonds et des règles de remboursement applicables aux frais professionnels.
    indices: [politique de frais, plafonds, règles de remboursement, barème, version datée]
    champs: [date, objet, date-effet, montant]
    nommage: "{date}_Politique-de-frais"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: date-document
      base: Arrêté du 20 décembre 2002
      sort-final: C
    registre: null
---

# 04.4 - Notes de frais

> Chemin : `04 - COMPTABILITE & FISCALITE/04.4 - Notes de frais`

## À quoi sert ce dossier

Les dépenses avancées par le dirigeant ou les salariés et remboursées par l'entreprise : déplacements, repas, hébergement, petits achats, indemnités kilométriques. Chaque note de frais regroupe les justificatifs du mois pour une personne.

## Documents à y ranger

- Notes de frais mensuelles signées (tableau récapitulatif par personne)
- Justificatifs : tickets, reçus, factures au nom de la personne, billets de transport, notes d'hôtel
- Indemnités kilométriques : relevé des trajets (date, motif, distance), copie de la carte grise, barème appliqué
- Politique de frais de l'entreprise (plafonds, règles) — version datée
- Justificatifs des frais de repas d'affaires (avec noms des invités et objet)

## Méthode de classement

**Par année, puis par mois** : `AAAA/AAAA-MM/`, un PDF par personne et par mois regroupant la note et ses justificatifs : `2026-03_NDF_NOM-Prenom.pdf`. Si l'entreprise a un outil de notes de frais, exporter l'archive mensuelle ici.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | 10 ans (pièces comptables) ; 6 ans au titre fiscal (déductibilité, TVA) ; 3 ans au titre social (contrôle URSSAF sur les frais professionnels). |
| **Recommandé** | 10 ans. |

Base : Code de commerce art. L.123-22 ; arrêté du 20 décembre 2002 (frais professionnels) ; LPF art. L.102 B et A.102 B-2 (numérisation des justificatifs).

## Conseils

- Les justificatifs papier peuvent être détruits après numérisation « fiable » (PDF, horodatage, pas de retouche) : c'est explicitement admis par l'administration.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
