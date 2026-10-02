---
schema: classement-documents/3.0
id: "04.5"
parent: "04"
niveau: sous-dossier
titre: 04.5 - Immobilisations
usage: >-
  Les biens durables de l'entreprise (matériel informatique, mobilier, véhicules, logiciels,
  agencements, site web capitalisé) : leur acquisition, leur amortissement et leur sortie.
classement: par-tiers
sensibilite: confidentielle
documents:
  - type: tableau-amortissement-immobilisation
    libelle: "Tableau d'amortissement d'une immobilisation"
    description: "Plan d'amortissement d'un bien durable, le plus souvent fourni par l'expert-comptable. Alimente le registre des immobilisations."
    indices: [immobilisation, "tableau d'amortissement", amortissement, durée, bien durable]
    champs: [exercice, designation, fournisseur, montant-ht, duree, date-debut]
    nommage: "{exercice}_Tableau-amortissement_{designation}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: sortie-bien
      base: PCG art. 214-1
      sort-final: D
    registre: { fichier: Registre-des-immobilisations.csv, cle: designation }
  - type: contrat-credit-bail-immobilisation
    libelle: Contrat de crédit-bail ou LOA
    description: "Contrat de crédit-bail ou de location avec option d'achat portant sur un bien, et la levée d'option."
    indices: [crédit-bail, loa, "option d'achat", loyer, leasing, "levée d'option"]
    champs: [date, designation, fournisseur, numero-contrat, montant-ht, duree, echeance]
    nommage: "{date}_Credit-bail_{fournisseur}_{designation}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: sortie-bien
      base: Code de commerce L123-22
      sort-final: D
    registre: { fichier: Registre-des-immobilisations.csv, cle: designation }
  - type: sortie-immobilisation
    libelle: "Sortie d'immobilisation"
    description: "Cession, mise au rebut, vol ou destruction d'un bien : facture de vente, PV de mise au rebut, attestation de destruction."
    indices: ["cession d'immobilisation", mise au rebut, destruction, vol, sortie du bien]
    champs: [date, designation, tiers, motif, montant-ht]
    nommage: "{date}_Sortie-immobilisation_{designation}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: sortie-bien
      base: Code de commerce L123-22
      sort-final: D
    registre: { fichier: Registre-des-immobilisations.csv, cle: designation }
va-ailleurs:
  - motif: Inventaire physique et attribution du matériel aux salariés
    vers: "07.6"
  - motif: "Véhicules (carte grise, entretien)"
    vers: "07.4"
  - motif: "Immobilisations financières (titres, participations, placements durables)"
    vers: "08"
---

# 04.5 - Immobilisations

> Chemin : `04 - COMPTABILITE & FISCALITE/04.5 - Immobilisations`

## À quoi sert ce dossier

Les biens durables de l'entreprise (matériel informatique, mobilier, véhicules, logiciels, agencements, site web capitalisé) : leur acquisition, leur amortissement et leur sortie. Le dossier vit aussi longtemps que le bien, puis 10 ans de plus.

## Documents à y ranger

- `Registre-des-immobilisations.csv` à la racine : désignation, date d'achat, fournisseur, montant HT, durée d'amortissement, localisation / attributaire, date de sortie
- Facture d'acquisition (copie — l'original comptable est dans `04.3`)
- Tableau d'amortissement du bien (souvent fourni par l'expert-comptable)
- Contrats de crédit-bail / LOA et options d'achat levées
- Cession, mise au rebut, vol ou destruction : facture de vente, attestation de destruction, déclaration de sinistre (`06.7`), PV de mise au rebut
- Subventions d'investissement rattachées (copie ; dossier dans `05.3`)

## Ne pas ranger ici

- Inventaire physique et attribution du matériel aux salariés → `07.6`
- Véhicules (carte grise, entretien) → `07.4`
- Immobilisations **financières** (titres, participations, placements durables) → `08`

## Méthode de classement

**Un sous-dossier par bien** : `AAAA - Désignation - Fournisseur` (ex. `2025 - Ordinateur portable - Fournisseur Alpha`). Pour les petits matériels nombreux, un sous-dossier par lot annuel (`2025 - Materiel informatique`).

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | 10 ans à compter de la clôture de l'exercice de **sortie** du bien (l'amortissement s'étale sur plusieurs exercices). |
| **Recommandé** | Durée de détention + 10 ans. |

Base : Code de commerce art. L.123-22 ; PCG art. 214-1 et s.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
