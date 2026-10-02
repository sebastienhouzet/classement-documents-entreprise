---
schema: classement-documents/3.0
id: "07.3"
parent: "07"
niveau: sous-dossier
titre: "07.3 - Locaux & services généraux"
usage: >-
  La vie quotidienne des locaux : sécurité, accès, maintenance, vérifications périodiques,
  consignes. Le bail est dans 02.4, les contrats de fournisseurs (énergie, ménage, maintenance)
  dans 02.5 / 02.2, l'assurance dans 06.2 ; ici les documents pratiques et réglementaires liés à
  l'occupation.
classement: par-tiers
sensibilite: normale
documents:
  - type: registre-securite-site
    libelle: Registre de sécurité du site
    description: "Registre de sécurité d'un site — vérifications des extincteurs, de l'installation électrique et de l'alarme, exercices d'évacuation."
    indices: [registre de securite, extincteur, alarme, desenfumage, "exercice d'evacuation", consignes de securite]
    champs: [date, lieu, objet, reference]
    nommage: "{date}_Registre-de-securite_{lieu}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-occupation
      base: Code du travail art. R4224-17
      sort-final: D
    registre: null
  - type: rapport-verification-periodique
    libelle: Rapport de vérification périodique
    description: "Rapport d'un organisme de contrôle sur une installation du site — électricité, gaz, ascenseur, climatisation — et attestation de conformité correspondante."
    indices: [verification periodique, rapport de verification, attestation de conformite, ascenseur, installation electrique]
    champs: [date, prestataire, lieu, objet, echeance]
    nommage: "{date}_Rapport-de-verification_{prestataire}_{objet}"
    conservation:
      legale: 5a
      recommandee: 10a
      declencheur: fin-occupation
      base: Code du travail art. R4226-16
      sort-final: D
    registre: null
  - type: registre-public-accessibilite
    libelle: "Registre public d'accessibilité"
    description: "Registre public d'accessibilité d'un ERP — dispositions prises, attestations, calendrier de maintenance — tenu à l'entrée principale. Distinct du registre de sécurité."
    indices: ["registre public d'accessibilite", erp, accessibilite, dispositions prises, calendrier de maintenance]
    champs: [date, lieu, objet, date-effet]
    nommage: "{date}_Registre-public-accessibilite_{lieu}"
    conservation:
      legale: aucune
      recommandee: 10a
      declencheur: fin-occupation
      base: Décret n° 2017-431 du 28 mars 2017
      sort-final: D
    registre: null
  - type: registre-suivi-dechets
    libelle: Registre de suivi des déchets
    description: "Registre de suivi des déchets — quantité, nature, origine, destination, mode de traitement — à produire sur demande. Déclarer sur Trackdéchets dispense d'un registre séparé."
    indices: [registre des dechets, tri 8 flux, trackdechets, mode de traitement, collecteur, valorisation]
    champs: [date, periode, prestataire, quantite, nature]
    nommage: "{date}_Registre-des-dechets_{prestataire}"
    conservation:
      legale: 3a
      recommandee: 10a
      declencheur: date-document
      base: "Code de l'environnement art. R541-43"
      sort-final: D
    registre: null
  - type: declaration-operat-tertiaire
    libelle: Déclaration OPERAT
    description: "Déclaration annuelle sur la plateforme OPERAT pour un site tertiaire de 1 000 m² ou plus, location comprise — année de référence, relevés de consommation, attestation annuelle générée. Échéance au 30 septembre."
    indices: [operat, decret tertiaire, annee de reference, releve de consommation, attestation annuelle, site tertiaire]
    champs: [date, lieu, surface, periode, reference]
    nommage: "{date}_Declaration-OPERAT_{lieu}"
    conservation:
      legale: aucune
      recommandee: 10a
      declencheur: fin-occupation
      base: Décret dit « tertiaire » et plateforme OPERAT
      sort-final: D
    registre: null
va-ailleurs:
  - motif: "Bail, états des lieux, charges"
    vers: "02.4"
  - motif: "Contrats énergie, télécom, ménage"
    vers: "02.5"
  - motif: Assurance des locaux
    vers: "06.2"
  - motif: Matériel
    vers: "07.6"
---

# 07.3 - Locaux & services généraux

> Chemin : `07 - ADMINISTRATIF & ORGANISMES/07.3 - Locaux & services généraux`

## À quoi sert ce dossier

La vie quotidienne des locaux : sécurité, accès, maintenance, vérifications périodiques, consignes. Le bail est dans `02.4`, les contrats de fournisseurs (énergie, ménage, maintenance) dans `02.5` / `02.2`, l'assurance dans `06.2` ; ici les documents pratiques et réglementaires liés à l'occupation.

## Documents à y ranger

- Registre de sécurité (ERP / code du travail) : vérifications extincteurs, installations électriques, alarme, exercices d'évacuation
- Rapports de vérification périodique (électricité, gaz, ascenseur, climatisation), attestations de conformité
- Plans des locaux, plan d'évacuation, consignes de sécurité affichées
- Gestion des accès : attribution des clés, badges, codes (registre des remises et restitutions — sans les codes eux-mêmes)
- **Registre public d'accessibilité** (tout ERP, quel que soit l'effectif) : dispositions prises pour l'accessibilité, attestations, calendrier de maintenance — à tenir à l'entrée principale, sur papier ou en numérique
- **Déchets — tri à la source 8 flux** : papier, métaux, plastique, verre, bois, textiles, biodéchets et huiles alimentaires usagées (au-delà de 60 litres par an) ; pour le BTP s'y ajoute le plâtre. Dispense pour le papier si le site compte 20 personnes de bureau ou moins
- **Attestation annuelle de valorisation des déchets** fournie par le collecteur, distincte du registre
- **Registre de suivi des déchets** : quantité, nature, origine, destination, mode de traitement — à conserver 3 ans et à produire sur demande. Déclarer sur Trackdéchets dispense de tenir un registre séparé
- **Déclaration OPERAT** (décret tertiaire) si le site héberge des activités tertiaires sur 1 000 m² ou plus, y compris en location : identification des entités assujetties, justification de l'année de référence, relevés de consommation, attestation annuelle générée par la plateforme — déclaration à faire chaque année **avant le 30 septembre**
- Relevés de compteurs, courriers du syndic, incidents (fuite, panne) hors sinistre assuré

## Ne pas ranger ici

- Bail, états des lieux, charges → `02.4`
- Contrats énergie, télécom, ménage → `02.5`
- Assurance des locaux → `06.2`
- Matériel → `07.6`

## Méthode de classement

**Un sous-dossier par site** (`Siege`, `Atelier`), puis `Securite et verifications/AAAA`, `Plans et consignes`, `Acces`, `Services/AAAA`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Registre de sécurité : durée d'occupation + 5 ans. Rapports de vérification : 5 ans (jusqu'à la vérification suivante au minimum). |
| **Recommandé** | Durée d'occupation + 10 ans pour le registre de sécurité et les rapports. |

Base : Code du travail art. R4224-17, R4226-16 et s. ; Code de la construction et de l'habitation art. R143-44 (ERP) ; décret n° 2017-431 du 28 mars 2017 (registre public d'accessibilité) ; Code de l'environnement art. R541-43 et D543-284 (déchets) ; décret dit « tertiaire » et plateforme OPERAT.

## Conseils

- Le **registre public d'accessibilité** est distinct du registre de sécurité et s'impose à tout ERP, même une simple boutique ou un cabinet recevant des clients. Sanctions du volet accessibilité : jusqu'à 45 000 € pour une personne physique et 225 000 € pour une personne morale, fermeture administrative possible.
- On parle désormais de **8 flux** et non de 7 : les huiles alimentaires usagées ont été ajoutées. Les sanctions administratives et pénales se cumulent, jusqu'à 750 000 € pour une personne morale dans les cas les plus graves.
- **OPERAT est l'obligation que les PME locataires ignorent le plus souvent** : elle vise le bâtiment, pas le propriétaire, et une entreprise qui loue 1 000 m² de bureaux est assujettie. L'échéance est annuelle, au 30 septembre, et le non-respect conduit à une amende et à une publication sur un site public.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
