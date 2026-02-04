# Here we define the agent, the nodes, conditional edges and the graph
from langgraph.graph import StateGraph, START, END

from src.agent.state import AgentState
from src.agent.nodes.conversation.node import conversation_node


def make_graph():
    """
    Función que construye y compila el grafo del agente.
    LangGraph espera esta función (no una clase) que retorne el grafo compilado.
    """
    workflow = StateGraph(AgentState)
    workflow.add_node("conversation", conversation_node)
    workflow.add_edge(START, "conversation")
    workflow.add_edge("conversation", END)
    return workflow.compile()