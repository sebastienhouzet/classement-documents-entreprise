# Convention de nommage

## Fichiers

Format unique : **`AAAA-MM-JJ_Type_Tiers_Objet.ext`**

| Élément | Règle | Exemples |
|---|---|---|
| `AAAA-MM-JJ` | Date du document (date de signature, d'émission ou de facture — pas la date de scan). Si seul le mois est connu : `AAAA-MM`. | `2026-03-15` |
| `Type` | Nature du document, en un mot, toujours le même | `Contrat`, `Avenant`, `Devis`, `Facture`, `Avoir`, `PV-AGO`, `Statuts`, `Attestation`, `Releve`, `Bulletin`, `LRAR`, `NDA`, `Bail`, `Kbis`, `DSN`, `CA3` |
| `Tiers` | Nom stable du client, fournisseur, salarié, organisme (le même que le nom de son dossier) | `Peps-Home`, `URSSAF`, `DUPONT-Jean`, `Credit-Agricole` |
| `Objet` | Précision utile, courte ; numéro de pièce quand il existe | `Refonte-site`, `F2026-0042`, `Approbation-comptes-2025`, `Mars` |
| `.ext` | PDF pour tout ce qui est figé ; le format natif (docx, xlsx) uniquement pour les fichiers vivants | |

Exemples complets :

- `2026-03-15_Contrat_Peps-Home_Refonte-site_signe.pdf`
- `2026-04-02_Facture_OVH_Hebergement-mars_35.88.pdf`
- `2026-06-30_PV-AGO_Approbation-comptes-2025.pdf`
- `2026-03_Bulletins.pdf` (dans `03.3 - Paie/2026/2026-03/`)
- `2026-01_Releve.pdf` (dans `05.1/Qonto - Compte courant/Releves/2026/`)

## Règles d'écriture

- Pas d'accent ni de caractère spécial dans les noms de fichiers (`é` → `e`, `&` → `et`) : cela évite les problèmes de synchronisation et de recherche. Les noms de **dossiers** de premier et second niveau font exception (ils sont fixes).
- Les espaces sont remplacés par des tirets `-` à l'intérieur d'un élément, et les éléments sont séparés par `_`.
- Suffixes utiles en fin de nom : `_signe` (version signée), `_v2` (version), `_copie` (copie d'un original rangé ailleurs), `_projet` (non signé).
- Une version signée remplace la version projet : ne garder le projet que s'il a une valeur (négociation).

## Dossiers

- **Dossiers fixes** (niveaux 1 et 2) : ne pas les renommer, l'ensemble des `index.md` y fait référence.
- **Dossiers par tiers** : `Nom du tiers` tel qu'il apparaît sur les contrats, sans forme juridique (`Peps Home`, pas `SAS Peps Home`). Un salarié : `NOM Prénom`.
- **Dossiers par année** : `AAAA` ; par mois : `AAAA-MM` (jamais `Mars 2026`, qui ne se trie pas).
- **Dossiers par opération ou affaire** : `AAAA-MM-JJ - Objet` ou `AAAA - Contrepartie - Objet`.
- **Dossiers clos** : ajouter `[CLOS]` ou `[détruire AAAA]` en fin de nom.

## Fichiers vivants

Certains fichiers sont mis à jour en continu (registres, tables de capitalisation, inventaires). Ils gardent un nom
sans date (`Registre-des-contrats.csv`) et on exporte une version figée datée (`Registre-des-contrats_2026-12-31.pdf`)
à chaque étape importante (clôture, contrôle, cession).
