---
schema: classement-documents/3.0
id: "08.1"
parent: "08"
niveau: sous-dossier
titre: "08.1 - Politique de placement & décisions"
usage: >-
  Le « pourquoi » des placements : le cadre que l'entreprise se donne et la trace de chaque
  décision d'investir. C'est le dossier qui protège en cas de contrôle fiscal ou de désaccord
  entre associés, parce qu'il montre que le placement a été décidé, par la bonne personne, dans
  l'intérêt de la société.
classement: chronologique
sensibilite: confidentielle
documents:
  - type: politique-de-placement
    libelle: Politique de placement de la trésorerie
    description: "Version datée de la politique de placement — horizon, part de trésorerie mobilisable, niveau de risque accepté, supports autorisés et interdits, plafond par ligne et par contrepartie."
    indices: [politique de placement, horizon, niveau de risque, supports autorises, plafond par ligne, version datee]
    champs: [date, date-effet, version, objet]
    nommage: "{date}_Politique-de-placement_{version}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: elaboration-version
      base: Code civil art. 2224
      sort-final: C
    registre: null
  - type: note-decision-placement
    libelle: "Note de décision d'investissement"
    description: "Note datée et signée pour chaque investissement — montant, support, intention de détention, durée visée, justification de l'intérêt social. L'intention conditionne le traitement comptable pendant toute la détention."
    indices: [note de decision, "decision d'investissement", intention de detention, interet social, horizon de placement]
    champs: [date, montant, support, intention-detention, duree, signataire]
    nommage: "{date}_Decision-placement_{support}_{montant}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: date-document
      base: CGI art. 39
      sort-final: C
    registre: null
  - type: mandat-gestion-placement
    libelle: Mandat de gestion ou convention de conseil
    description: "Mandat de gestion, convention de conseil en investissement ou lettre de mission du conseiller ou du banquier privé."
    indices: [mandat de gestion, convention de conseil en investissement, lettre de mission, banquier prive, conseiller financier]
    champs: [date-signature, gestionnaire, numero-contrat, objet, duree]
    nommage: "{date}_Mandat-de-gestion_{gestionnaire}_{objet}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: fin-mandat
      base: Code monétaire et financier art. L.533-11
      sort-final: C
    registre: null
  - type: rapport-adequation-conseil
    libelle: Documents réglementaires avant souscription
    description: "Document d'entrée en relation, questionnaire de connaissance et d'expérience, profil de risque, catégorisation de la personne morale et rapport d'adéquation remis avant souscription."
    indices: ["rapport d'adequation", profil de risque, questionnaire de connaissance, "document d'entree en relation", categorisation]
    champs: [date, gestionnaire, objet, reference]
    nommage: "{date}_Rapport-d-adequation_{gestionnaire}_{objet}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: date-document
      base: Code monétaire et financier art. L.533-11
      sort-final: T
    registre: null
va-ailleurs:
  - motif: "PV d'assemblée originaux"
    vers: "01.3"
  - motif: Le contrat de chaque placement
    vers: "08.2"
  - motif: Budget et plan de trésorerie
    vers: "04.8"
---

# 08.1 - Politique de placement & décisions

> Chemin : `08 - PLACEMENTS & PARTICIPATIONS/08.1 - Politique de placement & décisions`

## À quoi sert ce dossier

Le « pourquoi » des placements : le cadre que l'entreprise se donne et la trace de chaque décision d'investir. C'est le dossier qui protège en cas de contrôle fiscal ou de désaccord entre associés, parce qu'il montre que le placement a été décidé, par la bonne personne, dans l'intérêt de la société.

## Documents à y ranger

- Politique de placement de la trésorerie (version datée) : horizon, part de la trésorerie mobilisable, niveau de risque accepté, supports autorisés et interdits, plafond par ligne et par contrepartie
- Vérification de l'objet social : extrait des clauses statutaires autorisant les opérations financières, avis de l'avocat ou de l'expert-comptable
- Note de décision datée et signée pour chaque investissement : montant, support, **intention de détention**, durée visée, justification de l'intérêt social
- PV ou décision de l'organe compétent quand les statuts l'exigent (copie — original dans `01.3`)
- Mandats de gestion, conventions de conseil en investissement, lettres de mission du conseiller ou du banquier privé
- Documents réglementaires reçus avant souscription : document d'entrée en relation, questionnaire de connaissance et d'expérience, profil de risque, catégorisation de la personne morale (client non professionnel ou professionnel), rapport d'adéquation
- Analyses, comparatifs et simulations ayant conduit au choix
- Revues périodiques du portefeuille : comptes rendus d'arbitrage, décisions de renforcement ou de cession

## Ne pas ranger ici

- PV d'assemblée originaux → `01.3`
- Le contrat de chaque placement → dans le sous-dossier de sa ligne (`08.2` à `08.8`)
- Budget et plan de trésorerie → `04.8`

## Méthode de classement

À plat pour la politique de placement (la version en vigueur à la racine, les précédentes dans `Anciennes versions`). Un sous-dossier `Decisions/AAAA` avec une note par décision : `AAAA-MM-JJ_Decision_Placement_Support-montant.pdf`. Un sous-dossier `Intermediaires/Nom` pour les documents réglementaires qui couvrent plusieurs placements.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | 5 ans (prescription de droit commun) ; les documents d'information et de conseil sont conservés 5 ans minimum par le prestataire. |
| **Recommandé** | Permanent — la note de décision est la seule pièce qui explique l'intention, et l'intention conditionne le traitement comptable et fiscal pendant toute la détention. |

Base : Code civil art. 2224 ; Code monétaire et financier art. L.533-11 et s. (obligations d'information et de conseil) ; CGI art. 39 et doctrine de l'acte anormal de gestion.

## Conseils

- Une note d'une page par décision suffit : date, montant, support, pourquoi, horizon, intention comptable, qui décide. C'est le document le plus utile du domaine, et le plus souvent absent.
- Vérifier que l'objet social couvre la gestion d'un portefeuille de titres ou d'actifs numériques ; sinon, faire modifier les statuts (`01.2`) avant d'investir.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
