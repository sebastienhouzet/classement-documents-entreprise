# Routage d'un document entrant — référence pour agent

Table de décision pour un agent qui doit classer un document dans ce plan de classement :
69 destinations, leurs déclencheurs et leurs arbitrages.

**Deux façons de l'utiliser.** Soit charger ce fichier en entier, une fois, en préfixe stable du
prompt — c'est le plus simple et le cache de prompt absorbe le coût après le premier appel. Soit
procéder en deux temps : ne charger que les sections « Procédure », « Aiguillage » et « Sortie
attendue », puis, le domaine choisi, ne charger que le bloc de ce domaine dans la section « Table ».
Le second mode divise le coût par environ six, au prix d'un aller-retour.

Ne lire le `index.md` d'un dossier que si la table ne suffit pas à trancher. C'est l'exception.

**Deux fichiers complètent celui-ci**, et se lisent par fragments plutôt qu'en entier :
`referentiel/dossiers.json` (compilé des en-têtes YAML des 78 `index.md`) donne, dossier par dossier,
les typologies documentaires, les champs à extraire, les gabarits de nom et les durées — c'est ce
qu'on lit à l'étape 6, pour un seul identifiant ; `97 - REFERENTIEL/champs.yaml` définit chaque champ
une fois pour toutes, avec son type et son format attendus. L'en-tête de chaque `index.md` porte les
mêmes données au plus près du dossier.

## Procédure

1. **Identifier le type de document**, pas son sujet. Une facture d'avocat est une facture (`04.3`),
   pas un document juridique. Un relevé de compte à terme est un placement (`08.2`), pas un document
   bancaire courant.
2. **Aiguiller vers un domaine** avec la table d'aiguillage ci-dessous.
3. **Chercher les déclencheurs** dans la colonne `cles` des destinations de ce domaine.
4. **Appliquer les arbitrages** de la colonne `arb` quand plusieurs destinations matchent. Ils sont
   écrits pour trancher exactement ces cas. La section « Pièges » couvre les confusions coûteuses.
5. **Construire le chemin** : `<dossier de tête>/<code> - <nom>/` + le motif de la colonne `chemin`,
   en remplaçant les variables par ce que dit le document (tiers, année, mois, objet).
   **Si une variable du motif est absente du document**, le dossier reste le bon : écrire `_INCONNU`
   à sa place dans le chemin, `INCONNU` sans tiret bas dans le nom de fichier (le tiret bas y sépare
   les segments), plafonner la confiance à 0,70 et ajouter `variable de chemin manquante : <nom>` à
   `actions`. Ne pas router en `00` pour cette seule raison : `00` est réservé au type de document
   non reconnu et aux destinations ex æquo. Ne jamais inventer un nom de tiers, de banque ou
   d'assureur qui n'est pas écrit sur le document : c'est ainsi qu'un même assureur finit sous trois
   orthographes. Une donnée que le document permet de **calculer** sans ambiguïté — une échéance à
   partir d'une date de signature et d'une durée écrite — se calcule ; l'interdiction porte sur ce
   qui s'invente, pas sur ce qui se déduit.
6. **Qualifier la typologie** en lisant `referentiel/dossiers.json` au seul identifiant retenu :
   `dossiers[<id>].documents` liste les types de ce dossier, chacun avec sa clé `type`, ses `indices`,
   les `champs` à extraire, son gabarit `nommage` et sa `conservation`. Renvoyer cette clé dans
   `type`, et les champs lus dans `champs`. Si aucun type ne correspond, laisser `type` à `null` et
   plafonner la confiance à 0,65 : le dossier est probablement bon, la pièce est inhabituelle.
   Un champ de la liste que le document ne porte pas vaut `null` — jamais `_INCONNU`, qui est
   réservé aux chemins et aux noms de fichiers, et jamais `0`. `champs.yaml` donne le type et le
   format attendus de chaque champ : un montant est un nombre, une date s'écrit `AAAA-MM-JJ`, une
   période `AAAA-MM`. Cette lecture ne porte que sur un dossier, pas sur le gabarit entier.
7. **Nommer le fichier** avec le gabarit `nommage` du type retenu à l'étape 6, qui fait foi — il
   compte deux, trois ou quatre segments selon la pièce et commence par `{date}`, `{periode}` ou
   `{exercice}`. Sans type reconnu, appliquer la convention générale `AAAA-MM-JJ_Type_Tiers_Objet`.
   Dans les deux cas : pas d'accent ni de caractère spécial, pas de point hors extension, le tiret
   bas sépare les segments. Suffixes utiles : `_signe`, `_copie`, `_projet`.
   **Si le document ne porte pas de date propre**, utiliser la date de l'événement qu'il atteste
   (période couverte, début de validité, date de l'opération) ; à défaut seulement, la date à
   laquelle nous l'avons reçu, préfixée `r` (`r2026-10-02_...`). La date du scan n'est jamais la date
   du document, sauf en `00` où elle est la seule disponible.
8. **Si la confiance est inférieure à 0,7, router vers `00`** avec le motif du doute. Un document mal
   classé coûte plus cher qu'un document resté dans le sas.

### Barème de confiance

| Valeur | Situation |
|---|---|
| 0,95 | Déclencheur littéral, une seule destination possible, toutes les variables du chemin lues |
| 0,85 | Déclencheur littéral et un arbitrage écrit qui tranche |
| 0,70 | Déclencheur reconnu par synonyme, ou dossier certain mais une variable de chemin manquante, ou aucune typologie du dossier ne correspond à la pièce |
| < 0,70 | Deux destinations plausibles sans arbitrage écrit, ou type de document non reconnu — seuls ces deux cas partent en `00` |

## Règles invariantes

- Un document n'a qu'**une seule place**. S'il est utile ailleurs, l'original va à sa place et une
  copie suffixée `_copie` va dans l'autre dossier.
- Un fichier = un document. Un scan qui contient plusieurs documents distincts va en `00`, à
  découper avant classement.
- Les sous-dossiers par tiers, par année ou par opération se **créent à la demande** : si le
  sous-dossier cible n'existe pas, le créer selon le motif.
- **Un avenant, une résiliation, un renouvellement, une mainlevée ou un ordre de mouvement va dans
  le dossier du document qu'il modifie**, jamais dans un dossier à lui.
- **Une attestation, une pièce de vigilance ou un certificat fourni par un tiers va dans le dossier
  de ce tiers**, à la destination où son contrat est classé. Nos propres attestations suivent la
  règle inverse : l'original dans son domaine, une copie à jour dans `97.1` (Kit administratif).
- `registre` est une **liste** : un contrat de prêt envoyé en recommandé en alimente deux. Les noms
  à renvoyer sont ceux des fichiers, tels que `dossiers.json` les écrit
  (`Registre-des-contrats.csv`, `Registre-des-recommandes.csv`…), et non les libellés abrégés de la
  colonne `reg`. La colonne `reg` dit quel registre *peut* être concerné ; ne le renseigner que si le document
  **crée ou modifie un engagement** (contrat, avenant, souscription, résiliation, garantie). Une
  simple attestation ou un relevé ne crée rien. Le registre des recommandés fait exception : il est
  global, et tout document parti ou arrivé en recommandé y est inscrit, même s'il ne crée aucun
  engagement — une mise en demeure reçue, par exemple. Les registres existants : `contrats`, `assurances`,
  `immobilisations`, `matériel`, `placements`, `recommandés` (global : tout envoi ou réception
  recommandé y est inscrit, quel que soit le dossier de classement), `archives`, `tableau de
  gestion`.
- Dans la colonne `chemin`, `|` sépare des sous-dossiers frères entre lesquels il faut choisir, et
  `<...>` marque une variable à lire dans le document. Pour `00` : `A classer` = type reconnu mais
  destination indécidable, `A traiter` = incomplet ou en attente d'une information, `Scans bruts` =
  à découper ou illisible.
- La règle « pas d'accent ni de caractère spécial » vise les **noms de fichiers**. Les noms de
  dossiers de niveau 1 et 2 sont fixes et gardent leurs accents ; les sous-dossiers créés à la
  demande suivent le motif tel qu'il est écrit.
- **Jamais dans l'arborescence** : mot de passe, clé privée, phrase de récupération, code
  d'authentification. Ni dans `08.5`, ni ailleurs. Un document qui en contient va en `00` avec
  l'alerte.

## Aiguillage

```
00|Document non identifié, illisible, ou scan multi-documents. Destination de repli.
01|Existence légale et gouvernance : statuts, assemblées, registres, dirigeants, associés, propriété intellectuelle, conformité, contentieux.
02|Engagements contractuels, hors travail, banque et assurance : clients, fournisseurs, sous-traitance, baux, abonnements, NDA.
03|Les personnes qui travaillent pour l'entreprise : registres, dossiers individuels, paie, organismes sociaux, recrutement, formation, absences, santé-sécurité, CSE.
04|Ce qui justifie une écriture comptable ou une déclaration : exercices, factures, notes de frais, immobilisations, impôts, facturation électronique.
05|L'argent qui ENTRE : comptes bancaires, emprunts, aides, investisseurs, moyens de paiement, garanties.
06|Assurances et sinistres, y compris la décennale et les garanties de construction.
07|Administrations, courrier, locaux, véhicules, certifications, matériel, marchés publics.
08|L'argent qui est PLACÉ : comptes à terme, titres, capitalisation, crypto-actifs, immobilier de placement, fonds, participations.
97|Référentiel et kit administratif : copies à jour des attestations courantes. Ne contient pas d'original.
98|Dossiers clos dont la durée de conservation court encore.
99|Lots proposés à la suppression, en attente de validation.
```

## Table

Colonnes : `code|nom|cles|chemin|cons|reg|arb`

`chemin` = motif du sous-chemin sous le dossier · `cons` = conservation (a = années, j = jours) ·
`reg` = registre à mettre à jour, `-` si aucun · `arb` = arbitrages, `-` si aucun

### 00 - INBOX

```
00|Inbox|non identifié, illisible, doute, plusieurs documents dans un fichier|A classer | A traiter | Scans bruts|sas, 30j max|-|destination de repli obligatoire quand la confiance est faible
```

### 01 - JURIDIQUE & GOUVERNANCE

```
01.1|Constitution|statuts constitutifs, dépôt de capital, annonce légale de constitution, immatriculation, M0, première DBE, non-condamnation, attestation de filiation|à plat|permanent|-|statuts modifiés depuis la création → 01.2
01.2|Statuts & modifications|statuts à jour, statuts modifiés, M2, transfert de siège, changement de dénomination, changement d'objet, transformation, récépissé greffe, annonce légale de modification|AAAA-MM-JJ - Objet de la modification/|permanent|-|le PV qui décide la modification → 01.3 (copie ici)
01.3|Assemblées & décisions|PV, procès-verbal, AGO, AGE, assemblée générale, convocation, ordre du jour, rapport de gestion, approbation des comptes, affectation du résultat, feuille de présence, pouvoir, dépôt des comptes au greffe|AAAA/|permanent|-|comptes annuels eux-mêmes → 04.1
01.4|Registres légaux|registre des mouvements de titres, ordre de mouvement, compte d'actionnaire, registre des décisions, bénéficiaires effectifs, DBE, registre coté et paraphé|un sous-dossier par registre|permanent|-|conventions réglementées : pas de registre légal, le rapport → 01.3
01.5|Dirigeants & mandats|nomination du dirigeant, révocation, démission, rémunération du dirigeant, délégation de pouvoir, délégation de signature, convention réglementée, affiliation SSI, TNS, mandat social|NOM Prénom/|permanent|-|RCMS, assurance du dirigeant → 06.6 ; bulletin du dirigeant assimilé salarié → 03.3
01.6|Associés & capital|pacte d'associés de NOTRE société, cession de parts, cession d'actions, augmentation de capital, réduction de capital, BSPCE, BSA, action gratuite, compte courant d'associé, table de capitalisation, agrément|un sous-dossier par thème ou par opération|permanent|-|titres détenus dans une AUTRE société → 08.8 ; levée de fonds → 05.4
01.7|Propriété intellectuelle|marque, INPI, EUIPO, OMPI, dépôt de marque, renouvellement de marque, preuve de propriété d'un nom de domaine, e-Soleau, cession de droits d'auteur, licence de contenu, brevet, dessin et modèle|un sous-dossier par actif|permanent tant qu'exploité|-|facture de dépôt → 04.3
01.8|Conformité|RGPD, registre des traitements, AIPD, DPA, sous-traitance de données, violation de données, politique de confidentialité, CGV, CGU, mentions légales, médiateur de la consommation, accessibilité numérique, RGAA, charte informatique, charte IA, littératie IA, lanceur d'alerte|RGPD | CGV-CGU | Mediation-consommation | Accessibilite-numerique | Intelligence-artificielle | Politiques et chartes|10a|-|charte signée par un salarié → 03.2 ; contrat client renvoyant aux CGV → 02.1
01.9|Contentieux & précontentieux|mise en demeure, assignation, conclusions, jugement, ordonnance, injonction de payer, huissier, commissaire de justice, avocat, protocole transactionnel, médiation, saisie|AAAA - Partie adverse - Objet/|10a|-|relance amiable d'une facture que NOUS avons émise → 04.2 ; mise en demeure reçue d'un fournisseur → ici ; sinistre assuré → 06.7
```

### 02 - CONTRATS

```
02.1|Clients|contrat client, contrat de prestation signé, devis accepté, proposition commerciale signée, bon de commande, ordre de service, PV de recette fonctionnelle, CGV acceptées, DPA client, résiliation client|Client/|10a|contrats|facture émise → 04.2 ; litige → 01.9 ; livrables → hors périmètre
02.2|Fournisseurs & prestataires|contrat fournisseur, contrat de prestation reçu, maintenance, conditions générales du fournisseur, attestation de vigilance d'un fournisseur, pièces de vigilance d'un tiers, devis fournisseur accepté|Fournisseur/|10a|contrats|facture reçue → 04.3 ; abonnement récurrent → 02.5 ; lettre de mission comptable → 04.7
02.3|Sous-traitance & partenariats|sous-traitance, contrat de sous-traitance, attestation de vigilance d'un sous-traitant, apport d'affaires, partenariat, distribution, revente, marque blanche, groupement, consortium, commissionnement|Partenaire ou sous-traitant/|10a|contrats|prestataire sans lien avec un client → 02.2
02.4|Baux & locaux|bail commercial, bail professionnel, bail précaire, état des lieux, dépôt de garantie, quittance de loyer comme pièce du bail, appel de charges, révision de loyer, indice ILC, domiciliation, coworking, congé, sous-location|Local/|10a|contrats|assurance du local → 06.2 ; énergie et ménage → 02.5 ; immeuble détenu comme placement → 08.6
02.5|Abonnements & licences|abonnement, SaaS, licence logicielle en cours, hébergement, facture de renouvellement de nom de domaine, télécom, mobile, énergie, électricité, eau, ménage, leasing de matériel, reconduction tacite, résiliation d'abonnement|Service/|5a|contrats|facture de l'abonnement → 04.3 ; matériel acheté → 07.6
02.6|Confidentialité (NDA)|NDA, accord de confidentialité, engagement de confidentialité isolé|à plat, ou Contrepartie/|10a|contrats|NDA inclus dans un contrat plus large → avec ce contrat
02.7|Modèles de contrats|modèle de contrat, contrat type, trame, modèle de devis, modèle de mise en demeure|un sous-dossier par type de modèle|tant qu'un contrat signé en dépend|-|modèles RH → 03.1
```

### 03 - RESSOURCES HUMAINES

```
03.1|Obligations & registres|registre unique du personnel, DUERP, document unique, affichage obligatoire, convention collective, IDCC, règlement intérieur, accord d'entreprise, TéléAccords, PAPRIPACT, registre de sécurité du personnel, vérification électrique, dangers graves et imminents, registre des alertes, repos hebdomadaire, travail en équipes, DOETH, index égalité|un sous-dossier par registre ou famille|DUERP 40a, reste 5a|-|registre des questions du CSE → 03.10 ; dossier individuel → 03.2
03.2|Dossiers salariés|contrat de travail, CDI, CDD, avenant, DPAE, promesse d'embauche, fiche de poste, entretien annuel, entretien professionnel, avertissement, mise à pied, rupture conventionnelle, licenciement, démission, solde de tout compte, certificat de travail, attestation France Travail, titre de séjour|NOM Prénom/01 Embauche | 02 Vie du contrat | 03 Sortie|5a après départ|-|bulletin de paie → 03.3 ; arrêt de travail et congés → 03.7 ; avis médical → 03.8
03.3|Paie|bulletin de paie, bulletin de salaire, journal de paie, livre de paie, DSN, net-entreprises, bordereau de cotisations, état des charges sociales, variables de paie|AAAA/AAAA-MM/|5a employeur, 50a bulletin électronique|-|notes de frais → 04.4 ; contrat mutuelle → 06.4
03.4|Organismes sociaux|URSSAF, AGIRC-ARRCO, retraite complémentaire, prévoyance, mutuelle obligatoire, médecine du travail, SPST, OPCO, SSI, DSI, contrôle URSSAF, lettre d'observations, DUE, notice d'information, notre propre attestation de vigilance|Organisme/|6a à 10a|-|bordereau mensuel → 03.3 ; contrat d'assurance mutuelle → 06.4
03.5|Recrutement|annonce d'emploi, offre d'emploi, CV, candidature, lettre de motivation, entretien de recrutement, grille d'entretien, test de recrutement, refus de candidature, cabinet de recrutement|AAAA-MM - Intitulé du poste/ | CV-theque/|5a après pourvoi du poste|-|candidat retenu → 03.2 ; CV spontané → sous-dossier CV-theque, 2a
03.6|Formation|plan de développement des compétences, convention de formation, convocation à une formation, émargement, attestation de formation, certificat de formation, prise en charge OPCO, SST, habilitation électrique|AAAA/AAAA-MM - Intitulé - Organisme/|10a|-|facture de formation → 04.3 ; Qualiopi de l'entreprise → 07.5
03.7|Temps & absences|demande de congés, planning des congés, compteur de congés, arrêt de travail, arrêt maladie, IJSS, subrogation, maternité, paternité, congé parental, relevé d'heures, heures supplémentaires, astreinte, forfait jours, avenant de télétravail|AAAA/Conges | Arrets de travail | Temps de travail|5a|-|certificat médical détaillé : ne pas conserver ; avis d'aptitude → 03.8
03.8|Santé & sécurité|visite médicale, visite d'information et de prévention, avis d'aptitude, inaptitude, aménagement de poste, accident du travail, DAT, maladie professionnelle, taux AT/MP, registre des accidents bénins, plan de prévention, fiche de données de sécurité, harcèlement|Suivi medical/NOM Prénom | Accidents du travail/AAAA | Prevention|10a, 40a exposition|-|DUERP → 03.1 ; arrêt de travail → 03.7
03.9|Stagiaires, alternants & freelances|convention de stage, stagiaire, gratification, contrat d'apprentissage, apprenti, professionnalisation, CFA, aide à l'embauche ASP, contrat de mission, freelance, indépendant, portage salarial, cession de droits du freelance|Stagiaires | Alternants | Freelances /NOM Prénom/|5a à 10a|-|facture du freelance → 04.3 ; prestataire en société → 02.2
03.10|Représentation du personnel|CSE, comité social et économique, élection professionnelle, protocole préélectoral, PV d'élection, PV de carence, liste électorale, réunion du CSE, consultation du CSE, BDESE, heures de délégation, registre des questions du CSE, salarié protégé|Mandature AAAA-AAAA/|permanent pour les PV d'élection|-|accords d'entreprise → 03.1
```

### 04 - COMPTABILITE & FISCALITE

```
04.1|Exercices comptables|bilan, compte de résultat, annexe, plaquette, liasse fiscale, 2065, 2050, 2033, grand livre, balance générale, journal comptable, FEC, inventaire, rapport du commissaire aux comptes, situation intermédiaire|AAAA/ (ou AAAA-MM_AAAA-MM si exercice décalé)|permanent pour les états, 10a pour les livres|-|déclarations fiscales → 04.6 ; PV d'approbation → 01.3
04.2|Factures clients|facture émise, facture de vente, facture client, avoir client, facture d'acompte, journal des ventes, relance de facture, échéancier accordé|AAAA/AAAA-MM/|10a|-|contrat ou devis signé → 02.1 ; impayé en contentieux → 01.9
04.3|Factures fournisseurs|facture fournisseur, facture d'achat, facture reçue, avoir fournisseur, note d'honoraires, honoraires, quittance de loyer comme pièce comptable, ticket de caisse, reçu, journal des achats|AAAA/AAAA-MM/|10a|-|dépense avancée par une personne → 04.4 ; bien amorti au-delà de 500 € HT → copie en 04.5 ; contrat → 02.2 ou 02.5
04.4|Notes de frais|note de frais, frais de déplacement, indemnité kilométrique, barème kilométrique, repas d'affaires, hôtel, péage, train, carburant remboursé, politique de frais|AAAA/AAAA-MM/|10a|-|facture au nom de l'entreprise → 04.3
04.5|Immobilisations|immobilisation, tableau d'amortissement d'un bien, amortissement, crédit-bail, LOA, option d'achat, mise au rebut, cession d'immobilisation, registre des immobilisations|AAAA - Désignation - Fournisseur/|détention + 10a|immobilisations|inventaire physique et attribution → 07.6 ; titres et participations → 08
04.6|Fiscalité|CA3, CA12, déclaration de TVA, crédit de TVA, DEB, EMEBI, 2571, 2572, acompte d'IS, solde d'IS, CFE, CVAE, 1447, taxe sur les salaires, TVS, C3S, avis d'imposition, proposition de rectification, contrôle fiscal, rescrit, attestation de régularité fiscale, 3916|Impôt/AAAA/|10a|-|liasse fiscale → 04.1 ; dossier CIR complet → 05.3 ; calcul de plus-value sur placement → 08.9
04.7|Expert-comptable & CAC|lettre de mission, expert-comptable, commissaire aux comptes, CAC, rapport général, rapport spécial, mandat EDI, EDI-TDFC, questionnaire de clôture, lettre d'affirmation|Expert-comptable | Commissaire aux comptes /Cabinet/|10a|-|honoraires facturés → 04.3
04.8|Budget & reporting|budget, prévisionnel, plan de trésorerie, tableau de bord, business plan, seuil de rentabilité, balance âgée, reporting interne|AAAA/Budget | Tresorerie | Tableaux de bord|5a|-|prévisionnel transmis à un financeur → copie dans 05.2, 05.3 ou 05.4
04.9|Facturation électronique & piste d'audit fiable|plateforme agréée, PA, PDP, plateforme de dématérialisation, Factur-X, e-reporting, piste d'audit fiable, PAF, statut de cycle de vie, annuaire de facturation, portabilité de plateforme, rejet de facture|Plateforme agreee | Piste d'audit fiable | Exports/AAAA | Incidents|10a|-|le CONTRAT avec la plateforme agréée → 02.5 (registre contrats), avec une copie ici ; seuls les flux, les incidents et la PAF restent ici ; les factures elles-mêmes → 04.2 et 04.3 ; logiciel de facturation → 02.5
```

### 05 - BANQUE & FINANCEMENT

```
05.1|Comptes bancaires|relevé de compte, relevé bancaire, convention de compte, RIB, relevé d'identité bancaire, IBAN, BIC, coordonnées bancaires, procuration bancaire, habilitation, KYC bancaire, agios, échelle d'intérêts, clôture de compte, attestation de solde|Banque - Type de compte/Releves/AAAA/|10a|-|compte à terme et livret → 08.2 ; relevé de prestataire de paiement → 05.5 ; un RIB n'arrive ici que s'il est au nom de NOTRE entreprise : le RIB d'un fournisseur → 02.2, celui d'un salarié → 03.2 ; un relevé ordinaire ne qualifie pas le type de compte : écrire « Compte courant » par défaut, et ne réserver _INCONNU qu'au cas où la banque elle-même n'est pas lisible
05.2|Emprunts & crédits|contrat de prêt, offre de prêt, tableau d'amortissement d'emprunt, PGE, prêt d'honneur, crédit-bail financier, affacturage, Dailly, découvert autorisé, assurance emprunteur, remboursement anticipé, mainlevée|AAAA - Établissement - Objet - Montant/|10a|contrats|caution ou nantissement adossé → 05.6 ; relevé du compte débité → 05.1
05.3|Aides & subventions|subvention, convention de subvention, Bpifrance, ADEME, fonds européens, conseil régional, CIR, CII, JEI, 2069-A, aide à l'embauche, ASP, demande de versement, rapport d'avancement|AAAA - Organisme - Dispositif/|10a après dernier versement|-|prêt à rembourser → 05.2 ; levée de fonds privée → 05.4
05.4|Investisseurs & levées de fonds|term sheet, lettre d'intention, contrat d'investissement, BSA-AIR, obligation convertible, bulletin de souscription de NOS titres, attestation de dépôt des fonds, due diligence de NOTRE levée, data room de NOTRE levée, reporting investisseurs, closing|AAAA - Nom de l'opération/|permanent|-|pacte d'associés de NOTRE société → 01.6 ; subvention publique → 05.3
05.5|Moyens de paiement|carte bancaire professionnelle, TPE, terminal de paiement, monétique, prestataire de paiement, payout, mandat SEPA, ICS, RUM, prélèvement, chéquier, remise de chèques, chargeback, contestation de paiement|Moyen ou prestataire/|10a|-|relevé de compte bancaire → 05.1
05.6|Cautions & garanties|caution personnelle, cautionnement, garantie bancaire, garantie à première demande, nantissement, gage, hypothèque, garantie Bpifrance, dépôt de garantie reçu, retenue de garantie, mainlevée, lettre d'intention de garantie|Donnees | Recues /Contrepartie ou contrat garanti/|10a après mainlevée|-|contrat de prêt garanti → 05.2 ; bail garanti → 02.4
```

### 06 - ASSURANCES

```
06.1|Responsabilité civile professionnelle|RC professionnelle, RC Pro, responsabilité civile professionnelle, RC exploitation, attestation RC Pro, questionnaire de souscription|Assureur - N° contrat/|10a après fin|assurances|sinistre → 06.7
06.2|Multirisque locaux|multirisque, multirisque professionnelle, incendie, dégât des eaux, vol, bris de machine, RC occupant, attestation pour le bailleur|Assureur - N° contrat/|10a après fin|assurances|bail et états des lieux → 02.4
06.3|Véhicules|carte verte, assurance automobile, mémo véhicule assuré, relevé d'information, bonus-malus, assurance mission, conducteur désigné au contrat|Assureur - N° contrat/|5a après fin|assurances|carte grise et entretien → 07.4 ; constat et sinistre → 06.7
06.4|Prévoyance & santé collective|mutuelle, complémentaire santé, prévoyance collective, contrat responsable, Madelin, GSC, PER entreprise, tableau de garanties, prévoyance TNS|Assureur - N° contrat/|permanent|assurances|DUE, notices et affiliations des salariés → 03.4 et 03.2
06.5|Cyber-risques|assurance cyber, cyber-risques, rançongiciel couvert, questionnaire de sécurité, frais de notification RGPD|Assureur - N° contrat/|10a après fin|assurances|politique de sécurité → 01.8 ; incident survenu → 06.7
06.6|Homme-clé & RC des dirigeants|RCMS, RC des mandataires sociaux, D&O, homme-clé, protection juridique professionnelle|Assureur - N° contrat/|10a après fin|assurances|mandats et nominations → 01.5
06.7|Sinistres|déclaration de sinistre, constat amiable, expertise, rapport d'expertise, contre-expertise, indemnisation, décompte d'indemnité, franchise appliquée, plainte, recours contre un tiers|AAAA-MM-JJ - Contrat - Objet/|10a après règlement|-|litige judiciaire qui en découle → 01.9
06.8|Décennale & garanties de construction|décennale, assurance décennale, dommages-ouvrage, PV de réception, réception des travaux, réserves, levée de réserves, parfait achèvement, garantie biennale, DOE, DIUO, PPSPS, attestation décennale du sous-traitant|Assureur - N° contrat/ puis AAAA - Client - Chantier/|10a après réception|assurances|sinistre déclaré → 06.7 ; contrat client → 02.1 ; sous-traitance → 02.3
```

### 07 - ADMINISTRATIF & ORGANISMES

```
07.1|Administrations|INSEE, avis de situation SIRENE, greffe, guichet unique, formalites.entreprises, RNE, CCI, CMA, douane, EORI, préfecture, mairie, enseigne, CNIL récépissé, syndicat professionnel, identifiants de l'entreprise|Organisme/|10a|-|impôts → 04.6 ; URSSAF et OPCO → 03.4 ; formalités statutaires → 01.2
07.2|Courrier|courrier, lettre recommandée, LRAR, accusé de réception, preuve de dépôt, LRE, recommandé électronique, réexpédition de courrier|AAAA/Entrant | Sortant|5a, 10a pour les recommandés|recommandés|si le courrier concerne un dossier existant, il va DANS ce dossier
07.3|Locaux & services généraux|registre de sécurité du site, vérification périodique, extincteur, alarme, désenfumage, ascenseur, exercice d'évacuation, plan d'évacuation, consignes de sécurité, badge, clé, registre public d'accessibilité, déchets, tri 8 flux, attestation de valorisation, Trackdéchets, OPERAT, décret tertiaire, relevé de compteur, syndic|Site/|occupation + 10a|-|bail → 02.4 ; contrats énergie et ménage → 02.5 ; assurance → 06.2
07.4|Véhicules|carte grise, certificat d'immatriculation, certificat de cession, contrôle technique, entretien du véhicule, carnet d'entretien, amende, avis de contravention, désignation du conducteur, LLD, LOA véhicule, restitution de véhicule, carte carburant, télépéage|Immatriculation - Marque Modèle/|détention + 10a|-|assurance du véhicule → 06.3 ; indemnités kilométriques → 04.4
07.5|Certifications & labels|Qualiopi, ISO 9001, ISO 27001, certification, audit de certification, non-conformité, plan d'actions, certificat de conformité, référencement fournisseur, questionnaire fournisseur, déclaration d'activité de formation, NDA formation, bilan pédagogique et financier, BPF|Certification ou label/|permanent|-|formations suivies par les salariés → 03.6
07.6|Matériel & inventaire|inventaire du matériel, numéro de série, remise de matériel, restitution de matériel, prêt de matériel, garantie constructeur, extension de garantie, inventaire des licences détenues, clé de licence, DEEE, attestation d'effacement, mise au rebut, recyclage|Inventaire | Remises et restitutions | Garanties | Licences | Mises au rebut|détention + 10a|matériel|facture d'achat → 04.3 et 04.5 ; abonnement SaaS → 02.5
07.7|Marchés publics|DC1, DC2, DC4, DUME, ATTRI1, acte d'engagement, mémoire technique, appel d'offres, avis de publicité, règlement de consultation, CCTP, CCAP, certificat de capacité, marché public, attribution, rejet d'offre|Dossier permanent/ puis AAAA-MM - Acheteur - Objet/|10a après exécution|-|client privé → 02.1 ; attestations en cours de validité → 97 Kit administratif
```

### 08 - PLACEMENTS & PARTICIPATIONS

```
08.1|Politique de placement & décisions|politique de placement, note de décision d'investissement, intention de détention, mandat de gestion, convention de conseil en investissement, profil de risque, rapport d'adéquation, questionnaire de connaissance, arbitrage de portefeuille|Decisions/AAAA/ | Intermediaires/Nom/|permanent|-|le contrat du placement → sous-dossier de sa ligne, 08.2 à 08.8
08.2|Placements bancaires|compte à terme, CAT, DAT, dépôt à terme, compte sur livret, bon de caisse, intérêts courus d'une ligne, pénalité de sortie anticipée, dénouement|AAAA - Banque - Support - Montant - Échéance/|10a après dénouement|placements|compte courant d'exploitation → 05.1 ; CAT nanti → garantie dans 05.6
08.3|Comptes-titres & valeurs mobilières|compte-titres, avis d'opéré, achat de titres, vente de titres, action, obligation, OPCVM, SICAV, FCP, ETF, ISIN, dividende, coupon, DIC, PRIIPS, dépréciation de titres, bordereau de transfert|Établissement - N° de compte/Avis d'opere/AAAA/|détention + 10a|placements|titre de participation non coté → 08.8 ; SCPI → 08.6 ; fonds non coté → 08.7 ; un avis d'opéré portant un cours et une date d'exécution désigne un titre négocié sur un marché : il va en 08.3 quel que soit le mot « fonds » dans le libellé du support, car 08.7 ne reçoit pas d'avis d'opéré mais des bulletins de souscription et des appels de capitaux
08.4|Contrats de capitalisation|contrat de capitalisation, bulletin de souscription d'un contrat de capitalisation, unité de compte, fonds en euros, arbitrage, rachat partiel, rachat total, imposition annuelle forfaitaire, taux de référence|Assureur - N° de contrat/|durée + 10a|placements|assurances de l'entreprise → 06 ; prévoyance → 06.4
08.5|Crypto-actifs|crypto, crypto-actif, bitcoin, ether, stablecoin, jeton, actif numérique, PSCA, MiCA, PSAN, export de transactions, historique de transactions, portefeuille, wallet, adresse publique, staking, airdrop, valeur vénale|Prestataire ou portefeuille/Exports/AAAA/ | Consolidation/AAAA/|sans purge tant que détenu|placements|clés privées et phrases de récupération : JAMAIS ici ; matériel de minage → 04.3
08.6|Immobilier de placement & SCPI|SCPI, OPCI, bulletin de souscription de parts de SCPI, part de SCI, immeuble de rapport, prix de retrait, bulletin trimestriel, relevé de distribution, société de gestion, acte notarié d'investissement|SCPI - Nom | SCI - Nom | Immeuble - Adresse/|permanent pour les actes|placements|local occupé par l'entreprise → 02.4 ; immeuble d'exploitation → 04.5
08.7|Non coté & private equity|FCPR, FPCI, fonds d'investissement, appel de capitaux, valeur liquidative, distribution de fonds, crowdfunding, crowdlending, financement participatif, obligation non cotée, prêt consenti à un tiers|AAAA - Gestionnaire - Nom du fonds/|détention + 10a|placements|prise de contrôle ou influence notable → 08.8 ; emprunt reçu → 05.2
08.8|Participations & filiales|titre de participation, pacte d'associés d'une société où NOUS entrons, filiale, holding, prise de participation, due diligence, garantie d'actif et de passif, management fees, convention de trésorerie, refacturation intragroupe, intégration fiscale, régime mère-fille, tableau des filiales|Nom de la société (SIREN)/|permanent|placements|votre propre capital → 01.6 ; titres cotés de trésorerie → 08.3
08.9|Valorisations & états annuels|valorisation au 31/12, attestation de valorisation, état récapitulatif des placements, plus-value réalisée, moins-value, provision pour dépréciation, intérêts courus non échus, cours retenu, horodatage du cours|AAAA/|10a|-|bilan et liasse → 04.1 ; déclarations → 04.6
```

### 97 - REFERENTIEL

```
97|Kit administratif|Kbis de moins de 3 mois, copie à jour de notre attestation de vigilance, attestation de régularité fiscale, attestation RC Pro, RIB de l'entreprise, avis de situation SIRENE, liste des bénéficiaires effectifs, pièce d'identité du dirigeant, fiche d'identité de l'entreprise|Kit administratif/ à plat|version en cours seulement|-|l'original et l'historique restent dans leur domaine : 01.1, 03.4, 04.6, 06.1, 05.1
```

### 98 - ARCHIVES

```
98|Archives|dossier clos, salarié parti, contrat terminé, exercice ancien, litige réglé, véhicule revendu, contrat résilié|AAAA de clôture/ + chemin d'origine reproduit|durée du domaine d'origine|archives|ce qui ne se détruit jamais reste dans son dossier d'origine
```

### 99 - SUPPRESSION

```
99|Suppression|proposition de suppression, durée écoulée, doublon, purge RGPD, demande d'effacement, scan illisible|AAAA-MM-JJ - Objet du lot/|délai de grâce 30j|archives|jamais un document encore dans sa durée, ni un document sous litige ou contrôle
```

## Pièges fréquents

- **Facture ou contrat ?** Le contrat va en `02`, la facture qu'il génère en `04.2` ou `04.3`. Les
  deux existent presque toujours pour le même tiers.
- **Facture ou note de frais ?** Au nom de l'entreprise → `04.3`. Avancée par une personne et
  remboursée → `04.4`.
- **Mon capital ou celui des autres ?** Pacte d'associés et BSPCE de votre société → `01.6`. Titres
  détenus dans une autre société → `08.8`.
- **Argent qui entre ou argent placé ?** Compte courant, emprunt, subvention, levée de fonds → `05`.
  Compte à terme, titres, crypto, SCPI, participation → `08`.
- **Local occupé ou immeuble de placement ?** Bail des bureaux → `02.4`. SCPI et immeuble de
  rapport → `08.6`.
- **Immobilisation corporelle ou financière ?** Matériel et véhicules → `04.5`. Titres et
  participations → `08`.
- **Bulletin de paie ou dossier salarié ?** Les bulletins sont classés par mois pour toute
  l'entreprise en `03.3`, jamais dans le dossier individuel `03.2`.
- **Assurance : contrat ou sinistre ?** Le contrat et ses attestations dans son dossier `06.x`. La
  déclaration et l'expertise en `06.7`, quel que soit le contrat concerné.
- **Courrier recommandé.** S'il concerne un dossier existant, il va dans ce dossier. `07.2` ne
  reçoit que le courrier général et le registre des recommandés.
- **Attestation en cours de validité.** L'original va dans son domaine (`03.4` pour l'URSSAF, `06.1`
  pour la RC Pro) ; une copie va dans le Kit administratif, dont l'identifiant est `97.1` et non
  `97` — le domaine `97` ne reçoit aucune pièce d'entreprise. Le kit ne garde que la version du
  moment : la copie précédente est remplacée, pas archivée.
- **Avis d'opéré de titres.** Conservé tant que la ligne est détenue : c'est lui qui porte le prix de
  revient. Ne jamais le proposer à la suppression.
- **Document dont la durée est écoulée.** Il ne part pas directement en `99` : il passe par `98`
  quand son dossier est clos, puis `99` propose le lot à validation.

## Coût en tokens

Mesuré sur ce fichier, estimation à 10 % près.

| Ce qu'on charge | Tokens |
|---|---|
| Le fichier entier | ~11737 |
| Tout sauf la table (procédure, règles, aiguillage, pièges, sortie) | ~4696 |
| La table entière | ~7041 |
| Le plus gros bloc de domaine | ~1094 |
| **Mode deux temps : tout sauf la table, puis un bloc** | **~5790 au pire** |

En préfixe stable d'un prompt, le fichier entier est mis en cache : le coût réel après le premier
appel tombe à une fraction de ces chiffres. Le mode deux temps n'a d'intérêt que sans cache, ou
quand le document à classer est lui-même très volumineux.

## Sortie attendue

Cas simple, une facture reçue :

```json
{
  "dossier": "04.3",
  "chemin": "04 - COMPTABILITE & FISCALITE/04.3 - Factures fournisseurs/2026/2026-03",
  "nom_fichier": "2026-03-04_Facture_Hebergeur-Alpha_Hebergement-mars-2026.pdf",
  "type": "facture-fournisseur",
  "declencheur": "cloture-exercice",
  "champs": {"date": "2026-03-04", "fournisseur": "Hebergeur Alpha", "numero": "F-2026-0310",
             "montant-ht": 240.00, "montant-ttc": 288.00},
  "sort_final": "D",
  "confiance": 0.95,
  "motif": "mentions TVA et numero de facture, emetteur tiers, a notre nom",
  "conservation": "10a",
  "registre": [],
  "echeances": [],
  "copies": [],
  "actions": []
}
```

Cas avec une variable de chemin manquante et une copie obligatoire : une attestation reçue de notre
assureur, dont le numéro de contrat n'est écrit nulle part sur la page.

```json
{
  "dossier": "06.1",
  "chemin": "06 - ASSURANCES/06.1 - Responsabilite civile professionnelle/Assureur-Alpha - _INCONNU",
  "nom_fichier": "2026_Attestation-RC-pro_Assureur-Alpha.pdf",
  "type": "attestation-rc-pro",
  "champs": {"exercice": "2026", "assureur": "Assureur Alpha", "numero-contrat": null,
             "objet": "Responsabilite civile professionnelle", "echeance": "2026-12-31"},
  "sort_final": "D",
  "confiance": 0.70,
  "motif": "attestation RC Pro ; numero de contrat absent du document, le dossier reste 06.1",
  "conservation": "2a",
  "declencheur": "fin-contrat",
  "registre": [],
  "echeances": [{"type": "validite", "date": "2026-12-31"}],
  "copies": [{"dossier": "97.1", "chemin": "97 - REFERENTIEL/Kit administratif"}],
  "actions": ["variable de chemin manquante : N contrat"]
}
```

Cas de repli, un scan multi-documents :

```json
{
  "dossier": "00",
  "chemin": "00 - INBOX/Scans bruts",
  "nom_fichier": "r2026-10-02_Document-entrant_Interne_38-pages-a-decouper.pdf",
  "type": "document-entrant-non-classe",
  "champs": {"date": "2026-10-02", "emetteur": "Interne", "sens": "entrant",
             "objet": "38 pages a decouper"},
  "sort_final": "D",
  "confiance": 0.98,
  "motif": "contient une facture, deux releves bancaires et un courrier : un fichier = un document",
  "conservation": "aucune",
  "declencheur": "aucun",
  "registre": [],
  "echeances": [],
  "copies": [],
  "actions": ["a_decouper"]
}
```

`type` est la clé du type documentaire lu à l'étape 6, ou `null` si aucune ne correspond.
`champs` reprend exactement les noms déclarés par ce type, un champ absent du document valant `null`.
`conservation` est le **minimum légal** du type (`conservation.legale` dans `dossiers.json`), écrit
tel quel (`10a`, `5a`, `permanent`), et `declencheur` dit à partir de quand il court. La colonne
`cons` de la table donne la même information en français au niveau du dossier : elle sert à la
première passe, pas à la sortie. Sans type reconnu, reprendre la colonne `cons`.
`sort_final` vaut `C` (conserver définitivement), `D` (détruire au terme) ou `T` (trier à l'échéance),
et se lit dans `conservation.sort-final` du type. Il n'est jamais déduit du dossier.
`registre` est une liste de noms de fichiers de registres, vide quand le document n'en alimente aucun.
`echeances` est une liste, car un même document peut en porter plusieurs ; `type` est pris dans
`contrat`, `preavis`, `placement`, `validite`, `paiement`, `garantie`, `retention`, `purge`,
`declaration` (un délai légal pour déclarer), `mise-a-jour` (une révision périodique obligatoire).
`copies` liste les destinations où une copie suffixée `_copie` doit être déposée.
`actions` est prise dans `a_decouper`, `a_renommer`, `variable de chemin manquante`,
`alerte_secret` (le document contient un mot de passe ou une clé : ne pas le classer).
