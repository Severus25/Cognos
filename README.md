<div align="center">
  <br />
  <h1>🤖 Cognos</h1>
  <h3>A Production-Ready AI Agent powered by the ReAct Framework</h3>
  <p>
    An intelligent agent that can reason, plan, and dynamically use tools to solve complex, multi-step problems that require more than just text generation.
  </p>
</div>

<div align="center">

![Language](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Framework](https://img.shields.io/badge/LangChain-0.1.20-purple.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

</div>

---

## 🚀 Overview

> Cognos is a production-level AI agent built on the powerful **"ReAct" (Reason + Act)** framework. Unlike traditional models that provide an immediate answer, Cognos externalizes its reasoning process. It analyzes complex problems, creates a multi-step plan, executes actions using a suite of tools (like web search and a calculator), and observes the results to adjust its plan until the final answer is found.

This project is an ideal showcase for a startup interview, as it demonstrates the ability to build sophisticated, autonomous AI systems that can solve real-world problems.

## ✨ Core Features & Skills Demonstrated

| Feature                  | Description                                                                                                                              |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **🧠 ReAct Framework**     | Masterful implementation of the **Thought -> Action -> Observation** loop, the cornerstone of modern agentic AI.                        |
| **🛠️ Dynamic Tool Use**      | The agent intelligently selects from a suite of tools (web search, calculator) based on its reasoning to solve a given sub-task.      |
| **🔗 Complex Decomposition** | Cognos can break down a complex, multi-hop question into a series of simpler, actionable steps.                                        |
| **👁️ Transparent Reasoning** | `verbose=True` output makes the agent's "thought process" visible, providing a clear audit trail of its plan.                           |
| **✅ Production-Ready**    | Organized with a modular architecture, dependency management (`requirements.txt`), and secure key management (`.env`).                   |

---

## ⚙️ How It Works: The ReAct Loop

Cognos operates on a continuous cycle until it arrives at a final answer. This iterative process allows it to build context and refine its approach at each step.

<p align="center">
  <img src="https://i.imgur.com/v14D35D.png" alt="ReAct Loop Diagram" width="700"/>
</p>

1.  **Thought:** Based on the user's query, the LLM thinks about what it needs to do next. It considers its goal and the tools it has available.
2.  **Action:** The agent chooses a tool and formulates an input for it.
3.  **Observation:** The `AgentExecutor` runs the tool and returns the result.
4.  **Repeat:** The observation is fed back to the LLM. It then begins the next `Thought` step, incorporating its new knowledge, and continues the cycle until it has enough information to give a final answer.

---

## 🤖 Sample Walkthrough

This example shows the agent's "chain of thought" as it tackles a problem that requires both searching for information and performing calculations.

**User Query:**
`What was the stock price of NVIDIA (NVDA) at the close of its IPO date, and how many times greater is its current stock price compared to that initial price?`

**Agent Execution Log:**
```shell
> Entering new AgentExecutor chain...

🤔 Thought: I need to find two pieces of information: NVIDIA's IPO closing price and its current stock price. After I have both values, I need to perform a division to find out how many times greater the current price is. I will start by finding the IPO price.
⚡ Action: Search
Action Input: "NVIDIA (NVDA) IPO date and price"

👀 Observation: NVIDIA (NVDA) went public on January 22, 1999, at a price of $12 per share. Due to multiple stock splits over the years, the split-adjusted IPO price is approximately $0.40.

🤔 Thought: I have found the split-adjusted IPO price, which is $0.40. This is the correct value to use for a fair comparison. Now, I need to find the current stock price of NVIDIA.
⚡ Action: Search
Action Input: "current stock price of NVIDIA (NVDA)"

👀 Observation: As of July 2025, the stock price for NVIDIA Corporation (NVDA) is approximately $131.88.

🤔 Thought: I have both the split-adjusted IPO price ($0.40) and the current price ($131.88). Now I must use the Calculator to find out how many times greater the current price is than the IPO price.
⚡ Action: Calculator
Action Input: 131.88 / 0.40

👀 Observation: Answer: 329.7

🤔 Thought: I have successfully found the IPO price, the current price, and performed the calculation to compare them. I now have the final answer.
✅ Final Answer: NVIDIA's split-adjusted IPO price was approximately $0.40 per share. Its current price is about $131.88, which is approximately 329.7 times greater than the initial price.

> Finished chain.
```
---

## 🛠️ Setup and Execution

### Prerequisites

*   Python 3.8+
*   A Google Gemini API Key

### Installation

1.  **Clone the repository and navigate into it.**
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

Execute the `main.py` script to see Cognos reason in real-time:
```bash
python main.py
Use code with caution.
Generated code
Use code with caution.
18.0s
