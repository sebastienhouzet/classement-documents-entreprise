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
2. **Lire trois fichiers** (10 minutes) :
   - [`index.md`](index.md) — le guide de classement : le cycle de vie d'un document, les règles, la routine, les accès ;
   - [`97 - REFERENTIEL/Convention-de-nommage.md`](97%20-%20REFERENTIEL/Convention-de-nommage.md) — comment nommer fichiers et dossiers ;
   - [`97 - REFERENTIEL/Durees-de-conservation.md`](97%20-%20REFERENTIEL/Durees-de-conservation.md) — le tableau des durées légales et recommandées.
3. **Remplir les registres CSV** avec l'existant (contrats, assurances, placements, matériel) : ce sont eux qui
   donnent la vue d'ensemble et les dates d'échéance.
4. **Ranger au fil de l'eau** : déposer les documents entrants dans `00 - INBOX`, puis les traiter par lot. En cas
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
├── 00 - INBOX/                        ← sas d'entrée : tout document reçu, en attente de classement
├── 01 - JURIDIQUE & GOUVERNANCE/      ← constitution, statuts, AG, registres, dirigeants, associés, PI, conformité, contentieux
├── 02 - CONTRATS/                     ← clients, fournisseurs, sous-traitance, baux, abonnements, NDA, modèles
├── 03 - RESSOURCES HUMAINES/          ← registres, dossiers salariés, paie, organismes sociaux, recrutement, formation, absences, santé-sécurité, CSE
├── 04 - COMPTABILITE & FISCALITE/     ← exercices, factures, notes de frais, immobilisations, impôts, expert-comptable, budget
├── 05 - BANQUE & FINANCEMENT/         ← comptes, emprunts, aides, investisseurs, moyens de paiement, garanties (l'argent qui entre)
├── 06 - ASSURANCES/                   ← un dossier par type de contrat, sinistres
├── 07 - ADMINISTRATIF & ORGANISMES/   ← administrations, courrier, locaux, véhicules, certifications, matériel
├── 08 - PLACEMENTS & PARTICIPATIONS/  ← comptes à terme, titres, capitalisation, crypto-actifs, SCPI, fonds, filiales (l'argent qui est placé)
├── 97 - REFERENTIEL/                  ← convention de nommage, durées de conservation, kit administratif
├── 98 - ARCHIVES/                     ← dossiers clos en attente de destruction
└── 99 - SUPPRESSION/                  ← lots proposés à la suppression, en attente de validation
```

Chaque domaine est découpé en sous-dossiers numérotés (`01.1`, `01.2`…), soit **75 dossiers** au total.
L'arborescence complète, avec le contenu de chaque sous-dossier, est décrite dans [`index.md`](index.md).

Les numéros `09` à `96` sont volontairement laissés libres : un nouveau domaine métier s'insère sans renuméroter
l'existant ni casser les renvois entre dossiers. La bande `97` à `99` est réservée aux dossiers système.

### Les trois logiques de classement

| Logique | Où | Exemple |
|---|---|---|
| **Par tiers** | Clients, fournisseurs, salariés, contrats d'assurance, comptes bancaires, lignes de placement | `02.1 - Clients/Peps Home/` |
| **Par année, puis par mois** | Factures, relevés, paie, notes de frais, courrier | `04.3 - Factures fournisseurs/2026/2026-03/` |
| **Par opération ou affaire** | AG, modifications statutaires, litiges, sinistres, prêts, levées de fonds, lots de suppression | `01.9 - Contentieux/2026 - SAS Dupont - Impayé/` |

Un document n'a qu'**une seule place**. Quand il est utile ailleurs, on y met une copie nommée `_copie` ou un
simple renvoi ; chaque `index.md` indique, dans sa section « Ne pas ranger ici », où va ce qui n'y a pas sa place.

## Anatomie d'un `index.md`

Chaque dossier contient un `index.md` construit sur le même modèle :

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

## Les registres

Sept fichiers CSV vides (séparateur `;`, encodage UTF-8, ouvrables dans Excel, Numbers ou LibreOffice) servent de
vue d'ensemble là où les dossiers ne suffisent pas :

| Registre | Emplacement | À quoi il sert |
|---|---|---|
| `Registre-des-contrats.csv` | `02 - CONTRATS/` | Échéances, préavis, dates limites de résiliation |
| `Registre-des-immobilisations.csv` | `04.5 - Immobilisations/` | Biens durables, amortissements, sorties |
| `Registre-des-assurances.csv` | `06 - ASSURANCES/` | Garanties, plafonds, franchises, échéances |
| `Registre-des-recommandes.csv` | `07.2 - Courrier/` | Preuves d'envoi et de réception des LRAR |
| `Inventaire-du-materiel.csv` | `07.6 - Matériel & inventaire/` | Qui a quoi, numéros de série, restitutions |
| `Registre-des-placements.csv` | `08 - PLACEMENTS & PARTICIPATIONS/` | Lignes détenues, prix de revient, échéances, valeur à la dernière clôture |
| `Registre-des-archives.csv` | `98 - ARCHIVES/` | Dossiers clos et **dates de destruction prévues** |

## Convention de nommage (résumé)

```
AAAA-MM-JJ_Type_Tiers_Objet.ext

2026-03-15_Contrat_Peps-Home_Refonte-site_signe.pdf
2026-04-02_Facture_OVH_Hebergement-mars_35.88.pdf
2026-06-30_PV-AGO_Approbation-comptes-2025.pdf
```

Date du document en tête (tri chronologique automatique), type en un mot, nom stable du tiers, objet court.
Pas d'accent ni de caractère spécial dans les noms de fichiers. Les dossiers par année s'écrivent `AAAA`, par
mois `AAAA-MM`. Le détail est dans [`Convention-de-nommage.md`](97%20-%20REFERENTIEL/Convention-de-nommage.md).

## Durées de conservation

Chaque `index.md` donne la durée **minimale légale** et une durée **recommandée** (souvent plus longue, alignée
sur les 10 ans de la comptabilité), avec l'article de référence. Le tableau complet est dans
[`Durees-de-conservation.md`](97%20-%20REFERENTIEL/Durees-de-conservation.md). Quelques repères :

| Documents | Minimum légal |
|---|---|
| Pièces et livres comptables | 10 ans après la clôture |
| Déclarations fiscales | 6 ans |
| Contrats commerciaux | 5 ans après la fin |
| Bulletins de paie, contrats de travail | 5 ans (après le départ pour le contrat) |
| DUERP | 40 ans |
| Candidatures non retenues | 2 ans maximum |
| Statuts, PV d'AG, registres | 5 ans après la radiation — en pratique, toujours |
| Contrats d'assurance | 2 ans après la fin (10 ans recommandés pour la RC) |
| Avis d'achat de titres, historique crypto | 10 ans — et jamais purgés tant que la ligne est détenue |

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
ou de votre avocat, et consultez la fiche officielle « Durée de conservation des documents d'une entreprise »
sur service-public.fr, mise à jour régulièrement.

## Licence

À définir par l'auteur — suggestion : [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.fr)
(réutilisation et adaptation libres, avec mention de la source), adaptée à un contenu documentaire.
