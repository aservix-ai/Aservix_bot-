from langgraph.graph import StateGraph, START, END
from src.agent.state import AgentState
from src.agent.nodes.conversation.node import conversation_node

# 1. Configuración del Grafo
workflow = StateGraph(AgentState)

# 2. Añadir el nodo que ya definimos
# El nombre "conversation" es el identificador del nodo
workflow.add_node("conversation", conversation_node)

# 3. Definir las conexiones (Aristas/Edges)
workflow.add_edge(START, "conversation")
workflow.add_edge("conversation", END)

# 4. Compilar el grafo
# Esto crea un ejecutable que mantiene el estado de la conversación
app = workflow.compile()

def chat():
    print("\n--- Aservix Bot (Modo Terminal) ---")
    print("Escribe 'salir' para finalizar la sesión.\n")
    
    # Aquí guardaremos el historial de la sesión actual
    thread = {"configurable": {"thread_id": "1"}}
    state = {"messages": []}

    while True:
        user_input = input(" Tú: ")
        
        if user_input.lower() in ["salir", "exit", "quit", "chau"]:
            print(" Bot: ¡Hasta luego!")
            break

        # Ejecutar el grafo con la entrada del usuario
        # Usamos stream para poder ver el proceso paso a paso si quisiéramos
        events = app.stream(
            {"messages": [("user", user_input)]}, 
            thread, 
            stream_mode="values"
        )

        for event in events:
            # Buscamos el último mensaje generado en el estado
            if "messages" in event:
                last_message = event["messages"][-1]
                # Solo imprimimos si el mensaje es del bot (AI)
                if last_message.type == "ai":
                    print(f" Bot: {last_message.content}\n")

if __name__ == "__main__":
    chat()