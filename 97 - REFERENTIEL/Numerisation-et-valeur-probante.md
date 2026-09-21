# Numérisation et valeur probante

Numériser un document, c'est en faire une copie. La question n'est pas de savoir si le scan est lisible, mais
si, le jour où quelqu'un le conteste, **il vaut l'original**. Le droit français répond oui, sous conditions —
et ces conditions sont précises.

## Ce que dit le droit

**Article 1379 du Code civil** : la copie fiable a la même force probante que l'original. La fiabilité est
laissée à l'appréciation du juge, **sauf** lorsqu'elle est présumée, c'est-à-dire lorsque le procédé de
reproduction répond aux conditions fixées par décret.

Une phrase du même article mérite d'être lue deux fois : **« Si l'original subsiste, sa présentation peut
toujours être exigée. »** La présomption ne prend tout son sens que lorsque l'original a disparu. Détruire le
papier est donc ce qui donne son intérêt à la copie fiable — et ce qui expose si le procédé est contestable.

## Les conditions de la copie fiable

**Décret n° 2016-1673 du 5 décembre 2016.** Pour une copie électronique, cinq conditions, cumulatives :

1. le procédé produit des **informations liées à la copie** : identification, conditions de la numérisation,
   et **date de création** ;
2. l'intégrité est attestée par une **empreinte électronique** permettant de détecter toute modification
   ultérieure ;
3. cette empreinte est **horodatée** ;
4. la conservation se fait dans des conditions propres à éviter toute altération, dans un environnement
   maîtrisé ;
5. lors des **migrations** ultérieures, l'empreinte initiale est conservée.

Le dispositif lui-même doit être **documenté** — procédés, mesures de sécurité, contrôle d'accès — et cette
documentation conservée pendant toute la durée de conservation des copies.

La présomption est **renforcée**, c'est-à-dire dispensée de la preuve du procédé, si l'empreinte est
horodatée, signée ou cachetée au moyen d'une signature ou d'un cachet électronique **qualifié** au sens du
règlement eIDAS.

## Le cas particulier des factures et pièces fiscales

**Article A102 B-2 du Livre des procédures fiscales**, issu de l'arrêté du 22 mars 2017, toujours en vigueur.
Il autorise la numérisation des factures papier, y compris **en cours de conservation** et pas seulement à
réception, à trois conditions.

**Fidélité** : reproduction conforme à l'original en image et en contenu, **sans aucun traitement d'image**,
couleurs reproduites à l'identique si un code couleur est utilisé, compression sans perte le cas échéant.

**Traçabilité** : opérations documentées, faisant l'objet de contrôles internes qui garantissent la
disponibilité, la lisibilité et l'intégrité des factures numérisées pendant toute la durée de conservation.
L'archivage peut être réalisé par l'entreprise elle-même ou par un tiers mandaté.

**Sécurisation** : conservation au format **PDF ou PDF A/3 (ISO 19005-3)**, assortie d'au moins un dispositif
parmi : cachet serveur fondé sur un certificat RGS d'au moins une étoile, empreinte numérique, signature
électronique fondée sur un certificat RGS, ou dispositif équivalent reposant sur un certificat délivré par une
autorité figurant sur la liste de confiance française. Et **horodatage de chaque fichier**, au moins au moyen
d'une source d'horodatage interne.

Point souvent mal rapporté : **le texte ne fixe aucune résolution en DPI.** L'exigence est fonctionnelle. Les
200 ou 300 dpi que l'on lit partout relèvent de la bonne pratique professionnelle (norme NF Z42-026), pas de
la règle.

## Ce qu'il ne faut jamais détruire

Même avec un procédé irréprochable, certains originaux se conservent sur papier :

- les actes sous signature privée dont l'original conditionne un droit — cautionnement, actes soumis à
  mention manuscrite ;
- les **titres de propriété** ;
- les **effets de commerce** ;
- les actes notariés ;
- tout document pour lequel un texte spécial impose la production de l'original.

Pour le reste, une règle de prudence : n'appliquer la destruction qu'aux flux de masse — factures
fournisseurs, justificatifs de notes de frais — et conserver le papier des pièces à fort enjeu contentieux
au moins pendant le délai de prescription applicable.

## Les normes, et ce qu'elles n'imposent pas

| Norme | Objet |
|---|---|
| **NF Z42-013** (2020) | Conception et exploitation d'un système d'archivage électronique (SAE) |
| **NF Z42-020** | Spécifications d'un composant coffre-fort numérique |
| **NF Z42-026** (2023) | Prestations de numérisation fidèle — la norme de référence pour appliquer les textes ci-dessus |
| **ISO 14641** | Équivalent international de NF Z42-013 |
| **ISO 15489**, **ISO 30301** | Records management : principes, puis système de management |

**Toutes ces normes sont volontaires.** Aucune obligation légale n'impose à une PME de se doter d'un système
d'archivage électronique ni d'obtenir une certification NF 461 ou NF 544. Ce qui est obligatoire, ce sont les
**résultats** : intégrité, lisibilité, disponibilité, traçabilité, sur toute la durée de conservation. Un SAE
certifié est un moyen d'y parvenir et surtout de le prouver, pas une condition de légalité.

## En pratique

Pour une TPE ou une PME qui n'a pas de solution d'archivage dédiée, une démarche proportionnée consiste à :

1. scanner en PDF/A, sans retouche, à une résolution qui reste lisible à l'écran comme à l'impression ;
2. calculer et conserver une **empreinte** (un hash SHA-256 suffit) de chaque fichier figé, dans un fichier
   d'index daté ;
3. **horodater** cet index, au minimum par un dépôt daté dans un système dont les journaux font foi ;
4. écrire une page décrivant le procédé — qui scanne, avec quel matériel, quels contrôles, quelle
   nomenclature — et la conserver ici, en la datant ;
5. ne détruire le papier qu'après ces quatre étapes, et jamais pour les documents de la liste ci-dessus.

Ce niveau d'exigence ne vaut pas la présomption renforcée d'une signature qualifiée. Il vaut nettement mieux
que rien, et il est à la portée d'une petite structure.
