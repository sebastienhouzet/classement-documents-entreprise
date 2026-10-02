---
schema: classement-documents/3.0
id: "02.2"
parent: "02"
niveau: sous-dossier
titre: "02.2 - Fournisseurs & prestataires"
usage: >-
  Les contrats avec ceux qui vendent quelque chose à l'entreprise : prestataires de services
  (comptable, avocat, agences, consultants), fournisseurs de matériel, sociétés de services.
classement: par-tiers
sensibilite: normale
documents:
  - type: contrat-fournisseur
    libelle: Contrat fournisseur
    description: "Contrat de prestation, de fourniture ou de maintenance signé avec un fournisseur, et ses avenants."
    indices: [contrat fournisseur, contrat de prestation recu, maintenance, conditions generales du fournisseur, avenant fournisseur]
    champs: [date-signature, fournisseur, numero, montant-ht, objet]
    nommage: "{date}_Contrat-fournisseur_{fournisseur}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code de commerce art. L.110-4
      sort-final: D
    registre: { fichier: Registre-des-contrats.csv, cle: numero }
  - type: attestation-vigilance-fournisseur
    libelle: "Attestation de vigilance d'un fournisseur"
    description: "Attestation de vigilance URSSAF, Kbis et pièces de vigilance exigées d'un fournisseur au-delà de 5 000 euros HT."
    indices: [attestation de vigilance, urssaf, pieces de vigilance, kbis du fournisseur, salaries etrangers, solidarite financiere]
    champs: [date, fournisseur, echeance, siren]
    nommage: "{date}_Attestation-vigilance_{fournisseur}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: date-document
      base: Code du travail art. D.8222-5
      sort-final: D
    registre: null
  - type: devis-accepte-fournisseur
    libelle: Devis fournisseur accepté
    description: "Devis fournisseur accepté ou bon de commande émis par l'entreprise."
    indices: [devis fournisseur accepte, bon de commande emis, confirmation de commande, acceptation de devis]
    champs: [date-signature, fournisseur, numero, montant-ht, objet]
    nommage: "{date}_Devis-accepte-fournisseur_{fournisseur}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code de commerce art. L.110-4
      sort-final: D
    registre: { fichier: Registre-des-contrats.csv, cle: numero }
  - type: resiliation-contrat-fournisseur
    libelle: Résiliation du contrat fournisseur
    description: "Courrier de résiliation ou de fin de contrat adressé à un fournisseur, avec sa preuve d'envoi."
    indices: [resiliation fournisseur, courrier de fin de contrat, denonciation, preavis fournisseur]
    champs: [date, fournisseur, numero, date-effet, motif]
    nommage: "{date}_Resiliation-contrat-fournisseur_{fournisseur}_{numero}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code de commerce art. L.110-4
      sort-final: D
    registre: { fichier: Registre-des-contrats.csv, cle: numero }
va-ailleurs:
  - motif: Factures fournisseurs
    vers: "04.3"
  - motif: Abonnements SaaS et licences
    vers: "02.5"
  - motif: Expert-comptable et CAC (lettre de mission)
    vers: "04.7"
  - motif: "Freelances intégrés à l'équipe"
    vers: "03.9"
---

# 02.2 - Fournisseurs & prestataires

> Chemin : `02 - CONTRATS/02.2 - Fournisseurs & prestataires`

## À quoi sert ce dossier

Les contrats avec ceux qui vendent quelque chose à l'entreprise : prestataires de services (comptable, avocat, agences, consultants), fournisseurs de matériel, sociétés de services. Y compris les pièces de vigilance qu'un donneur d'ordre doit exiger.

## Documents à y ranger

- Contrats de prestation, de fourniture, de maintenance, et leurs avenants
- Conditions générales du fournisseur acceptées (version datée)
- Devis acceptés, bons de commande émis
- Pièces de vigilance (obligatoires pour toute prestation ≥ 5 000 € HT, à renouveler tous les 6 mois) : attestation de vigilance URSSAF, Kbis, liste des salariés étrangers le cas échéant
- Accords de traitement des données (DPA) quand le fournisseur traite des données pour l'entreprise
- Résiliations et courriers de fin de contrat
- `Fiche-fournisseur.md` : contacts, conditions, SIREN, échéances

## Ne pas ranger ici

- Factures fournisseurs → `04.3`
- Abonnements SaaS et licences → `02.5`
- Expert-comptable et CAC (lettre de mission) → `04.7`
- Freelances intégrés à l'équipe → `03.9`

## Méthode de classement

**Un sous-dossier par fournisseur**. À l'intérieur : `Contrat`, `Vigilance` (attestations par date), `Courriers`. Fichiers `AAAA-MM-JJ_Type_Objet.pdf`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | 5 ans après la fin du contrat ; attestations de vigilance : 5 ans (délai de contrôle de la solidarité financière). |
| **Recommandé** | 10 ans après la fin du contrat. |

Base : Code de commerce art. L.110-4 ; Code du travail art. L.8222-1 et D.8222-5 (obligation de vigilance).

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
