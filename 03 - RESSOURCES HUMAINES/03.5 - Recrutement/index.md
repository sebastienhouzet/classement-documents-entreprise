---
schema: classement-documents/3.0
id: "03.5"
parent: "03"
niveau: sous-dossier
titre: 03.5 - Recrutement
usage: >-
  Les campagnes de recrutement : offre, candidatures, entretiens, décision. Sa règle a changé,
  et dans le sens de la conservation : le référentiel CNIL d'avril 2026 impose de garder les
  candidatures non retenues 5 ans à compter du pourvoi du poste, et non plus 2 ans, parce que
  c'est le délai pendant lequel une action en discrimination…
classement: par-operation
sensibilite: rh
documents:
  - type: candidature-non-retenue
    libelle: Candidature non retenue
    description: "CV et lettre d'un candidat écarté sur un poste ouvert. Conservée pour la durée de l'action en discrimination."
    indices: [cv, candidature, lettre de motivation, refus de candidature, discrimination]
    champs: [date, tiers, intitule-poste, motif, candidat]
    nommage: "{date}_Candidature_{tiers}_{intitule-poste}"
    conservation:
      legale: 5a
      recommandee: 5a
      declencheur: pourvoi-poste
      base: Code du travail L1134-5
      sort-final: D
    registre: null
  - type: cv-theque-spontane
    libelle: Candidature spontanée (CV-thèque)
    description: "Candidature reçue hors d'un poste précis, rangée dans la CV-thèque et soumise à une durée propre."
    indices: [cv, candidature spontanée, cv-thèque, dernier contact, vivier]
    champs: [date, tiers, objet, candidat]
    nommage: "{date}_CV_{tiers}"
    conservation:
      legale: 2a
      recommandee: 2a
      declencheur: dernier-contact
      base: RGPD art. 5.1.e
      sort-final: D
    registre: null
  - type: annonce-emploi
    libelle: "Annonce d'emploi publiée"
    description: "Offre d'emploi telle que publiée, avec sa date et ses supports de diffusion."
    indices: ["annonce d'emploi", "offre d'emploi", publication, poste ouvert, diffusion]
    champs: [date, intitule-poste, objet, lieu]
    nommage: "{date}_Annonce_{intitule-poste}"
    conservation:
      legale: 5a
      recommandee: 5a
      declencheur: pourvoi-poste
      base: Code du travail L1134-5
      sort-final: D
    registre: null
  - type: grille-selection-recrutement
    libelle: Grille de sélection et dossier de décision
    description: "Critères retenus, grille d'entretien, grille comparative et motivation du choix. C'est la défense de l'employeur en cas de contestation."
    indices: ["grille d'entretien", entretien de recrutement, test de recrutement, critères, décision]
    champs: [date, intitule-poste, objet, effectif]
    nommage: "{date}_Grille-de-selection_{intitule-poste}"
    conservation:
      legale: 5a
      recommandee: 5a
      declencheur: pourvoi-poste
      base: Code du travail L1134-5
      sort-final: D
    registre: null
va-ailleurs:
  - motif: Dossier du candidat embauché
    vers: null
---

# 03.5 - Recrutement

> Chemin : `03 - RESSOURCES HUMAINES/03.5 - Recrutement`

## À quoi sert ce dossier

Les campagnes de recrutement : offre, candidatures, entretiens, décision. Sa règle a changé, et dans le sens de la conservation : le référentiel CNIL d'avril 2026 impose de garder les candidatures non retenues **5 ans à compter du pourvoi du poste**, et non plus 2 ans, parce que c'est le délai pendant lequel une action en discrimination reste possible. Ces pièces sont la défense de l'employeur, pas seulement une contrainte. Le candidat recruté, lui, rejoint `03.2` : sa candidature n'a plus à être conservée ici.

## Documents à y ranger

- Fiche de poste et annonce publiée (avec date et supports)
- Candidatures reçues (CV, lettres) — non retenues
- Grilles d'entretien, comptes rendus, tests
- Promesses d'embauche, refus motivés
- Contrats avec cabinets de recrutement ou plateformes (factures → `04.3`)
- Aides à l'embauche demandées (dossiers, décisions)
- Dossier de la décision : critères retenus, grille comparative, motivation du choix — c'est ce qui permet de justifier un recrutement s'il est contesté

## Ne pas ranger ici

- Dossier du candidat embauché → `03.2/NOM Prénom/01 Embauche`

## Méthode de classement

**Un sous-dossier par poste ouvert** : `AAAA-MM - Intitulé du poste`. À l'intérieur : `Annonce`, `Candidatures`, `Entretiens`, `Decision`. Une fois le poste pourvu, déplacer les pièces du candidat retenu vers `03.2` et **noter la date du pourvoi dans le nom du dossier** — c'est elle qui fait courir les 5 ans : `2026-03 - Developpeur [pourvu 2026-05-12]`. Un sous-dossier `CV-theque` à la racine pour les candidatures spontanées, qui obéissent à une autre durée.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Candidatures non retenues : **5 ans à compter de la date à laquelle le poste a été pourvu** (prescription de l'action en discrimination). CV-thèque : 2 ans à compter du dernier contact. |
| **Recommandé** | 5 ans, puis purge. Ne pas détruire plus tôt : en cas d'action en discrimination, ce sont ces pièces qui permettent de démontrer que le choix reposait sur des critères objectifs. |

Base : Code du travail art. L1134-5 (prescription 5 ans) ; RGPD art. 5.1.e ; référentiel CNIL des durées de conservation en gestion des ressources humaines du 2 avril 2026, qui qualifie cette durée d'obligation et non de recommandation.

## Conseils

- La page générique de la CNIL sur les durées affiche encore « 2 ans maximum » : c'est une incohérence avec son propre référentiel d'avril 2026. La durée de 5 ans est celle qui protège l'employeur.
- Les 2 ans ne valent que pour la CV-thèque — les candidatures conservées hors d'un poste précis — et courent à compter du **dernier contact** avec la personne, pas de la réception du CV.
- Conserver la grille de sélection autant que les candidatures : sans critères écrits, la défense repose sur la mémoire.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
