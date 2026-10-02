---
schema: classement-documents/3.0
id: "97.1"
parent: "97"
niveau: sous-dossier
titre: Kit administratif
usage: >-
  Copies à jour des justificatifs que l'entreprise doit fournir régulièrement : ouverture de
  compte, réponse à un appel d'offres, référencement chez un client, demande de prêt, contrat
  avec un grand compte.
classement: alphabetique
sensibilite: normale
documents:
  - type: copie-attestation-a-jour
    libelle: "Copie à jour d'une attestation"
    description: "Copie de travail à jour d'un justificatif à fournir régulièrement — Kbis de moins de 3 mois, attestation de vigilance URSSAF, attestation de régularité fiscale, attestation RC Pro, RIB, statuts à jour, liste des bénéficiaires effectifs, avis de situation SIRENE. Un seul exemplaire — la version renouvelée remplace l'ancienne, l'original reste dans son domaine."
    indices: [kbis de moins de 3 mois, attestation de vigilance, regularite fiscale, attestation rc pro, "rib de l'entreprise", beneficiaires effectifs]
    champs: [date, organisme, echeance, objet]
    nommage: "{date}_Copie-attestation-a-jour_{organisme}_{objet}"
    conservation:
      legale: aucune
      recommandee: aucune
      declencheur: aucun
      sort-final: D
    registre: null
  - type: fiche-identite-kit-administratif
    libelle: "Fiche d'identité de l'entreprise"
    description: "Fiche d'identité de l'entreprise au format texte — SIREN, TVA intracommunautaire, NAF, capital, effectif, adresse, contacts — tenue à jour pour être envoyée avec le kit. Seule la version en cours est conservée."
    indices: ["fiche d'identite de l'entreprise", capital, effectif, adresse, contacts, naf]
    champs: [date, siren, numero-tva, adresse, effectif]
    nommage: "{date}_Fiche-identite-entreprise_{siren}"
    conservation:
      legale: aucune
      recommandee: aucune
      declencheur: aucun
      sort-final: D
    registre: null
va-ailleurs:
  - motif: "Les originaux et l'historique"
    vers: "01.1"
---

# Kit administratif

> Chemin : `97 - REFERENTIEL/Kit administratif`

## À quoi sert ce dossier

Copies **à jour** des justificatifs que l'entreprise doit fournir régulièrement : ouverture de compte, réponse à un appel d'offres, référencement chez un client, demande de prêt, contrat avec un grand compte. L'idée est de pouvoir envoyer un dossier complet en cinq minutes sans fouiller les autres dossiers.

## Documents à y ranger

- Extrait Kbis de moins de 3 mois
- Attestation de vigilance URSSAF (valable 6 mois)
- Attestation de régularité fiscale (impots.gouv, espace professionnel)
- Attestation d'assurance RC Pro de l'année en cours
- RIB de l'entreprise
- Statuts à jour (copie)
- Pièce d'identité du (des) dirigeant(s)
- Liste des bénéficiaires effectifs
- Avis de situation SIRENE
- Fiche d'identité de l'entreprise (SIREN, TVA intracom., NAF, capital, effectif, adresse, contacts) au format texte

## Ne pas ranger ici

- Les originaux et l'historique → dossiers de domaine (`01.1`, `03.4`, `04.6`, `06.1`, `05.1`)

## Méthode de classement

Un seul exemplaire de chaque document, nommé avec sa date d'émission (`Kbis_2026-09-01.pdf`). Quand un document est renouvelé, on **remplace** l'ancien : l'original reste rangé dans son dossier de domaine (le Kbis dans `01.1`, l'attestation URSSAF dans `03.4`, etc.).

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Aucune : ce sont des copies de travail. |
| **Recommandé** | Ne garder que la version la plus récente. Vérifier les dates de validité tous les trimestres (Kbis 3 mois, URSSAF 6 mois, RC Pro 1 an). |

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
