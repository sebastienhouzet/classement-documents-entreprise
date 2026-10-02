---
schema: classement-documents/3.0
id: "07.2"
parent: "07"
niveau: sous-dossier
titre: 07.2 - Courrier
usage: >-
  Le courrier entrant et sortant qui ne se rattache à aucun dossier précis, et la preuve des
  envois recommandés. Règle : si un courrier concerne un dossier existant (un client, un
  salarié, un contrat, un litige), il est rangé dans ce dossier ; ici ne restent que le courrier
  général et le registre des recommandés.
classement: chronologique
sensibilite: normale
documents:
  - type: courrier-entrant-general
    libelle: Courrier entrant général
    description: "Courrier entrant numérisé qui ne se rattache à aucun dossier existant, publicités et courriers sans valeur exclus."
    indices: [courrier entrant, courrier recu, numerisation du courrier, reexpedition de courrier]
    champs: [date, emetteur, objet, sens]
    nommage: "{date}_Courrier-entrant_{emetteur}_{objet}"
    conservation:
      legale: 5a
      recommandee: 5a
      declencheur: date-document
      base: Code de commerce art. L.110-4
      sort-final: D
    registre: null
  - type: courrier-sortant-general
    libelle: Courrier sortant général
    description: "Copie de la version envoyée d'un courrier sortant qui ne se rattache à aucun dossier existant."
    indices: [courrier sortant, copie du courrier envoye, lettre simple, courrier general]
    champs: [date, destinataire, objet, sens]
    nommage: "{date}_Courrier-sortant_{destinataire}_{objet}"
    conservation:
      legale: 5a
      recommandee: 5a
      declencheur: date-document
      base: Code de commerce art. L.110-4
      sort-final: D
    registre: null
  - type: lettre-recommandee-avec-ar
    libelle: Lettre recommandée avec accusé de réception
    description: "Preuve de dépôt, accusé de réception et contenu d'un recommandé papier, réunis en un seul PDF. Un recommandé suit la durée du dossier auquel il se rattache."
    indices: [lettre recommandee, lrar, accuse de reception, preuve de depot, recommande]
    champs: [date, destinataire, numero-recommande, objet]
    nommage: "{date}_LRAR_{destinataire}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: date-document
      base: Code de commerce art. L.110-4
      sort-final: T
    registre: { fichier: Registre-des-recommandes.csv, cle: numero-recommande }
  - type: recommande-electronique-lre
    libelle: Recommandé électronique (LRE)
    description: "Preuve de dépôt et de réception d'un recommandé électronique émis par un prestataire qualifié."
    indices: [lre, recommande electronique, preuve de depot electronique, preuve de reception]
    champs: [date, destinataire, numero-recommande, objet, plateforme]
    nommage: "{date}_LRE_{destinataire}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: date-document
      base: Code de commerce art. L.110-4
      sort-final: T
    registre: { fichier: Registre-des-recommandes.csv, cle: numero-recommande }
---

# 07.2 - Courrier

> Chemin : `07 - ADMINISTRATIF & ORGANISMES/07.2 - Courrier`

## À quoi sert ce dossier

Le courrier entrant et sortant qui ne se rattache à aucun dossier précis, et la preuve des envois recommandés. Règle : si un courrier concerne un dossier existant (un client, un salarié, un contrat, un litige), il est rangé **dans ce dossier** ; ici ne restent que le courrier général et le registre des recommandés.

## Documents à y ranger

- Courrier entrant numérisé (publicités et courriers sans valeur exclus)
- Courrier sortant (copie de la version envoyée)
- Lettres recommandées : preuve de dépôt + accusé de réception + contenu, réunis en un seul PDF
- Recommandés électroniques (LRE) : preuve de dépôt et de réception
- `Registre-des-recommandes.csv` : date, destinataire, objet, n° de recommandé, dossier de rangement
- Contrats de domiciliation / réexpédition du courrier (copie ; contrat dans `02.4` ou `02.5`)

## Méthode de classement

**Par année**, puis `Entrant` et `Sortant`. Nommage : `AAAA-MM-JJ_Expediteur-ou-Destinataire_Objet.pdf` ; recommandés : `AAAA-MM-JJ_LRAR_Destinataire_Objet.pdf`. Numériser le courrier dès réception, puis détruire le papier sauf originaux à valeur juridique (actes, chèques, LRAR reçus).

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Correspondance commerciale : 5 ans. Un recommandé suit la durée du dossier auquel il se rattache. |
| **Recommandé** | 5 ans, purge annuelle ; 10 ans pour les recommandés. |

Base : Code de commerce art. L.110-4.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
