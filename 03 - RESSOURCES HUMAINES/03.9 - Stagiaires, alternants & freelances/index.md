---
schema: classement-documents/3.0
id: "03.9"
parent: "03"
niveau: sous-dossier
titre: "03.9 - Stagiaires, alternants & freelances"
usage: >-
  Les personnes qui travaillent dans l'entreprise sans être salariées « classiques » :
  stagiaires (convention tripartite), alternants (apprentissage, professionnalisation — qui sont
  des salariés mais avec un dossier spécifique), et freelances / indépendants intégrés à
  l'équipe sur une mission longue.
classement: par-tiers
sensibilite: rh
documents:
  - type: convention-de-stage
    libelle: Convention de stage
    description: "Convention tripartite signée par l'entreprise, le stagiaire et l'établissement, et l'attestation de stage."
    indices: [convention de stage, stagiaire, gratification, attestation de stage, établissement]
    champs: [date, salarie, organisme-formation, date-debut, date-fin, montant]
    nommage: "{date}_Convention-de-stage_{salarie}"
    conservation:
      legale: 5a
      recommandee: 5a
      declencheur: fin-contrat
      base: "Code de l'éducation L124-1"
      sort-final: D
    registre: null
  - type: contrat-apprentissage
    libelle: "Contrat d'apprentissage ou de professionnalisation"
    description: "Cerfa du contrat en alternance, son enregistrement OPCO et la convention avec le CFA."
    indices: ["contrat d'apprentissage", apprenti, professionnalisation, cfa, "aide à l'embauche", asp]
    champs: [date, salarie, organisme-formation, date-debut, date-fin, montant]
    nommage: "{date}_Contrat-apprentissage_{salarie}"
    conservation:
      legale: 5a
      recommandee: 5a
      declencheur: depart-salarie
      base: Code du travail L6221-1
      sort-final: D
    registre: null
  - type: contrat-mission-freelance
    libelle: "Contrat de mission d'un freelance"
    description: "Contrat de prestation ou de mission d'un indépendant intégré à l'équipe, ses avenants et la fin de mission."
    indices: [freelance, indépendant, contrat de mission, portage salarial, requalification]
    champs: [date, fournisseur, objet, date-debut, date-fin, montant-ht]
    nommage: "{date}_Contrat-de-mission_{fournisseur}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code du travail L8221-6
      sort-final: D
    registre: null
  - type: attestation-vigilance-freelance
    libelle: "Pièces de vigilance d'un freelance"
    description: "Attestation de vigilance URSSAF du prestataire tous les six mois, extrait SIRENE ou Kbis, attestation RC Pro."
    indices: [attestation de vigilance, pièces de vigilance, sirene, kbis, rc pro, prestataire]
    champs: [date, fournisseur, numero, date-fin]
    nommage: "{date}_Attestation-vigilance_{fournisseur}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: date-document
      base: Code du travail L8222-1
      sort-final: D
    registre: null
va-ailleurs:
  - motif: Factures des freelances
    vers: "04.3"
  - motif: "Prestataires en société (agences, cabinets)"
    vers: "02.2"
---

# 03.9 - Stagiaires, alternants & freelances

> Chemin : `03 - RESSOURCES HUMAINES/03.9 - Stagiaires, alternants & freelances`

## À quoi sert ce dossier

Les personnes qui travaillent dans l'entreprise sans être salariées « classiques » : stagiaires (convention tripartite), alternants (apprentissage, professionnalisation — qui sont des salariés mais avec un dossier spécifique), et freelances / indépendants intégrés à l'équipe sur une mission longue. Les agences et sociétés prestataires restent dans `02.2`.

## Documents à y ranger

- **Stagiaires** : convention de stage signée par les trois parties, avenants, attestation de stage, gratification (bulletins → `03.3`), inscription au registre du personnel (`03.1`)
- **Alternants** : contrat d'apprentissage ou de professionnalisation (Cerfa), enregistrement OPCO, convention de formation avec le CFA, aides à l'embauche (ASP), calendrier d'alternance, évaluations, fin de contrat
- **Freelances / indépendants** : contrat de prestation ou de mission, avenants, cession de droits d'auteur (copie dans `01.7`), pièces de vigilance (attestation URSSAF tous les 6 mois, extrait SIRENE / Kbis, attestation RC Pro), NDA, remise de matériel/accès, fin de mission
- Portage salarial : convention de portage, contrat commercial

## Ne pas ranger ici

- Factures des freelances → `04.3`
- Prestataires en société (agences, cabinets) → `02.2`

## Méthode de classement

Trois sous-dossiers `Stagiaires`, `Alternants`, `Freelances`, puis **un sous-dossier par personne** `NOM Prénom`, organisé comme un dossier salarié (`01 Debut`, `02 Mission`, `03 Fin`).

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Stagiaires : 5 ans après la fin (registre du personnel). Alternants : comme un salarié, 5 ans après le départ. Freelances : 5 ans après la fin du contrat (10 ans recommandé) ; attestations de vigilance 5 ans. |
| **Recommandé** | 5 ans après la fin pour stagiaires et alternants ; 10 ans pour les freelances (risque de requalification : garder ce qui prouve l'indépendance — devis, factures, absence de lien de subordination). |

Base : Code de l'éducation art. L.124-1 et s. (stages) ; Code du travail art. L.6221-1 et s. (apprentissage), L.8221-6 (présomption de non-salariat), L.8222-1 (vigilance).

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
