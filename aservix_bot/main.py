import os
from dotenv import load_dotenv
from src.agent import app

#  llaves de API 
load_dotenv()

def run_chat():
    print("--- Bot de Aservix Iniciado (Escribe 'salir' para terminar) ---")
    
    # El thread_id permite que el bot recuerde
    config = {"configurable": {"thread_id": "1"}}
    
    while True:
        user_input = input("Tú: ")
        if user_input.lower() in ["salir", "quit", "exit"]:
            break

        # el mensaje al grafo
        for event in app.stream({"messages": [("user", user_input)]}, config):
            for value in event.values():
                print(f"Asistente: {value['messages'][-1].content}")
