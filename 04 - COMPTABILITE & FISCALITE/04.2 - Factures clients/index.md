---
schema: classement-documents/3.0
id: "04.2"
parent: "04"
niveau: sous-dossier
titre: 04.2 - Factures clients
usage: >-
  Toutes les factures et avoirs émis par l'entreprise, avec les éléments qui les justifient
  (devis accepté, bon de commande, PV de recette) quand ils ne sont pas déjà dans le dossier
  client.
classement: chronologique
sensibilite: confidentielle
documents:
  - type: facture-client
    libelle: Facture client
    description: "Facture émise par l'entreprise, dans le format envoyé au client. Numérotation chronologique et continue."
    indices: [facture émise, facture de vente, facture client, numérotation, tva]
    champs: [date, client, numero, montant-ht, montant-tva, montant-ttc, echeance]
    nommage: "{date}_Facture_{client}_{numero}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: Code de commerce L123-22
      sort-final: D
    registre: null
  - type: avoir-client
    libelle: Avoir client
    description: Note de crédit annulant ou réduisant une facture émise.
    indices: [avoir client, note de crédit, annulation, rectification, facture émise]
    champs: [date, client, numero, reference, montant-ht, montant-tva, montant-ttc]
    nommage: "{date}_Avoir_{client}_{numero}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: Code de commerce L441-9
      sort-final: D
    registre: null
  - type: facture-acompte-client
    libelle: "Facture d'acompte client"
    description: "Facture d'acompte émise avant exécution, rattachée ensuite à la facture définitive."
    indices: ["facture d'acompte", acompte, avance, tva sur encaissement, échéancier]
    champs: [date, client, numero, reference, montant-ht, montant-ttc]
    nommage: "{date}_Facture-acompte_{client}_{numero}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: CGI art. 289
      sort-final: D
    registre: null
  - type: journal-des-ventes
    libelle: Journal des ventes
    description: "Export mensuel du journal des ventes produit par l'outil de facturation."
    indices: [journal des ventes, export, facturation, mensuel, "chiffre d'affaires"]
    champs: [periode, montant-ht, montant-tva, montant-ttc]
    nommage: "{periode}_Journal-des-ventes"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: Code de commerce L123-22
      sort-final: D
    registre: null
va-ailleurs:
  - motif: Impayés passés en recouvrement contentieux
    vers: "01.9"
  - motif: Contrats et devis signés
    vers: "02.1"
---

# 04.2 - Factures clients

> Chemin : `04 - COMPTABILITE & FISCALITE/04.2 - Factures clients`

## À quoi sert ce dossier

Toutes les factures et avoirs émis par l'entreprise, avec les éléments qui les justifient (devis accepté, bon de commande, PV de recette) quand ils ne sont pas déjà dans le dossier client. La numérotation doit être chronologique et continue, sans trou.

## Documents à y ranger

- Factures émises (PDF tel qu'envoyé au client) et factures d'acompte
- Avoirs
- Devis / bons de commande acceptés rattachés à la facture (copie ; l'original signé reste dans `02.1`)
- Relances amiables et échéanciers de paiement accordés
- Justificatifs d'encaissement en cas de litige (remise de chèque, avis de virement)
- Journal des ventes mensuel (export de l'outil de facturation)

## Ne pas ranger ici

- Impayés passés en recouvrement contentieux → `01.9` (copie de la facture)
- Contrats et devis signés → `02.1`

## Méthode de classement

**Par année, puis par mois de la date de facture** : `AAAA/AAAA-MM/`. Nommage : `AAAA-MM-JJ_F2026-0042_Client_Objet.pdf` ; avoirs `AAAA-MM-JJ_AV2026-0003_Client.pdf`. Ne pas créer de sous-dossier par client ici (le dossier client `02.1` donne cette vue) ; la recherche par nom de fichier suffit.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | 10 ans à compter de la clôture de l'exercice (pièce comptable) ; 6 ans au titre fiscal. |
| **Recommandé** | 10 ans. |

Base : Code de commerce art. L.123-22 et L.441-9 ; CGI art. 289 ; LPF art. L.102 B.

## Conseils

- Avec la facturation électronique, la facture de référence est celle déposée sur la plateforme : garder ici l'export PDF/Factur-X avec son identifiant de dépôt.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
