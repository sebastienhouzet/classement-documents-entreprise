---
schema: classement-documents/3.0
id: "01.3"
parent: "01"
niveau: sous-dossier
titre: "01.3 - Assemblées & décisions"
usage: >-
  Les décisions des associés (AG ordinaires et extraordinaires, décisions de l'associé unique)
  et, le cas échéant, du conseil d'administration ou du comité stratégique.
classement: chronologique
sensibilite: confidentielle
documents:
  - type: pv-assemblee-generale
    libelle: "Procès-verbal d'assemblée générale"
    description: "Procès-verbal signé d'une AGO, d'une AGE, d'une décision de l'associé unique ou du conseil."
    indices: [pv, proces-verbal, ago, age, assemblee generale, approbation des comptes, affectation du resultat]
    champs: [date, exercice, objet, signataire]
    nommage: "{date}_PV-assemblee-generale_{objet}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: fin-utilisation
      base: Code de commerce art. L.225-117
      sort-final: C
    registre: null
  - type: convocation-assemblee
    libelle: Convocation et ordre du jour
    description: "Convocation des associés, ordre du jour et texte des résolutions proposées."
    indices: [convocation, ordre du jour, resolutions proposees, assemblee generale, delai de convocation]
    champs: [date, destinataire, objet, exercice]
    nommage: "{date}_Convocation-AG_{destinataire}_{objet}"
    conservation:
      legale: 3a
      recommandee: permanent
      declencheur: cloture-exercice
      base: Code de commerce art. R.225-89
      sort-final: D
    registre: null
  - type: rapport-de-gestion-dirigeant
    libelle: Rapport de gestion
    description: "Rapport de gestion du dirigeant présenté à l'assemblée, et rapport du commissaire aux comptes le cas échéant."
    indices: [rapport de gestion, rapport du commissaire aux comptes, situation de la societe, resolutions, exercice ecoule]
    champs: [date, exercice, signataire, objet]
    nommage: "{date}_Rapport-de-gestion_{exercice}"
    conservation:
      legale: 3a
      recommandee: permanent
      declencheur: cloture-exercice
      base: Code de commerce art. L.223-26
      sort-final: C
    registre: null
  - type: feuille-presence-pouvoirs
    libelle: Feuille de présence et pouvoirs
    description: "Feuille de présence de l'assemblée, pouvoirs et procurations donnés par les associés."
    indices: [feuille de presence, pouvoir, procuration, quorum, "mandataire d'associe"]
    champs: [date, associe, exercice, effectif]
    nommage: "{date}_Feuille-de-presence_{exercice}"
    conservation:
      legale: 3a
      recommandee: permanent
      declencheur: cloture-exercice
      base: Code de commerce art. R.225-89
      sort-final: T
    registre: null
  - type: recepisse-depot-comptes
    libelle: Récépissé de dépôt des comptes au greffe
    description: "Récépissé du dépôt annuel des comptes au greffe, avec le cas échéant la déclaration de confidentialité."
    indices: [depot des comptes au greffe, recepisse de depot, confidentialite des comptes, greffe, comptes annuels deposes]
    champs: [date, organisme, exercice, reference]
    nommage: "{date}_Recepisse-depot-comptes_{exercice}"
    conservation:
      legale: 5a
      recommandee: permanent
      declencheur: cloture-exercice
      base: Code de commerce art. L.223-26
      sort-final: C
    registre: null
va-ailleurs:
  - motif: Comptes annuels et liasses
    vers: "04.1"
  - motif: "Statuts modifiés à la suite d'une AGE"
    vers: "01.2"
---

# 01.3 - Assemblées & décisions

> Chemin : `01 - JURIDIQUE & GOUVERNANCE/01.3 - Assemblées & décisions`

## À quoi sert ce dossier

Les décisions des associés (AG ordinaires et extraordinaires, décisions de l'associé unique) et, le cas échéant, du conseil d'administration ou du comité stratégique. C'est ici que vit la preuve de l'approbation annuelle des comptes.

## Documents à y ranger

- Convocations et ordres du jour
- Rapport de gestion du dirigeant, texte des résolutions proposées
- Rapport du commissaire aux comptes (si CAC)
- Feuilles de présence, pouvoirs, procurations
- Procès-verbaux signés (AGO, AGE, décisions de l'associé unique, conseil)
- Récépissé de dépôt des comptes annuels au greffe (et option de confidentialité)
- Décisions courantes : affectation du résultat, distribution de dividendes, rémunération du dirigeant, conventions réglementées, nomination du CAC

## Ne pas ranger ici

- Comptes annuels et liasses → `04.1`
- Statuts modifiés à la suite d'une AGE → `01.2`

## Méthode de classement

**Un sous-dossier par exercice** (`2025`, `2026`…). À l'intérieur, nommage `AAAA-MM-JJ_PV-AGO_Approbation-comptes-2025.pdf`. Si plusieurs organes délibèrent (AG et conseil), créer un sous-dossier par organe dans l'année.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Registres de PV : 5 ans à compter de la fin de leur utilisation. Feuilles de présence, pouvoirs, rapports : 3 derniers exercices. |
| **Recommandé** | Permanent pour les PV. Garder feuilles de présence et rapports avec le PV auquel ils se rattachent (même durée). |

Base : Code de commerce, art. L.225-117, L.223-26, R.225-89 ; Code civil art. 1844-1.

## Conseils

- Déposer les comptes au greffe dans le mois suivant l'AG (2 mois si dépôt en ligne) et ranger le récépissé ici, dans l'année concernée.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
