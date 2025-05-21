# BrainBucks Chatbot

A conversational AI chatbot built using **RASA** for BrainBucks, designed to provide intelligent, interactive user assistance. This project demonstrates building a custom chatbot capable of handling user queries, managing dialogs, and integrating with backend services via custom actions.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Customization](#customization)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

BrainBucks chatbot leverages the open-source RASA framework to create an intelligent agent that understands natural language, manages conversation flow, and performs specific tasks through custom actions. This chatbot can be used in educational, IT, or customer support scenarios.

---

## Features

- Natural Language Understanding (NLU) with custom intents and entities.
- Dialogue management with stories and rules.
- Custom actions for backend logic and API integration.
- Multi-channel support potential (e.g., web, Slack).
- Dockerized setup for easy deployment.
- Configurable via YAML files (`domain.yml`, `config.yml`, etc.).

---

## Tech Stack

- **RASA Open Source**: NLU and Dialogue Management.
- **Python**: Custom actions and backend logic.
- **Docker**: Containerized environment.
- **YAML**: Configuration files for intents, stories, and domain.
- **JavaScript/HTML**: for frontend integration.

---


---

## 💻 Installation and Setup

### (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

### Install dependencies:

```bash
pip install -r requirements.txt
pip install -r requirements_actions.txt
```

### Train the chatbot model:

```bash
rasa train
```

### Run the action server (in a new terminal):

```bash
rasa run actions
```

### Run the chatbot server:

```bash
rasa shell
```
or

```bash
rasa run
```

---

## 💬 Usage

- Interact with the chatbot through the command line interface or integrate it with channels like Web UI, Telegram, etc.
- Customize intents and responses in the `data/` folder.
- Update or add new Python functions in the `actions/` directory to perform tasks like querying databases or calling APIs.
- Improve and validate the conversation design using interactive learning:

```bash
rasa interactive
```

---

## 📁 Project Structure

```
rasa/
├── actions/                 # Custom Python actions
├── data/                    # Training data (NLU, stories)
├── models/                  # Trained models
├── tests/                   # Test cases
├── config.yml               # RASA pipeline and policies config
├── domain.yml               # Intents, entities, slots, responses, actions
├── endpoints.yml            # Endpoints for action server, trackers
├── credentials.yml          # Channel credentials
├── docker-compose.yml       # Docker Compose setup
├── Dockerfile               # Docker image config
├── requirements.txt         # Python dependencies for core
├── requirements_actions.txt # Python dependencies for actions
└── README.md                # Project overview and instructions
```

---

## ✏️ Customization Guide

- **Intents/Entities**: Add or update in `data/nlu.yml`
- **Dialogues**: Add stories in `data/stories.yml` or rules in `data/rules.yml`
- **Actions**: Define Python logic in `actions/actions.py`
- **Domain Config**: Reflect changes in `domain.yml` (intents, responses, slots, etc.)

---

## ✅ Testing

Add test stories to the `tests/` folder and use the RASA CLI to test:

```bash
rasa test
```

---

## 🚀 Deployment

You can containerize and deploy the chatbot using Docker:

```bash
docker-compose up --build
```

Also deployable to AWS EC2, Azure App Service, Google Cloud Run, or on-prem servers.

---

## 🤝 Contributing

We welcome contributions to improve this chatbot! Steps to contribute:

1. Fork the repository
2. Create a new branch:  
   `git checkout -b feature-name`
3. Commit your changes:  
   `git commit -m "Add new feature"`
4. Push to your fork:  
   `git push origin feature-name`
5. Create a Pull Request

---

## 📜 License

Specify your license here (e.g., MIT License). If none provided, default to private/internal use only.

---
   git clone https://github.com/Nikitajain121/rasa.git
   cd rasa
