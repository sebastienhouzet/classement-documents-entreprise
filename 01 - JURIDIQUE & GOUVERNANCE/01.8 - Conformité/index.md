---
schema: classement-documents/3.0
id: "01.8"
parent: "01"
niveau: sous-dossier
titre: 01.8 - Conformité
usage: >-
  Les documents qui prouvent que l'entreprise respecte ses obligations réglementaires
  transverses : RGPD, conditions générales, accessibilité numérique, usage de l'intelligence
  artificielle, politiques internes.
classement: alphabetique
sensibilite: normale
documents:
  - type: version-cgv-cgu
    libelle: Version datée des CGV ou CGU
    description: "Chaque version des conditions générales de vente ou d'utilisation, avec sa date d'entrée en vigueur."
    indices: [cgv, cgu, conditions generales de vente, version datee, entree en vigueur, mediateur de la consommation]
    champs: [date, date-effet, reference, objet]
    nommage: "{date}_CGV_{reference}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: Code de la consommation art. L213-1
      sort-final: C
    registre: null
  - type: registre-traitements-rgpd
    libelle: Registre des activités de traitement
    description: "Registre des traitements et ses exports datés, avec les analyses d'impact et la politique de confidentialité publiée."
    indices: [rgpd, registre des traitements, aipd, "analyse d'impact", politique de confidentialite, export date]
    champs: [date, objet, reference, date-effet]
    nommage: "{date}_Registre-des-traitements_{reference}"
    conservation:
      legale: permanent
      recommandee: 5a
      declencheur: aucun
      base: RGPD art. 30
      sort-final: C
    registre: null
  - type: registre-violations-donnees
    libelle: Registre des violations de données
    description: "Consignation de toute violation de données, notifiée ou non, avec la justification de la non-notification."
    indices: [violation de donnees, registre des violations, notification cnil, incident de securite, non-notification]
    champs: [date, objet, motif, effectif]
    nommage: "{date}_Registre-des-violations_{objet}"
    conservation:
      legale: permanent
      recommandee: 5a
      declencheur: aucun
      base: RGPD art. 33.5
      sort-final: C
    registre: null
  - type: dpa-sous-traitance-donnees
    libelle: Accord de traitement des données (DPA)
    description: "Contrat de sous-traitance de données signé avec un prestataire qui traite des données pour l'entreprise."
    indices: [dpa, accord de traitement, sous-traitance de donnees, article 28, clauses contractuelles types]
    champs: [date-signature, fournisseur, objet, duree]
    nommage: "{date}_DPA_{fournisseur}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-contrat
      base: RGPD art. 28
      sort-final: C
    registre: null
  - type: charte-usage-interne
    libelle: Charte ou politique interne
    description: "Charte informatique, charte d'usage de l'IA, politique de sécurité et procédure de recueil des signalements, en versions datées."
    indices: [charte informatique, charte ia, litteratie ia, politique de securite, "lanceur d'alerte", signalement]
    champs: [date, date-effet, objet, effectif]
    nommage: "{date}_Charte-usage-interne_{objet}"
    conservation:
      legale: aucune
      recommandee: 5a
      declencheur: aucun
      base: "Règlement européen sur l'IA art. 4"
      sort-final: C
    registre: null
va-ailleurs:
  - motif: Contrats clients signés (qui renvoient aux CGV)
    vers: "02.1"
  - motif: Charte informatique signée par chaque salarié
    vers: "03.2"
  - motif: "Le « registre des demandes d'exercice des droits » n'est pas un registre légal nommé : c'est une preuve d'accountability (RGPD art. 5.2 et 24). Le conserver, oui ; le présenter comme une obligation, non"
    vers: null
---

# 01.8 - Conformité

> Chemin : `01 - JURIDIQUE & GOUVERNANCE/01.8 - Conformité`

## À quoi sert ce dossier

Les documents qui prouvent que l'entreprise respecte ses obligations réglementaires transverses : RGPD, conditions générales, accessibilité numérique, usage de l'intelligence artificielle, politiques internes. Ce sont des documents versionnés : on garde chaque version datée, car un client peut avoir contracté sous une version ancienne, et un contrôle porte sur l'état du droit au moment des faits.

## Documents à y ranger

- **RGPD** : registre des activités de traitement (fichier vivant + exports datés), analyses d'impact (AIPD), contrats de sous-traitance et DPA signés avec les prestataires, procédure de gestion des violations et **registre des violations** — obligatoire sans seuil et pour toute violation, même non notifiée —, politique de confidentialité (chaque version datée), mentions légales, désignation du DPO le cas échéant, suivi des demandes d'exercice des droits
- **Référentiel interne des durées de conservation** : le même document que le `Tableau-de-gestion.csv` de `97 - REFERENTIEL`, vu sous l'angle RGPD — durée en base active, durée d'archivage intermédiaire, sort final
- **CGV / CGU / CGA** : chaque version datée, avec sa date d'entrée en vigueur
- **Médiateur de la consommation** : contrat d'adhésion à un dispositif agréé et preuve de cotisation — obligatoire pour tout professionnel vendant à des consommateurs, coordonnées à faire figurer dans les CGV et sur le site
- **Accessibilité numérique** : informations sur l'accessibilité du service publiées, rapport d'audit RGAA, et le cas échéant le **dossier de charge disproportionnée** motivé et chiffré, à réexaminer tous les 5 ans. Pour les entreprises de plus de 250 M€ de CA moyen, s'y ajoutent la déclaration d'accessibilité, le schéma pluriannuel et le plan d'action annuel
- **Intelligence artificielle** : inventaire des systèmes d'IA utilisés, y compris les outils SaaS et l'IA générative ; charte d'usage interne ; attestations de formation à la « littératie IA » ; mentions de transparence sur les agents conversationnels et les contenus générés
- **Politiques et chartes** : charte informatique, politique de sécurité, politique de télétravail, charte éthique, procédure de recueil des signalements (obligatoire ≥ 50 salariés, après consultation du CSE)
- Obligations sectorielles éventuelles (agrément, déclaration d'activité, autorisation)

## Ne pas ranger ici

- Contrats clients signés (qui renvoient aux CGV) → `02.1`
- Charte informatique signée par chaque salarié → dossier du salarié `03.2`
- Le « registre des demandes d'exercice des droits » n'est pas un registre légal nommé : c'est une preuve d'*accountability* (RGPD art. 5.2 et 24). Le conserver, oui ; le présenter comme une obligation, non

## Méthode de classement

Six sous-dossiers : `RGPD`, `CGV-CGU`, `Mediation-consommation`, `Accessibilite-numerique`, `Intelligence-artificielle`, `Politiques et chartes`. Dans chacun, fichiers nommés `AAAA-MM-JJ_CGV_v3.pdf` ; le fichier en vigueur peut être dupliqué sous le nom `CGV-en-vigueur.pdf` pour être trouvé immédiatement.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | CGV : 5 ans après la fin du dernier contrat conclu sous cette version (10 ans pour les contrats électroniques ≥ 120 €). Registre RGPD : à tenir à jour en permanence. |
| **Recommandé** | Garder toutes les versions des CGV/CGU pendant 10 ans après leur remplacement. Versions du registre RGPD : 5 ans. |

Base : RGPD art. 5.2, 24, 28, 30 et 33.5 ; Code de la consommation art. L213-1 (conservation), L612-1 (médiation) et L412-13 (accessibilité) ; décret n° 2023-931 du 9 octobre 2023 ; règlement européen sur l'IA, art. 4 et 50 ; Code civil art. 2224.

## Conseils

- **Accessibilité numérique : le seuil est très bas.** Depuis le 28 juin 2025, un site de e-commerce n'est exempté que s'il est exploité par une microentreprise — moins de 10 salariés **et** chiffre d'affaires ou bilan ≤ 2 M€. Dès 10 salariés, l'obligation s'applique, avec un contrôle de la DGCCRF et une contravention de 5e classe cumulable. À ne pas confondre avec le régime de l'article 47 de la loi de 2005 (déclaration, schéma pluriannuel, Arcom), qui ne vise dans le privé que les entreprises à plus de 250 M€ de chiffre d'affaires moyen.
- **Le médiateur de la consommation est l'obligation la plus souvent oubliée** de ce dossier : elle date de 2016, vise tout professionnel vendant à des consommateurs, et son non-respect coûte jusqu'à 15 000 € pour une personne morale. À vérifier au passage : la plateforme européenne de règlement en ligne des litiges est **fermée depuis le 20 juillet 2025** — les CGV qui la mentionnent encore sont à reprendre.
- **IA** : les obligations de transparence sont applicables et sanctionnables depuis le 2 août 2026, et l'obligation de formation du personnel qui utilise l'IA depuis février 2025. Un inventaire des outils et une charte d'usage suffisent à documenter la conformité d'une PME ; l'analyse d'impact sur les droits fondamentaux ne devient nécessaire qu'en cas d'usage à haut risque, par exemple un tri de candidatures assisté par IA (échéance de décembre 2027).
- Le registre des violations de données est obligatoire **pour toutes les organisations, sans seuil, et pour toute violation** — y compris celles qui n'ont pas été notifiées à la CNIL. Y consigner alors la justification de la non-notification.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
