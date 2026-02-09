import os
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
from src.agent.nodes.conversation.prompt import SYSTEM_PROMPT
from src.agent.state import AgentState

load_dotenv()


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,

)

def conversation_node(state: AgentState) -> dict:
    """
    Nodo de conversación que procesa los mensajes y genera respuestas.
    """
    # obtener el historial actual
    messages = state["messages"]

    # Construir la lista de mensajes. 
    full_messages = [SystemMessage(content=SYSTEM_PROMPT)] + list(messages)

    # Invocación
    response = llm.invoke(full_messages)

    # Retornar la respuesta. 
    return {"messages": [response]}