---
schema: classement-documents/3.0
id: "02.4"
parent: "02"
niveau: sous-dossier
titre: "02.4 - Baux & locaux"
usage: >-
  Tout ce qui lie l'entreprise à ses locaux : bail commercial ou professionnel, contrat de
  domiciliation, coworking, sous-location.
classement: par-tiers
sensibilite: normale
documents:
  - type: bail-commercial
    libelle: Bail commercial ou professionnel
    description: "Bail commercial, professionnel ou précaire, ses avenants, renouvellements et cessions de bail."
    indices: [bail commercial, bail professionnel, bail precaire, 3-6-9, renouvellement de bail, cession de bail]
    champs: [date-signature, tiers, numero, montant-ht, surface, adresse]
    nommage: "{date}_Bail-commercial_{tiers}_{adresse}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code de commerce art. L.145-1
      sort-final: D
    registre: { fichier: Registre-des-contrats.csv, cle: numero }
  - type: contrat-domiciliation
    libelle: Contrat de domiciliation ou de coworking
    description: "Contrat de domiciliation, de coworking ou de sous-location des locaux de l'entreprise."
    indices: [domiciliation, coworking, sous-location, contrat de domiciliation, attestation de domiciliation]
    champs: [date-signature, tiers, numero, montant-ht, adresse]
    nommage: "{date}_Contrat-domiciliation_{tiers}_{adresse}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code civil art. 2224
      sort-final: D
    registre: { fichier: Registre-des-contrats.csv, cle: numero }
  - type: etat-des-lieux-local
    libelle: État des lieux
    description: "État des lieux d'entrée ou de sortie avec photos, et pièces de versement et de restitution du dépôt de garantie."
    indices: [etat des lieux, entree, sortie, depot de garantie, restitution des locaux, photos]
    champs: [date, tiers, adresse, surface, montant]
    nommage: "{date}_Etat-des-lieux_{tiers}_{adresse}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code civil art. 2224
      sort-final: D
    registre: null
  - type: revision-loyer-charges
    libelle: Révision de loyer et régularisation de charges
    description: "Courriers de révision ou d'indexation du loyer, appels de charges et régularisations annuelles."
    indices: [revision de loyer, indexation, indice ilc, ilat, appel de charges, regularisation de charges, taxe fonciere refacturee]
    champs: [date, tiers, montant-ht, taux, periode]
    nommage: "{date}_Revision-de-loyer_{tiers}_{periode}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code de commerce art. L.145-1
      sort-final: D
    registre: null
  - type: conge-resiliation-bail
    libelle: Congé ou résiliation du bail
    description: "Congé donné ou reçu, résiliation du bail par LRAR ou acte de commissaire de justice."
    indices: [conge, resiliation du bail, "acte d'huissier", preavis, fin de bail]
    champs: [date, tiers, numero, date-effet, adresse]
    nommage: "{date}_Conge-de-bail_{tiers}_{adresse}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code de commerce art. L.145-1
      sort-final: D
    registre: { fichier: Registre-des-contrats.csv, cle: numero }
va-ailleurs:
  - motif: Factures de loyer (si pièces comptables)
    vers: "04.3"
  - motif: Assurance multirisque des locaux
    vers: "06.2"
  - motif: "Contrats d'énergie, eau, ménage"
    vers: "02.5"
---

# 02.4 - Baux & locaux

> Chemin : `02 - CONTRATS/02.4 - Baux & locaux`

## À quoi sert ce dossier

Tout ce qui lie l'entreprise à ses locaux : bail commercial ou professionnel, contrat de domiciliation, coworking, sous-location. Dossier à conserver longtemps : les litiges de fin de bail portent souvent sur l'état des lieux d'entrée réalisé dix ans plus tôt.

## Documents à y ranger

- Bail (commercial 3-6-9, professionnel, précaire, dérogatoire), avenants, renouvellements, cessions de bail
- Contrat de domiciliation, contrat de coworking, sous-location
- États des lieux d'entrée et de sortie (avec photos)
- Dépôt de garantie (versement, restitution)
- Révisions et indexations de loyer (courriers, indices ILC/ILAT)
- Régularisations annuelles de charges, appels de fonds, taxe foncière refacturée
- Diagnostics (amiante, DPE, ERP), règlement de copropriété, PV d'AG de copropriété transmis
- Autorisations de travaux, accords du bailleur
- Congé / résiliation (LRAR ou acte d'huissier)

## Ne pas ranger ici

- Factures de loyer (si pièces comptables) → `04.3` (une copie des quittances peut rester ici)
- Assurance multirisque des locaux → `06.2`
- Contrats d'énergie, eau, ménage → `02.5`

## Méthode de classement

**Un sous-dossier par local** (`Siege - 12 rue de la Gare`). À l'intérieur : `Bail`, `Etats des lieux`, `Loyers et charges/AAAA`, `Travaux`, `Fin de bail`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Durée du bail + 5 ans après sa fin ; actes d'acquisition immobilière : 30 ans. |
| **Recommandé** | 10 ans après la fin du bail (quittances comprises). |

Base : Code de commerce art. L.145-1 et s. ; Code civil art. 2224 et 2227.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
