---
schema: classement-documents/3.0
id: "03.7"
parent: "03"
niveau: sous-dossier
titre: "03.7 - Temps & absences"
usage: >-
  Le suivi du temps de travail et des absences : congés payés, RTT, arrêts de travail, congés
  spéciaux, télétravail, heures supplémentaires, forfaits jours.
classement: chronologique
sensibilite: rh
documents:
  - type: decompte-temps-travail
    libelle: Décompte du temps de travail
    description: "Relevé d'heures, heures supplémentaires et heures d'astreinte du mois."
    indices: ["relevé d'heures", heures supplémentaires, astreinte, décompte, temps de travail]
    champs: [periode, salarie, quantite]
    nommage: "{periode}_Releve-heures_{salarie}"
    conservation:
      legale: 1a
      recommandee: 5a
      declencheur: date-document
      base: Code du travail D3171-16
      sort-final: D
    registre: null
  - type: suivi-forfait-jours
    libelle: Suivi du forfait jours
    description: "Suivi obligatoire des jours travaillés d'un salarié au forfait et entretiens de charge de travail."
    indices: [forfait jours, suivi, charge de travail, entretien, jours travaillés]
    champs: [periode, salarie, quantite, objet]
    nommage: "{periode}_Forfait-jours_{salarie}"
    conservation:
      legale: 3a
      recommandee: 5a
      declencheur: date-document
      base: Code du travail L3121-65 et D3171-16
      sort-final: D
    registre: null
  - type: arret-travail-volet-employeur
    libelle: Arrêt de travail (volet employeur)
    description: "Volet employeur de l'avis d'arrêt, sans mention médicale. Le certificat médical détaillé ne se conserve pas."
    indices: [arrêt de travail, arrêt maladie, volet employeur, maternité, paternité, congé parental]
    champs: [date, salarie, date-debut, date-fin]
    nommage: "{date}_Arret-de-travail_{salarie}"
    conservation:
      legale: 5a
      recommandee: 5a
      declencheur: date-document
      base: Code de la sécurité sociale L244-3
      sort-final: D
    registre: null
  - type: attestation-salaire-ijss
    libelle: Attestation de salaire pour IJSS
    description: Attestation de salaire transmise à la CPAM et notification de subrogation.
    indices: [attestation de salaire, ijss, subrogation, cpam, indemnités journalières]
    champs: [date, salarie, organisme, montant, date-debut]
    nommage: "{date}_Attestation-de-salaire_{salarie}"
    conservation:
      legale: 5a
      recommandee: 5a
      declencheur: date-document
      base: Code de la sécurité sociale L244-3
      sort-final: D
    registre: null
va-ailleurs:
  - motif: "Certificats médicaux détaillés : ne pas conserver (données de santé) — seul l'avis d'arrêt volet employeur est utile"
    vers: null
  - motif: Notes de frais
    vers: "04.4"
---

# 03.7 - Temps & absences

> Chemin : `03 - RESSOURCES HUMAINES/03.7 - Temps & absences`

## À quoi sert ce dossier

Le suivi du temps de travail et des absences : congés payés, RTT, arrêts de travail, congés spéciaux, télétravail, heures supplémentaires, forfaits jours. Ces pièces alimentent la paie et servent de preuve en cas de litige sur les heures ou les congés.

## Documents à y ranger

- Demandes de congés validées, planning annuel des congés, compteurs (export annuel)
- Arrêts de travail (volet employeur — sans mention médicale), attestations de salaire pour IJSS, notifications de subrogation
- Congés maternité / paternité / parental, congés pour événements familiaux (justificatifs)
- Décomptes du temps de travail : relevés d'heures, heures supplémentaires, astreintes, suivi des forfaits jours (obligatoire), entretiens de charge de travail
- Accords / avenants de télétravail individuels (copie dans `03.2`)
- Tableaux de suivi des absences pour la paie (variables mensuelles)

## Ne pas ranger ici

- Certificats médicaux détaillés : ne pas conserver (données de santé) — seul l'avis d'arrêt volet employeur est utile
- Notes de frais → `04.4`

## Méthode de classement

**Par année, puis par type** : `AAAA/Conges`, `AAAA/Arrets de travail`, `AAAA/Temps de travail`. Fichiers `AAAA-MM-JJ_Type_NOM-Prenom.pdf`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Décompte des horaires et heures d'astreinte : 1 an. Forfaits jours : 3 ans. Arrêts de travail et attestations IJSS : 5 ans (avec la paie). |
| **Recommandé** | 5 ans pour tout, aligné sur la paie. |

Base : Code du travail art. D.3171-16 (1 an), L.3121-65 et D.3171-16 (3 ans forfaits) ; Code de la sécurité sociale art. L.244-3.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
