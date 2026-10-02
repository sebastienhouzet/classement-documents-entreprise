# Template Entreprise — Guide de classement

Ce dossier est le plan de classement de l'ensemble des documents de **gestion** d'une entreprise française :
administratif, juridique, RH, contrats, assurances, comptabilité, banque, placements. La partie opérationnelle
(projets, livrables, production) est classée ailleurs.

Chaque dossier contient un fichier `index.md` qui explique à quoi il sert, quels documents y ranger,
comment les classer et combien de temps les conserver.

## Le cycle de vie d'un document

Tout document suit le même trajet. Il entre par `00 - INBOX`, il est nommé puis rangé dans l'un des huit domaines
métier (`01` à `08`), il y vit tant qu'il est utile, il part dans `98 - ARCHIVES` quand son dossier est clos, et il
n'est détruit qu'après un passage validé par `99 - SUPPRESSION`. Le `97 - REFERENTIEL` porte les règles du jeu et ne
contient aucun document d'entreprise.

## Les cinq règles

1. **Un document n'a qu'une seule place.** La facture d'un fournisseur va en comptabilité, son contrat en
   contrats, son attestation d'assurance en assurances. Quand un document est utile à deux endroits, on range
   l'original à sa place et on met une **copie** clairement nommée `(copie)` dans l'autre, ou un simple renvoi.
2. **Un seul format de nom de fichier** : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir
   `97 - REFERENTIEL/Convention-de-nommage.md`. Les fichiers se trient tout seuls par date.
3. **Les dossiers volumineux sont découpés par année, puis par mois** (factures, relevés, paie) ;
   les dossiers relationnels sont découpés **par tiers** (clients, fournisseurs, salariés, contrats d'assurance,
   lignes de placement).
4. **On ne supprime rien sans trace.** Les dossiers clos vont dans `98 - ARCHIVES` avec leur date de destruction
   prévue ; la destruction elle-même passe par `99 - SUPPRESSION`, proposée par une personne et validée par une autre.
5. **On numérise tout** (PDF/A, sans retouche), mais on ne détruit le papier qu'à des conditions précises —
   empreinte, horodatage, procédé documenté — décrites dans
   `97 - REFERENTIEL/Numerisation-et-valeur-probante.md`, qui liste aussi les originaux à ne jamais détruire.

## Arborescence

| Dossier | Contenu | Découpage |
|---|---|---|
| `00 - INBOX` | Sas d'entrée : tout document reçu, en attente de traitement et de classement | à plat, se vide en continu |
| `01 - JURIDIQUE & GOUVERNANCE` | Constitution, statuts, AG, registres, dirigeants, associés, PI, conformité, contentieux | par thème, puis par année ou par opération |
| `02 - CONTRATS` | Clients, fournisseurs, sous-traitance, baux, abonnements, NDA, modèles | par tiers |
| `03 - RESSOURCES HUMAINES` | Registres, dossiers salariés, paie, organismes sociaux, recrutement, formation, absences, santé-sécurité, CSE | par personne ; paie par année/mois |
| `04 - COMPTABILITE & FISCALITE` | Exercices, factures clients et fournisseurs, notes de frais, immobilisations, impôts, expert-comptable, budget | par année, puis par mois |
| `05 - BANQUE & FINANCEMENT` | Comptes, emprunts, aides, investisseurs, moyens de paiement, garanties — l'argent qui **entre** | par établissement ou opération |
| `06 - ASSURANCES` | Un dossier par contrat, sinistres | par contrat ; attestations par année |
| `07 - ADMINISTRATIF & ORGANISMES` | Administrations, courrier, locaux, véhicules, certifications, matériel | par organisme, par année ou par objet |
| `08 - PLACEMENTS & PARTICIPATIONS` | Comptes à terme, titres, capitalisation, crypto-actifs, SCPI, fonds, filiales — l'argent qui est **placé** | par ligne de placement |
| `97 - REFERENTIEL` | Ce guide, la convention de nommage, les durées de conservation, le kit administratif | à plat |
| `98 - ARCHIVES` | Dossiers clos en attente de destruction | par année de clôture, même chemin qu'à l'origine |
| `99 - SUPPRESSION` | Lots proposés à la suppression, en attente de validation | par lot daté |

Les numéros `09` à `96` sont volontairement laissés libres : un nouveau domaine métier s'insère sans renuméroter
l'existant ni casser les renvois entre dossiers.

## Qui a accès à quoi

| Dossier | Accès |
|---|---|
| `03 - RESSOURCES HUMAINES` | Dirigeant + personne chargée de la paie/RH uniquement (données personnelles, santé) |
| `04`, `05`, `08` | Dirigeant + comptabilité ; expert-comptable en lecture |
| `01.6`, `05.4`, `06.6`, `08.8` | Dirigeant (et associés pour `01.6`) |
| `98 - ARCHIVES` | **Plus restrictif que les dossiers courants** : lecture seule par défaut, habilitations nominatives, accès journalisés — c'est ce que le RGPD exige de l'archivage intermédiaire |
| `99 - SUPPRESSION` | Dépôt ouvert à l'équipe de gestion, validation réservée au dirigeant |
| Le reste | Équipe de gestion |

La sauvegarde, les droits d'accès, les formats pérennes et la destruction sécurisée sont traités dans
`97 - REFERENTIEL/Securite-et-sauvegarde.md`. Le minimum : une sauvegarde **hors ligne**, un test de
restauration annuel, et l'authentification multifacteur sur le service qui héberge ce dossier.

## Routine

- **À réception d'un document** : le déposer dans `00 - INBOX`, puis, au traitement, le nommer, le ranger, et
  s'il crée une échéance (contrat, assurance, garantie, placement), la noter dans le registre du domaine
  (`Registre-des-contrats.csv`, `Registre-des-assurances.csv`, `Registre-des-placements.csv`, …).
- **Chaque semaine** : vider `00 - INBOX`. Aucun document ne doit y séjourner plus de 30 jours.
- **Chaque mois** : télécharger les relevés bancaires, de paiement et de placement, classer les factures du mois,
  archiver la paie.
- **Chaque trimestre** : vérifier la validité des pièces du `Kit administratif` (Kbis 3 mois, URSSAF 6 mois).
- **Chaque année (janvier)** : figer l'exercice clos dans `04.1`, constituer le dossier de clôture des
  placements dans `08.9`, mettre à jour le DUERP (obligatoire à partir de 11 salariés), tester une
  restauration de sauvegarde, purger les candidatures dont le poste a été pourvu il y a plus de 5 ans,
  déplacer les dossiers clos vers `98 - ARCHIVES`, et proposer dans `99 - SUPPRESSION` ce qui a dépassé sa date.
- **Chaque année (avant le 30 septembre)** : déclaration OPERAT si vous occupez 1 000 m² de tertiaire ou plus,
  même en location.

## Ce qui ne vous concerne probablement pas

Utile à savoir pour ne pas s'inquiéter à tort. Ces obligations ont des seuils élevés et **ne visent pas une
TPE ou une PME** : rapport de durabilité CSRD (1 000 salariés et 450 M€ de chiffre d'affaires, cumulatifs,
depuis la directive Omnibus de février 2026), devoir de vigilance (5 000 salariés et 1,5 Md€), bilan GES
réglementaire (500 salariés), NIS2 (non transposée en France à la rédaction de ce gabarit).

Un point à connaître en revanche, parce qu'il se négocie : la directive Omnibus crée un **plafond de chaîne de
valeur** juridiquement contraignant. Un donneur d'ordre n'a plus le droit d'exiger d'un fournisseur de moins
de 1 000 salariés des informations excédant le référentiel **VSME**. Un questionnaire ESG démesuré peut être
refusé, texte à l'appui. Préparer un petit dossier « réponses VSME » reste utile commercialement.

## Point de départ

1. Ouvrir `documentation.html` à la racine : le plan de classement complet, consultable et
   cherchable, sans avoir à parcourir les dossiers un par un.
2. Lire `97 - REFERENTIEL/Convention-de-nommage.md` (5 minutes).
3. Créer les sous-dossiers par tiers au fur et à mesure (un client, un fournisseur, un salarié, une ligne de
   placement) — ne pas les créer à l'avance.
4. Remplir les registres CSV avec l'existant : contrats, assurances, placements, matériel.
5. Remplir le `Tableau-de-gestion.csv` du référentiel : il est prérempli avec les principales typologies et
   leur sort final, à compléter avec les vôtres. C'est lui qui rend `99 - SUPPRESSION` utilisable.
6. Supprimer les sous-dossiers qui ne concernent pas l'entreprise (`03.10` sans CSE, `07.4` sans véhicule,
   `06.8` sans activité de travaux, `07.7` sans marchés publics, `08.5` sans crypto-actifs…) ou les laisser
   vides : leur `index.md` explique quand ils deviennent nécessaires.
