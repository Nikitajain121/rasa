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

## ⚙️ Rasa `config.yml` QnA

### 🔁 Q39: What is the purpose of the `pipeline` section in `config.yml`?
**Answer:**  
It defines the sequence of components used for Natural Language Understanding (NLU), such as tokenization, featurization, intent classification, and entity extraction.

---

### 🧩 Q40: What does the `WhitespaceTokenizer` component do?
**Answer:**  
It splits the user input into tokens based on whitespace, preparing the text for further processing.

---

### 🔍 Q41: How does the `RegexFeaturizer` help in NLU?
**Answer:**  
It extracts features from user inputs by matching predefined regular expressions, helping detect patterns in the text.

---

### 🕸️ Q42: What is the role of `CRFEntityExtractor`?
**Answer:**  
It uses Conditional Random Fields (CRF) to extract entities by considering the context and sequence of tokens, improving entity recognition accuracy.

---

### 🔄 Q43: What is the function of `EntitySynonymMapper`?
**Answer:**  
It maps different entity values to a canonical synonym, ensuring consistency in how entities are handled internally.

---

### 📊 Q44: Why use `CountVectorsFeaturizer` with `analyzer: "char_wb"` and n-grams?
**Answer:**  
This featurizer creates vector representations based on character n-grams within word boundaries, capturing subword information useful for recognizing typos or variations.

---

### 🧠 Q45: What does the `DIETClassifier` component do?
**Answer:**  
It is a transformer-based classifier that jointly performs intent classification and entity extraction, providing efficient and accurate predictions.

---

### 🧭 Q46: How does `FallbackClassifier` improve conversation flow?
**Answer:**  
It triggers fallback actions when the confidence of intent recognition falls below the specified threshold (0.4), helping handle unclear user inputs gracefully.

---

### 📜 Q47: What is the role of `RulePolicy` in the `policies` section?
**Answer:**  
It manages simple and predictable conversation flows (rules), including fallback handling based on confidence thresholds.

---

### 🔄 Q48: Why is `MemoizationPolicy` important?
**Answer:**  
It remembers previous conversation turns and helps the bot predict the next action based on exact dialogue history matches, useful for replicating story flows.

---

### 📝 Q49: Why is `SpacyNLP` and `SpacyEntityExtractor` included?
**Answer:**  
`SpacyNLP` provides a pretrained language model for better text processing, while `SpacyEntityExtractor` leverages SpaCy’s entity recognition to extract entities like PERSON.

---

### 🎯 Q50: What is the significance of setting epochs for `DIETClassifier` and `ResponseSelector` to 150?
**Answer:**  
More epochs generally mean more training iterations, which can improve model accuracy but increase training time. Here, both are set to 150 to balance performance.

---

### 🔍 Q51: What is the difference between `ResponseSelector` and `DIETClassifier`?
**Answer:**  
- `DIETClassifier`: Used for intent classification and entity extraction.  
- `ResponseSelector`: Used to classify user inputs into predefined response templates, useful for FAQs or chitchat.

---

### ⚠️ Q52: Why might the `FallbackClassifier` threshold be set at 0.4?
**Answer:**  
A threshold of 0.4 means the bot will trigger fallback if intent confidence is below 40%, balancing between false positives and catching uncertain inputs.

---

### 🧩 Q53: What are the commented-out lines about in the config file?
**Answer:**  
They show alternative or previous pipeline configurations and provide notes on the role of certain components like CRF, lexical-syntactic featurizer, and vectorizers.

---

### 📌 Q54: What does the `version: "3.1"` specify?
**Answer:**  
It indicates the version of the Rasa configuration schema to ensure compatibility with the Rasa framework.

---
# Why Use Particular Policies in Rasa? Q&A

---

### Q1: Why did you use `RulePolicy` in the config.yml?

**Answer:**  
`RulePolicy` is used to handle simple, predictable conversation paths such as FAQs, greetings, or fallback handling. It allows defining explicit conversational rules that must be strictly followed and ensures fallback actions are triggered when confidence falls below a threshold (0.4).

**Example:**  
User asks "What are your hours?" → Bot replies with a fixed answer using a rule.

---

### Q2: Why did you use `MemoizationPolicy` in the config.yml?

**Answer:**  
`MemoizationPolicy` remembers exact conversation turn histories and predicts the next action if the current state matches a memorized sequence. It is effective for short, repetitive multi-turn dialogues and predefined stories.

**Example:**  
User says "Hi" → Bot replies "Hello, how can I help?" → User asks about pricing → Bot replies with pricing info. This exact sequence is memorized for quick response prediction.

---

### Q3: Why not use other policies like `TEDPolicy` or `AugmentedMemoizationPolicy`?

**Answer:**  
- **TEDPolicy** is transformer-based and better for complex, flexible dialogues requiring generalization but is more resource-intensive.  
- **AugmentedMemoizationPolicy** offers some generalization but adds complexity.  
- Your bot’s current requirements are simpler and don’t need these advanced policies yet.

---

### Q4: Why avoid deprecated or less flexible policies like `FallbackPolicy` or `MappingPolicy`?

**Answer:**  
- `FallbackPolicy` is deprecated and replaced by the fallback mechanism in `RulePolicy`.  
- `MappingPolicy` is less flexible, mainly used for direct intent-action mappings in simple bots, which may not suit more dynamic conversations.

---

### Q5: When should you consider switching or adding other policies?

**Answer:**  
- When your bot needs to handle **complex conversations** that are not predictable or memorized.  
- If you want the bot to **generalize to unseen user inputs** better.  
- When working with **large dialogue datasets** or requiring transformer-based prediction.

---

### Summary Table

| Policy                | Purpose                                  | Why Used / Not Used Here                         |
|-----------------------|------------------------------------------|-------------------------------------------------|
| `RulePolicy`          | Handle simple rules and fallback        | Used for predictable flows and fallback control |
| `MemoizationPolicy`   | Memorize exact conversation sequences   | Used for fast, accurate prediction in known flows |
| `TEDPolicy`           | Transformer-based, flexible dialogs     | Not used due to complexity and resource needs    |
| `AugmentedMemoizationPolicy` | Mix of memoization + generalization | Not needed for current bot complexity            |
| `FallbackPolicy`      | Old fallback mechanism                   | Deprecated, replaced by `RulePolicy`             |
| `MappingPolicy`       | Direct intent to action mapping          | Less flexible, avoided for richer conversations  |

---


# RASA domain.yml - Technical Interview Analysis

---

## 1. Intents Definition

- The `intents` list is well-structured and covers diverse user queries (e.g., `course_queries`, `about_company`, `earn_bb_money`, etc.).
- **Best Practice:** Intents should be **mutually exclusive** and cover typical user needs.
- **Example Interview Question:**  
  *How would you design intents for a multi-domain chatbot?*  
  **Answer:** Group related intents logically, avoid overlap, and consider hierarchical intent classification if needed.

---

## 2. Responses

- Responses (`utter_*`) include both text and **buttons**, enhancing user experience by guiding replies.
- Using buttons helps reduce input ambiguity and speeds up interaction.
- **Example Interview Question:**  
  *Why use buttons in chatbot responses?*  
  **Answer:** Buttons constrain user inputs, reduce errors, and provide clear navigation choices.

---

## 3. Reusability

- Many responses reuse the same set of buttons, ensuring consistency.
- **Improvement:** To avoid repetition, consider using custom actions or templates to generate buttons dynamically.
- **Example Interview Question:**  
  *How do you maintain DRY (Don't Repeat Yourself) principles in RASA?*  
  **Answer:** By using custom actions, reusable templates, or forms to share logic and UI components.

---

## 4. Versioning

- The domain specifies `version: '3.1'` for compatibility with RASA framework updates.
- **Example Interview Question:**  
  *Why is specifying version important in the domain file?*  
  **Answer:** It ensures the domain file is compatible with the specific RASA version and avoids unexpected errors.

---

## 5. Scalability Considerations

- Many similar intents (e.g., `query_exam_upsc`, `query_exam_ssc`) can lead to sparse training data.
- **Suggestion:** Use a general intent like `query_exam` combined with entities (e.g., `exam_type`) to reduce the intent count and improve NLU performance.
- **Example Interview Question:**  
  *How do you handle numerous related intents efficiently?*  
  **Answer:** Combine intents using entities to represent variable parts, improving model scalability and accuracy.

---

## 6. Fallback and Error Handling

- `utter_default` is defined to handle fallback situations when the bot doesn’t understand user input.
- **Example Interview Question:**  
  *How does fallback handling improve chatbot experience?*  
  **Answer:** It allows the bot to gracefully manage unexpected inputs and guide users back on track.

---

## 7. Entities and Slots

- The current domain file lacks **entities** and **slots**, which are important for capturing user information and maintaining context.
- **Example Interview Question:**  
  *What are entities and slots in RASA, and why are they important?*  
  **Answer:** Entities extract key data from user messages; slots store these values to track conversation context and customize responses.

---

## Summary Table

| Aspect              | Observation / Best Practice                   | Potential Improvement                      | Interview Question                             |
|---------------------|-----------------------------------------------|-------------------------------------------|------------------------------------------------|
| Intents             | Clear and diverse                             | Consolidate related intents using entities | How to design intents for scalability?          |
| Responses & Buttons | Use buttons for guided user input             | Use reusable components or custom actions  | Benefits of buttons in chatbot conversations     |
| Versioning          | Domain version specified                      | N/A                                       | Why specify version in RASA domain file?          |
| Fallback Handling   | Defined fallback response                      | Customize fallback policy                   | How to handle unrecognized inputs effectively?   |
| Entities & Slots    | Not defined in current domain                  | Add entities and slots for context tracking | What is the role of entities and slots in RASA?  |

---





