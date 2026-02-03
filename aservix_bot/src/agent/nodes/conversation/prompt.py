# Acá va a estar el prompt del agente del nodo de conversacion
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un asistente amable de la empresa Aservix. Tu objetivo es ayudar a los clientes con sus dudas iniciales."),
    MessagesPlaceholder(variable_name="messages"),
])