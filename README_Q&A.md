# 🔍 RASA + OpenAI + PostgreSQL Integration - Interview Q&A

## 📦 Q1: How is the OpenAI API key managed in the code?
**Answer:**  
The API key is retrieved using `os.getenv("OPENAI_API_KEY")`, which assumes the key is stored as an environment variable.  
This avoids hardcoding sensitive credentials.

---

## 🤖 Q2: What is the purpose of `ActionHandleOutOfContext`?
**Answer:**  
This custom action sends the user's message to the OpenAI API and returns the generated response.  
It is useful for handling fallback or general-purpose questions not covered by predefined intents.

---

## 🧠 Q3: What model is used for the OpenAI chat completion?
**Answer:**  
`gpt-3.5-turbo-0125` is used in the `ActionHandleOutOfContext` class for generating the response.

---

## 📇 Q4: What does `DataUpdate(user_name, phone)` do?
**Answer:**  
This function connects to a PostgreSQL database and inserts a record into the `t1` table using the provided `user_name` and `phone`.

---

## 🛡️ Q5: What are best practices followed for DB connection?
**Answer:**
- Uses `try-except-finally` for error handling and resource cleanup.
- Commits the transaction after insertion.
- Closes cursor and connection in the `finally` block.

---

## 🧩 Q6: Why is `SlotSet` used in `ActionGetUserName`?
**Answer:**  
`SlotSet("name", name)` is used to store the extracted name into a slot, which allows RASA to remember user information during the conversation.

---

## 🗃️ Q7: What is the role of `Tracker.get_latest_entity_values("name")`?
**Answer:**  
It extracts the most recent value for the entity `"name"` from the user input, which is used to update the slot and database.

---

## ❗ Q8: What happens if the name is not detected in `ActionGetUserName`?
**Answer:**  
If no name is found, the bot prompts the user with `"What is your name?"`, and returns an empty list (no slot updates).

---

## 🧪 Q9: What error is specifically caught in `DataUpdate`?
**Answer:**  
`psycopg2.OperationalError`, which usually indicates issues with connecting to the PostgreSQL database.

---

## 📈 Q10: How does `ActionHandleOutOfContext` structure messages for OpenAI?
**Answer:**  
It creates a list of message dicts for system and user roles:

messages = [
    {"role": "system", "content": "You answer question about given data"},
    {"role": "user", "content": user_message},
]

# 🧠 Custom RASA Actions – Q&A

### 📬 Q11: How does `dispatcher.utter_message` work?  
**Answer:**  
It's used to send a text response back to the user from a custom action.

---

### 📌 Q12: Where should the `.env` file be placed and why is it used?  
**Answer:**  
It should be in the root directory of the RASA project. It's used to store secrets like API keys without exposing them in code.

---

### 🛠️ Q13: How is modularization achieved in this project?  
**Answer:**  
- `actions.py`: Contains all action logic (OpenAI integration, slot setting).  
- `db.py`: Contains database utility functions.  
- Uses `from .module import function` for cleaner code reuse.

---

### 🧩 Q14: What would happen if `SlotSet("name", name)` is not returned?  
**Answer:**  
The slot would not be updated in the tracker memory, and subsequent actions would not have access to the user's name.

---

### 🧠 Q15: How can OpenAI usage be optimized for costs and latency?  
**Answer:**  
- Use `temperature=0` for deterministic output.  
- Choose smaller models (e.g., `gpt-3.5`) over `gpt-4` for routine tasks.  
- Avoid sending unnecessary system messages.

---

### 📊 Q16: What table is data inserted into and what fields are required?  
**Answer:**  
- **Table:** `t1`  
- **Fields:** `user_name`, `phone`  
- **SQL:**  
  ```sql
  INSERT INTO t1 (user_name, phone) VALUES (%s, %s)


---

### 📑 Q17: Why are `print` statements used throughout the actions?  
**Answer:**  
To provide debug checkpoints (e.g., `Checkpost-111111`) for tracing the execution flow during development.

---

### 🔁 Q18: Can this code be extended to retrieve data?  
**Answer:**  
Yes, you can extend `db.py` with `SELECT` statements and return values in a similar fashion using `cursor.fetchall()`.

---

### 🔐 Q19: What are the security risks in the current database code?  
**Answer:**  
- DB credentials are hardcoded — should be moved to environment variables.  
- No SQL injection risk in this code due to parameterized queries, but caution is needed elsewhere.

---

### 🧹 Q20: How could error handling be improved?  
**Answer:**  
- Catch and log all exceptions, not just `OperationalError`.  
- Return meaningful error messages to users and logs.  
- Use connection pooling if scaled.

---

### 📘 Q21: What is the purpose of the `nlu.yml` file?
**Answer:**  
It contains training examples for user intents and synonyms. It helps RASA's NLU component classify user input correctly and map synonymous terms.

---

### 🔍 Q22: What are synonyms used for in `nlu.yml`?
**Answer:**  
Synonyms help normalize different expressions to a common value.  
E.g., all forms like "BB coin", "virtual currency", etc., are mapped to `bb_money`.

---

### 💬 Q23: How does RASA use the `rules.yml` file?
**Answer:**  
`rules.yml` defines strict, single-turn conversations.  
Example:

- rule: Respond to utter_recorded_class_response
  steps:
  - intent: ask_recorded_class
  - action: utter_recorded_class_response

---

### 🔁 Q24: How do rules differ from stories?
**Answer:**

- **Rules**: One-turn or simple predictable paths. Used for FAQs or fixed logic.  
- **Stories**: Multi-turn conversations that reflect real user interactions.

---

### 📖 Q25: What happens in the `interactive_story_1` story?
**Answer:**  
This story handles greeting the user, extracting their name and phone number, and saving it. Steps include:
1. User greets → bot replies.  
2. User provides name → slot is set.  
3. Bot asks for phone → user replies.  
4. Slot is set → data is saved using a custom action.

---

### ⚙️ Q26: What is the purpose of `action_extract_slots` and `action_save_data`?
**Answer:**

- `action_extract_slots`: Extracts user input entities and sets them to slots.  
- `action_save_data`: Custom action that likely saves user data (e.g., name, phone) to a database.

---

### 📦 Q27: Can one intent be reused in multiple stories or rules?
**Answer:**  
Yes. Intents like `get_user_name` or `greet` can appear in multiple stories/rules to model different conversation flows.

---

### 🛠️ Q28: How would you make `ask_recorded_class` intent more robust?
**Answer:**

- Add more diverse training examples.  
- Ensure `utter_recorded_class_response` is relevant.  
- Validate via RASA NLU interactive mode or tests.

---

### 🔐 Q29: What is the risk of overlapping intent examples like "BB coin?"?
**Answer:**  
Overlapping examples between intents can confuse the classifier. It’s important to:
- Add clear, distinct examples.  
- Use `rasa test nlu` and `rasa data validate` to detect confusion.

---

### 🔄 Q30: What is the best practice for writing stories?
**Answer:**

- Keep stories modular and focused on specific use cases.  
- Avoid repetition — use rules for simple paths.  
- Use checkpoints or story fragments for reusable sequences.  
- Test frequently with `rasa interactive` and `rasa test`.

---

## 🐳 Docker & CI/CD - Rasa Bot Deployment QnA

### 🔁 Q31: What is the purpose of the main `Dockerfile` in the Rasa project?
**Answer:**  
The main Dockerfile sets up the environment to run the Rasa chatbot. It:
- Uses Python 3.8.10 slim as the base image.
- Installs Python dependencies from `requirements.txt`.
- Copies the Rasa project files into the container.
- (Optionally) includes commands to train the model or run the Rasa server.

---

### ⚙️ Q32: What does the Rasa custom action Dockerfile (`actions` folder) do?
**Answer:**  
It builds a Docker container specifically for the custom action server:
- Base image: `rasa/rasa-sdk:3.6.2`.
- Installs dependencies listed in `requirements_actions.txt`.
- Copies the `actions/` folder into the image.
- Switches from root to a safer non-root user (`1001`) to run the container.

---

### 🔄 Q33: Why is a separate Dockerfile used for custom actions?
**Answer:**  
To isolate the action server from the main Rasa chatbot. This ensures:
- Cleaner deployment pipelines.
- Smaller images per service.
- Custom dependencies only in the action server.

---

### 🔐 Q34: What does the `USER 1001` line mean in Dockerfiles?
**Answer:**  
It switches from the default `root` user to a non-root user (`1001`) to follow Docker security best practices. This prevents accidental file or system modifications by running the container with limited permissions.

---

### 🚀 Q35: What is the role of `action_server.yml` GitHub Actions workflow?
**Answer:**  
It automates building and deploying the custom action server Docker image:
- Triggers on `push` to the `main` branch.
- Uses `RasaHQ/action-server-gha` GitHub Action to:
  - Build the Docker image.
  - Push it to DockerHub using credentials stored in GitHub secrets.

---

### 🧠 Q36: How can you tag your Docker image using GitHub Actions?
**Answer:**  
Using `${{ github.sha }}` assigns the image a unique tag based on the commit hash, which helps track and rollback to specific versions.

---

### 🔁 Q37: What files are critical to the Docker-based Rasa deployment?
**Answer:**  
- `Dockerfile` – for the main Rasa server.
- `requirements.txt` – Python dependencies for Rasa bot.
- `requirements_actions.txt` – dependencies for custom actions.
- `Dockerfile` in `/actions/` – builds action server image.
- `.github/workflows/action_server.yml` – CI/CD pipeline for deployment.

---

### 📦 Q38: Why is `COPY . .` used in the Dockerfile?
**Answer:**  
It copies all local project files into the container’s working directory (`/src`) so the Rasa bot can access training data, configuration, and models inside the container.

---


