# Sécurité et sauvegarde du dossier

Ce dossier contient la mémoire administrative de l'entreprise : sa comptabilité, ses contrats, ses données de
paie. Le perdre, c'est perdre la capacité à se défendre en contrôle. Le laisser accessible à tous, c'est un
manquement au RGPD dès lors qu'il contient des données personnelles — et il en contient toujours.

L'**article 32 du RGPD** impose une obligation de sécurité. Les recommandations ci-dessous viennent de
l'ANSSI et de cybermalveillance.gouv.fr ; elles ne sont pas contraignantes en elles-mêmes, mais elles sont ce
que l'on attend d'une entreprise diligente.

## Sauvegarder

**La règle 3-2-1** : trois copies des données, sur deux supports différents, dont **une copie hors ligne,
déconnectée**. C'est la seule protection réelle contre un rançongiciel : un logiciel malveillant chiffre tout
ce qui est monté, y compris le disque de sauvegarde branché en permanence et le cloud synchronisé.

- **chiffrer** les sauvegardes et les supports amovibles ;
- **tester la restauration** au moins une fois par an, et le noter — une sauvegarde jamais restaurée n'est pas
  une sauvegarde, c'est une hypothèse ;
- sauvegarder aussi **de quoi relire** : une facture Factur-X sans lecteur, une base sans son logiciel, c'est
  une donnée perdue ;
- surveiller le **vieillissement des supports** : un disque externe ou un DVD ne sont pas des supports
  d'archivage à dix ans.

## Restreindre et tracer les accès

Le RGPD distingue la **base active** et l'**archivage intermédiaire**, et impose que le second soit séparé du
premier, accessible aux seules personnes spécifiquement habilitées, avec **traçabilité des accès**. Dans ce
plan de classement, cela se traduit ainsi :

| Dossier | Accès |
|---|---|
| `03 - RESSOURCES HUMAINES` | Dirigeant et personne chargée de la paie uniquement — données personnelles et de santé |
| `04`, `05`, `08` | Dirigeant et comptabilité ; expert-comptable en lecture |
| `98 - ARCHIVES` | Droits **plus restrictifs** que les dossiers courants, lecture seule par défaut, accès journalisés |
| `99 - SUPPRESSION` | Dépôt ouvert à l'équipe de gestion, validation réservée au dirigeant |
| Le reste | Équipe de gestion |

Revoir ces droits périodiquement, en particulier au départ d'une personne. Journaliser les accès et les
suppressions sur les dossiers sensibles.

## Choisir des formats qui durent

Privilégier **PDF/A**, **XML**, **CSV**, et proscrire les formats propriétaires fermés pour tout ce qui doit
survivre dix ans. Les fichiers vivants (tableurs, documents de travail) peuvent rester dans leur format
natif ; les documents figés basculent en PDF/A au moment où ils sont classés.

## Détruire pour de bon

La suppression d'un fichier ne le détruit pas. À l'issue de la durée de conservation, et après le passage par
`99 - SUPPRESSION` :

- **effacement sécurisé** ou destruction physique du support ;
- destruction des clés si les données étaient chiffrées ;
- destruction du **papier correspondant**, à mentionner dans la proposition de suppression ;
- pour les données personnelles, l'alternative est l'**anonymisation**, à condition qu'elle soit
  irréversible — une pseudonymisation n'en est pas une.

## Le minimum vital

Si vous ne faisiez que quatre choses : une sauvegarde hors ligne, un test de restauration annuel, des droits
d'accès restreints sur `03` et `98`, et l'authentification multifacteur sur le service qui héberge ce dossier.
