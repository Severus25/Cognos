# Project: "Cognos" - The ReAct-Powered Reasoning Agent

## 🚀 Overview

Cognos is a production-level AI agent built on the powerful **"ReAct" (Reason + Act)** framework. Unlike traditional models that provide an immediate answer, Cognos externalizes its reasoning process. It analyzes complex problems, creates a multi-step plan, executes actions using a suite of tools (like web search and a calculator), and observes the results to adjust its plan until the final answer is found.

This project is an ideal showcase for a startup interview, as it demonstrates the ability to build sophisticated, autonomous AI systems that can solve real-world problems requiring more than just text generation.

---

## ✨ Core Concepts & Skills Demonstrated

- **ReAct Framework:** Masterful implementation of the "Thought, Action, Observation" loop, the cornerstone of modern agentic AI.
- **Dynamic Tool Use:** The agent intelligently selects from a suite of tools (web search, calculator) based on its reasoning to solve a given sub-task.
- **Complex Task Decomposition:** Cognos can break down a complex, multi-hop question into a series of simpler, actionable steps.
- **Agentic Thinking:** The `verbose=True` output makes the agent's "thought process" visible, providing a clear demonstration of its ability to reason, plan, and self-correct.
- **Production-Ready Code:** The project is organized with a modular architecture, dependency management (`requirements.txt`), and secure key management (`.env`), showcasing professional software engineering practices.

---

## ⚙️ How It Works: The "ReAct" Loop

Cognos operates on a continuous cycle until it arrives at a final answer:

1.  **Thought:** Based on the user's query, the LLM thinks about what it needs to do next. It considers its goal and the tools it has available.
2.  **Action:** The agent chooses a tool (e.g., `Search` or `Calculator`) and formulates an input for that tool.
3.  **Observation:** The `AgentExecutor` runs the tool with the provided input and returns the result (e.g., a search result or a calculated number).
4.  **Repeat:** The observation is fed back to the LLM. It then begins the next `Thought` step, incorporating its new knowledge, and continues the cycle until it has enough information to give a final answer.

---

## 🛠️ Setup and Execution

### Prerequisites

- Python 3.8+
- A Google Gemini API Key

### Installation

1.  **Clone the repository and navigate into it:**

    ```bash
    git clone <your-repo-link>
    cd cognos_project
    ```

2.  **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install all required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your API Key:**
    Create a file named `.env` in the `cognos_project` directory and add your Google Gemini API key:
    ```
    GOOGLE_API_KEY="your-gemini-api-key"
    ```

### Running the Application

To run Cognos and see the ReAct process in action, simply execute the `main.py` script:

```bash
python main.py
```
