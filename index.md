# Template Entreprise — Guide de classement

Ce dossier est le plan de classement de l'ensemble des documents de **gestion** d'une entreprise française
(administratif, juridique, RH, contrats, assurances, comptabilité, banque). La partie opérationnelle
(projets, livrables, production) est classée ailleurs.

Chaque dossier contient un fichier `index.md` qui explique à quoi il sert, quels documents y ranger,
comment les classer et combien de temps les conserver.

## Les cinq règles

1. **Un document n'a qu'une seule place.** La facture d'un fournisseur va en comptabilité, son contrat en
   contrats, son attestation d'assurance en assurances. Quand un document est utile à deux endroits, on range
   l'original à sa place et on met une **copie** clairement nommée `(copie)` dans l'autre, ou un simple renvoi.
2. **Un seul format de nom de fichier** : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir
   `00 - REFERENTIEL/Convention-de-nommage.md`. Les fichiers se trient tout seuls par date.
3. **Les dossiers volumineux sont découpés par année, puis par mois** (factures, relevés, paie) ;
   les dossiers relationnels sont découpés **par tiers** (clients, fournisseurs, salariés, contrats d'assurance).
4. **On ne supprime rien avant sa date** : les dossiers clos vont dans `08 - ARCHIVES` avec leur date de
   destruction prévue, et on purge une fois par an.
5. **On numérise tout** (PDF, sans retouche) : une copie numérique fidèle a la même valeur que l'original
   papier pour la comptabilité et le fisc. Les originaux papier à valeur juridique (actes signés, LRAR reçus)
   sont gardés dans un classeur qui suit le même plan.

## Arborescence

| Dossier | Contenu | Découpage |
|---|---|---|
| `00 - REFERENTIEL` | Ce guide, la convention de nommage, les durées de conservation, le kit administratif | à plat |
| `01 - JURIDIQUE & GOUVERNANCE` | Constitution, statuts, AG, registres, dirigeants, associés, PI, conformité, contentieux | par thème, puis par année ou par opération |
| `02 - CONTRATS` | Clients, fournisseurs, sous-traitance, baux, abonnements, NDA, modèles | par tiers |
| `03 - RESSOURCES HUMAINES` | Registres, dossiers salariés, paie, organismes sociaux, recrutement, formation, absences, santé-sécurité, CSE | par personne ; paie par année/mois |
| `04 - COMPTABILITE & FISCALITE` | Exercices, factures clients et fournisseurs, notes de frais, immobilisations, impôts, expert-comptable, budget | par année, puis par mois |
| `05 - BANQUE & FINANCEMENT` | Comptes, emprunts, aides, investisseurs, moyens de paiement, garanties | par établissement ou opération ; relevés par année |
| `06 - ASSURANCES` | Un dossier par contrat, sinistres | par contrat ; attestations par année |
| `07 - ADMINISTRATIF & ORGANISMES` | Administrations, courrier, locaux, véhicules, certifications, matériel | par organisme, par année ou par objet |
| `08 - ARCHIVES` | Dossiers clos en attente de destruction | par année de clôture, même chemin qu'à l'origine |

## Qui a accès à quoi

| Dossier | Accès |
|---|---|
| `03 - RESSOURCES HUMAINES` et ses archives | Dirigeant + personne chargée de la paie/RH uniquement (données personnelles, santé) |
| `04`, `05` | Dirigeant + comptabilité ; expert-comptable en lecture |
| `01.6`, `05.4`, `06.6` | Dirigeant (et associés pour `01.6`) |
| Le reste | Équipe de gestion |

## Routine

- **À réception d'un document** : le nommer, le ranger, et s'il crée une échéance (contrat, assurance, garantie),
  la noter dans le registre du domaine (`Registre-des-contrats.csv`, `Registre-des-assurances.csv`, …).
- **Chaque mois** : télécharger les relevés bancaires et de paiement, classer les factures du mois, archiver la paie.
- **Chaque trimestre** : vérifier la validité des pièces du `Kit administratif` (Kbis 3 mois, URSSAF 6 mois).
- **Chaque année (janvier)** : figer l'exercice clos dans `04.1`, purger les candidatures de plus de 2 ans,
  déplacer les dossiers clos vers `08 - ARCHIVES`, détruire ce qui a dépassé sa date et le noter dans le registre.

## Point de départ

1. Lire `00 - REFERENTIEL/Convention-de-nommage.md` (5 minutes).
2. Créer les sous-dossiers par tiers au fur et à mesure (un client, un fournisseur, un salarié) — ne pas les créer à l'avance.
3. Remplir les registres CSV avec l'existant : contrats, assurances, matériel.
4. Supprimer les sous-dossiers qui ne concernent pas l'entreprise (`03.10` sans CSE, `07.4` sans véhicule…) ou les laisser vides : leur `index.md` explique quand ils deviennent nécessaires.
