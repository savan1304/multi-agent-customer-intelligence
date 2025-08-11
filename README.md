# Multi-Agent Customer Intelligence System (Completed System)

This project is a complete, end-to-end simulation of a multi-agent system designed to proactively reduce customer churn. It uses n8n for workflow automation and Google Gemini as the intelligent core for multiple, specialized AI agents that collaborate to analyze, strategize, and act on customer data.

This system demonstrates a sophisticated, real-world business automation process, moving beyond simple analysis to intelligent, automated intervention.

---

## ► How It Works: The End-to-End Process

The system operates on an automated workflow that intelligently routes customers based on their behavior and sentiment, ensuring that action is only taken when necessary.

              +--------------------+
              | 1. Load Customer   |
              |    Data            |
              +--------------------+
                       |
                       v
              +--------------------+
              | 2. Sentiment       |
              |    Analysis Agent  |
              +--------------------+
                       |
                       v
              +--------------------+
              | 3. Risk Scoring    |
              |    Agent (Rules)   |
              +--------------------+
                       |
  +--------------------+--------------------+
  | (High/Medium Risk) |      (Low Risk)    |
  v                    v                    v
+--------------------+  +--------------------+  +----------------+
| 4. Intervention    |  | 5. Automated       |  | No Action      |
|    Design Agent    |  |    Outreach Agent  |  | Needed         |
+--------------------+  +--------------------+  +----------------+
|                           |
| (High Risk) -> Creates Urgent Task
|
+-------------> (Medium Risk) -> Sends Proactive Email


---

## ► The Agents

This system is composed of several specialized agents, each with a distinct role:

* **Sentiment Analysis Agent:** The first point of analysis. It reads unstructured text from support tickets and determines the customer's emotional state (Positive, Negative, Neutral).
* **Risk Scoring Agent:** A logic-based agent that acts as an analyst. It uses the sentiment and other metadata (like last login date) to classify the customer's churn risk into High, Medium, or Low tiers.
* **Intervention Design Agent:** The creative strategist. For at-risk customers, this agent uses the full context to generate a personalized, empathetic email draft designed to resolve the customer's issue and retain their business.
* **Automated Outreach Agent:** The final action-taker. This agent executes the intervention designed by the previous agent, routing it to the appropriate channel (e.g., creating a high-priority task in a CRM for high-risk cases, or sending an automated email for medium-risk cases).

---

## ► Tech Stack

* **Orchestration**: [n8n.io](https://n8n.io/) - The low-code platform used to build and automate the entire multi-agent workflow.
* **Intelligence**: [Google Gemini](https://ai.google.dev/) - The LLM used as the "brain" for the Sentiment and Intervention Design agents.
* **Logic**: n8n Switch Node - Used to implement the rule-based Risk Scoring agent.
* **Data**: CSV file containing synthetic customer data.
* **Deployment**: Self-hosted on a local machine (Ubuntu).

---

## ► Setup & Usage

**1. Prerequisites:**
* You must have Node.js and n8n installed globally.
* You need a Google Gemini API key from [Google AI Studio](https://ai.google.dev/).

**2. Install the Gemini Community Node:**
    This project requires the `n8n-nodes-google-gemini` community node. If you don't have it, shut down n8n and run:
    ```bash
    npm install n8n-nodes-google-gemini
    ```
    Then restart n8n.

**3. Import the Workflow:**
* Download the `n8n/workflow.json` file from this repository.
* In n8n, import the `workflow.json` file.

**4. Configure Credentials:**
* Open the imported workflow. You will see two **Google Gemini** nodes.
* For each one, select your pre-configured Gemini credential.

**5. To Use:**
* Click the **"Execute Workflow"** button.
* Observe the output. You will see the different sample customers being routed down the different paths of the Switch node. Check the output of the final nodes to see the simulated email drafts and CRM tasks.