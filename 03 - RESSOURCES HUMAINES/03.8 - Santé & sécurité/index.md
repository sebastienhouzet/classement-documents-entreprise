---
schema: classement-documents/3.0
id: "03.8"
parent: "03"
niveau: sous-dossier
titre: "03.8 - Santé & sécurité"
usage: >-
  La prévention des risques professionnels et le suivi médical : visites médicales, accidents du
  travail, plans de prévention, formations sécurité.
classement: par-tiers
sensibilite: rh
documents:
  - type: declaration-accident-travail
    libelle: "Déclaration d'accident du travail"
    description: "DAT adressée à la CPAM dans les 48 heures, avec les courriers et la décision de prise en charge."
    indices: [accident du travail, dat, maladie professionnelle, cpam, prise en charge, taux at/mp]
    champs: [date, salarie, organisme, numero-dossier, lieu]
    nommage: "{date}_DAT_{salarie}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: date-document
      base: Code de la sécurité sociale L441-2
      sort-final: C
    registre: null
  - type: avis-medical-aptitude
    libelle: "Avis d'aptitude ou d'inaptitude"
    description: "Attestation de suivi médical, avis d'aptitude ou d'inaptitude et aménagements de poste préconisés. Accès restreint."
    indices: [visite médicale, "visite d'information et de prévention", "avis d'aptitude", inaptitude, aménagement de poste]
    champs: [date, salarie, organisme, nature, intitule-poste]
    nommage: "{date}_Avis-medical_{salarie}"
    conservation:
      legale: 5a
      recommandee: 5a
      declencheur: depart-salarie
      base: Code du travail R4624-1
      sort-final: D
    registre: null
  - type: fiche-exposition-risques
    libelle: "Document d'exposition aux risques"
    description: "Pièce documentant l'exposition d'un salarié à un risque professionnel, conservée aussi longtemps que le DUERP."
    indices: [exposition, risque professionnel, fiche de données de sécurité, plan de prévention, protocole de sécurité]
    champs: [date, salarie, nature, intitule-poste, lieu]
    nommage: "{date}_Fiche-exposition_{salarie}"
    conservation:
      legale: 40a
      recommandee: 40a
      declencheur: date-document
      base: Code du travail L4121-3-1
      sort-final: C
    registre: null
  - type: registre-accidents-benins
    libelle: Registre des accidents bénins
    description: Registre des accidents sans arrêt de travail et enquêtes internes attachées.
    indices: [registre des accidents bénins, accident bénin, enquête interne, signalement, danger grave]
    champs: [date, salarie, lieu, nature]
    nommage: "{date}_Registre-accidents-benins"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: date-document
      base: Code de la sécurité sociale L441-2
      sort-final: D
    registre: null
va-ailleurs:
  - motif: DUERP
    vers: "03.1"
  - motif: "Contrats d'assurance prévoyance"
    vers: "06.4"
  - motif: Arrêts de travail
    vers: "03.7"
---

# 03.8 - Santé & sécurité

> Chemin : `03 - RESSOURCES HUMAINES/03.8 - Santé & sécurité`

## À quoi sert ce dossier

La prévention des risques professionnels et le suivi médical : visites médicales, accidents du travail, plans de prévention, formations sécurité. Certaines pièces se conservent très longtemps (exposition à des risques : 40 ans, comme le DUERP). Données de santé : accès restreint.

## Documents à y ranger

- Attestations de suivi médical (visite d'information et de prévention, visites périodiques, de reprise), avis d'aptitude / inaptitude, aménagements de poste préconisés
- Accidents du travail et maladies professionnelles : déclarations (DAT), registre des accidents bénins, enquêtes, courriers CPAM, décisions de prise en charge, taux AT/MP notifiés
- Plans de prévention avec entreprises extérieures, protocoles de sécurité, fiches de données de sécurité (produits)
- Vérifications et formations sécurité : SST, incendie, exercices d'évacuation, habilitations
- Fiche d'entreprise du service de prévention et de santé au travail
- Signalements (harcèlement, danger grave et imminent), enquêtes internes

## Ne pas ranger ici

- DUERP → `03.1`
- Contrats d'assurance prévoyance → `06.4`
- Arrêts de travail → `03.7`

## Méthode de classement

Trois sous-dossiers : `Suivi medical` (un sous-dossier par salarié `NOM Prénom`), `Accidents du travail/AAAA` (un sous-dossier par accident), `Prevention` (par thème). Le DUERP reste dans `03.1`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Déclarations d'accident du travail : 5 ans. Avis médicaux : durée du contrat + 5 ans. Documents d'exposition aux risques : 40 ans (aligné DUERP). |
| **Recommandé** | 10 ans pour les accidents du travail ; 40 ans pour tout ce qui documente une exposition à un risque. |

Base : Code du travail art. R.4624-1 et s., L.4121-3-1 (40 ans) ; Code de la sécurité sociale art. L.441-2 (DAT 48 h).

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
