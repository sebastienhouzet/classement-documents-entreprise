---
schema: classement-documents/3.0
id: "08.6"
parent: "08"
niveau: sous-dossier
titre: "08.6 - Immobilier de placement & SCPI"
usage: >-
  L'immobilier détenu comme placement, et non pour être occupé : parts de SCPI, d'OPCI, parts de
  SCI, immeubles de rapport.
classement: par-tiers
sensibilite: confidentielle
documents:
  - type: bulletin-souscription-scpi
    libelle: "Bulletin de souscription de parts de SCPI ou d'OPCI"
    description: "Bulletin de souscription de parts de SCPI ou d'OPCI, avec les statuts, la note d'information de la société de gestion, le DIC et le prix de souscription payé par part. À conserver sans limite de durée."
    indices: [scpi, opci, bulletin de souscription, societe de gestion, prix de souscription, "note d'information"]
    champs: [date-signature, gestionnaire, designation, quantite, cours, montant]
    nommage: "{date}_Bulletin-souscription-SCPI_{gestionnaire}_{designation}"
    conservation:
      legale: 10a
      recommandee: permanent
      declencheur: cession-ligne
      base: Code monétaire et financier art. L.214-86
      sort-final: C
    registre: { fichier: Registre-des-placements.csv, cle: designation }
  - type: acte-notarie-immeuble-placement
    libelle: Acte notarié et titre de propriété
    description: "Acte notarié d'acquisition et titre de propriété d'un immeuble de rapport, avec les diagnostics et les baux consentis aux locataires. Les parts de SCI relèvent du même traitement que leur acte de souscription."
    indices: [acte notarie, titre de propriete, immeuble de rapport, diagnostic, sci, "acte d'acquisition"]
    champs: [date, tiers, designation, adresse, montant, surface]
    nommage: "{date}_Acte-notarie-immeuble_{tiers}_{adresse}"
    conservation:
      legale: 30a
      recommandee: permanent
      declencheur: sortie-bien
      base: Code civil art. 2227
      sort-final: C
    registre: { fichier: Registre-des-placements.csv, cle: designation }
  - type: bulletin-trimestriel-scpi
    libelle: Bulletin trimestriel et relevé de distribution
    description: "Bulletins trimestriels, relevés de distribution, relevé fiscal annuel et détail des revenus perçus avec leur traitement comptable."
    indices: [bulletin trimestriel, releve de distribution, releve fiscal annuel, revenu percu, quittance de loyer]
    champs: [date, gestionnaire, designation, periode, montant]
    nommage: "{date}_Bulletin-trimestriel_{gestionnaire}_{periode}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cession-ligne
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: null
  - type: valorisation-immobilier-placement
    libelle: "Valorisation de l'immobilier de placement"
    description: "Valorisation au 31/12 — prix de retrait pour une SCPI, expertise ou valeur d'expertise pour un immeuble, et provisions éventuelles."
    indices: [prix de retrait, "valeur d'expertise", expertise immobiliere, valorisation au 31/12, provision]
    champs: [date, exercice, designation, cours, montant]
    nommage: "{date}_Valorisation-immobilier_{exercice}_{designation}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: null
  - type: cession-parts-immobilier-placement
    libelle: "Cession de parts ou de l'immeuble"
    description: "Avis de retrait ou de cession de parts, compromis, acte de vente, décompte du notaire et calcul de la plus-value de cession."
    indices: [avis de retrait, cession de parts, compromis, decompte notaire, plus-value de cession]
    champs: [date, gestionnaire, designation, quantite, montant]
    nommage: "{date}_Cession-immobilier-placement_{gestionnaire}_{designation}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cession-ligne
      base: Code de commerce art. L.123-22
      sort-final: C
    registre: { fichier: Registre-des-placements.csv, cle: designation }
va-ailleurs:
  - motif: "Locaux occupés par l'entreprise"
    vers: "02.4"
  - motif: "Immeuble d'exploitation détenu en propre"
    vers: "04.5"
  - motif: "Assurance de l'immeuble"
    vers: "06.2"
---

# 08.6 - Immobilier de placement & SCPI

> Chemin : `08 - PLACEMENTS & PARTICIPATIONS/08.6 - Immobilier de placement & SCPI`

## À quoi sert ce dossier

L'immobilier détenu comme placement, et non pour être occupé : parts de SCPI, d'OPCI, parts de SCI, immeubles de rapport. Les locaux que l'entreprise occupe relèvent de `02.4` (bail) ou de `04.5` (s'ils sont détenus en propre et amortis comme immobilisation d'exploitation).

## Documents à y ranger

- **SCPI et OPCI** : bulletin de souscription, statuts et note d'information de la société de gestion, DIC, prix de souscription et de retrait, bulletins trimestriels, relevés de distribution, relevé fiscal annuel, avis de retrait ou de cession de parts
- **Parts de SCI** : statuts, acte d'acquisition ou de souscription, PV d'assemblée de la SCI, comptes annuels de la SCI, convention de compte courant d'associé
- **Immeuble détenu en direct** : acte notarié et titre de propriété, diagnostics, prêt associé (renvoi `05.2`), baux consentis aux locataires, quittances, travaux, taxe foncière
- Valorisation au 31/12 : prix de retrait pour une SCPI, expertise ou valeur d'expertise pour un immeuble ; provisions éventuelles
- Détail des revenus perçus et de leur traitement comptable — une société à l'IS amortit l'immeuble et la quote-part d'immeuble, contrairement à un particulier
- Cession : compromis, acte, décompte notaire, calcul de la plus-value

## Ne pas ranger ici

- Locaux occupés par l'entreprise → `02.4` (bail) et `07.3` (exploitation au quotidien)
- Immeuble d'exploitation détenu en propre → `04.5`
- Assurance de l'immeuble → `06.2`

## Méthode de classement

**Un sous-dossier par actif** : `SCPI - Nom`, `SCI - Nom`, `Immeuble - Adresse`. À l'intérieur : `Souscription` ou `Acquisition`, `Revenus/AAAA`, `Valorisation/AAAA`, `Assemblees` (SCPI, SCI), `Cession`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Actes de propriété immobilière : 30 ans. Pièces comptables : 10 ans. Documents fiscaux : 10 ans. |
| **Recommandé** | Permanent pour les actes de propriété et les bulletins de souscription ; durée de détention + 10 ans pour le reste. |

Base : Code civil art. 2227 (prescription en matière immobilière) ; Code monétaire et financier art. L.214-86 et s. (SCPI) ; Code de commerce art. L.123-22.

## Conseils

- Conserver le bulletin de souscription et le prix payé par part sans limite de durée : la plus-value de cession se calcule dessus, parfois vingt ans plus tard.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
