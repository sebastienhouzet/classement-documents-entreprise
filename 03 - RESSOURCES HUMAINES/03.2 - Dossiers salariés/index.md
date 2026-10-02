---
schema: classement-documents/3.0
id: "03.2"
parent: "03"
niveau: sous-dossier
titre: 03.2 - Dossiers salariés
usage: >-
  Un dossier par salarié (CDI, CDD, dirigeant assimilé salarié) qui suit la personne de son
  embauche à sa sortie. C'est le dossier que l'on ouvre pour un avenant, un entretien, une
  rupture ou un contentieux prud'homal.
classement: par-tiers
sensibilite: rh
documents:
  - type: contrat-de-travail
    libelle: Contrat de travail
    description: "CDI, CDD ou contrat du dirigeant assimilé salarié, dans le dossier individuel du salarié."
    indices: [contrat de travail, cdi, cdd, dpae, "promesse d'embauche", fiche de poste]
    champs: [date, salarie, intitule-poste, date-debut, montant]
    nommage: "{date}_Contrat_{salarie}_{intitule-poste}"
    conservation:
      legale: 5a
      recommandee: 5a
      declencheur: depart-salarie
      base: Code du travail L1471-1
      sort-final: D
    registre: null
  - type: avenant-contrat-travail
    libelle: Avenant au contrat de travail
    description: "Modification du contrat en cours de vie : poste, rémunération, durée du travail, télétravail."
    indices: [avenant, changement de poste, télétravail, augmentation, prime]
    champs: [date, salarie, objet, date-effet, montant]
    nommage: "{date}_Avenant_{salarie}_{objet}"
    conservation:
      legale: 5a
      recommandee: 5a
      declencheur: depart-salarie
      base: Code du travail L1471-1
      sort-final: D
    registre: null
  - type: sanction-disciplinaire
    libelle: Courrier disciplinaire
    description: "Avertissement, blâme ou mise à pied notifié au salarié ; retiré du dossier au bout de trois ans."
    indices: [avertissement, mise à pied, sanction, disciplinaire, entretien préalable]
    champs: [date, salarie, motif, nature]
    nommage: "{date}_Avertissement_{salarie}_{motif}"
    conservation:
      legale: 3a
      recommandee: 3a
      declencheur: date-document
      base: Code du travail L1332-5
      sort-final: D
    registre: null
  - type: solde-tout-compte
    libelle: Reçu pour solde de tout compte
    description: "Reçu remis au départ du salarié, avec le détail des sommes versées."
    indices: [solde de tout compte, démission, licenciement, rupture conventionnelle, fin de cdd]
    champs: [date, salarie, montant, date-fin]
    nommage: "{date}_Solde-de-tout-compte_{salarie}"
    conservation:
      legale: 5a
      recommandee: 5a
      declencheur: depart-salarie
      base: Code du travail L1471-1
      sort-final: D
    registre: null
  - type: certificat-de-travail
    libelle: Certificat de travail et attestation France Travail
    description: "Documents de fin de contrat remis au salarié, attestant la période et l'emploi occupé."
    indices: [certificat de travail, attestation france travail, fin de contrat, sortie, portabilité]
    champs: [date, salarie, intitule-poste, date-debut, date-fin]
    nommage: "{date}_Certificat-de-travail_{salarie}"
    conservation:
      legale: 5a
      recommandee: 5a
      declencheur: depart-salarie
      base: Code du travail L1471-1
      sort-final: D
    registre: null
  - type: rib-salarie
    libelle: Coordonnées bancaires du salarié
    description: RIB remis par le salarié pour le versement de son salaire. Donnée personnelle — accès restreint au même titre que le reste du dossier individuel.
    indices: [rib, coordonnees bancaires, iban, virement du salaire]
    champs: [date, salarie, iban, bic]
    nommage: "{date}_RIB_{salarie}"
    conservation:
      legale: 5a
      recommandee: 5a
      declencheur: depart-salarie
      base: Code du travail L1471-1
      sort-final: D
    registre: null
va-ailleurs:
  - motif: Bulletins de paie
    vers: "03.3"
  - motif: Arrêts de travail et congés
    vers: "03.7"
  - motif: Avis médicaux
    vers: "03.8"
  - motif: Candidature initiale
    vers: null
---

# 03.2 - Dossiers salariés

> Chemin : `03 - RESSOURCES HUMAINES/03.2 - Dossiers salariés`

## À quoi sert ce dossier

Un dossier par salarié (CDI, CDD, dirigeant assimilé salarié) qui suit la personne de son embauche à sa sortie. C'est le dossier que l'on ouvre pour un avenant, un entretien, une rupture ou un contentieux prud'homal. Il ne contient **pas** les bulletins de paie (→ `03.3`), qui sont classés par mois pour toute l'entreprise.

## Documents à y ranger

- **01 Embauche** : promesse d'embauche, DPAE (accusé URSSAF), contrat de travail et avenants, fiche de poste, pièce d'identité (et titre de séjour / autorisation de travail si concerné), justificatif de domicile, RIB, affiliation mutuelle ou dispense, désignation prévoyance, charte informatique signée, remise du matériel (`07.6`), clause de non-concurrence / de confidentialité
- **02 Vie du contrat** : comptes rendus d'entretiens annuels et d'entretiens professionnels (tous les 2 ans, bilan à 6 ans), attestations de formation, augmentations et primes (courriers), changements de poste, télétravail (avenant), courriers disciplinaires (avertissements — à retirer du dossier après 3 ans), demandes diverses
- **03 Sortie** : démission, rupture conventionnelle (Cerfa + homologation), licenciement (convocation, entretien, notification), fin de CDD, reçu pour solde de tout compte, certificat de travail, attestation France Travail, portabilité mutuelle/prévoyance, restitution du matériel, levée de clause de non-concurrence

## Ne pas ranger ici

- Bulletins de paie → `03.3`
- Arrêts de travail et congés → `03.7`
- Avis médicaux → `03.8`
- Candidature initiale → supprimer (elle a servi)

## Méthode de classement

**Un sous-dossier par salarié** `NOM Prénom`, contenant les trois sous-dossiers `01 Embauche`, `02 Vie du contrat`, `03 Sortie`. Fichiers `AAAA-MM-JJ_Type_Objet.pdf`. Au départ du salarié : déplacer tout son dossier dans `98 - ARCHIVES/AAAA/03 - RH/`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Contrat, avenants, primes, indemnités, solde de tout compte : 5 ans après le départ. Sanctions disciplinaires : 3 ans (ne peuvent plus être invoquées). Titre de séjour : durée du contrat. |
| **Recommandé** | 5 ans après le départ, puis destruction (sauf contentieux en cours). Supprimer les copies de pièces d'identité dès le départ du salarié. |

Base : Code du travail art. L.1332-5 (sanctions 3 ans), L.3245-1 (salaires 3 ans), L.1471-1 (prud'hommes 2 ans / 5 ans) ; Code civil art. 2224 ; CNIL.

## Conseils

- Accès strictement limité. Si le stockage est partagé (Drive, NAS), ce dossier doit avoir ses propres droits.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
