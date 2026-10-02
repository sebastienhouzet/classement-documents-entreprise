---
schema: classement-documents/3.0
id: "08.8"
parent: "08"
niveau: sous-dossier
titre: "08.8 - Participations & filiales"
usage: >-
  Les titres détenus dans d'autres sociétés avec l'intention de les conserver durablement, parce
  qu'ils donnent le contrôle ou une influence sur l'activité : filiales, sociétés sœurs,
  participations minoritaires stratégiques, holding.
classement: par-tiers
sensibilite: confidentielle
documents:
  - type: acte-acquisition-titres-participation
    libelle: "Acte d'acquisition de titres de participation"
    description: "Acte d'acquisition ou de souscription des titres d'une société détenue, ordre de mouvement, agrément des associés, audit d'acquisition, garantie d'actif et de passif et acte de cession ultérieur."
    indices: [titre de participation, "acte d'acquisition", ordre de mouvement, due diligence, "garantie d'actif et de passif", filiale]
    champs: [date-signature, societe-detenue, designation, quantite, montant, siren]
    nommage: "{date}_Acte-acquisition-titres_{societe-detenue}_{designation}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: cession-ligne
      base: Code de commerce art. L.123-22
      sort-final: C
    registre: { fichier: Registre-des-placements.csv, cle: designation }
  - type: convention-intragroupe
    libelle: Convention intragroupe
    description: "Convention de prestations de services, de management fees, de trésorerie ou de refacturation intragroupe, avec la justification de la réalité de la prestation et de son prix."
    indices: [management fees, convention de tresorerie, refacturation intragroupe, prestation de services, realite de la prestation]
    champs: [date-signature, societe-detenue, montant, taux, objet]
    nommage: "{date}_Convention-intragroupe_{societe-detenue}_{objet}"
    conservation:
      legale: 10a
      recommandee: permanent
      declencheur: derniere-operation
      base: Code de commerce art. L.123-22
      sort-final: C
    registre: null
  - type: attestation-inscription-titres
    libelle: "Attestation d'inscription en compte"
    description: "Attestation d'inscription en compte ou extrait du registre des mouvements de titres de la société détenue, et statuts de cette société avec le pacte d'associés le cas échéant."
    indices: ["attestation d'inscription en compte", registre des mouvements de la societe detenue, statuts de la filiale, "pacte d'associes"]
    champs: [date, societe-detenue, quantite, numero, siren]
    nommage: "{date}_Attestation-inscription-titres_{societe-detenue}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: cession-ligne
      base: Code de commerce art. L.123-22
      sort-final: C
    registre: null
  - type: comptes-annuels-societe-detenue
    libelle: Comptes annuels et assemblées de la société détenue
    description: "PV d'assemblée de la société détenue, comptes annuels reçus, rapports de gestion, décisions de distribution et avis de versement de dividendes."
    indices: [comptes annuels recus, "pv d'assemblee de la filiale", distribution de dividendes, rapport de gestion, tableau des filiales]
    champs: [date, societe-detenue, exercice, montant, objet]
    nommage: "{date}_Comptes-annuels-societe-detenue_{societe-detenue}_{exercice}"
    conservation:
      legale: 10a
      recommandee: permanent
      declencheur: cloture-exercice
      base: Code de commerce art. R.123-197
      sort-final: T
    registre: null
  - type: convention-compte-courant-filiale
    libelle: "Compte courant d'associé consenti à la filiale"
    description: "Convention d'avance en compte courant consentie à une société détenue, échéancier, convention de blocage et calcul des intérêts et du taux maximal déductible."
    indices: [compte courant consenti a la filiale, convention de blocage, taux maximal deductible, avance en compte courant, echeancier]
    champs: [date-signature, societe-detenue, montant, taux, echeance]
    nommage: "{date}_Convention-compte-courant-filiale_{societe-detenue}"
    conservation:
      legale: 10a
      recommandee: permanent
      declencheur: fin-contrat
      base: Code de commerce art. L.123-22
      sort-final: C
    registre: null
va-ailleurs:
  - motif: "Le capital de votre propre société, votre pacte d'associés, vos BSPCE"
    vers: "01.6"
  - motif: Titres cotés détenus pour placer la trésorerie
    vers: "08.3"
  - motif: Parts de fonds sans influence sur la gestion
    vers: "08.7"
  - motif: Levée de fonds dans votre société
    vers: "05.4"
---

# 08.8 - Participations & filiales

> Chemin : `08 - PLACEMENTS & PARTICIPATIONS/08.8 - Participations & filiales`

## À quoi sert ce dossier

Les titres détenus dans d'autres sociétés avec l'intention de les conserver durablement, parce qu'ils donnent le contrôle ou une influence sur l'activité : filiales, sociétés sœurs, participations minoritaires stratégiques, holding. À ne pas confondre avec `01.6`, qui traite du capital de **votre** société : ici, il s'agit du capital des autres.

## Documents à y ranger

- Acte d'acquisition ou de souscription des titres, ordre de mouvement, agrément des associés
- Statuts de la société détenue et pacte d'associés le cas échéant
- Attestation d'inscription en compte ou extrait du registre des mouvements de titres de la société détenue
- Audit d'acquisition (due diligence), garantie d'actif et de passif, séquestre
- Vie de la participation : PV d'assemblée de la société détenue, comptes annuels reçus, rapports de gestion, décisions de distribution, avis de versement de dividendes
- Comptes courants d'associé consentis à la filiale : convention, échéancier, convention de blocage, calcul des intérêts et du taux maximal déductible
- Conventions intragroupe : prestations de services, management fees, convention de trésorerie, refacturations — avec la justification de la réalité de la prestation et de son prix
- Régimes de groupe : option et convention d'intégration fiscale, régime mère-fille (attestation de détention d'au moins 5 % pendant deux ans), justificatifs
- Valorisation à la clôture, tests de dépréciation des titres et leur justification
- Tableau des filiales et participations annexé aux comptes
- Cession : lettre d'intention, protocole, acte de cession, enregistrement, calcul de la plus-value

## Ne pas ranger ici

- Le capital de votre propre société, votre pacte d'associés, vos BSPCE → `01.6`
- Titres cotés détenus pour placer la trésorerie → `08.3`
- Parts de fonds sans influence sur la gestion → `08.7`
- Levée de fonds **dans** votre société → `05.4`

## Méthode de classement

**Un sous-dossier par société détenue** : `Nom de la société (SIREN)`. À l'intérieur : `Acquisition`, `Titres et statuts`, `Assemblees et comptes/AAAA`, `Conventions intragroupe`, `Compte courant`, `Fiscalite`, `Cession`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Actes de cession de titres : 5 ans. Pièces comptables : 10 ans après la sortie. Documents fiscaux et conventions intragroupe : 10 ans après la dernière application. |
| **Recommandé** | Permanent. La chaîne de propriété des titres et les conventions intragroupe sont les premières pièces demandées lors d'une cession, d'un contrôle fiscal ou d'une due diligence. |

Base : Code de commerce art. L.123-22 et R.123-197 (tableau des filiales et participations) ; CGI art. 145 et 216 (régime mère-fille), art. 219 I-a quinquies (plus-values sur titres de participation), art. 223 A et s. (intégration fiscale).

## Conseils

- Les conventions intragroupe non écrites ou non facturées sont la faiblesse la plus fréquente des groupes de PME : un contrat daté, une facture et une preuve de la prestation, rangés ici par convention, valent mieux qu'une explication a posteriori.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
