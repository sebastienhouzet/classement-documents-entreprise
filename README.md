# Template Entreprise — plan de classement des documents de gestion d'une entreprise française

Une arborescence de dossiers prête à l'emploi pour ranger **tous les documents de gestion** d'une entreprise
française — juridique, contrats, RH, comptabilité, fiscalité, banque, placements, assurances, administratif —
avec, dans chaque dossier, un fichier `index.md` qui explique quoi y mettre, comment le classer et combien de
temps le garder.

Ce dépôt ne contient aucun document : c'est un **gabarit vide et documenté**, à copier sur votre disque, votre
NAS ou votre espace cloud (Drive, OneDrive, Dropbox, Nextcloud…) pour y ranger vos propres pièces.

## Pour qui

TPE, PME, startups, indépendants en société, agences, associations ayant une activité économique. Le plan de
classement est pensé pour une société (SAS, SARL, SASU, EURL…) mais fonctionne aussi pour une entreprise
individuelle : il suffit d'ignorer les dossiers qui ne s'appliquent pas (assemblées, registres de titres, CSE…).

Il couvre la **gestion** de l'entreprise, pas son activité opérationnelle (projets, production, livrables clients),
qui a sa propre organisation ailleurs.

## Démarrage rapide

1. **Récupérer le gabarit** : cloner le dépôt ou télécharger l'archive ZIP (bouton *Code → Download ZIP*),
   puis copier le dossier à l'endroit où vous rangerez vos documents.
2. **Ouvrir [`documentation.html`](documentation.html)** : le plan complet dans une seule page,
   avec une fiche par dossier et un champ de recherche. C'est le moyen le plus rapide de savoir où
   va un document sans parcourir l'arborescence.
3. **Lire trois fichiers** (10 minutes) :
   - [`index.md`](index.md) — le guide de classement : le cycle de vie d'un document, les règles, la routine, les accès ;
   - [`97 - REFERENTIEL/Convention-de-nommage.md`](97%20-%20REFERENTIEL/Convention-de-nommage.md) — comment nommer fichiers et dossiers ;
   - [`97 - REFERENTIEL/Durees-de-conservation.md`](97%20-%20REFERENTIEL/Durees-de-conservation.md) — le tableau des durées légales et recommandées.

   Deux autres fichiers du référentiel se lisent au moment où la question se pose :
   [`Numerisation-et-valeur-probante.md`](97%20-%20REFERENTIEL/Numerisation-et-valeur-probante.md) avant de détruire
   du papier, et [`Securite-et-sauvegarde.md`](97%20-%20REFERENTIEL/Securite-et-sauvegarde.md) au moment de choisir
   où héberger le dossier.
4. **Remplir les registres CSV** avec l'existant (contrats, assurances, placements, matériel) : ce sont eux qui
   donnent la vue d'ensemble et les dates d'échéance.
5. **Ranger au fil de l'eau** : déposer les documents entrants dans `00 - INBOX`, puis les traiter par lot. En cas
   de doute sur la destination, ouvrir l'`index.md` du dossier concerné. Les sous-dossiers par client, par salarié
   ou par année se créent quand le besoin apparaît, pas à l'avance.

## Le cycle de vie d'un document

Tout document suit le même trajet : il **entre** par `00 - INBOX`, il est nommé puis **rangé** dans l'un des huit
domaines métier (`01` à `08`), il y vit tant qu'il est utile, il passe en `98 - ARCHIVES` quand son dossier est clos,
et il n'est **détruit** qu'après un passage validé par `99 - SUPPRESSION`. Le `97 - REFERENTIEL` porte les règles du
jeu et ne contient aucun document d'entreprise.

```
00 - INBOX  →  01 … 08 (domaines métier)  →  98 - ARCHIVES  →  99 - SUPPRESSION
   sas d'entrée         vie du document        dossier clos      destruction validée
```

## Structure

```
Template Entreprise/
├── README.md                          ← ce fichier
├── index.md                           ← guide de classement (cycle de vie, règles, routine, accès)
├── documentation.html                 ← le plan complet en une page, cherchable (à ouvrir dans un navigateur)
├── CHANGELOG.md                       ← historique des versions
├── AUDIT-CONFORMITE-2026-09.md        ← confrontation du gabarit aux sources officielles
├── referentiel/dossiers.json          ← les 78 en-têtes YAML compilés en un seul fichier
├── scripts/                           ← lint, compilateur, migration, génération de la documentation
├── 00 - INBOX/                        ← sas d'entrée : tout document reçu, en attente de classement
├── 01 - JURIDIQUE & GOUVERNANCE/      ← constitution, statuts, AG, registres, dirigeants, associés, PI, conformité, contentieux
├── 02 - CONTRATS/                     ← clients, fournisseurs, sous-traitance, baux, abonnements, NDA, modèles
├── 03 - RESSOURCES HUMAINES/          ← registres, dossiers salariés, paie, organismes sociaux, recrutement, formation, absences, santé-sécurité, CSE
├── 04 - COMPTABILITE & FISCALITE/     ← exercices, factures, notes de frais, immobilisations, impôts, expert-comptable, budget
├── 05 - BANQUE & FINANCEMENT/         ← comptes, emprunts, aides, investisseurs, moyens de paiement, garanties (l'argent qui entre)
├── 06 - ASSURANCES/                   ← un dossier par type de contrat, sinistres
├── 07 - ADMINISTRATIF & ORGANISMES/   ← administrations, courrier, locaux, véhicules, certifications, matériel
├── 08 - PLACEMENTS & PARTICIPATIONS/  ← comptes à terme, titres, capitalisation, crypto-actifs, SCPI, fonds, filiales (l'argent qui est placé)
├── 97 - REFERENTIEL/                  ← nommage, durées, tableau de gestion, numérisation, sécurité, routage pour agent
├── 98 - ARCHIVES/                     ← dossiers clos en attente de destruction
└── 99 - SUPPRESSION/                  ← lots proposés à la suppression, en attente de validation
```

Chaque domaine est découpé en sous-dossiers numérotés (`01.1`, `01.2`…), soit **78 dossiers** au total.
L'arborescence complète, avec le contenu de chaque sous-dossier, est décrite dans [`index.md`](index.md).

Les numéros `09` à `96` sont volontairement laissés libres : un nouveau domaine métier s'insère sans renuméroter
l'existant ni casser les renvois entre dossiers. La bande `97` à `99` est réservée aux dossiers système.

### Les trois logiques de classement

| Logique | Où | Exemple |
|---|---|---|
| **Par tiers** | Clients, fournisseurs, salariés, contrats d'assurance, comptes bancaires, lignes de placement | `02.1 - Clients/Client Alpha/` |
| **Par année, puis par mois** | Factures, relevés, paie, notes de frais, courrier | `04.3 - Factures fournisseurs/2026/2026-03/` |
| **Par opération ou affaire** | AG, modifications statutaires, litiges, sinistres, prêts, levées de fonds, lots de suppression | `01.9 - Contentieux/2026 - Client Beta - Impayé/` |

Un document n'a qu'**une seule place**. Quand il est utile ailleurs, on y met une copie nommée `_copie` ou un
simple renvoi ; chaque `index.md` indique, dans sa section « Ne pas ranger ici », où va ce qui n'y a pas sa place.

## Anatomie d'un `index.md`

Chaque `index.md` a deux étages : un **en-tête YAML** que les programmes lisent, et un **corps
Markdown** que les humains lisent. Les deux disent la même chose, dans deux langues.

### L'en-tête YAML (depuis la 3.0)

```yaml
---
schema: classement-documents/3.0
id: "04.3"
parent: "04"
niveau: sous-dossier
titre: 04.3 - Factures fournisseurs
usage: >-
  Toutes les factures reçues : achats, prestations, abonnements, loyers, honoraires…
classement: chronologique
sensibilite: confidentielle
documents:
  - type: facture-fournisseur
    libelle: Facture fournisseur
    indices: [facture, fournisseur, tva, net a payer]
    champs: [date, fournisseur, numero, montant-ht, montant-tva, montant-ttc]
    nommage: "{date}_Facture_{fournisseur}_{objet}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: Code de commerce L123-22
      sort-final: D
    registre: null
va-ailleurs:
  - motif: Notes de frais avancées par un salarié
    vers: "04.4"
---
```

| Champ | Ce qu'il porte |
|---|---|
| `id`, `parent`, `niveau` | La position du dossier dans l'arbre. L'`id` ne change jamais, même si le dossier est renommé — **toujours entre guillemets**, sans quoi `04.3` serait lu comme le nombre 4,3 |
| `titre`, `usage` | Le nom affiché et un texte court, destiné à être vectorisé pour pré-sélectionner les dossiers candidats |
| `classement` | `chronologique`, `par-tiers`, `par-contrat`, `par-operation` ou `alphabetique` |
| `sensibilite` | `normale`, `confidentielle` ou `rh` — sert à restreindre l'accès et à anonymiser avant de passer un document à un modèle |
| `documents[]` | **Les typologies que le dossier accueille** : clé stable, champs à extraire, gabarit de nom de fichier, durées, sort final, registre alimenté |
| `va-ailleurs[]` | Les règles négatives, avec l'`id` de la vraie destination |

Les valeurs sont énumérées : kebab-case, sans accent. Le catalogue des champs extractibles est dans
[`97 - REFERENTIEL/champs.yaml`](97%20-%20REFERENTIEL/champs.yaml) (78 champs, chacun avec son type et
son format) et le format de l'en-tête lui-même dans
[`97 - REFERENTIEL/schema-index.json`](97%20-%20REFERENTIEL/schema-index.json) (JSON Schema
draft 2020-12). Un champ absent du catalogue fait échouer le lint : c'est ce qui garantit qu'un même
numéro de contrat s'appelle `numero-contrat` dans les 78 dossiers.

### Le corps Markdown

Inchangé depuis la 1.0, et toujours la référence rédactionnelle :

| Section | Contenu |
|---|---|
| **À quoi sert ce dossier** | Le périmètre en quelques lignes, et ses limites |
| **Documents à y ranger** | La liste concrète des pièces attendues |
| **Ne pas ranger ici** | Ce qui ressemble mais va ailleurs, avec le dossier cible |
| **Méthode de classement** | Par tiers, par année/mois ou par opération ; structure des sous-dossiers ; exemples de noms de fichiers |
| **Durée de conservation** | Minimum légal, durée recommandée, et la base juridique |
| **Conseils** | Points d'attention pratiques (délais, pièges, obligations liées) |

Les `index.md` ont aussi un rôle technique : Git ne versionne pas les dossiers vides, c'est leur présence qui
permet au dépôt de contenir l'arborescence complète.

Ce sont eux la source de vérité : `documentation.html`, `AGENT-ROUTAGE.md`, `routage.json` et
`referentiel/dossiers.json` en sont **générés**, et ne peuvent donc pas diverger du contenu des
dossiers.

## Outillage

Quatre scripts, sans dépendance au-delà de `pyyaml` et `jsonschema` :

| Commande | Ce qu'elle fait |
|---|---|
| `python3 scripts/lint.py .` | Contrôle les 78 en-têtes : schéma, unicité des `id` et des clés `type`, champs hors catalogue, variables de nommage orphelines, renvois `va-ailleurs` cassés, registres inexistants, concordance des sorts finaux avec le tableau de gestion |
| `python3 scripts/compiler.py .` | Compile les en-têtes en `referentiel/dossiers.json`, avec deux index : `index_types` donne le dossier d'un type documentaire en une lecture, `index_chemins` donne son chemin |
| `python3 scripts/migrer-frontmatter.py <votre-copie>` | Pose l'en-tête 3.0 sur une copie personnalisée du gabarit **sans toucher au corps Markdown**. Essai à blanc par défaut, `--ecrire` pour appliquer, sauvegardes en `*.avant-3.0` |
| `python3 scripts/gendoc.py .` | Régénère `documentation.html`, `AGENT-ROUTAGE.md` et `routage.json` |

Le lint tourne en intégration continue à chaque poussée
([`.github/workflows/lint.yml`](.github/workflows/lint.yml)), et vérifie au passage que
`referentiel/dossiers.json` est bien à jour. Si vous modifiez un `index.md`, relancez le
compilateur avant de pousser.

## Les registres

Huit fichiers CSV (séparateur `;`, encodage UTF-8, ouvrables dans Excel, Numbers ou LibreOffice) servent de
vue d'ensemble là où les dossiers ne suffisent pas. Sept sont vides ; le tableau de gestion est prérempli :

| Registre | Emplacement | À quoi il sert |
|---|---|---|
| `Registre-des-contrats.csv` | `02 - CONTRATS/` | Échéances, préavis, dates limites de résiliation |
| `Registre-des-immobilisations.csv` | `04.5 - Immobilisations/` | Biens durables, amortissements, sorties |
| `Registre-des-assurances.csv` | `06 - ASSURANCES/` | Garanties, plafonds, franchises, échéances |
| `Registre-des-recommandes.csv` | `07.2 - Courrier/` | Preuves d'envoi et de réception des LRAR |
| `Inventaire-du-materiel.csv` | `07.6 - Matériel & inventaire/` | Qui a quoi, numéros de série, restitutions |
| `Registre-des-placements.csv` | `08 - PLACEMENTS & PARTICIPATIONS/` | Lignes détenues, prix de revient, échéances, valeur à la dernière clôture |
| `Registre-des-archives.csv` | `98 - ARCHIVES/` | Dossiers clos et **dates de destruction prévues** |
| `Tableau-de-gestion.csv` | `97 - REFERENTIEL/` | Une ligne par typologie : producteur, durée, **sort final** (conserver / détruire / trier), référence juridique, et la **clé de type** qui relie la ligne à l'en-tête YAML du dossier |

## Pour un agent qui classe automatiquement

Le fichier [`97 - REFERENTIEL/AGENT-ROUTAGE.md`](97%20-%20REFERENTIEL/AGENT-ROUTAGE.md) est la
version compacte du plan, écrite pour un agent d'ingestion : une procédure en huit points, une table
de décision de 69 destinations avec leurs déclencheurs et leurs arbitrages, les pièges de
classement les plus coûteux, un barème de confiance et un contrat de sortie JSON.

Il est conçu pour être chargé en préfixe stable d'un prompt. Coût mesuré : environ **11 700 tokens**
pour le fichier entier, ou **5 800 au pire** en deux temps — aiguillage vers un domaine, puis
chargement du seul bloc de ce domaine. Le fichier porte lui-même le détail de ces mesures.

Les mêmes données sont disponibles dans
[`97 - REFERENTIEL/routage.json`](97%20-%20REFERENTIEL/routage.json) pour un usage programmatique :
préfiltrage déterministe par mots-clés, puis appel au modèle sur les seuls cas ambigus.

Règle de sûreté intégrée : en dessous de 0,7 de confiance, l'agent ne classe pas, il dépose dans
`00 - INBOX` avec le motif du doute. Un document mal classé coûte plus cher qu'un document resté
dans le sas.

Le classement se fait en deux passes, et c'est ce qui le rend économe. La première choisit le
dossier, avec `AGENT-ROUTAGE.md` seul. La seconde qualifie la pièce : l'agent lit, dans
[`referentiel/dossiers.json`](referentiel/dossiers.json), le seul dossier retenu — il y trouve les
typologies possibles, les champs à extraire, le gabarit de nom et la durée de conservation. Il n'a
jamais besoin de charger les 298 typologies du gabarit pour en reconnaître une. Sa sortie JSON porte
alors la clé `type`, les `champs` extraits et le `sort_final`, directement joignables au tableau de
gestion.

## Convention de nommage (résumé)

```
AAAA-MM-JJ_Type_Tiers_Objet.ext

2026-03-15_Contrat_Client-Alpha_Refonte-site_signe.pdf
2026-04-02_Facture_Hebergeur-Alpha_Hebergement-mars_35.88.pdf
2026-06-30_PV-AGO_Approbation-comptes-2025.pdf
```

Date du document en tête (tri chronologique automatique), type en un mot, nom stable du tiers, objet court.
Tous les exemples de ce dépôt utilisent des noms fictifs (`Client Alpha`, `Banque Alpha`, `NOM-Prenom`…) :
aucune entreprise, banque ou personne réelle n'y est citée, en dehors des organismes publics et des dispositifs
officiels (URSSAF, INPI, Bpifrance, OPCO…) mentionnés au titre de la réglementation.
Pas d'accent ni de caractère spécial dans les noms de fichiers. Les dossiers par année s'écrivent `AAAA`, par
mois `AAAA-MM`. Le détail est dans [`Convention-de-nommage.md`](97%20-%20REFERENTIEL/Convention-de-nommage.md).

## Durées de conservation

Chaque `index.md` donne la durée **minimale légale** et une durée **recommandée** (souvent plus longue, alignée
sur les 10 ans de la comptabilité), avec l'article de référence. Le tableau complet est dans
[`Durees-de-conservation.md`](97%20-%20REFERENTIEL/Durees-de-conservation.md). Quelques repères :

| Documents | Minimum légal |
|---|---|
| Pièces et livres comptables | 10 ans après la clôture |
| Déclarations fiscales | 10 ans (6 ans avant la loi du 25 juin 2026) |
| Contrats commerciaux | 5 ans après la fin |
| Bulletins de paie, contrats de travail | 5 ans (après le départ pour le contrat) |
| DUERP | 40 ans |
| Candidatures non retenues | 5 ans à compter du pourvoi du poste |
| Statuts, PV d'AG, registres | 5 ans après la radiation — en pratique, toujours |
| Contrats d'assurance | 2 ans après la fin (10 ans recommandés pour la RC) |
| Avis d'achat de titres, historique crypto | 10 ans — et jamais purgés tant que la ligne est détenue |
| Assurance décennale, PV de réception | 10 ans après la réception du chantier |

## Adapter le gabarit à votre entreprise

- **Supprimer** ou laisser vides les dossiers qui ne vous concernent pas (`03.10` sans CSE, `07.4` sans
  véhicule, `08.5` sans crypto-actifs, `05.4` sans investisseurs…). Leur `index.md` explique à partir de quand
  ils deviennent nécessaires.
- **Ne pas renommer** les dossiers de niveau 1 et 2 : tous les `index.md` s'y réfèrent par leur numéro.
- **Ajouter** des sous-dossiers de niveau 3 librement (par tiers, par année, par opération) selon les règles de
  chaque `index.md`.
- **Ajouter un domaine** en prenant un numéro libre entre `09` et `96`, sans toucher aux autres.
- **Restreindre les accès** : `03 - RESSOURCES HUMAINES` contient des données personnelles et de santé, `04`,
  `05` et `08` révèlent la trésorerie et le patrimoine ; ces dossiers doivent avoir leurs propres droits si le
  stockage est partagé. La grille d'accès proposée est dans [`index.md`](index.md).
- **Ne jamais versionner de documents réels** dans un dépôt Git public : si vous forkez ce dépôt pour l'utiliser,
  ajoutez un `.gitignore` qui n'autorise que les `*.md` et les `*.csv` de gabarit, ou travaillez hors Git. Aucun
  secret (mot de passe, clé privée, phrase de récupération) n'a sa place dans cette arborescence, même privée.

## Contribuer

Les corrections et compléments sont bienvenus, en particulier sur les durées de conservation (qui évoluent avec
les textes) et sur les cas particuliers (secteurs réglementés, associations, professions libérales).
Ouvrez une *issue* ou une *pull request* en précisant la source (article de code, fiche service-public.fr, doctrine).

## Avertissement

Ce gabarit est une aide à l'organisation, pas un conseil juridique, comptable ou fiscal. Les durées de
conservation et les règles citées correspondent aux textes en vigueur à la date de rédaction (septembre 2026)
et sont données à titre indicatif ; vérifiez-les pour votre situation, notamment auprès de votre expert-comptable
ou de votre avocat, et consultez le simulateur officiel « Combien de temps une entreprise doit conserver ses
documents » sur service-public.gouv.fr.

Le fichier [`AUDIT-CONFORMITE-2026-09.md`](AUDIT-CONFORMITE-2026-09.md) documente la confrontation du gabarit
aux sources officielles, avec les références de chaque durée, les points vérifiés et ceux qui restent à
confirmer. Deux réserves y sont signalées et méritent d'être connues : l'allongement du délai fiscal de 6 à
10 ans est récent et sa date d'entrée en vigueur fait l'objet de sources divergentes, et la CNIL est en
contradiction avec elle-même sur la durée de conservation des candidatures.

## Licence

À définir par l'auteur — suggestion : [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.fr)
(réutilisation et adaptation libres, avec mention de la source), adaptée à un contenu documentaire.
