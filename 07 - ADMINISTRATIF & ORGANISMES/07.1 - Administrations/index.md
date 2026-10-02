---
schema: classement-documents/3.0
id: "07.1"
parent: "07"
niveau: sous-dossier
titre: 07.1 - Administrations
usage: >-
  La relation générale avec chaque administration et organisme public : identifiants, espaces en
  ligne, courriers d'information, attestations.
classement: par-tiers
sensibilite: normale
documents:
  - type: fiche-identifiants-entreprise
    libelle: "Fiche des identifiants de l'entreprise"
    description: "Fiche tenue à jour des identifiants de l'entreprise — SIREN, SIRET, TVA intracommunautaire, code NAF, IDCC, numéros d'affiliation. Jamais de mot de passe."
    indices: ["identifiants de l'entreprise", siren, siret, tva intracommunautaire, code naf, "numero d'affiliation"]
    champs: [date, siren, siret, numero-tva]
    nommage: "{date}_Fiche-identifiants_{siren}"
    conservation:
      legale: aucune
      recommandee: permanent
      declencheur: aucun
      base: Code civil art. 2224
      sort-final: C
    registre: null
  - type: avis-situation-sirene
    libelle: Avis de situation SIRENE
    description: "Avis de situation au répertoire SIRENE délivré par l'INSEE, classé par date d'émission."
    indices: [insee, avis de situation, sirene, repertoire, situation au repertoire]
    champs: [date, organisme, siren, adresse]
    nommage: "{date}_Avis-de-situation-SIRENE_{organisme}"
    conservation:
      legale: aucune
      recommandee: 10a
      declencheur: date-document
      base: Code civil art. 2224
      sort-final: D
    registre: null
  - type: recepisse-formalite-organisme
    libelle: "Récépissé de formalité d'un organisme"
    description: "Récépissés de formalités et de déclarations reçus du greffe, du guichet unique, du RNE ou d'une autorité sectorielle (récépissé CNIL). La formalité statutaire elle-même reste en 01.2."
    indices: [recepisse, greffe, guichet unique, rne, formalites entreprises, cnil recepisse]
    champs: [date, organisme, reference, objet]
    nommage: "{date}_Recepisse-formalite_{organisme}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: date-document
      base: Code civil art. 2224
      sort-final: C
    registre: null
  - type: autorisation-administrative-locale
    libelle: Autorisation administrative locale
    description: "Autorisation délivrée par la préfecture, la mairie ou une collectivité — enseigne, occupation du domaine public, autorisation sectorielle — avec sa durée de validité."
    indices: [prefecture, mairie, collectivite, enseigne, occupation du domaine public, autorisation]
    champs: [date, organisme, objet, echeance, adresse]
    nommage: "{date}_Autorisation-administrative_{organisme}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: date-document
      base: Code civil art. 2224
      sort-final: C
    registre: null
  - type: courrier-organisme-public
    libelle: "Courrier d'un organisme public"
    description: "Correspondance générale avec une administration ou un organisme public — ouverture d'espace en ligne, cotisation CCI ou CMA, courrier des douanes, adhésion à un syndicat professionnel."
    indices: [courrier, administration, cci, cma, douane, eori, syndicat professionnel, espace en ligne]
    champs: [date, organisme, objet, reference]
    nommage: "{date}_Courrier-organisme_{organisme}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: date-document
      base: Code civil art. 2224
      sort-final: D
    registre: null
va-ailleurs:
  - motif: Impôts (SIE)
    vers: "04.6"
  - motif: "URSSAF, retraite, OPCO, médecine du travail"
    vers: "03.4"
  - motif: Formalités juridiques
    vers: "01.2"
---

# 07.1 - Administrations

> Chemin : `07 - ADMINISTRATIF & ORGANISMES/07.1 - Administrations`

## À quoi sert ce dossier

La relation générale avec chaque administration et organisme public : identifiants, espaces en ligne, courriers d'information, attestations. Les documents à contenu fiscal (→ `04.6`) ou social (→ `03.4`) vont dans leur domaine ; ici on garde la correspondance générale et les identifiants.

## Documents à y ranger

- Identifiants et références de l'entreprise : SIREN/SIRET, TVA intracommunautaire, code NAF, IDCC, numéros d'affiliation — dans une `Fiche-identifiants.md` (jamais de mot de passe : ils vont dans le gestionnaire de mots de passe)
- Courriers d'ouverture des espaces en ligne (impots.gouv pro, net-entreprises, URSSAF, guichet unique INPI, France Travail employeur)
- INSEE : avis de situation SIRENE (par date)
- Greffe / guichet unique : récépissés de formalités, courriers (les formalités elles-mêmes → `01.2`)
- CCI / CMA : cotisations, courriers, adhésions
- Douanes : EORI, déclarations (si import/export)
- Préfecture, mairie, collectivités : autorisations (enseigne, occupation du domaine public), courriers
- Autorités sectorielles : CNIL (récépissés), ARCOM, etc.
- Adhésions à des syndicats professionnels, fédérations, réseaux (contrats → `02.5` si abonnement)

## Ne pas ranger ici

- Impôts (SIE) → `04.6`
- URSSAF, retraite, OPCO, médecine du travail → `03.4`
- Formalités juridiques → `01.2` / `01.4`

## Méthode de classement

**Un sous-dossier par organisme** (`INSEE`, `Greffe`, `CCI`, `Douanes`, `Prefecture`, `CNIL`…), puis `Courriers/AAAA` et `Attestations`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | 5 ans pour la correspondance ; attestations : durée de validité. |
| **Recommandé** | 10 ans pour ce qui pourrait servir de preuve (autorisations, récépissés) ; permanent pour la fiche d'identifiants. |

Base : Code civil art. 2224.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
