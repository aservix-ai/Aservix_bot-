from langgraph.graph import StateGraph, START, END

# Importar state ANTES de conversation_node para evitar dependencia circular
from src.agent.state import AgentState
from src.agent.nodes.conversation.node import conversation_node

# 1. Creamos el constructor del Grafo
workflow = StateGraph(AgentState)

# 2. Añadimos el nodo que ya programamos
workflow.add_node("conversation", conversation_node)

# 3. Definimos las conexiones
workflow.add_edge(START, "conversation")
workflow.add_edge("conversation", END)

# 4. Compilamos el grafo para que pueda ser usado
app = workflow.compile()
