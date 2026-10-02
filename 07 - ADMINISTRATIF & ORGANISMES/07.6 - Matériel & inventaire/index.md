---
schema: classement-documents/3.0
id: "07.6"
parent: "07"
niveau: sous-dossier
titre: "07.6 - Matériel & inventaire"
usage: >-
  L'inventaire physique du matériel (ordinateurs, téléphones, écrans, mobilier, outillage) et
  son attribution aux personnes, ainsi que les licences logicielles détenues.
classement: alphabetique
sensibilite: normale
documents:
  - type: inventaire-du-materiel
    libelle: Inventaire du matériel
    description: "Fichier vivant de l'inventaire physique du matériel — désignation, marque et modèle, numéro de série, date d'achat, fournisseur, prix, attributaire, localisation, état, date de sortie."
    indices: [inventaire du materiel, numero de serie, attributaire, localisation, qui a quoi, etat du materiel]
    champs: [date, designation, fournisseur, numero-serie, lieu, salarie]
    nommage: "{date}_Inventaire-du-materiel_{designation}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: sortie-bien
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: { fichier: Inventaire-du-materiel.csv, cle: designation }
  - type: fiche-remise-materiel
    libelle: Fiche de remise ou de restitution de matériel
    description: "Fiche de remise ou de restitution de matériel signée par un salarié ou un freelance, y compris le matériel de télétravail et les prêts. Copie dans le dossier individuel."
    indices: [remise de materiel, restitution de materiel, pret de materiel, materiel en teletravail, fiche signee]
    champs: [date, salarie, designation, numero-serie, lieu]
    nommage: "{date}_Fiche-de-remise-materiel_{salarie}_{designation}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: depart-salarie
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: null
  - type: garantie-constructeur-materiel
    libelle: Garantie et extension de garantie
    description: "Garantie constructeur, extension de garantie et contrat de maintenance d'un bien matériel. L'original du contrat de maintenance reste en 02.2."
    indices: [garantie constructeur, extension de garantie, maintenance materielle, duree de garantie]
    champs: [date, fournisseur, designation, echeance, montant-ht, numero-serie]
    nommage: "{date}_Garantie-materiel_{fournisseur}_{designation}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-garantie
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: null
  - type: licence-logicielle-detenue
    libelle: Licence logicielle détenue
    description: "Preuve d'achat d'une licence logicielle, clé, compte titulaire et nombre de postes couverts. Sans mot de passe. Les abonnements SaaS relèvent de 02.5."
    indices: [licence logicielle, cle de licence, nombre de postes, compte titulaire, inventaire des licences]
    champs: [date, fournisseur, designation, quantite, reference]
    nommage: "{date}_Licence-logicielle_{fournisseur}_{designation}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-utilisation
      base: Code de commerce art. L.123-22
      sort-final: D
    registre: null
  - type: mise-au-rebut-materiel
    libelle: Mise au rebut de matériel
    description: "Procès-verbal de mise au rebut, attestation d'effacement des données ou de destruction et certificat de recyclage DEEE. Copie en 04.5."
    indices: [mise au rebut, "attestation d'effacement", destruction de donnees, deee, certificat de recyclage]
    champs: [date, designation, prestataire, numero, motif]
    nommage: "{date}_Mise-au-rebut_{prestataire}_{designation}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: sortie-bien
      base: "Code de l'environnement art. R.543-172"
      sort-final: D
    registre: null
va-ailleurs:
  - motif: "Factures d'achat"
    vers: "04.3"
  - motif: Abonnements SaaS
    vers: "02.5"
  - motif: Politique informatique et charte
    vers: "01.8"
---

# 07.6 - Matériel & inventaire

> Chemin : `07 - ADMINISTRATIF & ORGANISMES/07.6 - Matériel & inventaire`

## À quoi sert ce dossier

L'inventaire physique du matériel (ordinateurs, téléphones, écrans, mobilier, outillage) et son attribution aux personnes, ainsi que les licences logicielles détenues. C'est le dossier qui répond à « qui a quoi » et « quand l'a-t-on acheté », complémentaire des immobilisations comptables (`04.5`).

## Documents à y ranger

- `Inventaire-du-materiel.csv` (fichier vivant) : désignation, marque/modèle, n° de série, date d'achat, fournisseur, prix, attributaire, localisation, état, date de sortie
- Fiches de remise et de restitution de matériel signées par les salariés et freelances (copie dans leur dossier `03.2` / `03.9`)
- Garanties et extensions de garantie, contrats de maintenance matériel (copie ; original dans `02.2`)
- Licences logicielles : preuves d'achat, clés, comptes titulaires (sans mots de passe), nombre de postes
- Mise au rebut : attestation d'effacement des données / de destruction, certificat de recyclage (DEEE), PV de mise au rebut (copie dans `04.5`)
- Prêts de matériel, matériel en télétravail (attestation)

## Ne pas ranger ici

- Factures d'achat → `04.3` / `04.5`
- Abonnements SaaS → `02.5`
- Politique informatique et charte → `01.8`

## Méthode de classement

Sous-dossiers `Inventaire`, `Remises et restitutions` (un fichier par personne et par date), `Garanties` (un sous-dossier par bien important), `Licences` (un par logiciel), `Mises au rebut/AAAA`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Durée de vie du matériel + 5 ans (garanties, litiges) ; fiches de remise : durée du contrat de travail + 5 ans. |
| **Recommandé** | Durée de détention + 10 ans pour rester aligné avec les immobilisations. |

Base : Code de commerce art. L.123-22 ; Code de l'environnement art. R.543-172 et s. (DEEE).

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
