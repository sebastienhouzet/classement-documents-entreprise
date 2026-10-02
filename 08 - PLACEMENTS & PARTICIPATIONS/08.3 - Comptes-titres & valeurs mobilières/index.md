---
schema: classement-documents/3.0
id: "08.3"
parent: "08"
niveau: sous-dossier
titre: "08.3 - Comptes-titres & valeurs mobilières"
usage: >-
  Les titres cotés détenus par l'entreprise via un compte-titres : actions, obligations, OPCVM
  (SICAV, FCP), ETF, produits structurés.
classement: par-contrat
sensibilite: confidentielle
documents:
  - type: convention-compte-titres
    libelle: Convention de compte-titres
    description: "Convention de compte-titres ordinaire au nom de la personne morale, conditions tarifaires, convention de services d'investissement et dossier KYC remis à l'établissement."
    indices: [convention de compte-titres, compte-titres ordinaire, conditions tarifaires, "services d'investissement", kyc personne morale]
    champs: [date-signature, banque, numero-compte, objet]
    nommage: "{date}_Convention-compte-titres_{banque}_{numero-compte}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: null
  - type: avis-opere-titres
    libelle: "Avis d'opéré sur titres"
    description: "Avis d'opéré de chaque achat et de chaque vente de titres cotés — c'est la pièce qui fixe le prix de revient de la ligne. Ne jamais purger tant que la ligne est détenue."
    indices: ["avis d'opere", achat de titres, vente de titres, isin, prix de revient, "bordereau d'execution"]
    champs: [date, banque, numero-compte, isin, designation, quantite, cours, devise]
    nommage: "{date}_Avis-d-opere_{banque}_{isin}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cession-ligne
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: { fichier: Registre-des-placements.csv, cle: designation }
  - type: releve-compte-titres
    libelle: Relevé de portefeuille
    description: "Relevés de portefeuille périodiques et relevé au 31/12, avec le DIC et le prospectus des supports dans la version en vigueur à la souscription."
    indices: [releve de portefeuille, releve au 31/12, dic, priips, prospectus, "document d'informations cles"]
    champs: [date, banque, numero-compte, periode, montant]
    nommage: "{date}_Releve-compte-titres_{banque}_{periode}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: date-document
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: null
  - type: avis-operation-sur-titres
    libelle: "Avis d'opération sur titres"
    description: "Avis de dividende, de coupon, de détachement, d'attribution, de regroupement ou d'offre publique, et état annuel des revenus de capitaux mobiliers fourni par l'établissement."
    indices: [dividende, coupon, detachement, regroupement, offre publique, revenus de capitaux mobiliers]
    champs: [date, banque, isin, montant, nature]
    nommage: "{date}_Avis-operation-sur-titres_{banque}_{isin}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: null
  - type: calcul-plus-value-titres
    libelle: Calcul des plus-values et dépréciations sur titres
    description: "Calcul des plus ou moins-values de cession avec la méthode retenue — premier entré premier sorti ou coût moyen pondéré — appliquée de façon constante, et provisions pour dépréciation à la clôture."
    indices: [plus-value de cession, moins-value, premier entre premier sorti, cout moyen pondere, depreciation de titres]
    champs: [date, exercice, isin, designation, montant, methode-valorisation]
    nommage: "{date}_Calcul-plus-value-titres_{exercice}_{isin}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: LPF art. L.102 B
      sort-final: D
    registre: null
va-ailleurs:
  - motif: Titres de participation dans une société non cotée
    vers: "08.8"
  - motif: "Parts de SCPI et d'OPCI"
    vers: "08.6"
  - motif: "Parts de fonds non cotés (FCPR, FPCI)"
    vers: "08.7"
---

# 08.3 - Comptes-titres & valeurs mobilières

> Chemin : `08 - PLACEMENTS & PARTICIPATIONS/08.3 - Comptes-titres & valeurs mobilières`

## À quoi sert ce dossier

Les titres cotés détenus par l'entreprise via un compte-titres : actions, obligations, OPCVM (SICAV, FCP), ETF, produits structurés. Une société ne peut pas ouvrir de PEA : il s'agit toujours d'un compte-titres ordinaire au nom de la personne morale.

## Documents à y ranger

- Convention de compte-titres, conditions tarifaires, convention de services d'investissement
- Dossier KYC de la personne morale remis à l'établissement (Kbis, statuts, bénéficiaires effectifs — copies)
- **Avis d'opéré de chaque achat et de chaque vente** : c'est la pièce qui fixe le prix de revient, à conserver ligne par ligne
- DIC / document d'informations clés et prospectus des supports, dans la version en vigueur à la souscription
- Relevés de portefeuille périodiques et relevé au 31/12
- Avis d'opérations sur titres : dividendes, coupons, détachements, attributions, regroupements, offres publiques
- État annuel des revenus de capitaux mobiliers et des plus-values fourni par l'établissement
- Calcul des plus ou moins-values de cession, avec la méthode retenue (premier entré-premier sorti ou coût moyen pondéré), appliquée de façon constante d'un exercice à l'autre
- Provisions pour dépréciation à la clôture : calcul et justificatif de la valeur retenue
- Mandat de gestion et comptes rendus de gestion, le cas échéant
- Clôture du compte ou transfert de titres vers un autre établissement (bordereau de transfert)

## Ne pas ranger ici

- Titres de participation dans une société non cotée → `08.8`
- Parts de SCPI et d'OPCI → `08.6`
- Parts de fonds non cotés (FCPR, FPCI) → `08.7`

## Méthode de classement

**Un sous-dossier par compte-titres** : `Établissement - N° de compte`. À l'intérieur : `Convention et KYC`, `Avis d'opere/AAAA` (un fichier par opération : `AAAA-MM-JJ_Achat_ISIN-Libelle_Quantite.pdf`), `Releves/AAAA`, `Cloture/AAAA` (valorisation au 31/12, calcul des plus-values, dépréciations), `Documentation` (DIC, prospectus).

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Pièces comptables : 10 ans après la clôture de l'exercice. Documents fiscaux : 10 ans. Relevés bancaires : 5 ans. |
| **Recommandé** | Durée de détention + 10 ans — et **ne jamais purger un avis d'achat tant que la ligne est détenue**, c'est lui qui porte le prix de revient. |

Base : Code de commerce art. L.123-22 ; LPF art. L.102 B ; PCG, comptes 50 (valeurs mobilières de placement) et 27 (titres immobilisés) selon l'intention de détention.

## Conseils

- Le classement comptable (valeurs mobilières de placement ou titres immobilisés) dépend de l'intention à l'achat : la note de décision de `08.1` doit la formuler, et la méthode de calcul des plus-values doit rester identique d'un exercice à l'autre.
- Pour un support libellé en devise, conserver aussi le cours de change appliqué à l'achat et à la vente.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
