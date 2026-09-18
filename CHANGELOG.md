# Changelog

Toutes les évolutions notables de ce plan de classement sont consignées ici.

Le format suit [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/) et le versionnage suit
[SemVer](https://semver.org/lang/fr/) : une version majeure signale un changement d'arborescence qui
oblige à renommer ou déplacer des dossiers existants.

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
