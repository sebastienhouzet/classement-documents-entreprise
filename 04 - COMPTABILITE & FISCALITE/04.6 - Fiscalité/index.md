---
schema: classement-documents/3.0
id: "04.6"
parent: "04"
niveau: sous-dossier
titre: 04.6 - Fiscalité
usage: >-
  Toutes les déclarations et tous les échanges avec l'administration fiscale : TVA, impôt sur
  les sociétés, CFE/CVAE, taxes diverses, contrôles fiscaux, rescrits, attestations.
classement: chronologique
sensibilite: confidentielle
documents:
  - type: declaration-tva
    libelle: Déclaration de TVA
    description: "CA3 ou CA12 et son accusé, demande de remboursement de crédit de TVA, état récapitulatif intracommunautaire."
    indices: [ca3, ca12, déclaration de tva, crédit de tva, deb, emebi]
    champs: [periode, organisme, numero, montant-ht, montant-tva]
    nommage: "{periode}_Declaration-TVA"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: date-document
      base: LPF L102 B
      sort-final: D
    registre: null
  - type: declaration-is
    libelle: "Déclaration d'impôt sur les sociétés"
    description: "Relevés d'acomptes 2571, relevé de solde 2572, avis d'imposition et options exercées."
    indices: ["acompte d'is", "solde d'is", "2571", "2572", "avis d'imposition", report en arrière]
    champs: [exercice, organisme, numero, montant, echeance]
    nommage: "{exercice}_Declaration-IS"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: date-document
      base: LPF L102 B
      sort-final: D
    registre: null
  - type: avis-cfe-cvae
    libelle: Avis et déclaration CFE / CVAE
    description: "Avis de CFE, déclaration 1447, CVAE et demandes d'exonération, par année et par établissement."
    indices: [cfe, cvae, "1447", exonération, avis, établissement]
    champs: [exercice, organisme, numero, lieu, montant]
    nommage: "{exercice}_Avis-CFE_{lieu}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: date-document
      base: LPF L102 B
      sort-final: D
    registre: null
  - type: dossier-controle-fiscal
    libelle: Dossier de contrôle fiscal
    description: "Avis de vérification, demandes de renseignements, propositions de rectification, réponses, réclamations, décisions et rescrits."
    indices: [contrôle fiscal, avis de vérification, proposition de rectification, rescrit, réclamation]
    champs: [date, organisme, numero-dossier, objet, exercice, montant]
    nommage: "{date}_Controle-fiscal_{numero-dossier}"
    conservation:
      legale: 10a
      recommandee: permanent
      declencheur: date-document
      base: LPF L102 B
      sort-final: C
    registre: null
  - type: attestation-regularite-fiscale
    libelle: Attestation de régularité fiscale
    description: "Attestation de régularité fiscale ou de résidence fiscale, classée par date de délivrance."
    indices: [attestation de régularité fiscale, résidence fiscale, sie, régularité, attestation]
    champs: [date, organisme, numero, date-fin]
    nommage: "{date}_Attestation-regularite-fiscale"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: date-document
      base: LPF L102 B
      sort-final: D
    registre: null
va-ailleurs:
  - motif: Liasses fiscales
    vers: "04.1"
  - motif: Dossiers CIR / CII / JEI complets
    vers: "05.3"
  - motif: Calculs de plus-values et valorisations de placements
    vers: "08.9"
---

# 04.6 - Fiscalité

> Chemin : `04 - COMPTABILITE & FISCALITE/04.6 - Fiscalité`

## À quoi sert ce dossier

Toutes les déclarations et tous les échanges avec l'administration fiscale : TVA, impôt sur les sociétés, CFE/CVAE, taxes diverses, contrôles fiscaux, rescrits, attestations. Classement par impôt puis par année, ce qui correspond à la façon dont l'administration contrôle.

## Documents à y ranger

- **TVA** : déclarations CA3 / CA12 et accusés, demandes de remboursement de crédit de TVA, état récapitulatif des opérations intracommunautaires (DEB/ERTVA)
- **IS** : relevés d'acomptes (2571), relevé de solde (2572), avis d'imposition, options (report en arrière, intégration)
- **CFE / CVAE** : avis, déclarations 1447, demandes d'exonération
- **Autres taxes** : taxe sur les salaires, taxe sur les véhicules de société (TVS / taxes annuelles), taxe d'apprentissage, C3S, TASCOM, droits d'enregistrement
- **Contrôles et rescrits** : avis de vérification, demandes de renseignements, propositions de rectification, réponses, réclamations, décisions, rescrits fiscaux (JEI, CIR…)
- **Attestations** : attestation de régularité fiscale (par date), attestation de résidence fiscale
- **Comptes et actifs à l'étranger** : formulaires 3916 / 3916-bis déposés le cas échéant — l'obligation vise les sociétés civiles, les associations et les GIE, mais pas les sociétés commerciales (SAS, SARL, SA)
- Courriers du SIE, mandats de télédéclaration, options fiscales (régime, franchise, TVA sur les débits)

## Ne pas ranger ici

- Liasses fiscales → `04.1` (avec l'exercice)
- Dossiers CIR / CII / JEI complets → `05.3` (le rescrit reste ici en copie)
- Calculs de plus-values et valorisations de placements → `08.9` (seules les déclarations restent ici)

## Méthode de classement

**Un sous-dossier par impôt** (`TVA`, `IS`, `CFE-CVAE`, `Autres taxes`, `Controles et rescrits`, `Attestations`), **puis par année** : `TVA/2026/2026-03_CA3.pdf`. Un contrôle fiscal a son propre sous-dossier `Controles et rescrits/AAAA - Objet/`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | **10 ans** à compter de la dernière opération ou de la date d'établissement, depuis la réforme du 25 juin 2026 (6 ans auparavant). Le délai de reprise de l'administration reste de 3 ans, porté à 6 ans en cas de manquement et 10 ans en cas d'activité occulte. |
| **Recommandé** | 10 ans, ce qui aligne désormais le fiscal sur le comptable ; permanent pour les dossiers de contrôle et les rescrits. |

Base : LPF art. L102 B (modifié par l'art. 36 de la loi n° 2026-534 du 25 juin 2026), L169, L176 ; CGI art. 1649 A et 1649 bis C (comptes bancaires et comptes d'actifs numériques ouverts à l'étranger) ; CGI art. 1649 quater B quater (télédéclaration).

## Conseils

- L'allongement du délai fiscal de 6 à 10 ans est récent et sa date d'entrée en vigueur fait l'objet de sources divergentes ; le BOFiP n'avait pas suivi à la rédaction. En pratique, conserver 10 ans règle la question dans tous les cas.
- Une société **commerciale** (SAS, SARL, SA) n'a pas à déposer de formulaire 3916 ou 3916-bis pour ses comptes bancaires ou ses comptes d'actifs numériques ouverts à l'étranger : l'article 1649 A du CGI ne vise que les personnes physiques, les associations et les sociétés n'ayant pas la forme commerciale. Une SCI, une association ou un GIE, en revanche, doit déclarer.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
