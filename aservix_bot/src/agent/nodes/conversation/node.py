from langchain-openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0.7)

prompt = PromptTemplate(template="Responde brevemente: {pregunta}", input_variables=["pregunta"])
chain = LLMChain(llm=llm, prompt=prompt)

respuesta = chain.run("¿Cómo estás?")
print(respuesta)

#------------------------------------------------------



