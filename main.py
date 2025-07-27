import os
from dotenv import load_dotenv

# --- IMPORTANT ---
# Load environment variables from .env file BEFORE importing other modules
load_dotenv()

from agent import agent_executor

def run_cognos():
    """
    Runs the Cognos agent with a complex, multi-step query.
    """
    print("="*80)
    print("🤖 Welcome to Cognos: The ReAct-Powered Reasoning Agent 🤖")
    print("="*80)

    # This query is designed to be complex and require multiple tools.
    complex_query = (
        "What was the stock price of NVIDIA (NVDA) at the close of its IPO date, "
        "and how many times greater is its current stock price compared to that initial price?"
    )
    
    print(f"Executing complex query: {complex_query}\n")

    # Invoke the agent executor with the query.
    result = agent_executor.invoke({"input": complex_query})

    print("\n" + "="*80)
    print("✅ Cognos has completed the task.")
    print("="*80)
    print(f"\nFinal Answer: {result['output']}")


if __name__ == "__main__":
    run_cognos()