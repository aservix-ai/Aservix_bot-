from langgraph.graph import StateGraph, START, END
from src.agent.state import AgentState
from src.agent.nodes.conversation.node import conversation_node

# 1. Configuración del Grafo
workflow = StateGraph(AgentState)

# Añadir el nodo del node.py
# "conversacion" -> identificador del nodo
workflow.add_node("conversacion", conversation_node)

# conexiones 
workflow.add_edge(START, "conversacion")
workflow.add_edge("conversacion", END)

# Compilar el grafo
app = workflow.compile()

def chat():
    print("\n--- Aservix Bot ---")
    print("Escribe 'salir' para finalizar la sesión.\n")
    
    # historial de la secion actual
    thread = {"configurable": {"thread_id": "1"}}
    state = {"messages": []}

    while True:
        user_input = input(" Tú: ")
        
        if user_input.lower() in ["salir", "exit", "quit", "chau"]:
            print(" Bot: ¡Hasta luego!")
            break

        # Ejecutar el grafo 
        # stream -> ver el proceso paso a paso si es necesario
        events = app.stream(
            {"messages": [("user", user_input)]}, 
            thread, 
            stream_mode="values"
        )

        for event in events:
            # el último mensaje generado en el estado
            if "messages" in event:
                last_message = event["messages"][-1]
                # Solo imprimimos si es Ai
                if last_message.type == "ai":
                    print(f" Bot: {last_message.content}\n")

if __name__ == "__main__":
    chat()