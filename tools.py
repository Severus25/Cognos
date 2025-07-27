from langchain.tools import Tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.chains.llm_math.base import LLMMathChain
from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize the LLM for the math chain
llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0)

# 1. The Search Tool
search = DuckDuckGoSearchRun()
search_tool = Tool.from_function(
    func=search.run,
    name="Search",
    description="Use this tool to search the internet for real-time information, news, dates, or facts."
)

# 2. The Calculator Tool (LLMMathChain)
math_chain = LLMMathChain.from_llm(llm=llm, verbose=False)
calculator_tool = Tool.from_function(
    func=math_chain.run,
    name="Calculator",
    description="Use this tool to solve any mathematical questions or perform calculations. The input should be a clear mathematical question."
)

# A list containing all the tools the agent can use.
tools = [search_tool, calculator_tool]