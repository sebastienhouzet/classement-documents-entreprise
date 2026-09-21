# Audit de conformité du plan de classement — septembre 2026

Confrontation de la version 2.0.0 du gabarit aux textes en vigueur, à la doctrine administrative et aux
référentiels publics français, au **18 septembre 2026**.

Ce document n'est pas un conseil juridique. Il signale des écarts et cite ses sources pour que chaque point
puisse être vérifié, notamment avec votre expert-comptable et votre avocat.

## Méthode et limites

Quatre recherches parallèles ont été menées sur les sources officielles : service-public / entreprendre,
BOFiP, economie.gouv.fr, impots.gouv.fr, CNIL, ANSSI, AFNOR, France Archives, cybermalveillance.gouv.fr.

Trois limites à garder en tête. **Legifrance a été inaccessible** depuis l'environnement de recherche (403
répétés) : les textes ont été vérifiés par des reprises officielles de second rang (BOFiP, code.travail.gouv.fr,
CNIL, fac-similés du Journal officiel), jamais par lecture directe du texte consolidé. **La fiche
service-public F10029 ne publie plus de tableau** : elle renvoie depuis le 8 juin 2026 à un simulateur
interactif, ce qui rend la vérification ligne à ligne impossible sans passer par le formulaire. Enfin,
**le BOFiP n'est pas à jour** sur le point le plus important de cet audit (voir écart n° 1).

Chaque point ci-dessous est donc marqué : **confirmé** (source officielle lue), **à confirmer** (source
sérieuse mais non primaire), ou **non vérifié**.

## Verdict d'ensemble

La structure du gabarit tient. Le découpage en domaines, la logique « une place par document », le cycle
inbox → domaines → archives → suppression et le principe d'un `index.md` par dossier correspondent aux bonnes
pratiques publiques de gestion documentaire, et vont même plus loin que ce que la plupart des PME pratiquent.

Ce qui ne tient plus, ce sont **des durées de conservation**, périmées par deux textes de 2026, et
**une quinzaine de documents obligatoires** qui n'ont aujourd'hui aucune place assignée. Aucun de ces écarts
ne remet en cause l'arborescence : ils se corrigent dans les `index.md` et par l'ajout de quelques
sous-dossiers.

Un point rassurant : la colonne **« Recommandé »** du gabarit, systématiquement plus longue que le minimum
légal et très souvent calée sur 10 ans, se révèle correcte même là où la colonne « Minimum légal » est
devenue fausse. Une entreprise qui a suivi la recommandation n'a rien détruit qu'elle aurait dû garder.

## 1. Corrections urgentes — durées devenues fausses

### Écart n° 1 — Documents fiscaux : 6 ans est périmé, c'est 10 ans

**À confirmer.** L'**article 36 de la loi n° 2026-534 du 25 juin 2026** relative à la lutte contre les fraudes
sociales et fiscales modifie l'**article L102 B du LPF** et porte le délai de conservation des documents
contrôlables de **6 à 10 ans**. L'application viserait les documents dont le délai de conservation expire
après le 1er janvier 2027.

Deux réserves sérieuses. Les sources divergent sur la date d'entrée en vigueur : la CCI Paris Île-de-France
retient le 1er janvier 2027, la CRCC de Paris le 1er septembre 2026. Et le **BOFiP n'a pas suivi** : la
version BOI-CF-COM-10-10-30 en vigueur au 3 septembre 2025 écrit toujours « au minimum six ans ».

**Où corriger** : `97 - REFERENTIEL/Durees-de-conservation.md` (ligne « Déclarations fiscales : 6 ans »),
`04 - COMPTABILITE & FISCALITE/index.md`, `04.6 - Fiscalité/index.md`, et toutes les lignes « Documents
fiscaux : 6 ans » des index de `04`, `05` et `08`.

**Effet pratique** : faible, puisque le gabarit recommandait déjà 10 ans partout. L'intérêt de la correction
est que l'écart 6/10 ans disparaît — le fiscal s'aligne enfin sur le comptable.

### Écart n° 2 — Candidatures non retenues : 2 ans est faux, c'est 5 ans

**Confirmé.** Le **référentiel CNIL des durées de conservation RH du 2 avril 2026** (mis à jour le 20 mai 2026)
retient, en **obligation** et non en recommandation, **5 ans à compter de la date à laquelle le poste a été
pourvu**, sur le fondement de l'**article L1134-5 du Code du travail** (prescription de l'action en
discrimination). Le « 2 ans » ne subsiste que pour la **CV-thèque**, et à compter du **dernier contact**.

À noter : la page générique de la CNIL sur les durées affiche encore « 2 ans maximum ». C'est une
incohérence interne à la CNIL, à ne pas propager.

**Où corriger** : `03.5 - Recrutement/index.md` (durée légale, durée recommandée et le conseil de purge
annuelle), la ligne « Candidatures non retenues » du tableau des durées, et la routine de janvier dans
`index.md` et `README.md`.

**Effet pratique** : important, et dans le sens de la prudence. Le gabarit conseille aujourd'hui de détruire
au bout de 2 ans des pièces qu'il faut conserver 5 ans pour se défendre d'une action en discrimination.
C'est la correction la plus urgente du lot.

### Écart n° 3 — Charges sociales : 3 ans est probablement sous-évalué

**À confirmer.** Le gabarit retient 3 ans (article L244-3 du Code de la sécurité sociale, prescription de
l'action en recouvrement URSSAF). Le référentiel CNIL de 2026 retient **6 ans** en archivage intermédiaire
pour l'assiette des cotisations, les bulletins de paie et la DSN, sur le fondement de l'**article L243-16 du
CSS**, qui vise la conservation des documents nécessaires au **contrôle**, et non au recouvrement.

Les deux fondements sont différents et le second est plus exigeant. Position recommandée : **6 ans**.

**Où corriger** : `03.3 - Paie/index.md`, `03.4 - Organismes sociaux/index.md`, tableau des durées.

### Écart n° 4 — Bulletin de paie : deux durées, pas une

**Confirmé.** Le gabarit ne retient que les 5 ans de l'article L3243-4 (double conservé par l'employeur).
Il manque l'obligation de **mise à disposition du bulletin électronique pendant 50 ans, ou jusqu'aux 75 ans
du salarié** (article D3243-8). Ce sont deux obligations distinctes qui ne portent pas sur le même objet.

**Où corriger** : `03.3 - Paie/index.md` et le tableau des durées.

### Écart n° 5 — Registre des conventions réglementées : il n'existe pas

**Confirmé.** Le gabarit liste, dans `01.4 - Registres légaux`, un « registre des conventions réglementées
(si tenu séparément) ». **Aucun texte n'impose ce registre** en SAS ni en SARL. Ce qui est obligatoire, c'est
le **rapport sur les conventions réglementées** présenté à l'assemblée d'approbation des comptes
(articles L227-10 pour la SAS, L223-19 pour la SARL).

La rubrique reste utile comme rubrique documentaire, mais doit être requalifiée : elle n'est pas un registre
légal. Même remarque pour le « suivi des demandes d'exercice des droits » du dossier `01.8` : il découle de
l'obligation d'*accountability* (articles 5.2 et 24 du RGPD), il n'est pas un registre obligatoire nommé.

### Écart n° 6 — Sinistre corporel : ligne manquante

**Confirmé.** Le dossier `06.7 - Sinistres` retient la prescription biennale de l'assurance. Il manque le cas
du **dommage corporel : 10 ans à compter de la consolidation du dommage** (article 2226 du Code civil).

### Écart n° 7 — Déclaration en douane : base juridique abrogée

**Confirmé pour l'abrogation, non vérifié pour la durée.** Les tableaux de durées qui circulent, y compris
les reprises de l'ancienne fiche F10029, fondent les 3 ans de la déclaration en douane sur le règlement CEE
2913/92, **abrogé**. La base actuelle est le Code des douanes de l'Union, règlement (UE) 952/2013. La durée
de 3 ans n'a pas pu être revérifiée sur source officielle.

## 2. Documents obligatoires sans place assignée

Ces éléments sont obligatoires ou fortement attendus, et n'ont aujourd'hui aucune destination claire dans le
gabarit. Classés par domaine d'accueil proposé.

### Dans `03 - RESSOURCES HUMAINES`

| Manque | Seuil | Pourquoi ça compte |
|---|---|---|
| **Registre des questions du CSE** | 11 à 49 salariés | Seul registre consultable par **les salariés eux-mêmes** ; délit d'entrave à 7 500 € |
| **Registre des dangers graves et imminents** | Dès l'existence d'un CSE | 10 000 € ; récidive 1 an d'emprisonnement + 30 000 € par salarié |
| **Registre des alertes santé publique et environnement** | Dès l'existence d'un CSE | Mêmes sanctions |
| **Registre spécial du repos hebdomadaire** | Si le repos n'est pas le même jour pour tous | 1 500 € par salarié |
| **Registre du travail en équipes** | Travail par relais ou roulement | 1 500 € par salarié |
| **Registre des vérifications des installations électriques** | **Toute** entreprise ayant des installations électriques | Article R4226-19 ; rapports d'organismes accrédités à annexer |
| **PAPRIPACT** | ≥ 50 salariés | Programme annuel de prévention, distinct du DUERP |

Le gabarit couvre bien le registre unique du personnel et le DUERP, mais il traite les registres CSE comme
des documents de `03.10` alors que ce sont des **registres de sécurité**, tenus en continu, consultables par
l'inspection du travail. Ils relèvent plutôt de `03.1` ou `03.8`.

**Point utile à documenter** : l'**article L4711-5 du Code du travail** autorise expressément à **regrouper
plusieurs registres obligatoires en un registre unique** dès lors que cela en facilite la tenue et la
consultation. C'est la base légale d'un « registre unique de sécurité » consolidé — une simplification que le
gabarit peut recommander.

### DUERP — le régime a durci en juin 2026

**Confirmé.** L'**article 48 de la loi n° 2026-534 du 25 juin 2026** instaure des **sanctions administratives**
pour manquement au DUERP, applicables depuis le 25 juin 2026 : avertissement ou **amende jusqu'à 4 000 € par
travailleur concerné**, prononcée par l'inspection du travail, **doublée en cas de récidive** dans les deux
ans. Elles s'ajoutent aux sanctions pénales existantes (7 500 € pour la personne morale, 15 000 € en récidive).

Le DUERP devient l'élément le plus exposé de tout le plan de classement. Deux précisions manquent aussi au
gabarit : la **périodicité de mise à jour dépend de l'effectif** — mise à jour annuelle obligatoire à partir
de **11 salariés**, et non 50 — et il faut tracer la **preuve de mise à disposition** au CSE et aux salariés,
actuels comme anciens.

### Dans `04 - COMPTABILITE & FISCALITE` — facturation électronique

Le gabarit annonce correctement le calendrier. Il manque les **pièces que la réforme oblige à conserver** :

- le **contrat avec la plateforme agréée** et les identifiants de routage (SIRET, annuaire) ;
- les **statuts de cycle de vie** des factures (déposée, rejetée, encaissée) — ce sont des preuves fiscales ;
- les **preuves de e-reporting** (données de transaction et de paiement) ;
- la **piste d'audit fiable (PAF)**, obligatoire au titre de l'article 289 VII 1° du CGI : contrôles
  documentés et permanents établissant un lien fiable entre chaque facture et la livraison sous-jacente. Son
  absence expose à un refus de déduction de la TVA. Elle n'apparaît nulle part dans le gabarit.

Vocabulaire à mettre à jour : le décret n° 2026-677 et l'arrêté du 27 juillet 2026 remplacent
**« plateforme de dématérialisation partenaire (PDP) »** par **« plateforme agréée (PA) »**.

Point d'attention de fond, et c'est l'angle mort classique : **la responsabilité de la conservation reste
celle de l'entreprise**, même en recourant à une plateforme agréée. Une PA assure la transmission, pas
l'archivage à valeur probante, et sa durée de rétention est contractuelle, souvent très inférieure à 10 ans.
Le gabarit doit le dire explicitement dans `04.2` et `04.3`.

### Dans `07 - ADMINISTRATIF & ORGANISMES`

| Manque | Qui est concerné |
|---|---|
| **Registre public d'accessibilité** | Tout ERP, quel que soit l'effectif — à l'entrée principale, décret n° 2017-431 |
| **Tri à la source : 8 flux, pas 7** | Le gabarit parle de « Tri 7 flux ». C'est désormais **8 flux** (ajout des huiles alimentaires usagées ≥ 60 l/an), décret n° 2021-950 |
| **Attestation annuelle de valorisation des déchets** | Article D543-284 — distincte du registre de suivi, souvent oubliée |
| **Registre de suivi des déchets** | Conservation **3 ans** ; déclarer sur **Trackdéchets** dispense de tenir un registre séparé |
| **Déclaration OPERAT (décret tertiaire)** | Tout local tertiaire ≥ 1 000 m², **y compris en location** — déclaration annuelle avant le **30 septembre**, amende 7 500 € et publication publique |

Exemption utile à mentionner pour le tri du papier : dispense si le site compte **20 personnes de bureau ou
moins**, ce qui couvre beaucoup de PME tertiaires.

### Dans `01.8 - Conformité` — trois obligations absentes

**Accessibilité numérique (European Accessibility Act).** Applicable **depuis le 28 juin 2025**, transposée
par l'ordonnance n° 2023-859 et le décret n° 2023-931. Le seuil d'exemption est **très bas** : seules les
microentreprises échappent à l'obligation, c'est-à-dire **moins de 10 salariés et (CA ≤ 2 M€ ou bilan ≤ 2 M€)**.
Dès 10 salariés, un site de e-commerce est dans le champ. Documents à conserver : **informations sur
l'accessibilité du service** (publiées), rapport d'audit RGAA, et le cas échéant le **dossier de charge
disproportionnée**, conservé **5 ans** et réexaminé tous les 5 ans. Contrôle DGCCRF, contravention de 5e
classe cumulable.

À ne pas confondre avec le régime de l'article 47 de la loi de 2005 (déclaration d'accessibilité, schéma
pluriannuel, Arcom), qui ne vise dans le privé que les entreprises à plus de **250 M€ de CA moyen**.

**Médiateur de la consommation.** Obligatoire depuis 2016 pour tout professionnel vendant à des
consommateurs (article L612-1 du Code de la consommation) : adhésion à un dispositif agréé CECMC, coordonnées
mentionnées dans les CGV et sur le site. Amende jusqu'à 15 000 € pour une personne morale. À conserver :
contrat d'adhésion et preuve de cotisation. Obligation massivement ignorée.

À corriger au passage dans les CGV : la **plateforme européenne de règlement en ligne des litiges (RLL) est
fermée depuis le 20 juillet 2025** — les CGV qui la mentionnent encore sont à reprendre.

**Règlement européen sur l'IA.** Depuis le **2 août 2026**, les obligations de transparence de l'article 50
sont applicables et **sanctionnables**, de même que l'obligation de « littératie IA » de l'article 4 (formation
et sensibilisation du personnel qui utilise l'IA), en vigueur depuis février 2025. Documents à constituer :
**inventaire des systèmes d'IA utilisés**, y compris les outils SaaS et l'IA générative ; **attestations de
formation** ; **charte d'usage interne** ; mentions de transparence sur les chatbots et contenus générés.
Si du recrutement assisté par IA est en jeu, une analyse d'impact sur les droits fondamentaux sera requise
pour décembre 2027.

### Dans `06 - ASSURANCES` — le BTP n'est pas couvert

Le gabarit couvre la RC Pro, les locaux, les véhicules, la prévoyance, le cyber et la RCMS. Il ne couvre pas
la **garantie décennale**, obligatoire pour toute activité de construction (article L241-1 du Code des
assurances), à souscrire **avant l'ouverture du chantier** et dont l'attestation doit figurer **sur les devis
et les factures**. Défaut d'assurance : **75 000 € d'amende et 6 mois d'emprisonnement**.

Manquent également les pièces qui vont avec : **PV de réception des travaux** — pièce maîtresse, puisque le
délai décennal court à compter du lendemain de sa signature — **DOE**, **DIUO**, levée des réserves et
garantie de parfait achèvement.

### Dossiers sectoriels sans place

| Activité | Documents | Où les mettre |
|---|---|---|
| Organisme de formation | Déclaration d'activité (NDA), **BPF** à déposer avant le 31 mai, preuves d'audit Qualiopi | `07.5` — le gabarit cite Qualiopi mais pas le BPF ni le NDA |
| Marchés publics | DC1, DC2, DC4, DUME, mémoire technique, certificats de capacité, attestations à jour | Nouveau sous-dossier, ou `07.5` |
| Alimentaire | Plan de maîtrise sanitaire, HACCP, traçabilité, relevés de températures | Hors périmètre, à signaler |
| Professions réglementées | Carte professionnelle, garantie financière, registre des mandats, dossiers KYC LCB-FT (5 ans) | Hors périmètre, à signaler |

À noter aussi, pour une PME de 11 à 49 salariés : depuis le **1er janvier 2025**, obligation expérimentale de
mettre en place un **dispositif de partage de la valeur** si le bénéfice net fiscal atteint 1 % du CA pendant
trois exercices. Documents : accord d'intéressement ou de participation, PV de mise en place, attestations de
versement.

### Ce qui, à l'inverse, ne concerne pas une TPE/PME

Utile à écrire noir sur blanc dans le gabarit, pour éviter de faire peur :

- **CSRD** : après la directive Omnibus I du 24 février 2026, le seuil passe à **1 000 salariés et 450 M€ de
  CA**, cumulatifs. Le nombre d'entreprises concernées dans l'UE passe de ~50 000 à ~5 000.
- **Devoir de vigilance (CS3D)** : seuil relevé à 5 000 salariés et 1,5 Md€.
- **Bilan GES réglementaire** : plus de 500 salariés.
- **NIS2** : **non transposée en France** au 18 septembre 2026 — le projet de loi Résilience est bloqué en
  séance publique. Aucune obligation NIS2 n'est juridiquement exigible aujourd'hui, mais une PME de services
  numériques de 50 à 249 salariés sera classée « entité importante » dès la transposition.

Point de négociation à connaître : l'Omnibus crée un **plafond de chaîne de valeur** juridiquement
contraignant. Un donneur d'ordre **n'a plus le droit d'exiger** d'un fournisseur de moins de 1 000 salariés
des informations excédant le référentiel **VSME** de l'EFRAG. Les clauses contraires sont sanctionnables.
Concrètement, une PME peut refuser un questionnaire ESG de 300 lignes. Un dossier « réponses VSME » reste
utile comme quasi-obligation commerciale.

## 3. Écarts méthodologiques par rapport aux référentiels publics

### Le tableau de gestion manque

Le référentiel public français de gestion documentaire est le **R2GA** (Référentiel général de gestion des
archives, SIAF, octobre 2013). Il n'est pas contraignant — les archives d'une entreprise privée sont des
archives privées au sens des articles L211-1 et L211-4 du Code du patrimoine, hors contrôle de l'État — mais
c'est la meilleure méthodologie publique disponible, et elle est transposable telle quelle.

Le R2GA attend **quatre outils**. Le gabarit en a deux :

| Outil R2GA | État dans le gabarit |
|---|---|
| **Plan de classement** fondé sur les fonctions et activités | Présent, et conforme : l'arborescence suit les fonctions, pas l'organigramme |
| **DUA** (durée d'utilité administrative) | Présente sous le nom « durée de conservation » |
| **Tableau de gestion** : une ligne par typologie, avec producteur, DUA, **sort final** et référence juridique | **Absent** |
| **Référentiel de conservation** croisant activités et règles | Partiellement couvert par `Durees-de-conservation.md` |

Le manque le plus net est le **sort final**, noté en archivistique **C** (conservation définitive),
**D** (destruction) ou **T** (tri). Le gabarit dit combien de temps garder, jamais **ce qu'on en fait après**
de façon systématique. C'est précisément l'information dont `99 - SUPPRESSION` a besoin pour fonctionner.

**Recommandation** : produire un `Tableau-de-gestion.csv` dans `97 - REFERENTIEL`, une ligne par typologie
documentaire, colonnes `Dossier | Typologie | Producteur | DUA | Sort final (C/D/T) | Référence juridique`.
C'est le même document que le référentiel de durées exigé par le RGPD, vu sous un autre angle : autant n'en
tenir qu'un.

### Les trois âges du document ne sont pas matérialisés

La CNIL impose — c'est une **obligation**, pas une recommandation — de distinguer trois phases : **base
active**, **archivage intermédiaire** et **archivage définitif**. L'archivage intermédiaire suppose une
**séparation physique ou logique** de la base active, un **accès restreint à des personnes spécifiquement
habilitées**, et une **traçabilité des accès**.

Le gabarit a bien deux des trois âges (`01`-`08` puis `98 - ARCHIVES`), mais il ne dit nulle part que
`98 - ARCHIVES` doit avoir des **droits d'accès plus restrictifs** que les dossiers courants et que les accès
doivent être tracés. La grille d'accès du guide racine mentionne les archives RH, pas le principe général.

### La numérisation « à valeur probante » est décrite trop légèrement

Le gabarit écrit qu'« une pièce numérisée a la même valeur qu'un original papier si la copie est fidèle
(PDF non modifiable, horodaté, sans compression destructrice) ». C'est l'esprit, mais pas les conditions.

**Article 1379 du Code civil** et **décret n° 2016-1673 du 5 décembre 2016** — pour bénéficier de la
présomption de fiabilité, une copie électronique exige **cumulativement** : des informations liées à la copie
(identification, conditions et **date de numérisation**) ; une **empreinte électronique** garantissant la
détection de toute modification ultérieure ; l'**horodatage** de cette empreinte ; des conditions de
conservation évitant l'altération ; et la **conservation de l'empreinte initiale lors des migrations**. Le
dispositif doit être **documenté** pendant toute la durée de conservation. La présomption est renforcée si
l'empreinte est signée ou cachetée au moyen d'un certificat **qualifié eIDAS**.

**Article A102 B-2 du LPF** et **arrêté du 22 mars 2017**, pour les factures et pièces fiscales — toujours en
vigueur : reproduction **à l'identique** sans traitement d'image, couleurs conservées si code couleur,
compression sans perte, opérations documentées et contrôlées, conservation en **PDF ou PDF A/3 (ISO 19005-3)**
assortie d'au moins un dispositif parmi cachet serveur RGS une étoile, empreinte numérique, signature
électronique RGS, et **horodatage de chaque fichier**. À noter : le texte **ne fixe aucune résolution en DPI**.
Les 200 ou 300 dpi souvent cités relèvent de la bonne pratique (norme NF Z42-026), pas de la règle.

Et une limite que le gabarit passe sous silence : l'article 1379 précise que **« si l'original subsiste, sa
présentation peut toujours être exigée »**. Certains originaux ne doivent jamais être détruits — actes sous
signature privée à mention manuscrite, cautionnements, titres de propriété, effets de commerce, actes notariés.

**Sur les normes** : NF Z42-013 (SAE, version 2020), NF Z42-020 (coffre-fort numérique), NF Z42-026
(numérisation fidèle, version 2023), ISO 14641, ISO 15489, ISO 30301 sont toutes **volontaires**. **Aucune
obligation légale d'utiliser un SAE pour une PME.** Ce qui est obligatoire, ce sont les résultats — intégrité,
lisibilité, disponibilité, traçabilité. Utile à écrire dans le gabarit, pour éviter que quelqu'un croie devoir
acheter une solution certifiée.

### La sécurité et la sauvegarde sont absentes

C'est le manque le plus étonnant pour un dossier destiné à contenir toute la mémoire administrative d'une
entreprise. Dès que les documents contiennent des données personnelles — paie, clients, fournisseurs,
candidatures — l'**article 32 du RGPD** impose une obligation de sécurité. Et l'ANSSI publie des
recommandations directement applicables.

Ce qu'un `index.md` racine devrait dire, en s'appuyant sur le guide **ANSSI-BP-100** de novembre 2025 et sur
cybermalveillance.gouv.fr :

- **règle 3-2-1** : trois copies, deux supports différents, dont **une hors ligne, déconnectée** — c'est la
  seule protection réelle contre un rançongiciel, qui chiffre tout ce qui est monté ;
- **chiffrement** des sauvegardes et des supports amovibles ;
- **test de restauration documenté**, au moins annuel — une sauvegarde jamais restaurée n'est pas une
  sauvegarde ;
- **droits d'accès nominatifs et restreints**, revus périodiquement, avec **journalisation** des accès et des
  suppressions ;
- **formats pérennes** : PDF/A, XML, CSV ; proscrire les formats propriétaires fermés pour le long terme ;
- sauvegarder aussi **de quoi relire** les données : une facture Factur-X sans lecteur est une facture perdue ;
- **effacement sécurisé ou destruction physique** des supports en fin de vie — ce qui complète utilement
  `99 - SUPPRESSION`, qui ne parle aujourd'hui que de fichiers.

## 4. Ce que le gabarit fait bien

Pour équilibrer : plusieurs choix se révèlent plus rigoureux que la pratique courante.

La **colonne « Recommandé »** systématiquement plus longue que le minimum légal absorbe la plupart des
évolutions réglementaires sans rien perdre. C'est ce qui fait que l'écart n° 1 est sans conséquence pratique.

La section **« Ne pas ranger ici »** de chaque index résout le problème principal d'un plan de classement,
qui n'est pas de savoir où ranger mais de ne pas ranger au mauvais endroit.

Le **DUERP à 40 ans** est correctement traité, alors qu'il est absent de la majorité des plans antérieurs
à 2022. Idem pour l'**attestation de vigilance tous les 6 mois** au-delà de 5 000 € HT, souvent collectée une
seule fois à la signature.

Le dossier **`08.1 - Politique de placement & décisions`**, avec sa note de décision datée portant l'intention
de détention, correspond exactement à ce que la doctrine attend pour écarter la qualification d'acte anormal
de gestion.

Le **cycle inbox → domaines → archives → suppression** correspond aux trois âges du R2GA et aux trois phases
de la CNIL. La structure est juste ; il lui manque le vocabulaire et les droits d'accès associés.

## 5. Plan d'action proposé

**À corriger tout de suite** — erreurs qui peuvent conduire à détruire ou à mal conserver :

1. Candidatures non retenues : 2 ans → **5 ans** à compter du pourvoi du poste (`03.5`).
2. Charges sociales : 3 ans → **6 ans** (`03.3`, `03.4`).
3. Documents fiscaux : 6 ans → **10 ans**, avec la réserve sur la date d'entrée en vigueur (`04.6` et tableau).
4. Bulletin de paie : ajouter la ligne **50 ans / 75 ans** pour le bulletin électronique (`03.3`).
5. Requalifier le « registre des conventions réglementées » (`01.4`) et le « suivi des demandes d'exercice
   des droits » (`01.8`) : ce ne sont pas des registres obligatoires.

**À ajouter ensuite** — documents obligatoires sans place :

6. Registres CSE et sécurité manquants, et mention de l'article L4711-5 sur le registre unique (`03.1`).
7. Sanctions administratives DUERP de juin 2026 et périodicité de mise à jour selon l'effectif (`03.1`).
8. Piste d'audit fiable, contrat de plateforme agréée, statuts de cycle de vie, preuves de e-reporting
   (`04.2`, `04.3`), et la phrase qui manque : la conservation reste votre responsabilité, pas celle de la
   plateforme.
9. Registre public d'accessibilité ERP, tri **8 flux**, attestation annuelle de valorisation, OPERAT (`07.3`).
10. Accessibilité numérique EAA, médiateur de la consommation, inventaire et littératie IA (`01.8`).
11. Garantie décennale, PV de réception, DOE, DIUO — un sous-dossier `06.8` ou une section conditionnelle.
12. BPF et déclaration d'activité pour les organismes de formation ; dossier de candidature aux marchés
    publics (`07.5`).

**À ajouter au référentiel** — méthodologie :

13. `Tableau-de-gestion.csv` avec le **sort final C/D/T** par typologie.
14. Section « Sécurité et sauvegarde » dans le guide racine : 3-2-1, chiffrement, test de restauration,
    journalisation, formats pérennes.
15. Réécriture de la section sur la numérisation à valeur probante, avec les conditions réelles du décret
    2016-1673 et de l'article A102 B-2, et la liste des originaux à ne jamais détruire.
16. Droits d'accès restreints et traçabilité sur `98 - ARCHIVES`, au titre de l'archivage intermédiaire CNIL.
17. Encadré « ce qui ne vous concerne pas » : CSRD, CS3D, BEGES, NIS2, avec les seuils et le plafond VSME
    opposable aux donneurs d'ordre.

## Sources

Durées et obligations générales : [simulateur DILA « Combien de temps conserver ses documents »](https://www.service-public.gouv.fr/simulateur/calcul/ConserverSesPapiersPro) · [economie.gouv.fr — conservation des documents](https://www.economie.gouv.fr/entreprises/gerer-sa-comptabilite-et-ses-demarches/entreprises-combien-de-temps-devez-vous) · [BOI-CF-COM-10-10-30 (03/09/2025)](https://bofip.impots.gouv.fr/bofip/645-PGP.html/identifiant=BOI-CF-COM-10-10-30-20250903) · [Bpifrance Création — durées de conservation](https://bpifrance-creation.fr/encyclopedie/gerer-lentreprise/gestion-commerciale-administrative-documentaire/duree-conservation)

Loi du 25 juin 2026 : [LOI n° 2026-534](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000054309429) · [CCI Paris IdF — délai fiscal à 10 ans](https://www.entreprises.cci-paris-idf.fr/actualites/allongement-du-delai-de-conservation-des-documents-fiscaux-10-ans) · [CRCC Paris](https://www.crcc-paris.fr/extension-a-10-ans-du-delai-de-conservation-des-documents-aux-fins-dun-controle-fiscal/) · [Service-Public — sanctions DUERP](https://entreprendre.service-public.gouv.fr/actualites/A18908)

CNIL : [référentiel des durées RH (avril 2026)](https://www.cnil.fr/fr/referentiel-durees-conservation-donnees-rh) · [PDF du référentiel](https://www.cnil.fr/sites/default/files/2026-04/referentiel_durees_de_conservation_gestion_des_ressources_humaines.pdf) · [durées de conservation](https://www.cnil.fr/fr/passer-laction/les-durees-de-conservation-des-donnees) · [concilier durées et archives](https://www.cnil.fr/fr/comment-concilier-les-durees-de-conservation-et-les-archives) · [registre des traitements](https://www.cnil.fr/fr/RGPD-le-registre-des-activites-de-traitement)

Registres et obligations : [registres obligatoires (F1784)](https://entreprendre.service-public.gouv.fr/vosdroits/F1784) · [registres de société (F37373)](https://entreprendre.service-public.gouv.fr/vosdroits/F37373) · [affichages (F23106)](https://entreprendre.service-public.gouv.fr/vosdroits/F23106) · [DUERP (F35360)](https://entreprendre.service-public.gouv.fr/vosdroits/F35360) · [seuils d'effectif (F31415)](https://entreprendre.service-public.gouv.fr/vosdroits/F31415) · [registre d'accessibilité ERP (F32873)](https://entreprendre.service-public.gouv.fr/vosdroits/F32873) · [tri à la source (F37782)](https://entreprendre.service-public.gouv.fr/vosdroits/F37782) · [registre des déchets (F37825)](https://entreprendre.service-public.gouv.fr/vosdroits/F37825) · [attestation de vigilance (F31422)](https://entreprendre.service-public.gouv.fr/vosdroits/F31422)

Facturation électronique : [impots.gouv.fr — plateformes agréées](https://www.impots.gouv.fr/facturation-electronique-et-plateformes-agreees) · [guide pratique de démarrage (PDF)](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/guide_pratique_facturation_electronique.pdf) · [economie.gouv.fr](https://www.economie.gouv.fr/tout-savoir-sur-la-facturation-electronique-pour-les-entreprises) · [BOI-TVA-DECLA-30-20-30-20 — piste d'audit fiable](https://bofip.impots.gouv.fr/bofip/8865-PGP.html/identifiant=BOI-TVA-DECLA-30-20-30-20-20180207)

Archivage et preuve : [décret n° 2016-1673](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000033538124) · [arrêté du 22 mars 2017](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000034307622/) · [BOI-CF-COM-10-10-30-10](https://bofip.impots.gouv.fr/bofip/8877-PGP.html) · [AFNOR — archivage électronique](https://www.afnor.org/en/decryptions/cybersecurity/electronic-archiving-faq/) · [AFNOR — numérisation fidèle](https://www.afnor.org/en/decryptions/responsible-purchasing/faq-on-the-fidele-digitization-service/) · [R2GA (France Archives)](https://francearchives.gouv.fr/fr/circulaire/R2GA_2013_10) · [modèle de tableau de gestion](https://francearchives.gouv.fr/fr/file/1980efb3b3ff27c8508249aaa60ce0acdc15dbe4/static_919.pdf)

Sécurité : [ANSSI — guide d'hygiène informatique](https://messervices.cyber.gouv.fr/guides/guide-dhygiene-informatique) · [ANSSI-BP-100 — sauvegarde (nov. 2025)](https://messervices.cyber.gouv.fr/documents-guides/anssi_fondamentaux_sauvegarde_systemes_dinformation_v1.1.pdf) · [ANSSI — cybersécurité TPE/PME en 13 questions](https://messervices.cyber.gouv.fr/documents-guides/20241212_np_anssi_guide_tpe-pme_v2.pdf) · [cybermalveillance.gouv.fr — sauvegardes](https://www.cybermalveillance.gouv.fr/tous-nos-contenus/bonnes-pratiques/sauvegardes)

Obligations récentes et sectorielles : [directive Omnibus I (UE) 2026/470](https://eur-lex.europa.eu/eli/dir/2026/470/oj) · [portail RSE — seuils CSRD](https://portail-rse.beta.gouv.fr/csrd/seuils-csrd-omnibus-criteres-d-application/) · [ANSSI — NIS2](https://cyber.gouv.fr/reglementation/cybersecurite-systemes-dinformation/directives-nis-nis2-et-dispositif-saiv/directive-nis-2/) · [DGCCRF — accessibilité des produits et services](https://www.economie.gouv.fr/dgccrf/les-fiches-pratiques/professionnels-vos-produits-et-services-doivent-etre-conformes-la-directive-accessibilite) · [décret n° 2023-931](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000048178349) · [CNIL — règlement IA](https://www.cnil.fr/fr/entree-en-vigueur-du-reglement-europeen-sur-lia-les-premieres-questions-reponses-de-la-cnil) · [assurance décennale (F2034)](https://entreprendre.service-public.gouv.fr/vosdroits/F2034) · [OPERAT (ADEME)](https://operat.ademe.fr/)
