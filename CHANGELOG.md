# Changelog

Toutes les évolutions notables de ce plan de classement sont consignées ici.

Le format suit [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/) et le versionnage suit
[SemVer](https://semver.org/lang/fr/) : une version majeure signale un changement d'arborescence qui
oblige à renommer ou déplacer des dossiers existants.

## [2.1.0] — 2026-09-21

Mise en conformité du gabarit à la suite d'un audit mené contre les sources officielles françaises
(service-public, BOFiP, CNIL, ANSSI, AFNOR, France Archives). Le détail, avec les références de chaque point
et les réserves de vérification, est dans `AUDIT-CONFORMITE-2026-09.md`.

Aucun changement d'arborescence incompatible : les domaines et sous-dossiers existants gardent leurs numéros.

### Corrigé — durées de conservation devenues fausses

- **Candidatures non retenues : 2 ans → 5 ans à compter du pourvoi du poste.** C'est la correction la plus
  importante de cette version : le gabarit conseillait de détruire des pièces qui servent à se défendre d'une
  action en discrimination. Le délai de 2 ans ne vaut plus que pour la CV-thèque, à compter du dernier contact
  (Code du travail art. L1134-5 ; référentiel CNIL du 2 avril 2026, qui en fait une obligation).
- **Charges sociales et DSN : 3 ans → 6 ans.** Les 3 ans correspondent à la prescription du recouvrement URSSAF
  (art. L244-3 CSS) ; la conservation pour le *contrôle* relève de l'art. L243-16 CSS.
- **Documents fiscaux : 6 ans → 10 ans** (art. 36 de la loi n° 2026-534 du 25 juin 2026, modifiant l'art. L102 B
  du LPF). Sans effet pratique pour qui suivait déjà la recommandation de 10 ans de ce gabarit.
- **Bulletin de paie : ajout de la seconde durée.** 5 ans pour le double conservé par l'employeur (L3243-4),
  **50 ans ou jusqu'aux 75 ans du salarié** pour la mise à disposition du bulletin électronique (D3243-8).
- **Sinistre corporel : 10 ans à compter de la consolidation du dommage** (Code civil art. 2226).

### Corrigé — qualifications erronées

- Le « registre des conventions réglementées » **n'existe pas** : aucun texte ne l'impose en SAS ni en SARL.
  L'obligation est le *rapport* présenté à l'assemblée d'approbation des comptes. La mention a été retirée de
  `01.4` et remplacée par un renvoi.
- Le « registre des demandes d'exercice des droits » n'est pas davantage un registre légal nommé : c'est une
  preuve d'*accountability* au sens des art. 5.2 et 24 du RGPD. Requalifié dans `01.8`.
- Le tri des déchets se fait désormais à **8 flux** et non 7 : les huiles alimentaires usagées ont été ajoutées.

### Ajouté — trois sous-dossiers

- **`04.9 - Facturation électronique & piste d'audit fiable`** — contrat de plateforme agréée et sa durée de
  rétention contractuelle, identifiants de routage, statuts de cycle de vie des factures, preuves de
  e-reporting, et surtout la **documentation de la piste d'audit fiable**, obligatoire au titre de l'art. 289
  VII 1° du CGI et dont l'absence expose à un refus de déduction de la TVA. Le dossier rappelle que la
  conservation reste la responsabilité de l'entreprise, pas celle de la plateforme.
- **`06.8 - Décennale & garanties de construction`** — assurance décennale et activités déclarées, PV de
  réception (qui fait courir le délai décennal), garanties de parfait achèvement et biennale, DOE, DIUO,
  vigilance des sous-traitants. Dossier conditionnel : sans activité de travaux, il reste vide.
- **`07.7 - Marchés publics`** — dossier permanent de candidature (DC1, DC2, DUME, mémoire technique,
  certificats de capacité) et suivi par consultation.

### Ajouté — documents obligatoires qui n'avaient pas de place

- `03.1` : registre des vérifications des installations électriques, registre des dangers graves et imminents,
  registre des alertes en matière de santé publique et d'environnement, registre spécial du repos hebdomadaire,
  tableau du travail en équipes, registre des travailleurs à domicile, PAPRIPACT.
- `03.1` : **sanctions administratives DUERP** instaurées par l'art. 48 de la loi du 25 juin 2026 — jusqu'à
  4 000 € par travailleur, doublés en récidive — et précision du seuil de **11 salariés** à partir duquel la
  mise à jour annuelle devient obligatoire. Mention de l'art. L4711-5, qui autorise le regroupement des
  registres en un registre unique.
- `03.10` : registre des questions du CSE (11 à 49 salariés), seul registre consultable par les salariés.
- `07.3` : registre public d'accessibilité (tout ERP), attestation annuelle de valorisation des déchets,
  registre de suivi des déchets, déclaration **OPERAT** pour les locaux tertiaires de 1 000 m² et plus, y
  compris en location.
- `07.5` : déclaration d'activité et **bilan pédagogique et financier** des organismes de formation.
- `01.8` : **accessibilité numérique** (seuil d'exemption à 10 salariés seulement), **médiateur de la
  consommation**, et **règlement européen sur l'IA** — inventaire des systèmes, charte d'usage, littératie.

### Ajouté — référentiel et méthode

- **`97 - REFERENTIEL/Tableau-de-gestion.csv`** — l'outil qui manquait : une ligne par typologie documentaire
  avec producteur, durée d'utilité administrative, **sort final** (conserver / détruire / trier) et référence
  juridique. Prérempli avec 27 typologies. C'est lui qui rend `99 - SUPPRESSION` utilisable, et il tient lieu
  de référentiel des durées au sens du RGPD.
- **`97 - REFERENTIEL/Numerisation-et-valeur-probante.md`** — les conditions réelles de la copie fiable
  (empreinte, horodatage, procédé documenté), le régime particulier des factures, la liste des originaux à ne
  jamais détruire, et le rappel qu'aucune norme d'archivage n'est obligatoire pour une PME.
- **`97 - REFERENTIEL/Securite-et-sauvegarde.md`** — règle 3-2-1 avec copie hors ligne, chiffrement, test de
  restauration annuel, droits d'accès et journalisation, formats pérennes, destruction sécurisée.
- `98 - ARCHIVES` : droits d'accès explicitement plus restrictifs que les dossiers courants, avec
  journalisation — ce que le RGPD exige de l'archivage intermédiaire.
- Guide racine : section sur la sécurité, et encadré « ce qui ne vous concerne probablement pas » (CSRD, devoir
  de vigilance, bilan GES, NIS2) avec le **plafond VSME** opposable aux donneurs d'ordre.

## [2.0.0] — 2026-09-18

Ajout de trois dossiers de niveau 1, dont un domaine métier complet sur les placements financiers, et
réorganisation de la numérotation pour séparer les dossiers métier des dossiers système.

### Changements incompatibles

- `00 - REFERENTIEL` devient `97 - REFERENTIEL`.
- `08 - ARCHIVES` devient `98 - ARCHIVES`.

La logique est désormais : `00 - INBOX` en tête, les huit domaines métier de `01` à `08`, puis la bande
système `97` / `98` / `99`. Les numéros `09` à `96` restent libres, ce qui permet d'insérer un futur domaine
sans renuméroter l'existant ni casser les renvois entre dossiers.

### Ajouté

- **`08 - PLACEMENTS & PARTICIPATIONS`** — nouveau domaine métier couvrant ce que l'entreprise fait de sa
  trésorerie, là où `05` ne traitait que l'argent qui entre. Neuf sous-dossiers : politique de placement et
  décisions (`08.1`), placements bancaires CAT et DAT (`08.2`), comptes-titres et valeurs mobilières (`08.3`),
  contrats de capitalisation (`08.4`), crypto-actifs (`08.5`), immobilier de placement et SCPI (`08.6`), non
  coté et private equity (`08.7`), participations et filiales (`08.8`), valorisations et états annuels (`08.9`).
  Principe : une ligne de placement égale un sous-dossier, de la souscription à la sortie.
- **`00 - INBOX`** — sas d'entrée unique pour tout document reçu et non encore classé. Règle : zéro document
  de plus de 30 jours. Trois sous-dossiers seulement (`A classer`, `A traiter`, `Scans bruts`) et aucune
  structure par tiers ou par année.
- **`99 - SUPPRESSION`** — sas de sortie, par lots datés accompagnés d'une `Proposition-de-suppression.md`,
  avec un délai de grâce de 30 jours et la règle « personne ne supprime seul » : une personne propose, une
  autre valide.
- `Registre-des-placements.csv` — septième registre, à la racine de `08`.
- Section « Placements et participations » dans `97 - REFERENTIEL/Durees-de-conservation.md`.
- Section « Le cycle de vie d'un document » dans le `README.md` et le guide racine.

### Points réglementaires intégrés

- **Crypto-actifs** (`08.5`) : le règlement ANC 2026-01 remplace le règlement ANC 2018-07 et devient
  obligatoire pour les exercices ouverts à compter du 1er janvier 2027, avec application anticipée possible
  (évaluation à la valeur vénale à chaque clôture, écarts latents en comptes d'attente, premier entré-premier
  sorti ou coût moyen pondéré, mentions en annexe).
- **Prestataires crypto** (`08.5`) : le régime PSAN a pris fin le 1er juillet 2026 au profit de l'agrément
  européen MiCA ; la preuve de l'agrément du prestataire fait désormais partie du dossier.
- **Comptes à l'étranger** (`04.6`, `08.5`) : les sociétés commerciales (SAS, SARL, SA) ne sont pas soumises
  au formulaire 3916-bis pour les comptes d'actifs numériques ouverts à l'étranger, contrairement aux sociétés
  civiles, aux associations et aux GIE — l'article 1649 A du CGI les exclut explicitement.

### Modifié

- Les 76 `index.md` ont été régénérés pour que tous les renvois croisés restent justes après la renumérotation.
- `98 - ARCHIVES` ne supprime plus directement : la destruction passe par `99 - SUPPRESSION`.
- Nouveaux renvois entre domaines : `01.6` vers `08.8` (capital de votre société contre titres détenus dans
  d'autres), `04.5` vers `08` (immobilisations corporelles contre financières), `04.6` vers `08.9`
  (déclarations contre calculs de plus-values), `05` et `05.1` vers `08` (argent qui entre contre argent placé).
- `README.md` et `index.md` : arborescence, grille d'accès et routine annuelle mises à jour.

### Confidentialité

- Tous les exemples utilisent désormais des noms fictifs et cohérents (`Client Alpha`, `Client Beta`,
  `Banque Alpha`, `Fournisseur Alpha`, `Hebergeur-Alpha`, `PSP Alpha`, `Plateforme Alpha`, `NOM-Prenom`,
  `AA-123-AA`). Plus aucune entreprise, banque, plateforme, marque commerciale ni adresse réelle n'est citée
  en exemple. Seuls subsistent les organismes publics et les dispositifs officiels (URSSAF, INPI, Bpifrance,
  OPCO, CNIL, AMF…), mentionnés au titre de la réglementation et non comme exemples de choix commerciaux.
- La correction a été faite dans le générateur du gabarit et non seulement dans les fichiers produits, afin
  qu'une régénération ne puisse plus réintroduire de noms réels.

### Migration depuis la 1.0.0

1. Renommer `00 - REFERENTIEL` en `97 - REFERENTIEL` et `08 - ARCHIVES` en `98 - ARCHIVES`.
2. Créer `00 - INBOX`, `08 - PLACEMENTS & PARTICIPATIONS` et `99 - SUPPRESSION` à partir de cette version.
3. Remplacer les `index.md` existants par ceux de cette version : les renvois internes y sont déjà à jour.

Aucun document n'est déplacé par cette version : les domaines `01` à `07` et leurs sous-dossiers sont inchangés.

## [1.0.0] — 2026-09-09

Première version publiée du plan de classement.

### Ajouté

- Arborescence complète des documents de gestion d'une entreprise française : `00 - REFERENTIEL`, puis sept
  domaines métier — juridique et gouvernance (`01`), contrats (`02`), ressources humaines (`03`), comptabilité
  et fiscalité (`04`), banque et financement (`05`), assurances (`06`), administratif et organismes (`07`) —
  et `08 - ARCHIVES`.
- Un `index.md` par dossier, construit sur un modèle unique : à quoi sert le dossier, documents à y ranger,
  ce qui va ailleurs, méthode de classement, durée de conservation légale et recommandée avec la base
  juridique, conseils pratiques.
- `Convention-de-nommage.md` : format unique `AAAA-MM-JJ_Type_Tiers_Objet.ext` pour les fichiers, règles de
  nommage des dossiers par tiers, par année et par opération.
- `Durees-de-conservation.md` : tableau des durées minimales légales et recommandées par famille de documents,
  avec les sources (Code de commerce, Livre des procédures fiscales, Code du travail, Code des assurances,
  Code civil, référentiel CNIL).
- Six registres CSV : contrats, immobilisations, assurances, recommandés, matériel, archives.
- Kit administratif : les justificatifs à jour à fournir régulièrement (Kbis, attestations URSSAF et fiscale,
  RC Pro, RIB…).
- `README.md` et guide de classement racine : règles, logiques de classement, grille d'accès, routine.
