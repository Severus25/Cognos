from langchain.agents import AgentExecutor, create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from tools import tools

# Initialize the LLM that will power the agent's reasoning
# THE FINAL FIX:
# 1. Use the full, version-specific model name 'gemini-1.5-pro-latest'.
#    This resolves the "NotFound" error for v1beta API keys.
# 2. Remove the deprecated 'convert_system_message_to_human' parameter.
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0)

# Define the ReAct prompt template directly in the code.
# This makes the project self-contained and reliable.
react_prompt_template = """
Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}
"""

# Create the prompt from the template string.
prompt = PromptTemplate.from_template(react_prompt_template)

# Create the ReAct agent.
agent = create_react_agent(llm, tools, prompt)

# Create the Agent Executor.
# verbose=True is crucial as it prints the agent's entire reasoning process.
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)