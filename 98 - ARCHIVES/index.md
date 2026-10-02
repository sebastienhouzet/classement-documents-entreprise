---
schema: classement-documents/3.0
id: "98"
parent: null
niveau: systeme
titre: 98 - Archives
usage: >-
  Les dossiers clos dont la durée de conservation n'est pas encore écoulée : anciens salariés,
  contrats terminés, exercices anciens, litiges réglés, véhicules revendus, contrats d'assurance
  résiliés.
classement: chronologique
sensibilite: confidentielle
documents:
  - type: dossier-clos-archive
    libelle: Dossier clos archivé
    description: "Dossier clos déplacé tel quel, par année de clôture et en reproduisant son chemin d'origine. Sa durée de conservation n'est pas propre à ce dossier — elle est héritée du domaine d'origine (voir 97 - REFERENTIEL/Durees-de-conservation.md), et la date de destruction prévue est portée au Registre-des-archives.csv ainsi que dans le nom du dossier entre crochets."
    indices: [dossier clos, salarie parti, contrat termine, exercice ancien, litige regle, vehicule revendu, contrat resilie]
    champs: [date, reference, objet, echeance, duree]
    nommage: "{date}_Dossier-clos-archive_{reference}"
    conservation:
      legale: aucune
      recommandee: aucune
      declencheur: aucun
      sort-final: T
    registre: { fichier: Registre-des-archives.csv, cle: reference }
va-ailleurs:
  - motif: Les dossiers encore actifs
    vers: null
  - motif: "Ce qui ne se détruit jamais (statuts, PV, registres, bilans, pactes)"
    vers: null
  - motif: Les dossiers dont la date de destruction est atteinte
    vers: "99"
---

# 98 - Archives

> Chemin : `98 - ARCHIVES`

## À quoi sert ce dossier

Les dossiers **clos** dont la durée de conservation n'est pas encore écoulée : anciens salariés, contrats terminés, exercices anciens, litiges réglés, véhicules revendus, contrats d'assurance résiliés. Les archiver ici allège les dossiers courants tout en respectant les obligations de conservation, et prépare la destruction à la bonne date.

## Documents à y ranger

- `Registre-des-archives.csv` à la racine : dossier archivé, chemin d'origine, date de clôture, durée de conservation, **date de destruction prévue**, date de destruction effective
- Les dossiers clos, déplacés tels quels (avec leur `index.md` d'origine si utile)
- Un fichier `Procedure-archivage.md` décrivant qui archive, quand (janvier de chaque année), et qui valide les destructions

## Ne pas ranger ici

- Les dossiers encore actifs → ils restent dans leur domaine d'origine
- Ce qui ne se détruit jamais (statuts, PV, registres, bilans, pactes) → reste dans son dossier d'origine, ne passe jamais par ici
- Les dossiers dont la date de destruction est atteinte → `99 - SUPPRESSION`

## Méthode de classement

**Par année de clôture, puis en reproduisant le chemin d'origine** : `AAAA/03 - RESSOURCES HUMAINES/03.2 - Dossiers salariés/NOM Prénom/`. La date de clôture est celle qui fait courir le délai (départ du salarié, fin du contrat, clôture de l'exercice, règlement du sinistre). Ajouter au nom du dossier la date de destruction prévue entre crochets : `NOM Prénom [détruire 2031]`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Chaque dossier conserve la durée de son domaine d'origine (voir `97 - REFERENTIEL/Durees-de-conservation.md`). |
| **Recommandé** | Passage en revue annuel (janvier) : ce dont la date de destruction est dépassée est déplacé vers `99 - SUPPRESSION` pour validation, jamais supprimé directement depuis ici. Ne jamais proposer à la suppression un dossier concerné par un litige ou un contrôle en cours. |

## Conseils

- Quand on hésite entre deux durées, prendre la plus longue : le coût du stockage est nul, le coût d'une pièce manquante en contrôle ne l'est pas.
- **Ce dossier n'a pas les mêmes droits que les dossiers courants.** Le RGPD impose que l'archivage intermédiaire soit séparé de la base active, accessible aux seules personnes spécifiquement habilitées, et que les accès soient tracés. Concrètement : droits restreints au dirigeant et à la personne chargée du sujet, lecture seule par défaut, journalisation des accès et des suppressions.
- Les archives contiennent des données personnelles d'anciens salariés : les personnes concernées conservent leurs droits d'accès et d'effacement sur cette base comme sur les autres.
- À l'issue de la durée, la destruction doit être **sécurisée** : effacement irréversible ou destruction physique du support, et non simple mise à la corbeille. L'anonymisation est une alternative, à condition d'être irréversible — une pseudonymisation ne suffit pas.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
