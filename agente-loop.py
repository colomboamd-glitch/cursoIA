from dotenv import load_dotenv
from agno.agent import Agent 
from agno.models.openai import OpenAIChat

load_dotenv()

agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    markdown=True
)

while True:
    pergunta = input("digite sua pergunta" )

    if pergunta.lower() == "sair" or pergunta.lower() == "exit":
        print("Encerrando agente... \nFique à vontade quando tiver mais duvidas!  ")
        break
    else:
        agente.print_response(pergunta)