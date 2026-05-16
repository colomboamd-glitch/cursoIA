from dotenv import load_dotenv
from agno.agent import Agent 
from agno.models.openai import OpenAIChat
#todos os agentes necessitam da chave de API e a função load_dotenv faz a leitura do arquivo no .env
load_dotenv()
agente = Agent(
    # essa linha define meu agente
    model= OpenAIChat(id="gpt-4o-mini"),
    markdown=True
)
pergunta = input("Faça uma pergunta: ")
agente.print_response (f"{pergunta}")    
#print(f"{pergunta}")
