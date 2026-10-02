---
schema: classement-documents/3.0
id: "01.7"
parent: "01"
niveau: sous-dossier
titre: 01.7 - Propriété intellectuelle
usage: >-
  Les actifs immatériels de l'entreprise et la preuve qu'elle en est bien titulaire : marques,
  noms de domaine, logiciels, créations, et surtout les cessions de droits d'auteur signées par
  les freelances et prestataires (sans cession écrite, les droits restent à l'auteur).
classement: par-tiers
sensibilite: normale
documents:
  - type: certificat-enregistrement-marque
    libelle: "Dépôt et certificat d'enregistrement de marque"
    description: "Dossier de dépôt et certificat d'enregistrement d'une marque auprès de l'INPI, de l'EUIPO ou de l'OMPI."
    indices: [marque, inpi, euipo, ompi, depot de marque, "certificat d'enregistrement", classes de produits]
    champs: [date, numero-depot, organisme, designation, echeance]
    nommage: "{date}_Certificat-marque_{organisme}_{designation}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: fin-protection
      base: Code de la propriété intellectuelle
      sort-final: C
    registre: null
  - type: renouvellement-marque
    libelle: Renouvellement de marque
    description: "Preuve de renouvellement décennal d'une marque, et pièces d'opposition le cas échéant."
    indices: [renouvellement de marque, redevance de renouvellement, opposition, echeance decennale, inpi]
    champs: [date, numero-depot, organisme, echeance, designation]
    nommage: "{date}_Renouvellement-marque_{designation}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: fin-protection
      base: Code de la propriété intellectuelle
      sort-final: C
    registre: null
  - type: preuve-propriete-nom-domaine
    libelle: "Preuve de propriété d'un nom de domaine"
    description: "Contrat registrar, relevé whois et pièces de transfert attestant la titularité d'un nom de domaine."
    indices: [nom de domaine, registrar, whois, transfert de domaine, preuve de propriete]
    champs: [date, designation, fournisseur, echeance]
    nommage: "{date}_Preuve-propriete-domaine_{designation}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: fin-protection
      base: Code de la propriété intellectuelle
      sort-final: C
    registre: null
  - type: cession-droits-auteur
    libelle: "Cession de droits d'auteur"
    description: "Cession de droits signée par un freelance, une agence ou un prestataire, et licences de contenus concédées ou obtenues."
    indices: ["cession de droits d'auteur", freelance, developpeur, photographe, titularite, licence de contenu]
    champs: [date-signature, tiers, objet, designation]
    nommage: "{date}_Cession-droits-auteur_{tiers}_{designation}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: fin-protection
      base: Code de la propriété intellectuelle
      sort-final: C
    registre: null
  - type: depot-probatoire
    libelle: Dépôt probatoire
    description: "Enveloppe e-Soleau, dépôt APP d'un logiciel ou horodatage servant de preuve d'antériorité."
    indices: [e-soleau, enveloppe soleau, depot app, horodatage, "preuve d'anteriorite", brevet]
    champs: [date, numero-depot, organisme, designation]
    nommage: "{date}_Depot-probatoire_{organisme}_{designation}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: fin-protection
      base: Code de la propriété intellectuelle
      sort-final: C
    registre: null
va-ailleurs:
  - motif: Factures de dépôt et de renouvellement
    vers: "04.3"
---

# 01.7 - Propriété intellectuelle

> Chemin : `01 - JURIDIQUE & GOUVERNANCE/01.7 - Propriété intellectuelle`

## À quoi sert ce dossier

Les actifs immatériels de l'entreprise et la preuve qu'elle en est bien titulaire : marques, noms de domaine, logiciels, créations, et surtout les cessions de droits d'auteur signées par les freelances et prestataires (sans cession écrite, les droits restent à l'auteur).

## Documents à y ranger

- Marques : dépôt, certificat d'enregistrement INPI / EUIPO / OMPI, renouvellements (tous les 10 ans), oppositions
- Noms de domaine : contrat registrar, preuve de propriété (whois), transferts (factures → `04.3`)
- Dépôts probatoires : enveloppe e-Soleau, dépôt APP (logiciels), horodatages
- Cessions de droits d'auteur (freelances, agences, développeurs, photographes, designers)
- Licences concédées ou obtenues (logiciels, contenus, images, polices)
- Brevets, dessins et modèles le cas échéant
- `Suivi-des-echeances.csv` à la racine : actif, date de dépôt, date de renouvellement, responsable

## Ne pas ranger ici

- Factures de dépôt et de renouvellement → `04.3` (copie possible ici)

## Méthode de classement

**Un sous-dossier par actif** (`Marque Alpha`, `Domaine example.com`, `Logiciel Beta`…). À l'intérieur : `Depot`, `Renouvellements`, `Cessions et licences`, `Litiges`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | 5 ans à compter de la fin de la protection. |
| **Recommandé** | Permanent tant que l'actif est exploité, puis 5 ans après la fin de protection. Les cessions de droits : permanent (la preuve de titularité n'a pas d'âge). |

Base : Code de la propriété intellectuelle ; Code civil art. 2224.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
