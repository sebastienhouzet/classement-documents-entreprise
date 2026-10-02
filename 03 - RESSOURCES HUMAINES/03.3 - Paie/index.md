---
schema: classement-documents/3.0
id: "03.3"
parent: "03"
niveau: sous-dossier
titre: 03.3 - Paie
usage: >-
  Les documents produits chaque mois par la paie : bulletins (double employeur), journal de
  paie, DSN et ses accusés, écritures comptables de paie.
classement: chronologique
sensibilite: rh
documents:
  - type: bulletin-paie-double-employeur
    libelle: Bulletin de paie (double employeur)
    description: "Exemplaire du bulletin conservé par l'employeur, y compris pour le dirigeant assimilé salarié."
    indices: [bulletin de paie, bulletin de salaire, double employeur, paie, variables de paie]
    champs: [periode, salarie, montant]
    nommage: "{periode}_Bulletin_{salarie}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: date-document
      base: Code du travail L3243-4
      sort-final: C
    registre: null
  - type: preuve-mise-a-disposition-bulletin-electronique
    libelle: Preuve de mise à disposition du bulletin électronique
    description: "Trace de la mise à disposition du bulletin dématérialisé au salarié et engagement du prestataire sur sa durée de rétention. Obligation distincte du double conservé par l'employeur."
    indices: [bulletin électronique, bulletin dématérialisé, mise à disposition, coffre-fort, prestataire de paie]
    champs: [periode, salarie, emetteur, duree]
    nommage: "{periode}_Bulletin-electronique_{salarie}"
    conservation:
      legale: 50a
      recommandee: permanent
      declencheur: date-document
      base: Code du travail D3243-8
      sort-final: C
    registre: null
  - type: dsn-mensuelle
    libelle: DSN et accusé de réception
    description: "Déclaration sociale nominative mensuelle ou événementielle, avec son accusé net-entreprises."
    indices: [dsn, net-entreprises, déclaration sociale nominative, accusé, événementielle]
    champs: [periode, organisme, numero, date]
    nommage: "{periode}_DSN_{organisme}"
    conservation:
      legale: 6a
      recommandee: 10a
      declencheur: date-document
      base: Code de la sécurité sociale L243-16
      sort-final: D
    registre: null
  - type: journal-de-paie
    libelle: Journal de paie mensuel
    description: "Journal ou livre de paie du mois, état des charges sociales et écritures de paie."
    indices: [journal de paie, livre de paie, état des charges sociales, od de paie, rapprochement]
    champs: [periode, montant, effectif]
    nommage: "{periode}_Journal-de-paie"
    conservation:
      legale: 6a
      recommandee: 10a
      declencheur: date-document
      base: Code de la sécurité sociale L243-16
      sort-final: D
    registre: null
  - type: bordereau-cotisations-sociales
    libelle: Bordereau de cotisations sociales
    description: "Bordereau ou appel de cotisations d'un organisme (URSSAF, retraite, prévoyance, mutuelle) rattaché au mois de paie."
    indices: [bordereau de cotisations, appel de cotisations, urssaf, retraite complémentaire, prévoyance]
    champs: [periode, organisme, montant, echeance]
    nommage: "{periode}_Bordereau_{organisme}"
    conservation:
      legale: 6a
      recommandee: 10a
      declencheur: date-document
      base: Code de la sécurité sociale L243-16
      sort-final: D
    registre: null
va-ailleurs:
  - motif: Contrats de travail
    vers: "03.2"
  - motif: Contrats mutuelle/prévoyance
    vers: "06.4"
---

# 03.3 - Paie

> Chemin : `03 - RESSOURCES HUMAINES/03.3 - Paie`

## À quoi sert ce dossier

Les documents produits chaque mois par la paie : bulletins (double employeur), journal de paie, DSN et ses accusés, écritures comptables de paie. Classés par mois pour toute l'entreprise, ce qui correspond à la façon dont ils sont produits et contrôlés.

## Documents à y ranger

- Bulletins de paie (exemplaire employeur), y compris ceux du dirigeant assimilé salarié
- Journal / livre de paie mensuel, état des charges sociales
- DSN mensuelles et accusés de réception (net-entreprises), DSN événementielles (arrêts, fins de contrat)
- Écritures de paie (OD) et état de rapprochement avec la comptabilité
- Bordereaux et appels de cotisations (URSSAF, retraite, prévoyance, mutuelle) si non rangés dans `03.4`
- Variables de paie du mois (fichier transmis au gestionnaire de paie), notes de frais → `04.4`
- Récapitulatifs annuels : état annuel des salaires, taxe sur les salaires, attestation fiscale
- Bulletins électroniques : preuve de la mise à disposition et engagement du prestataire sur sa durée — obligation distincte du double conservé par l'employeur

## Ne pas ranger ici

- Contrats de travail → `03.2`
- Contrats mutuelle/prévoyance → `06.4`

## Méthode de classement

**Par année, puis par mois** : `AAAA/AAAA-MM/`. À l'intérieur, un fichier par type : `2026-03_Bulletins.pdf`, `2026-03_Journal-de-paie.pdf`, `2026-03_DSN_accuse.pdf`. Un sous-dossier `AAAA/Annuel` pour les récapitulatifs.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Bulletins de paie, double conservé par l'employeur : 5 ans. **Mise à disposition du bulletin électronique au salarié : 50 ans, ou jusqu'à ses 75 ans.** Documents nécessaires au contrôle des cotisations, assiette et DSN : 6 ans. |
| **Recommandé** | 10 ans (ces pièces justifient des écritures comptables). En pratique, beaucoup d'entreprises gardent les bulletins sans limite : ils servent aux salariés pour reconstituer leur carrière. |

Base : Code du travail art. L3243-4 (double employeur, 5 ans) et D3243-8 (bulletin électronique, 50 ans ou 75 ans du salarié) ; Code de la sécurité sociale art. L243-16 (conservation pour le contrôle) ; Code de commerce art. L123-22 (10 ans).

## Conseils

- Ne pas confondre les deux durées du bulletin de paie : **5 ans** pour le double que l'employeur conserve, **50 ans** pour la mise à disposition du bulletin dématérialisé au salarié. Si la paie est externalisée, vérifier noir sur blanc ce que le prestataire s'engage à conserver, et pendant combien de temps.
- Les 3 ans souvent cités pour les charges sociales correspondent à la prescription du **recouvrement** URSSAF (art. L244-3). La conservation pour le **contrôle** relève de l'art. L243-16, et la CNIL retient 6 ans : c'est la durée à appliquer.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
