from dotenv import load_dotenv
from agno.agent import Agent 
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.tavily import TavilyTools


load_dotenv()
#crio modelo de AI
agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description="Voçê é um agente que faz pesquisas importantes",
    add_history_to_context=True,
    tools=[DuckDuckGoTools(), TavilyTools],
    markdown=True
)

while True:
    pergunta = input("digite sua pergunta ")

    if pergunta.lower() == "sair" or pergunta.lower() == "exit":
        print("Encerrando agente... \nFique à vontade quando tiver mais duvidas!  ")
        break
    else:
        agente.print_response(pergunta)