#  Projet Rasa - Assistant Intelligent

Ce projet est une implémentation d’un assistant conversationnel utilisant [Rasa](https://rasa.com/), un framework open source pour le traitement du langage naturel (NLP) et les dialogues basés sur l’apprentissage machine.

---

##  Structure du projet

```bash
├── actions/              # Actions personnalisées (Python)
├── data/                 # Données d'entraînement (nlu.yml, stories.yml, rules.yml)
├── domain.yml            # Définition des intentions, entités, réponses, actions...
├── endpoints.yml         # Configuration des endpoints pour actions, tracker store, etc.
├── credentials.yml       # Configuration des canaux (e.g. REST, Telegram, etc.)
├── models/               # Modèles entraînés (générés localement, non suivis par Git)
├── tests/                # Scénarios de test
└── README.md             # Ce fichier
