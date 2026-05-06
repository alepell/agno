from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
from agno.models.groq import Groq
from dotenv import load_dotenv
load_dotenv()

agent  = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools()]
)

agent.print_response("Qual a cotação da Apple atual?")