from typing import Annotated, Sequence
from typing_extensions import TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    # La anotación add_messages es la que permite que el historial crezca
    messages: Annotated[Sequence[BaseMessage], add_messages]