# 🧠 Rasa Project – Intelligent Assistant (Flight Booking)

> A smart conversational assistant built with [Rasa](https://rasa.com/) to help users **book flights** and understand their requests step by step in natural language.

---

## 🎯 Project Goals
- Enable users to **search and book a flight** (departure city, arrival city, date, number of passengers…)
- **Recognize intents and entities** related to booking (e.g. `book_flight`, `departure_city`, `arrival_city`, `date`, `passengers`)
- Guide the user with **contextual questions** to complete missing information
- Integrate **custom actions** to connect to flight services or APIs
- Provide **natural and contextual answers** in English or Arabic

---

## 🗂 Project Structure
```bash
├── actions/              # Custom Python actions (API calls, business logic)
├── data/                 # Training data (intents: book_flight, cancel_flight …)
├── domain.yml            # Intents, entities, slots, responses, actions
├── endpoints.yml         # Endpoints configuration (API, tracker store)
├── credentials.yml       # Channels configuration (REST, Telegram, Slack …)
├── models/               # Trained models
├── tests/                # Automated test scenarios
└── README.md             # Project documentation
```
## ⚙️ Running the Project
- Train the model
```bash
rasa train
```

- Run the main server
```bash
rasa run
```

- Run the custom actions server
```bash
rasa run actions
```

- Test the assistant in the shell
```bash
rasa shell
```
