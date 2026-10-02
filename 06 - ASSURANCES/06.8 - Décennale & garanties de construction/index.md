---
schema: classement-documents/3.0
id: "06.8"
parent: "06"
niveau: sous-dossier
titre: "06.8 - Décennale & garanties de construction"
usage: >-
  Assurance décennale et garanties de construction des entreprises du bâtiment : contrat et
  attestations décennales, procès-verbaux de réception de travaux, garantie de parfait
  achèvement, DOE et DIUO par chantier.
classement: par-operation
sensibilite: normale
documents:
  - type: contrat-assurance-decennale
    libelle: "Contrat d'assurance décennale"
    description: "Contrat d'assurance décennale (et dommages-ouvrage le cas échéant) — conditions particulières et générales, et surtout la liste des activités déclarées, seules garanties."
    indices: [assurance decennale, dommages-ouvrage, activites declarees, conditions particulieres, "obligation d'assurance"]
    champs: [date-effet, assureur, numero-contrat, objet, montant, plafond-garantie, franchise]
    nommage: "{date}_Contrat-assurance-decennale_{assureur}_{numero-contrat}"
    conservation:
      legale: 2a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code des assurances art. L241-1
      sort-final: C
    registre: { fichier: Registre-des-assurances.csv, cle: numero-contrat }
  - type: attestation-decennale
    libelle: "Attestation d'assurance décennale"
    description: "Attestation annuelle de décennale, à joindre aux devis et aux factures et à obtenir avant l'ouverture du chantier (copie de l'année en cours dans 97/Kit administratif)."
    indices: [attestation decennale, avant ouverture de chantier, a joindre au devis, activites garanties, attestation du sous-traitant]
    champs: [exercice, assureur, numero-contrat, objet, echeance]
    nommage: "{exercice}_Attestation-decennale_{assureur}"
    conservation:
      legale: 2a
      recommandee: 10a
      declencheur: reception-travaux
      base: Code des assurances art. L241-1
      sort-final: C
    registre: null
  - type: pv-reception-travaux
    libelle: Procès-verbal de réception des travaux
    description: "Procès-verbal de réception du chantier, avec ou sans réserves, et procès-verbal de levée des réserves — le délai décennal court à compter du lendemain de sa signature."
    indices: [pv de reception, reception des travaux, reserves, levee de reserves, point de depart de la decennale]
    champs: [date, client, chantier, adresse, statut]
    nommage: "{date}_PV-de-reception_{client}_{chantier}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: reception-travaux
      base: Code civil art. 1792-6
      sort-final: C
    registre: null
  - type: garantie-parfait-achevement
    libelle: Garantie de parfait achèvement
    description: "Courriers de signalement, interventions et preuves de reprise au titre de la garantie de parfait achèvement, qui couvre l'année suivant la réception."
    indices: [parfait achevement, reprise de desordre, signalement apres reception, intervention sous garantie]
    champs: [date, client, chantier, objet, montant]
    nommage: "{date}_Garantie-parfait-achevement_{client}_{chantier}"
    conservation:
      legale: 1a
      recommandee: 10a
      declencheur: reception-travaux
      base: Code civil art. 1792-6
      sort-final: T
    registre: null
  - type: doe-diuo-chantier
    libelle: DOE et DIUO du chantier
    description: "Dossier des ouvrages exécutés (plans conformes à l'exécution, notices, fiches produits) et dossier d'intervention ultérieure sur l'ouvrage ; ils suivent la durée de vie de l'ouvrage."
    indices: [doe, diuo, "plans conformes a l'execution", notices, fiches produits, ppsps]
    champs: [date, client, chantier, adresse, designation]
    nommage: "{date}_DOE-DIUO_{client}_{chantier}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: reception-travaux
      base: Code du travail art. L4532-16
      sort-final: C
    registre: null
va-ailleurs:
  - motif: "Déclaration et suivi d'un sinistre"
    vers: "06.7"
  - motif: Contrat client et devis
    vers: "02.1"
  - motif: Contrats de sous-traitance
    vers: "02.3"
---

# 06.8 - Décennale & garanties de construction

> Chemin : `06 - ASSURANCES/06.8 - Décennale & garanties de construction`

## À quoi sert ce dossier

Ne concerne que les entreprises qui réalisent des travaux de construction : bâtiment, second œuvre, rénovation, installation d'équipements indissociables de l'ouvrage. L'assurance décennale y est obligatoire, doit être souscrite **avant l'ouverture du chantier**, et son attestation doit figurer sur les devis et les factures. Si vous ne faites pas de travaux, laissez ce dossier vide ou supprimez-le.

## Documents à y ranger

- Contrat d'assurance décennale : conditions particulières et générales, et surtout la liste des **activités déclarées** — la garantie ne couvre que celles-là
- Attestations annuelles, à joindre aux devis et aux factures (copie de l'année en cours dans `97/Kit administratif`)
- Assurance dommages-ouvrage lorsque l'entreprise est maître d'ouvrage
- **Procès-verbal de réception des travaux**, avec ou sans réserves — pièce maîtresse du dossier : le délai décennal court à compter du lendemain de sa signature
- Levée des réserves et procès-verbal correspondant
- **Garantie de parfait achèvement** (1 an) et **garantie biennale de bon fonctionnement** (2 ans) : courriers, interventions, preuves de reprise
- **DOE**, dossier des ouvrages exécutés : plans conformes à l'exécution, notices, fiches produits
- **DIUO**, dossier d'intervention ultérieure sur l'ouvrage
- PPSPS, plan de prévention, déclaration préalable de chantier
- Sous-traitance : DC4, attestations de vigilance et attestations de décennale des sous-traitants, à renouveler tous les 6 mois

## Ne pas ranger ici

- Déclaration et suivi d'un sinistre → `06.7`
- Contrat client et devis → `02.1`
- Contrats de sous-traitance → `02.3`

## Méthode de classement

Le contrat et les attestations à la racine, nommés comme les autres contrats d'assurance (`Assureur - N° contrat`), puis **un sous-dossier par chantier** : `AAAA - Client - Adresse du chantier`, contenant `Reception`, `Garanties`, `DOE-DIUO`, `Sous-traitance`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Assurance : 2 ans après la fin du contrat (prescription biennale). Responsabilité décennale : 10 ans à compter de la réception. Parfait achèvement : 1 an. Garantie biennale : 2 ans. |
| **Recommandé** | **Attestation de décennale et PV de réception : au moins 10 ans après la réception de chaque chantier**, et en pratique sans limite. DOE et DIUO suivent la durée de vie de l'ouvrage. |

Base : Code des assurances art. L241-1 (obligation d'assurance) ; Code civil art. 1792, 1792-3 et 1792-6 (garanties légales) ; Code du travail art. L4532-16 (DIUO).

## Conseils

- Le défaut d'assurance décennale est un **délit** : 75 000 € d'amende et six mois d'emprisonnement. L'attestation s'obtient avant l'ouverture du chantier, pas après.
- Vérifier que les activités déclarées au contrat couvrent réellement ce que l'entreprise exécute : une activité non déclarée n'est pas garantie, et c'est le motif de refus le plus fréquent.
- Le PV de réception est la pièce la plus importante de ce dossier. Sans procès-verbal daté, le point de départ des garanties est discutable — et le doute joue rarement en faveur de l'entreprise.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
