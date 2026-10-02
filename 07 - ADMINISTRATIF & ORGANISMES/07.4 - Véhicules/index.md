---
schema: classement-documents/3.0
id: "07.4"
parent: "07"
niveau: sous-dossier
titre: 07.4 - Véhicules
usage: >-
  Chaque véhicule détenu ou loué par l'entreprise : documents d'immatriculation, contrat de
  location, entretien, contrôle technique, amendes.
classement: par-tiers
sensibilite: normale
documents:
  - type: certificat-immatriculation-vehicule
    libelle: "Certificat d'immatriculation"
    description: "Carte grise du véhicule détenu ou loué par l'entreprise."
    indices: [carte grise, immatriculation, certificat, vehicule]
    champs: [date, immatriculation, designation, tiers]
    nommage: "{date}_Carte-grise_{immatriculation}_{designation}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: sortie-bien
      base: Code de commerce L123-22
      sort-final: D
    registre: null
  - type: certificat-cession-vehicule
    libelle: Certificat de cession de véhicule
    description: "Certificat de cession établi à l'achat et à la revente du véhicule, preuve du transfert de propriété."
    indices: [certificat de cession, revente du vehicule, achat du vehicule, transfert de propriete]
    champs: [date, immatriculation, tiers, montant, date-effet]
    nommage: "{date}_Certificat-de-cession_{immatriculation}_{tiers}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: sortie-bien
      base: Code de commerce art. L.123-22
      sort-final: C
    registre: null
  - type: controle-technique-vehicule
    libelle: Procès-verbal de contrôle technique
    description: "Procès-verbal de contrôle technique du véhicule, avec la date de la visite suivante."
    indices: [controle technique, visite technique, proces-verbal de controle, contre-visite]
    champs: [date, immatriculation, prestataire, echeance]
    nommage: "{date}_Controle-technique_{immatriculation}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: sortie-bien
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: null
  - type: entretien-reparation-vehicule
    libelle: Entretien et réparation du véhicule
    description: "Carnet d'entretien et copies des factures d'entretien et de réparation du véhicule. Les originaux restent en 04.3."
    indices: ["carnet d'entretien", entretien du vehicule, reparation, revision, pneumatiques]
    champs: [date, immatriculation, fournisseur, designation, montant-ht]
    nommage: "{date}_Entretien-vehicule_{immatriculation}_{designation}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: sortie-bien
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: null
  - type: avis-contravention-vehicule
    libelle: Avis de contravention et désignation du conducteur
    description: "Avis de contravention reçu par la société et preuve de la désignation du conducteur, obligatoire sous 45 jours sous peine d'amende majorée."
    indices: [amende, avis de contravention, designation du conducteur, amende majoree, antai]
    champs: [date, immatriculation, organisme, montant, salarie]
    nommage: "{date}_Avis-de-contravention_{immatriculation}"
    conservation:
      legale: 3a
      recommandee: 10a
      declencheur: date-document
      base: Code de la route art. L.121-6
      sort-final: D
    registre: null
va-ailleurs:
  - motif: Assurance du véhicule
    vers: "06.3"
  - motif: "Constat d'accident et sinistre"
    vers: "06.7"
  - motif: Indemnités kilométriques (véhicules personnels)
    vers: "04.4"
---

# 07.4 - Véhicules

> Chemin : `07 - ADMINISTRATIF & ORGANISMES/07.4 - Véhicules`

## À quoi sert ce dossier

Chaque véhicule détenu ou loué par l'entreprise : documents d'immatriculation, contrat de location, entretien, contrôle technique, amendes. Un dossier par véhicule, de l'acquisition à la revente ou restitution.

## Documents à y ranger

- Certificat d'immatriculation (carte grise), certificat de cession à l'achat et à la revente
- Facture d'achat (copie — original dans `04.3` / `04.5`) ou contrat de LOA / LLD / crédit-bail et tableau de loyers
- Attribution du véhicule à un salarié (avenant, charte d'utilisation, avantage en nature — copie dans `03.2`)
- Carnet d'entretien, factures d'entretien et de réparation (copie ; originaux dans `04.3`)
- Contrôles techniques
- Amendes et avis de contravention, désignation du conducteur (obligatoire sous 45 jours, sinon amende majorée pour la société)
- Cartes carburant et badges télépéage (contrats → `02.5`)
- Restitution (PV de restitution LLD, frais de remise en état) ou revente

## Ne pas ranger ici

- Assurance du véhicule → `06.3`
- Constat d'accident et sinistre → `06.7`
- Indemnités kilométriques (véhicules personnels) → `04.4`

## Méthode de classement

**Un sous-dossier par véhicule** : `Immatriculation - Marque Modèle` (ex. `AA-123-AA - Utilitaire`), puis `Documents`, `Entretien et CT`, `Amendes`, `Fin`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Durée de détention + 5 ans. Avis de contravention : 3 ans (prescription) — conserver la preuve de désignation. |
| **Recommandé** | Durée de détention + 10 ans (le véhicule est une immobilisation). |

Base : Code de la route art. L.121-6 (désignation du conducteur) ; Code de commerce art. L.123-22.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
