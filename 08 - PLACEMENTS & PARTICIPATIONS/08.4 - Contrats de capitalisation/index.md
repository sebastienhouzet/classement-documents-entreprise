---
schema: classement-documents/3.0
id: "08.4"
parent: "08"
niveau: sous-dossier
titre: 08.4 - Contrats de capitalisation
usage: >-
  Les contrats de capitalisation souscrits par la personne morale. Une société ne peut pas
  souscrire d'assurance-vie, réservée aux personnes physiques : le contrat de capitalisation en
  est l'équivalent pour une entreprise.
classement: par-contrat
sensibilite: confidentielle
documents:
  - type: bulletin-souscription-capitalisation
    libelle: "Bulletin de souscription d'un contrat de capitalisation"
    description: "Bulletin de souscription, conditions générales et particulières, note d'information et attestation d'adhésion. Porte le taux de référence retenu à la souscription, indispensable au calcul du rachat."
    indices: [contrat de capitalisation, bulletin de souscription, "attestation d'adhesion", taux de reference, fonds en euros, unite de compte]
    champs: [date-signature, assureur, numero-contrat, designation, support, montant, taux]
    nommage: "{date}_Bulletin-souscription-capitalisation_{assureur}_{designation}"
    conservation:
      legale: 2a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code des assurances art. L.114-1
      sort-final: C
    registre: { fichier: Registre-des-placements.csv, cle: designation }
  - type: avenant-versement-arbitrage-capitalisation
    libelle: "Avenant, versement ou arbitrage"
    description: "Avenant au contrat de capitalisation — versement complémentaire, arbitrage entre supports, changement d'option."
    indices: [versement complementaire, arbitrage, "changement d'option", avenant au contrat, unite de compte]
    champs: [date, assureur, numero-contrat, designation, support, montant]
    nommage: "{date}_Avenant-capitalisation_{assureur}_{designation}"
    conservation:
      legale: 2a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code des assurances art. L.114-1
      sort-final: D
    registre: { fichier: Registre-des-placements.csv, cle: designation }
  - type: releve-situation-capitalisation
    libelle: Relevé de situation et de valorisation
    description: "Relevés de situation périodiques, relevé de valorisation au 31/12 et relevé annuel de frais du contrat de capitalisation."
    indices: [releve de situation, releve de valorisation, valorisation au 31/12, releve annuel de frais]
    champs: [date, assureur, numero-contrat, exercice, montant]
    nommage: "{date}_Releve-situation-capitalisation_{assureur}_{exercice}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: null
  - type: calcul-imposition-annuelle-capitalisation
    libelle: "Calcul de l'imposition annuelle forfaitaire"
    description: "Éléments de calcul de l'imposition annuelle forfaitaire propre aux personnes morales à l'IS — taux de référence retenu à la souscription, base, montant déclaré. Sert au calcul de la régularisation lors du rachat."
    indices: [imposition annuelle forfaitaire, "personne morale a l'is", taux de reference, base taxable, regularisation au rachat]
    champs: [date, exercice, numero-contrat, taux, montant]
    nommage: "{date}_Calcul-imposition-capitalisation_{exercice}_{numero-contrat}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: CGI art. 238 septies E
      sort-final: C
    registre: null
  - type: rachat-contrat-capitalisation
    libelle: Rachat partiel ou total
    description: "Demande de rachat partiel ou total, décompte, avis de règlement et calcul de la plus-value nette de l'imposition déjà acquittée."
    indices: [rachat partiel, rachat total, decompte de rachat, avis de reglement, plus-value nette]
    champs: [date, assureur, numero-contrat, designation, montant, motif]
    nommage: "{date}_Rachat-capitalisation_{assureur}_{designation}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: { fichier: Registre-des-placements.csv, cle: designation }
va-ailleurs:
  - motif: "Assurances de l'entreprise (RC Pro, multirisque, cyber)"
    vers: "06"
  - motif: Prévoyance et retraite des dirigeants et salariés
    vers: "06.4"
---

# 08.4 - Contrats de capitalisation

> Chemin : `08 - PLACEMENTS & PARTICIPATIONS/08.4 - Contrats de capitalisation`

## À quoi sert ce dossier

Les contrats de capitalisation souscrits par la personne morale. Une société ne peut pas souscrire d'assurance-vie, réservée aux personnes physiques : le contrat de capitalisation en est l'équivalent pour une entreprise. Il obéit à une fiscalité annuelle propre aux sociétés à l'IS, et le dossier doit permettre de reconstituer la base taxable chaque année jusqu'au rachat.

## Documents à y ranger

- Bulletin de souscription, conditions générales et particulières, note d'information
- Attestation d'adhésion, numéro de contrat, liste des supports (fonds en euros, unités de compte)
- DIC / documents d'informations clés des unités de compte souscrites
- Avenants : versements complémentaires, arbitrages, changements d'option
- Relevés de situation périodiques et **relevé de valorisation au 31/12**
- Éléments de calcul de l'imposition annuelle forfaitaire propre aux personnes morales à l'IS : taux de référence retenu à la souscription, base, montant déclaré chaque année
- Rachats partiels et rachat total : demande, décompte, avis de règlement, calcul de la plus-value nette de l'imposition déjà acquittée
- Nantissement du contrat, le cas échéant (copie — original dans `05.6`)
- Relevé annuel de frais

## Ne pas ranger ici

- Assurances de l'entreprise (RC Pro, multirisque, cyber) → `06`
- Prévoyance et retraite des dirigeants et salariés → `06.4`

## Méthode de classement

**Un sous-dossier par contrat** : `Assureur - N° de contrat`. À l'intérieur : `Souscription`, `Versements et arbitrages`, `Releves/AAAA`, `Fiscalite/AAAA` (le calcul de l'imposition annuelle), `Rachats`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Contrat d'assurance : 2 ans après la fin (prescription biennale). Pièce comptable : 10 ans. Documents fiscaux : 10 ans. |
| **Recommandé** | Durée du contrat + 10 ans. Conserver impérativement le **taux de référence retenu à la souscription** et l'historique des impositions annuelles déjà acquittées : ils servent au calcul de la régularisation lors du rachat, parfois quinze ans plus tard. |

Base : Code des assurances art. L.114-1 ; CGI art. 238 septies E (imposition annuelle des primes de remboursement pour les personnes morales) ; Code de commerce art. L.123-22.

## Conseils

- Le régime fiscal d'un contrat de capitalisation détenu par une société à l'IS diffère nettement de celui d'un particulier : faire valider le calcul par l'expert-comptable dès la première clôture et ranger sa note ici, elle resservira chaque année.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
