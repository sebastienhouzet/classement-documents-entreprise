---
schema: classement-documents/3.0
id: "07.7"
parent: "07"
niveau: sous-dossier
titre: 07.7 - Marchés publics
usage: >-
  Le dossier de candidature de l'entreprise aux marchés publics, maintenu en permanence à jour,
  et le suivi des consultations auxquelles elle répond.
classement: par-operation
sensibilite: normale
documents:
  - type: dossier-candidature-dc1-dc2
    libelle: "Dossier de candidature DC1, DC2 ou DUME"
    description: "Lettre de candidature DC1, déclaration du candidat DC2 ou DUME, déclaration sur l'honneur d'absence d'interdiction de soumissionner et pièces de moyens. À réviser à chaque clôture."
    indices: [dc1, dc2, dume, lettre de candidature, declaration du candidat, interdiction de soumissionner]
    champs: [date, acheteur-public, numero-dossier, exercice, objet]
    nommage: "{date}_Dossier-de-candidature_{acheteur-public}_{objet}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-dossier
      base: Code de la commande publique
      sort-final: D
    registre: null
  - type: memoire-technique
    libelle: Mémoire technique
    description: "Mémoire technique dans sa version de référence et ses déclinaisons par type de marché, versionné par date."
    indices: [memoire technique, version de reference, declinaison par marche, offre technique]
    champs: [date, reference, objet, version]
    nommage: "{date}_Memoire-technique_{reference}_{objet}"
    conservation:
      legale: aucune
      recommandee: 10a
      declencheur: cloture-dossier
      base: Code de la commande publique
      sort-final: T
    registre: null
  - type: offre-marche-public
    libelle: Offre déposée et pièces de la consultation
    description: "Offre déposée avec l'acte d'engagement ATTRI1, le DC4 en cas de sous-traitance, et les pièces de la consultation — avis de publicité, règlement de consultation, CCTP, CCAP."
    indices: [attri1, "acte d'engagement", dc4, reglement de consultation, cctp, ccap, avis de publicite, offre deposee]
    champs: [date, acheteur-public, numero-dossier, montant-ht, objet]
    nommage: "{date}_Offre-marche-public_{acheteur-public}_{objet}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-dossier
      base: Code de la commande publique
      sort-final: D
    registre: null
  - type: certificat-capacite-reference
    libelle: Certificat de capacité et référence
    description: "Certificat de capacité signé par le maître d'ouvrage et référence de moins de 3 ans (5 ans pour les travaux). À conserver sans limite — ces pièces servent à toutes les candidatures suivantes."
    indices: [certificat de capacite, reference de moins de 3 ans, "maitre d'ouvrage", attestation de bonne execution]
    champs: [date, acheteur-public, designation, montant-ht, date-fin]
    nommage: "{date}_Certificat-de-capacite_{acheteur-public}_{designation}"
    conservation:
      legale: 10a
      recommandee: permanent
      declencheur: cloture-dossier
      base: Code de la commande publique
      sort-final: C
    registre: null
  - type: decision-attribution-rejet
    libelle: "Courrier d'attribution ou de rejet"
    description: "Courrier d'attribution ou de rejet de l'offre avec ses motifs, et pièces de suivi d'exécution du marché — ordres de service, décomptes, pénalités."
    indices: [attribution, "rejet d'offre", motifs du rejet, ordre de service, decompte, penalite]
    champs: [date, acheteur-public, numero-dossier, motif, montant-ht]
    nommage: "{date}_Decision-attribution-rejet_{acheteur-public}_{numero-dossier}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-dossier
      base: Code de la commande publique
      sort-final: D
    registre: null
va-ailleurs:
  - motif: Contrat et exécution avec un client privé
    vers: "02.1"
  - motif: Originaux des attestations
    vers: null
---

# 07.7 - Marchés publics

> Chemin : `07 - ADMINISTRATIF & ORGANISMES/07.7 - Marchés publics`

## À quoi sert ce dossier

Le dossier de candidature de l'entreprise aux marchés publics, maintenu en permanence à jour, et le suivi des consultations auxquelles elle répond. L'enjeu est la fraîcheur : les attestations ont une validité courte et une candidature incomplète est écartée sans examen, quelle que soit la qualité de l'offre.

## Documents à y ranger

- **Dossier permanent** : DC1 (lettre de candidature), DC2 (déclaration du candidat : chiffres d'affaires des trois derniers exercices, références, moyens humains et matériels), ou DUME
- Attestations à jour : attestation de vigilance URSSAF de moins de 6 mois, attestation de régularité fiscale, attestations d'assurance RC professionnelle et décennale le cas échéant, extrait Kbis
- Déclaration sur l'honneur d'absence d'interdiction de soumissionner
- **Mémoire technique** : version de référence et déclinaisons par type de marché
- Références de moins de 3 ans (5 ans pour les travaux) et certificats de capacité signés par les maîtres d'ouvrage
- Moyens : effectifs, qualifications, matériel, certifications
- **Par consultation** : avis de publicité, règlement de consultation, CCTP et CCAP, offre déposée, ATTRI1 (acte d'engagement), DC4 en cas de sous-traitance, courrier d'attribution ou de rejet avec ses motifs
- Suivi d'exécution : ordres de service, procès-verbaux, décomptes, pénalités

## Ne pas ranger ici

- Contrat et exécution avec un client privé → `02.1`
- Originaux des attestations → leur domaine d'origine ; les copies en cours de validité → `97/Kit administratif`

## Méthode de classement

Un sous-dossier `Dossier permanent` à la racine, tenu à jour et daté, puis **un sous-dossier par consultation** : `AAAA-MM - Acheteur - Objet`, avec `Consultation`, `Offre`, `Resultat`, `Execution`. Un `Suivi-des-consultations.csv` y gagne à lister les dates limites de remise, qui sont la vraie contrainte.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Pièces du marché exécuté : 10 ans (prescription et contrôle). Attestations : leur durée de validité propre, 6 mois pour l'attestation de vigilance. |
| **Recommandé** | 10 ans après la fin d'exécution. Conserver les certificats de capacité sans limite : ils servent de références pour toutes les candidatures suivantes. |

Base : Code de la commande publique ; Code du travail art. L8222-1 (obligation de vigilance).

## Conseils

- Les attestations fiscales et sociales sont exigées **au stade de l'attribution**, pas de la candidature : ne pas retarder un dépôt pour les attendre.
- La dématérialisation est intégrale au-dessus de 40 000 € HT. Les seuils de publicité sont de 60 000 € HT pour les fournitures et services, 100 000 € HT pour les travaux.
- Réviser le dossier permanent au moins une fois par an, et à chaque clôture : le DC2 demande les chiffres d'affaires des trois derniers exercices.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
