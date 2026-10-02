---
schema: classement-documents/3.0
id: "02.5"
parent: "02"
niveau: sous-dossier
titre: "02.5 - Abonnements & licences"
usage: >-
  Les engagements récurrents : logiciels SaaS, licences, télécom, hébergement, énergie, leasing
  de matériel. Ce sont des petits contrats souvent acceptés en ligne, mais qui cumulés pèsent
  lourd et se reconduisent tacitement : le suivi des dates de résiliation est l'enjeu principal.
classement: par-tiers
sensibilite: normale
documents:
  - type: contrat-abonnement-saas
    libelle: "Contrat d'abonnement ou de licence"
    description: "Contrat ou conditions acceptées d'un service SaaS, d'une licence logicielle, d'un hébergement ou d'un nom de domaine."
    indices: [abonnement, saas, licence logicielle, hebergement, cgu acceptees, nom de domaine, reconduction tacite]
    champs: [date-signature, fournisseur, numero, montant-ht, echeance, objet]
    nommage: "{date}_Contrat-abonnement_{fournisseur}_{objet}"
    conservation:
      legale: 5a
      recommandee: 5a
      declencheur: fin-contrat
      base: Code de commerce art. L.110-4
      sort-final: D
    registre: { fichier: Registre-des-contrats.csv, cle: numero }
  - type: contrat-leasing-materiel
    libelle: Contrat de leasing de matériel
    description: "Location longue durée ou leasing de matériel, hors véhicules, avec ses conditions de restitution."
    indices: [leasing de materiel, location longue duree, loyer mensuel, "option d'achat", restitution de materiel]
    champs: [date-signature, fournisseur, numero, montant-ht, designation, duree]
    nommage: "{date}_Contrat-leasing_{fournisseur}_{designation}"
    conservation:
      legale: 5a
      recommandee: 5a
      declencheur: fin-contrat
      base: Code de commerce art. L.110-4
      sort-final: D
    registre: { fichier: Registre-des-contrats.csv, cle: numero }
  - type: contrat-energie-telecom
    libelle: "Contrat d'énergie, télécom ou services du local"
    description: "Contrat d'électricité, d'eau, de télécom, de ménage ou de sécurité attaché à un local."
    indices: [energie, electricite, eau, menage, telecom, mobile, securite du site]
    champs: [date-signature, fournisseur, numero, montant-ht, adresse]
    nommage: "{date}_Contrat-services-locaux_{fournisseur}_{adresse}"
    conservation:
      legale: 5a
      recommandee: 5a
      declencheur: fin-contrat
      base: Code de commerce art. L.110-4
      sort-final: D
    registre: { fichier: Registre-des-contrats.csv, cle: numero }
  - type: preuve-resiliation-abonnement
    libelle: "Preuve de résiliation d'abonnement"
    description: "Preuve de résiliation d'un abonnement ou d'une licence, avec la date de prise d'effet et le respect du préavis."
    indices: ["resiliation d'abonnement", preuve de resiliation, reconduction tacite, preavis, accuse de reception]
    champs: [date, fournisseur, numero, date-effet, motif]
    nommage: "{date}_Resiliation-abonnement_{fournisseur}_{numero}"
    conservation:
      legale: 5a
      recommandee: 5a
      declencheur: fin-contrat
      base: Code de la consommation art. L.215-1
      sort-final: D
    registre: { fichier: Registre-des-contrats.csv, cle: numero }
va-ailleurs:
  - motif: Factures
    vers: "04.3"
  - motif: "Licences de propriété intellectuelle (droits d'usage de contenus/marques)"
    vers: "01.7"
  - motif: Matériel acheté (inventaire)
    vers: "07.6"
---

# 02.5 - Abonnements & licences

> Chemin : `02 - CONTRATS/02.5 - Abonnements & licences`

## À quoi sert ce dossier

Les engagements récurrents : logiciels SaaS, licences, télécom, hébergement, énergie, leasing de matériel. Ce sont des petits contrats souvent acceptés en ligne, mais qui cumulés pèsent lourd et se reconduisent tacitement : le suivi des dates de résiliation est l'enjeu principal.

## Documents à y ranger

- Contrats et conditions acceptées (SaaS, licences logicielles, hébergement, nom de domaine, télécom, énergie, eau, ménage, sécurité)
- Contrats de location longue durée / leasing de matériel (hors véhicules → `07.4`)
- Bons de commande, confirmations d'abonnement, courriels d'acceptation des conditions
- Preuves de résiliation
- `Suivi-des-abonnements.csv` : service, usage, titulaire du compte, coût, date d'engagement, préavis, date limite de résiliation

## Ne pas ranger ici

- Factures → `04.3`
- Licences de propriété intellectuelle (droits d'usage de contenus/marques) → `01.7`
- Matériel acheté (inventaire) → `07.6`

## Méthode de classement

**Un sous-dossier par service** (`Suite bureautique`, `Hebergement web`, `Telephonie mobile`…). Fichiers `AAAA-MM-JJ_Type_Objet.pdf`. Pour les services sans contrat formel, un simple PDF de la page de tarification et des CGU acceptées, daté, suffit.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | 5 ans après la résiliation. |
| **Recommandé** | 5 ans après la résiliation ; les factures (→ `04.3`) suivent la règle comptable de 10 ans. |

Base : Code de commerce art. L.110-4 ; Code de la consommation art. L.215-1 (reconduction tacite).

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
