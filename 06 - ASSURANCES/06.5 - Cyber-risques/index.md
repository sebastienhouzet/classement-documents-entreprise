---
schema: classement-documents/3.0
id: "06.5"
parent: "06"
niveau: sous-dossier
titre: 06.5 - Cyber-risques
usage: >-
  L'assurance contre les incidents informatiques : intrusion, rançongiciel, fuite de données,
  interruption d'activité, frais de notification RGPD.
classement: par-contrat
sensibilite: confidentielle
documents:
  - type: contrat-assurance-cyber
    libelle: "Contrat d'assurance cyber-risques"
    description: "Contrat cyber — conditions, plafonds, exclusions et avenants — intrusion, rançongiciel, fuite de données, interruption d'activité, frais de notification RGPD."
    indices: [assurance cyber, cyber-risques, rancongiciel, fuite de donnees, "interruption d'activite", frais de notification]
    champs: [date-effet, assureur, numero-contrat, montant, objet, plafond-garantie, franchise]
    nommage: "{date}_Contrat-assurance-cyber_{assureur}_{numero-contrat}"
    conservation:
      legale: 2a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code des assurances art. L.124-5
      sort-final: C
    registre: { fichier: Registre-des-assurances.csv, cle: numero-contrat }
  - type: questionnaire-securite-cyber
    libelle: Questionnaire de sécurité du contrat cyber
    description: "Questionnaire de souscription détaillé décrivant les mesures de sécurité déclarées (sauvegardes, MFA, mises à jour) et ses mises à jour annuelles — l'assureur les vérifie en cas de sinistre."
    indices: [questionnaire de securite, mesures declarees, sauvegardes, mfa, mises a jour, declaration de risque]
    champs: [date, assureur, numero-contrat, version, objet]
    nommage: "{date}_Questionnaire-securite-cyber_{assureur}_{version}"
    conservation:
      legale: 2a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code des assurances art. L.114-1
      sort-final: C
    registre: null
  - type: procedure-declaration-sinistre-cyber
    libelle: Procédure de déclaration et assistance 24/7
    description: "Procédure de déclaration de sinistre cyber et numéro d'assistance 24/7, à conserver aussi sous forme imprimée."
    indices: [procedure de declaration, assistance 24/7, "numero d'urgence", cellule de crise, version imprimee]
    champs: [date, assureur, numero-contrat, reference]
    nommage: "{date}_Procedure-declaration-cyber_{assureur}"
    conservation:
      legale: 2a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code des assurances art. L.124-5
      sort-final: D
    registre: null
  - type: quittance-assurance-cyber
    libelle: Quittance de prime cyber
    description: "Quittance ou appel de prime du contrat cyber, attestations et courriers de l'assureur."
    indices: [quittance cyber, appel de prime, attestation cyber, "avis d'echeance", "courrier de l'assureur"]
    champs: [periode, assureur, numero-contrat, montant]
    nommage: "{periode}_Quittance-assurance-cyber_{assureur}"
    conservation:
      legale: 2a
      recommandee: 10a
      declencheur: date-document
      base: Code des assurances art. L.114-1
      sort-final: D
    registre: null
va-ailleurs:
  - motif: Politique de sécurité et charte informatique
    vers: "01.8"
  - motif: Incident survenu
    vers: "06.7"
---

# 06.5 - Cyber-risques

> Chemin : `06 - ASSURANCES/06.5 - Cyber-risques`

## À quoi sert ce dossier

L'assurance contre les incidents informatiques : intrusion, rançongiciel, fuite de données, interruption d'activité, frais de notification RGPD. Le questionnaire de souscription y est déterminant : il décrit les mesures de sécurité déclarées, et l'assureur les vérifiera en cas de sinistre.

## Documents à y ranger

- Contrat, conditions, plafonds et exclusions, avenants
- Questionnaire de souscription détaillé (mesures de sécurité déclarées : sauvegardes, MFA, mises à jour…) et ses mises à jour annuelles
- Procédure de déclaration de sinistre et numéro d'assistance 24/7 (à imprimer aussi : en cas d'attaque, les fichiers ne sont plus accessibles)
- Attestations, quittances, courriers

## Ne pas ranger ici

- Politique de sécurité et charte informatique → `01.8`
- Incident survenu → `06.7` (et registre des violations RGPD dans `01.8`)

## Méthode de classement

**Un sous-dossier par contrat** `Assureur - N° contrat`, puis `Contrat`, `Attestations/AAAA`, `Quittances/AAAA`, `Courriers`. En cas de changement d'assureur, garder l'ancien contrat dans son propre sous-dossier (ne pas fusionner).

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | 2 ans après la fin du contrat. |
| **Recommandé** | 10 ans après la fin du contrat. |

Base : Code des assurances art. L.114-1, L.124-5.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
