---
schema: classement-documents/3.0
id: "02.1"
parent: "02"
niveau: sous-dossier
titre: 02.1 - Clients
usage: >-
  Les engagements pris avec chaque client : contrat cadre, devis et propositions commerciales
  acceptés, bons de commande, conditions particulières, avenants, procès-verbaux de recette.
classement: par-tiers
sensibilite: normale
documents:
  - type: contrat-client
    libelle: Contrat client
    description: "Contrat cadre ou contrat de prestation signé avec un client, avec ses conditions particulières et le DPA éventuel."
    indices: [contrat client, contrat de prestation signe, contrat cadre, conditions particulieres, cgv acceptees, dpa client]
    champs: [date-signature, client, numero, montant-ht, objet]
    nommage: "{date}_Contrat-client_{client}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code de commerce art. L.110-4
      sort-final: D
    registre: { fichier: Registre-des-contrats.csv, cle: numero }
  - type: devis-accepte-client
    libelle: Devis ou proposition accepté
    description: "Devis ou proposition commerciale accepté par le client, bon de commande ou ordre de service."
    indices: [devis accepte, proposition commerciale signee, bon de commande, ordre de service, accord ecrit]
    champs: [date-signature, client, numero, montant-ht, objet]
    nommage: "{date}_Devis-accepte_{client}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code de commerce art. L.110-4
      sort-final: D
    registre: { fichier: Registre-des-contrats.csv, cle: numero }
  - type: avenant-contrat-client
    libelle: Avenant au contrat client
    description: "Avenant modifiant le périmètre, la durée ou le prix d'un contrat client."
    indices: [avenant, modification de perimetre, prolongation, revision de prix, complement de mission]
    champs: [date-signature, client, numero, montant-ht, date-effet]
    nommage: "{date}_Avenant-contrat-client_{client}_{numero}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code de commerce art. L.110-4
      sort-final: D
    registre: { fichier: Registre-des-contrats.csv, cle: numero }
  - type: pv-recette-client
    libelle: PV de recette client
    description: "Procès-verbal de recette ou de réception, décharge de fin de mission signée par le client."
    indices: [pv de recette, recette fonctionnelle, reception de livrable, decharge de fin de mission, reserves]
    champs: [date, client, numero, objet, statut]
    nommage: "{date}_PV-de-recette_{client}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code de commerce art. L.110-4
      sort-final: D
    registre: null
  - type: resiliation-contrat-client
    libelle: Résiliation du contrat client
    description: Résiliation ou protocole de fin de contrat conclu avec un client.
    indices: [resiliation client, protocole de fin de contrat, denonciation, preavis, fin de mission]
    champs: [date, client, numero, date-effet, motif]
    nommage: "{date}_Resiliation-contrat-client_{client}_{numero}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code de commerce art. L.110-4
      sort-final: D
    registre: { fichier: Registre-des-contrats.csv, cle: numero }
va-ailleurs:
  - motif: Factures et avoirs
    vers: "04.2"
  - motif: "Livrables, sources, maquettes (partie opérationnelle)"
    vers: null
  - motif: Litige avec le client
    vers: "01.9"
---

# 02.1 - Clients

> Chemin : `02 - CONTRATS/02.1 - Clients`

## À quoi sert ce dossier

Les engagements pris avec chaque client : contrat cadre, devis et propositions commerciales acceptés, bons de commande, conditions particulières, avenants, procès-verbaux de recette. C'est le dossier que l'on ouvre en cas de désaccord sur le périmètre ou le prix.

## Documents à y ranger

- Contrat cadre ou contrat de prestation signé, et ses avenants
- Devis / propositions commerciales acceptés (signés ou avec accord écrit — courriel d'acceptation joint)
- Bons de commande, ordres de service
- CGV acceptées (préciser la version — les versions elles-mêmes sont dans `01.8`)
- Accord de traitement des données (DPA) signé avec le client
- PV de recette / de réception, décharges de fin de mission
- Résiliations, protocoles de fin de contrat
- Fiche client : contacts, SIREN, conditions de paiement, référent (`Fiche-client.md`)

## Ne pas ranger ici

- Factures et avoirs → `04.2`
- Livrables, sources, maquettes (partie opérationnelle) → hors de ce classement
- Litige avec le client → `01.9`

## Méthode de classement

**Un sous-dossier par client** nommé de façon stable (`Client Alpha`, pas `client-alpha.fr`). Si un client a de nombreux projets : `Client/AAAA - Nom du projet/`. Fichiers : `AAAA-MM-JJ_Devis-D2026-014_Refonte-site_signe.pdf`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | 5 ans après la fin du contrat (10 ans si contrat électronique ≥ 120 €). |
| **Recommandé** | 10 ans après la fin de la relation. Un client sans contrat actif depuis 3 ans → déplacer son dossier vers `98 - ARCHIVES`. |

Base : Code de commerce art. L.110-4 ; Code de la consommation art. L.213-1.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
