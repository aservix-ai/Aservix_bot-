#Conexion con whatsapp para que nustro agente pueda responder mensajes allí
import os
from fastapi import APIRouter, Request
from src.agent import app

router = APIRouter()

@router.post("/webhook")
async def handle_whatsapp(request: Request):
    data = await request.json()
    
    # Extraemos el mensaje y el número del remitente
    try:
        msg_obj = data['entry'][0]['changes'][0]['value']['messages'][0]
        user_phone = msg_obj['from']
        text = msg_obj['text']['body']
        
        # El thread_id es el número de teléfono 
        config = {"configurable": {"thread_id": user_phone}}
        
        # Ejecutamos el bot
        inputs = {"messages": [("user", text)]}
        # Nota: app.ainvoke es asíncrono
        final_state = await app.ainvoke(inputs, config)
        
        # La respuesta final
        bot_msg = final_state["messages"][-1].content
        print(f"Enviando a {user_phone}: {bot_msg}")
        
        # TODO: llamar a la API de Meta para enviar el mensaje real
        
    except KeyError:
        pass
        
    return {"status": "ok"}