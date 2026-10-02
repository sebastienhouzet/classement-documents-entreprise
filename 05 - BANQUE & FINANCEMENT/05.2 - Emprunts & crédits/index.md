---
schema: classement-documents/3.0
id: "05.2"
parent: "05"
niveau: sous-dossier
titre: "05.2 - Emprunts & crédits"
usage: >-
  Chaque financement bancaire ou assimilé : prêt d'équipement, prêt de trésorerie, PGE, prêt
  d'honneur, crédit-bail, affacturage, découvert autorisé.
classement: par-operation
sensibilite: confidentielle
documents:
  - type: contrat-pret-bancaire
    libelle: Contrat de prêt
    description: "Offre de prêt, accord et contrat de prêt signé — prêt d'équipement, prêt de trésorerie, PGE, prêt d'honneur."
    indices: [contrat de pret, offre de pret, pge, "pret d'honneur", credit-bail financier, decouvert autorise]
    champs: [date-signature, banque, numero, montant, taux, echeance]
    nommage: "{date}_Contrat-de-pret_{banque}_{numero}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code civil art. 2224
      sort-final: C
    registre: { fichier: Registre-des-contrats.csv, cle: numero }
  - type: tableau-amortissement-emprunt
    libelle: "Tableau d'amortissement d'emprunt"
    description: "Tableau d'amortissement du prêt et ses versions après renégociation, report d'échéances ou remboursement anticipé."
    indices: ["tableau d'amortissement", echeancier, renegociation, "report d'echeances", remboursement anticipe, decompte final]
    champs: [date, banque, numero, montant, taux, echeance]
    nommage: "{date}_Tableau-amortissement_{banque}_{numero}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: null
  - type: attestation-interets-capital-restant
    libelle: "Attestation d'intérêts et de capital restant dû"
    description: "Attestation annuelle d'intérêts payés et de capital restant dû, remise à l'expert-comptable pour la clôture."
    indices: ["attestation d'interets", capital restant du, cloture annuelle, assurance emprunteur, attestation annuelle]
    champs: [exercice, banque, numero, montant, taux]
    nommage: "{exercice}_Attestation-interets_{banque}_{numero}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: null
  - type: mainlevee-garantie-pret
    libelle: Mainlevée des garanties du prêt
    description: "Mainlevée des garanties adossées au financement à la fin du prêt, et décompte final de solde."
    indices: [mainlevee, fin de pret, liberation de garantie, nantissement leve, hypotheque levee]
    champs: [date, banque, numero, montant, objet]
    nommage: "{date}_Mainlevee-de-garantie_{banque}_{numero}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: mainlevee
      base: Code civil art. 2224
      sort-final: C
    registre: null
  - type: contrat-affacturage-dailly
    libelle: "Contrat d'affacturage ou de cession Dailly"
    description: "Contrat d'affacturage ou de cession Dailly, avec ses bordereaux de cession et ses relevés de compte de factor."
    indices: [affacturage, dailly, factor, bordereau de cession, relance du factor, retenue de garantie factor]
    champs: [date-signature, banque, numero, montant, taux]
    nommage: "{date}_Contrat-affacturage_{banque}_{numero}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: { fichier: Registre-des-contrats.csv, cle: numero }
va-ailleurs:
  - motif: Relevés du compte sur lequel le prêt est débité
    vers: "05.1"
---

# 05.2 - Emprunts & crédits

> Chemin : `05 - BANQUE & FINANCEMENT/05.2 - Emprunts & crédits`

## À quoi sert ce dossier

Chaque financement bancaire ou assimilé : prêt d'équipement, prêt de trésorerie, PGE, prêt d'honneur, crédit-bail, affacturage, découvert autorisé. Un dossier par financement, de la demande à la mainlevée des garanties.

## Documents à y ranger

- Dossier de demande (prévisionnel transmis, pièces fournies), offre de prêt, accord
- Contrat de prêt signé et tableau d'amortissement
- Garanties associées : caution personnelle du dirigeant (copie — original dans `05.6`), nantissement, garantie Bpifrance, hypothèque
- Assurance emprunteur (adhésion, attestation annuelle)
- Attestations annuelles d'intérêts et de capital restant dû (pour la clôture)
- Renégociation, report d'échéances, remboursement anticipé, décompte final
- Mainlevée des garanties à la fin du prêt
- Affacturage / Dailly : contrat, bordereaux, relevés
- Prêts d'honneur (Initiative, Réseau Entreprendre) : convention, échéancier

## Ne pas ranger ici

- Relevés du compte sur lequel le prêt est débité → `05.1`

## Méthode de classement

**Un sous-dossier par financement** : `AAAA - Établissement - Objet - Montant` (ex. `2024 - Banque Alpha - Pret equipement - 40k`). À l'intérieur : `Demande`, `Contrat et garanties`, `Vie du pret/AAAA`, `Fin`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Durée du prêt + 5 ans (prescription) ; le contrat est aussi une pièce comptable : 10 ans après la dernière écriture. |
| **Recommandé** | 10 ans après la dernière échéance, y compris la mainlevée. |

Base : Code civil art. 2224 ; Code de commerce art. L.123-22.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
