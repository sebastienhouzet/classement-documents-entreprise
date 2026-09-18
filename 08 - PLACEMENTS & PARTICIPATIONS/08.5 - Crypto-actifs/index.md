# 08.5 - Crypto-actifs

> Chemin : `08 - PLACEMENTS & PARTICIPATIONS/08.5 - Crypto-actifs`

## À quoi sert ce dossier

Les actifs numériques détenus par l'entreprise : bitcoin, ether, stablecoins, jetons. C'est le dossier le plus exigeant du domaine, pour deux raisons. La traçabilité repose sur des exports de plateformes qui peuvent fermer ou supprimer l'historique, et le cadre comptable français vient de changer : le règlement ANC 2026-01 remplace le règlement ANC 2018-07 et s'applique obligatoirement aux exercices ouverts à compter du 1er janvier 2027, avec application anticipée possible.

## Documents à y ranger

- **Vérification du prestataire** : preuve de son agrément MiCA (prestataire de services sur crypto-actifs), consultée sur le registre de l'AMF ou de l'ESMA, avec la date de consultation — le régime PSAN a pris fin le 1er juillet 2026 et a été remplacé par l'agrément européen
- Contrat et conditions générales de la plateforme, dossier KYC constitué au nom de la société, grille de frais
- **Historique complet des transactions** : export CSV ou API de chaque plateforme, au minimum à chaque clôture et à chaque changement de prestataire — achats, ventes, échanges, frais, transferts entre portefeuilles, staking, airdrops
- Justificatifs d'acquisition : avis d'exécution, relevés bancaires correspondants (renvoi `05.1`), preuve de l'origine des fonds
- `Inventaire-des-portefeuilles.md` : pour chaque portefeuille, son type (plateforme ou auto-hébergé), son adresse publique, les actifs détenus et qui y a accès
- Valorisation à la clôture : cours retenus, **source du cours et horodatage**, méthode appliquée — le règlement impose une évaluation à la valeur vénale à chaque clôture, les écarts latents transitant par des comptes d'attente
- Méthode de calcul du prix de revient retenue et appliquée de façon constante : premier entré-premier sorti ou coût unitaire moyen pondéré
- Éléments exigés pour l'annexe : méthode de valorisation, sources des cours, intention de détention, actifs nantis ou prêtés
- Note de l'expert-comptable sur le traitement retenu ; décision d'investir (copie — original dans `08.1`)
- Sécurité : procédure d'accès et de transmission des accès, en indiquant **où** sont conservés les moyens d'authentification, jamais lesquels
- Incident : perte de clés, piratage, défaillance de la plateforme — plainte, déclarations, échanges

## Ne pas ranger ici

- **Phrases de récupération, clés privées, mots de passe, codes d'authentification : jamais dans ce dossier, ni dans aucun dossier synchronisé.** Ils vont dans un gestionnaire de mots de passe ou sur un support hors ligne ; ce dossier n'indique que l'endroit où ils sont conservés
- Crypto-actifs détenus personnellement par le dirigeant → hors de ce classement (patrimoine privé)
- Factures d'achat de matériel → `04.3` et `04.5`
- Assurance cyber et sinistre → `06.5` et `06.7`

## Méthode de classement

**Un sous-dossier par prestataire ou portefeuille** (`Coinbase`, `Kraken`, `Ledger - portefeuille froid`), puis `Contrat et KYC`, `Exports/AAAA` (un export daté par trimestre, au minimum un par clôture), `Cloture/AAAA` (valorisation, cours retenus, calculs). Un sous-dossier `Consolidation/AAAA` à la racine réunit l'inventaire global et le calcul consolidé de l'exercice.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Pièces comptables : 10 ans à compter de la clôture de l'exercice. Documents fiscaux : 6 ans (délai de reprise porté à 10 ans en cas d'activité occulte). |
| **Recommandé** | **Historique complet conservé sans purge tant que des actifs sont détenus**, puis 10 ans après la cession totale. Une ligne achetée en 2021 et vendue en 2031 impose de produire en 2031 le justificatif de 2021 : aucune plateforme ne le garantit, c'est à l'entreprise de le conserver. |

Base : Règlement ANC 2026-01 (obligatoire pour les exercices ouverts à compter du 1er janvier 2027, application anticipée possible ; remplace le règlement ANC 2018-07) ; règlement européen MiCA ; Code de commerce art. L.123-22 ; LPF art. L.102 B.

## Conseils

- Exporter l'historique **avant** de fermer un compte ou de changer de plateforme : après, la reconstitution est impossible ou coûteuse.
- Une société à l'IS ne relève pas du régime des particuliers : les gains sont imposés à l'IS et l'évaluation à la valeur vénale en clôture peut faire apparaître des écarts latents. Le traitement exact se cale avec l'expert-comptable et se documente ici chaque année.
- Les sociétés **commerciales** (SAS, SARL, SA) ne sont pas soumises à la déclaration des comptes d'actifs numériques ouverts à l'étranger ; les sociétés civiles, les associations et les GIE le sont (formulaire 3916-bis). À vérifier selon votre forme juridique.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
