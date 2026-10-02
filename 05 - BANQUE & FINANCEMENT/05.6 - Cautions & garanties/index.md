---
schema: classement-documents/3.0
id: "05.6"
parent: "05"
niveau: sous-dossier
titre: "05.6 - Cautions & garanties"
usage: >-
  Les engagements de garantie, dans les deux sens : ceux que l'entreprise ou son dirigeant
  donnent (caution personnelle sur un prêt, garantie bancaire au bailleur, garantie à première
  demande à un client) et ceux qu'elle reçoit (dépôt de garantie, caution d'un sous-traitant,
  garantie bancaire d'un client).
classement: par-contrat
sensibilite: confidentielle
documents:
  - type: caution-personnelle-dirigeant
    libelle: Caution personnelle du dirigeant
    description: "Acte de cautionnement personnel du dirigeant avec sa mention manuscrite, et information annuelle de la caution par la banque."
    indices: [caution personnelle, cautionnement, mention manuscrite, information annuelle de la caution, engagement du dirigeant]
    champs: [date-signature, dirigeant, banque, montant, echeance]
    nommage: "{date}_Caution-personnelle_{dirigeant}_{banque}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-garantie
      base: Code civil art. 2288 et s.
      sort-final: C
    registre: null
  - type: garantie-bancaire-donnee
    libelle: Garantie bancaire donnée
    description: "Garantie bancaire ou garantie à première demande émise pour le compte de l'entreprise — garantie de loyer, de restitution d'acompte, de bonne fin — et garanties publiques sur prêt."
    indices: [garantie bancaire, garantie a premiere demande, garantie de loyer, bonne fin, garantie bpifrance]
    champs: [date, banque, beneficiaire, montant, echeance]
    nommage: "{date}_Garantie-bancaire-donnee_{banque}_{beneficiaire}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-garantie
      base: Code civil art. 2224
      sort-final: C
    registre: null
  - type: nantissement-hypotheque
    libelle: "Nantissement, gage ou hypothèque"
    description: "Acte de nantissement (fonds de commerce, parts sociales, compte-titres), gage ou hypothèque consenti en garantie d'un engagement."
    indices: [nantissement, gage, hypotheque, fonds de commerce, parts sociales nanties, inscription de surete]
    champs: [date, beneficiaire, numero, montant, designation]
    nommage: "{date}_Nantissement_{beneficiaire}_{designation}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: mainlevee
      base: Code civil art. 2224
      sort-final: C
    registre: null
  - type: garantie-recue-tiers
    libelle: "Garantie reçue d'un tiers"
    description: "Garanties reçues par l'entreprise — dépôt de garantie client, garantie à première demande, caution de sous-traitant, lettre d'intention, retenue de garantie."
    indices: [garantie recue, depot de garantie, caution de sous-traitant, retenue de garantie, "lettre d'intention de garantie"]
    champs: [date, tiers, montant, echeance, objet]
    nommage: "{date}_Garantie-recue_{tiers}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-garantie
      base: Code de commerce art. L.110-4
      sort-final: T
    registre: null
  - type: mainlevee-attestation-fin-garantie
    libelle: Mainlevée et attestation de fin de garantie
    description: "Mainlevée d'une garantie donnée ou reçue, et attestation de fin de garantie — preuve à conserver impérativement."
    indices: [mainlevee, attestation de fin de garantie, liberation de caution, restitution de depot de garantie, "radiation d'inscription"]
    champs: [date, beneficiaire, numero, montant, date-effet]
    nommage: "{date}_Mainlevee-de-fin-de-garantie_{beneficiaire}_{numero}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: mainlevee
      base: Code civil art. 2224
      sort-final: C
    registre: null
va-ailleurs:
  - motif: Contrat de prêt garanti
    vers: "05.2"
  - motif: Bail garanti
    vers: "02.4"
---

# 05.6 - Cautions & garanties

> Chemin : `05 - BANQUE & FINANCEMENT/05.6 - Cautions & garanties`

## À quoi sert ce dossier

Les engagements de garantie, dans les deux sens : ceux que l'entreprise ou son dirigeant **donnent** (caution personnelle sur un prêt, garantie bancaire au bailleur, garantie à première demande à un client) et ceux qu'elle **reçoit** (dépôt de garantie, caution d'un sous-traitant, garantie bancaire d'un client). Ils survivent souvent au contrat qu'ils garantissent.

## Documents à y ranger

- Cautions personnelles du dirigeant (acte, mention manuscrite, information annuelle de la banque)
- Garanties bancaires données (garantie de loyer, garantie de restitution d'acompte, garantie de bonne fin)
- Garanties Bpifrance et autres garanties publiques sur prêts
- Nantissements (fonds de commerce, parts sociales, comptes-titres), gages, hypothèques
- Garanties reçues : dépôts de garantie clients, garanties à première demande, cautions de sous-traitants, lettres d'intention, retenues de garantie
- Mainlevées et attestations de fin de garantie
- `Registre-des-garanties.csv` : garantie, bénéficiaire, montant, date, échéance, contrat lié, mainlevée

## Ne pas ranger ici

- Contrat de prêt garanti → `05.2`
- Bail garanti → `02.4`

## Méthode de classement

Deux sous-dossiers `Donnees` et `Recues`, puis **un sous-dossier par contrepartie ou par contrat garanti**, nommé comme le contrat correspondant (`2024 - Banque Alpha - Pret equipement`).

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Durée de la garantie + 5 ans (prescription). |
| **Recommandé** | 10 ans après la mainlevée, en gardant impérativement la preuve de mainlevée. |

Base : Code civil art. 2288 et s. (cautionnement), art. 2224 ; Code de commerce art. L.110-4.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
