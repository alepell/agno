from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.openai import OpenAIChat
from fastapi.middleware.cors import CORSMiddleware
from agno.os import AgentOS
from agno.db.sqlite import SqliteDb

# from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()


def celsius_to_fh(temperatura_celsius: float):
    """
    Converte uma temperatura de Celsius para Fahrenheit.

    Args:
        temperatura_celsius (float): Temperatura em graus Celsius.

    Returns:
        float: Temperatura equivalente em graus Fahrenheit.
    """
    return (temperatura_celsius * 9 / 5) + 32


agent = Agent(
    name="Agente do Tempo",
    model=OpenAIChat(id="gpt-5.4-mini"),
    tools=[TavilyTools(), celsius_to_fh],
    add_history_to_context=True,
    db=SqliteDb(db_file="agent.db"),
    num_history_runs=3,
)

agent_os = AgentOS(agents=[agent])

app = agent_os.get_app()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://app.agno.com", "http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
# agent.print_response("Use suas ferramentas para pesquisar a temperatura de hoje em Sao Paulo em Fahrenheit, mostre em uma tabela comparando celsius e fahrenheit")
