from langgraph.graph import StateGraph, START, END
from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages
from src.agent.nodes.conversation.node import conversation_node

# Definimos el esquema del estado aquí mismo
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

# 1. Creamos el constructor del Grafo
workflow = StateGraph(AgentState)

# 2. Añadimos el nodo que ya programamos
workflow.add_node("conversation", conversation_node)

# 3. Definimos las conexiones
# Empezamos en la conversación y, por ahora, terminamos ahí
workflow.add_edge(START, "conversation")
workflow.add_edge("conversation", END)

# 4. Compilamos el grafo para que pueda ser usado
app = workflow.compile()