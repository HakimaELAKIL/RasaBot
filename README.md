🧠 Projet Rasa – Assistant Intelligent (Réservation de Vols)

Ce projet met en place un assistant conversationnel basé sur Rasa
.
Il est conçu pour aider les utilisateurs à réserver un vol en comprenant leurs demandes en langage naturel et en guidant l’interaction étape par étape.

🎯 Objectifs du projet

Permettre aux utilisateurs de chercher et réserver un vol (ville de départ, ville d’arrivée, date, nombre de passagers…).

Reconnaître les intentions et entités liées à la réservation (par ex. : book_flight, departure_city, arrival_city, date, passengers).

Guider l’utilisateur avec des questions contextuelles pour compléter les informations manquantes.

Intégrer des actions personnalisées pour se connecter à un service ou une API de vols.

Fournir des réponses naturelles et contextualisées.

🗂 Structure du projet
├── actions/              # Actions personnalisées en Python (connexion à une API de vols)
├── data/                 # Données d'entraînement (intents book_flight, cancel_flight…)
├── domain.yml            # Intents, entités, slots, réponses, actions
├── endpoints.yml         # Configuration des endpoints (API, tracker store)
├── credentials.yml       # Canaux d'intégration (REST, Telegram, Slack…)
├── models/               # Modèles entraînés
├── tests/                # Scénarios de test automatisés
└── README.md             # Documentation du projet
