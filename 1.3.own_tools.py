from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.groq import Groq
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
    return (temperatura_celsius * 9/5) + 32

agent  = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[TavilyTools(), celsius_to_fh],
)

agent.print_response("Use suas ferramentas para pesquisar a temperatura de hoje em Sao Paulo em Fahrenheit")
