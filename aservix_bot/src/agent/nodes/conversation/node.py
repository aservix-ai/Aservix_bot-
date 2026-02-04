import os
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI

from src.agent.nodes.conversation.prompt import SYSTEM_PROMPT
from src.agent.state import AgentState

load_dotenv()

llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.7,
    model="gpt-4o-mini",
)


def conversation_node(state: AgentState) -> dict:
    """
    Nodo de conversación que procesa los mensajes y genera respuestas.
    Usa .invoke() para que el LLM responda según el estado actual.
    """
    messages = state["messages"]

    # Construir mensajes con el system prompt al inicio
    full_messages = [SystemMessage(content=SYSTEM_PROMPT)] + list(messages)

    # Invocar el LLM para obtener la respuesta
    response = llm.invoke(full_messages)

    # Devolver solo el mensaje nuevo; add_messages lo añadirá al estado
    return {"messages": [response]}

