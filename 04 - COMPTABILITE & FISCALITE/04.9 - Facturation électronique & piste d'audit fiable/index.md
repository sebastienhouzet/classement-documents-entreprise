---
schema: classement-documents/3.0
id: "04.9"
parent: "04"
niveau: sous-dossier
titre: "04.9 - Facturation électronique & piste d'audit fiable"
usage: >-
  Factures électroniques émises et reçues au format structuré, statuts de cycle de vie, preuves
  de e-reporting et documentation de la piste d'audit fiable. Le dossier qui prouve la
  conformité à la réforme de la facturation électronique.
classement: chronologique
sensibilite: confidentielle
documents:
  - type: documentation-piste-audit-fiable
    libelle: "Documentation de la piste d'audit fiable"
    description: "Description des contrôles, des acteurs, des responsabilités, du calendrier, et de la façon dont chaque facture est reliée à la livraison sous-jacente. Document vivant, versionné."
    indices: ["piste d'audit fiable", paf, contrôles, responsabilités, rejet de facture, anomalie]
    champs: [date, reference, objet, signataire]
    nommage: "{date}_Piste-audit-fiable_{reference}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: derniere-operation
      base: CGI art. 289 VII 1°
      sort-final: D
    registre: null
  - type: export-statuts-cycle-de-vie
    libelle: Export des statuts de cycle de vie
    description: "Export périodique des statuts de cycle de vie des factures émises et reçues (déposée, rejetée, encaissée). Preuve fiscale."
    indices: [statut de cycle de vie, plateforme agréée, pa, pdp, export, déposée, rejetée]
    champs: [periode, plateforme, numero, quantite, statut-facture]
    nommage: "{periode}_Statuts-cycle-de-vie_{plateforme}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: LPF L102 B
      sort-final: D
    registre: null
  - type: preuve-e-reporting
    libelle: Preuve de e-reporting
    description: "Données de transaction et de paiement transmises à l'administration, avec leurs accusés."
    indices: [e-reporting, données de transaction, accusé, transmission, administration]
    champs: [periode, plateforme, organisme, numero, montant-ht]
    nommage: "{periode}_E-reporting_{plateforme}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: cloture-exercice
      base: LPF L102 B
      sort-final: D
    registre: null
  - type: immatriculation-plateforme-agreee
    libelle: "Preuve d'immatriculation de la plateforme agréée"
    description: "Relevé de la liste officielle publiée par l'administration, avec la date de consultation, et le paramétrage de routage (SIRET, annuaire)."
    indices: [plateforme agréée, pa, immatriculation, annuaire de facturation, siret, routage]
    champs: [date, plateforme, numero, reference]
    nommage: "{date}_Immatriculation-plateforme_{plateforme}"
    conservation:
      legale: 10a
      recommandee: 10a
      declencheur: date-document
      base: Décret n° 2026-677 et arrêté du 27 juillet 2026
      sort-final: D
    registre: null
va-ailleurs:
  - motif: Les factures elles-mêmes
    vers: "04.2"
  - motif: "Le logiciel de facturation ou de comptabilité, quand il n'est pas lui-même la plateforme agréée"
    vers: "02.5"
---

# 04.9 - Facturation électronique & piste d'audit fiable

> Chemin : `04 - COMPTABILITE & FISCALITE/04.9 - Facturation électronique & piste d'audit fiable`

## À quoi sert ce dossier

La réforme change la nature même de la facture : ce n'est plus un PDF qu'on classe, c'est un flux structuré qui transite par une plateforme agréée. Ce dossier réunit ce que la réforme oblige à conserver et qui n'a sa place ni dans les factures clients ni dans les factures fournisseurs : le dispositif lui-même, les preuves de son fonctionnement, et la piste d'audit fiable.

## Documents à y ranger

- Contrat avec la **plateforme agréée (PA)** — terme qui remplace « plateforme de dématérialisation partenaire » depuis le décret et l'arrêté du 27 juillet 2026 —, conditions tarifaires, engagements de service et surtout **durée de rétention contractuelle des flux**
- Identifiants de routage : SIRET, coordonnées d'annuaire, paramétrage des flux entrants et sortants
- Preuve de l'immatriculation de la plateforme, relevée sur la liste officielle publiée par l'administration, avec la date de consultation
- **Statuts de cycle de vie** des factures émises et reçues (déposée, rejetée, encaissée) : exports périodiques — ce sont des preuves fiscales
- **Preuves de e-reporting** : données de transaction et de paiement transmises à l'administration, et leurs accusés
- **Documentation de la piste d'audit fiable** : description des contrôles, acteurs, responsabilités, calendrier, et la façon dont on relie chaque facture à la livraison ou à la prestation sous-jacente
- Procédure de traitement des rejets et des anomalies
- Changement de plateforme : accord de portabilité daté et signé, preuves de reprise des flux
- Preuves de trajectoire de mise en conformité : échanges avec les prestataires, messages d'erreur, horodatages des tentatives, actions correctives

## Ne pas ranger ici

- Les factures elles-mêmes → `04.2` pour les clients, `04.3` pour les fournisseurs
- Le logiciel de facturation ou de comptabilité, quand il n'est pas lui-même la plateforme agréée → `02.5`

## Méthode de classement

Quatre sous-dossiers : `Plateforme agreee`, `Piste d'audit fiable`, `Exports/AAAA` (statuts de cycle de vie et e-reporting, au minimum un export par trimestre), `Incidents`. La documentation de la piste d'audit fiable est un document vivant : version en vigueur à la racine de son sous-dossier, précédentes dans `Anciennes versions`.

## Durée de conservation

| | |
|---|---|
| **Minimum légal** | Piste d'audit fiable : aussi longtemps que les factures qu'elle documente, soit 10 ans. Factures électroniques : conservées **dans leur format d'origine**, 10 ans au titre comptable comme au titre fiscal. |
| **Recommandé** | 10 ans, en conservant le **format natif** (XML, Factur-X) et non une simple impression PDF. |

Base : CGI art. 289 VII 1° (piste d'audit fiable) ; LPF art. L102 B ; Code de commerce art. L123-22 ; décret n° 2026-677 et arrêté du 27 juillet 2026 ; BOI-TVA-DECLA-30-20-30-20.

## Conseils

- La **piste d'audit fiable est obligatoire** dès lors qu'on n'utilise ni signature électronique qualifiée ni EDI conforme, et son absence expose à un refus de déduction de la TVA. Le niveau de détail attendu est proportionné à la taille de l'entreprise : pour une PME, quelques pages disant qui contrôle quoi, à quelle fréquence, et comment on relie une facture à sa livraison, suffisent.
- **Ne pas confondre transmission et archivage.** Une plateforme agréée transmet ; elle n'est pas juridiquement un service d'archivage à valeur probante. Vérifier au contrat combien de temps elle conserve les flux — c'est souvent très en deçà de dix ans — et organiser votre propre conservation. La responsabilité reste la vôtre.
- Une facture nativement électronique se conserve dans le format où elle a été émise ou reçue. Une impression PDF d'un fichier Factur-X n'est pas la facture, c'est une vue de la facture.
- L'administration a annoncé ne pas sanctionner automatiquement, pendant la phase de démarrage, les entreprises justifiant d'une trajectoire sérieuse de mise en conformité. D'où l'intérêt de garder ici la trace des difficultés rencontrées et des actions engagées.

---

Convention de nommage des fichiers : `AAAA-MM-JJ_Type_Tiers_Objet.ext` — voir `97 - REFERENTIEL/Convention-de-nommage.md`.
