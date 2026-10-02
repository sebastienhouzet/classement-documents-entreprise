---
schema: classement-documents/3.0
id: "08.7"
parent: "08"
niveau: sous-dossier
titre: "08.7 - Non coté & private equity"
usage: >-
  Les investissements dans des actifs non cotés et peu liquides, sans prise de contrôle : fonds
  d'investissement (FCPR, FPCI), financement participatif en prêt ou en capital, obligations non
  cotées, prêts consentis à des tiers.
classement: par-operation
sensibilite: confidentielle
documents:
  - type: bulletin-souscription-fonds
    libelle: "Bulletin de souscription d'un fonds non coté"
    description: "Bulletin de souscription d'un FCPR ou d'un FPCI, règlement du fonds et note d'information. Les investissements donnant le contrôle ou une influence notable relèvent de 08.8."
    indices: [fcpr, fpci, "fonds d'investissement", bulletin de souscription, reglement du fonds, private equity]
    champs: [date-signature, gestionnaire, designation, montant, quantite]
    nommage: "{date}_Bulletin-souscription-fonds_{gestionnaire}_{designation}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: cession-ligne
      base: Code monétaire et financier art. L.214-27
      sort-final: C
    registre: { fichier: Registre-des-placements.csv, cle: designation }
  - type: appel-de-capitaux-fonds
    libelle: Appel de capitaux
    description: "Appel de capitaux successif d'un fonds fermé, avec son échéance de versement. Conserver l'intégralité des appels — sans eux, le prix de revient est introuvable à la sortie."
    indices: [appel de capitaux, appel de fonds, versement, fonds ferme, prix de revient]
    champs: [date, gestionnaire, designation, montant, echeance]
    nommage: "{date}_Appel-de-capitaux_{gestionnaire}_{designation}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cession-ligne
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: { fichier: Registre-des-placements.csv, cle: designation }
  - type: contrat-pret-consenti-tiers
    libelle: Contrat de prêt consenti ou obligation non cotée
    description: "Contrat de prêt consenti à un tiers, contrat de financement participatif en prêt ou contrat d'émission d'obligations non cotées, avec son échéancier et les garanties reçues."
    indices: [pret consenti, crowdlending, financement participatif, obligation non cotee, echeancier, "contrat d'emission"]
    champs: [date-signature, tiers, designation, montant, taux, echeance]
    nommage: "{date}_Contrat-de-pret-consenti_{tiers}_{designation}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code de commerce art. L.110-4
      sort-final: C
    registre: { fichier: Registre-des-placements.csv, cle: designation }
  - type: reporting-valeur-liquidative
    libelle: Reporting et valeur liquidative
    description: "Reportings périodiques, valeur liquidative annuelle, avis de distribution, relevés de plateforme et avis de défaut. Une dépréciation à la clôture doit s'appuyer sur un élément externe rangé avec le calcul."
    indices: [valeur liquidative, reporting periodique, avis de distribution, releve de plateforme, avis de defaut]
    champs: [date, gestionnaire, designation, periode, cours, montant]
    nommage: "{date}_Reporting-valeur-liquidative_{gestionnaire}_{periode}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cession-ligne
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: null
  - type: sortie-ligne-non-cotee
    libelle: "Sortie d'une ligne non cotée"
    description: "Cession de parts, avis de liquidation du fonds, remboursement d'obligations ou quittance de remboursement d'un prêt, avec le décompte final et le calcul de la plus ou moins-value."
    indices: [cession de parts, liquidation du fonds, avis de remboursement, decompte final, recouvrement]
    champs: [date, gestionnaire, designation, montant, nature]
    nommage: "{date}_Sortie-ligne-non-cotee_{gestionnaire}_{designation}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cession-ligne
      base: Code de commerce art. L.123-22
      sort-final: C
    registre: { fichier: Registre-des-placements.csv, cle: designation }
va-ailleurs:
  - motif: Titres donnant le contrôle ou une influence notable
    vers: "08.8"
  - motif: "Prêt ou emprunt reçu par l'entreprise"
    vers: "05.2"
  - motif: Subventions reçues
    vers: "05.3"
---

# 08.7 - Non coté & private equity

> Chemin : `08 - PLACEMENTS & PARTICIPATIONS/08.7 - Non coté & private equity`

## À quoi sert ce dossier

Les investissements dans des actifs non cotés et peu liquides, sans prise de contrôle : fonds d'investissement (FCPR, FPCI), financement participatif en prêt ou en capital, obligations non cotées, prêts consentis à des tiers. Dès que l'investissement vise à contrôler ou à influencer durablement une société, il relève de `08.8`.

## Documents à y ranger

- **Fonds** : bulletin de souscription, règlement du fonds, note d'information, appels de capitaux successifs, avis de distribution, reportings périodiques, valeur liquidative annuelle, avis de liquidation
- **Financement participatif** : conditions de la plateforme, contrats de prêt ou bulletins de souscription, échéanciers, relevés de la plateforme, avis de défaut et procédures de recouvrement
- **Obligations non cotées** : contrat d'émission, bulletin de souscription, échéancier de coupons, avis de remboursement
- **Prêts consentis** : contrat de prêt, échéancier, garanties reçues (copie — original dans `05.6`), quittances, preuve de remboursement
- Valorisation à la clôture et provisions pour dépréciation, avec le justificatif de la valeur retenue
- Attestations de détention et justificatifs des régimes fiscaux spécifiques éventuels
- Sortie : cession de parts, liquidation du fonds, décompte final, calcul de la plus ou moins-value

## Ne pas ranger ici

- Titres donnant le contrôle ou une influence notable → `08.8`
- Prêt ou emprunt **reçu** par l'entreprise → `05.2`
- Subventions reçues → `05.3`

## Méthode de classement

**Un sous-dossier par ligne** : `AAAA - Gestionnaire - Nom du fonds` ou `AAAA - Emprunteur - Objet`. À l'intérieur : `Souscription`, `Appels et distributions/AAAA`, `Reporting/AAAA`, `Valorisation/AAAA`, `Sortie`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Pièces comptables : 10 ans. Contrats : 5 ans après la fin. Documents fiscaux : 10 ans. |
| **Recommandé** | Durée de détention + 10 ans. Les fonds fermés vivent souvent dix ans : conserver l'intégralité des appels de capitaux, sans lesquels le prix de revient est introuvable au moment de la sortie. |

Base : Code de commerce art. L.110-4 et L.123-22 ; Code monétaire et financier art. L.214-27 et s. (FCPR) ; LPF art. L.102 B.

## Conseils

- Sur le non coté, une dépréciation à la clôture doit s'appuyer sur un élément externe (dernière valeur liquidative, dernier tour de table, défaut constaté) : ranger cet élément avec le calcul, faute de quoi la provision est contestable.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
