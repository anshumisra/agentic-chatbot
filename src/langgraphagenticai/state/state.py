from typing_extensions import TypedDict,List
from langgraph.graph.message import add_messages,AnyMessage
from typing import Annotated

class State(TypedDict):
    """
    Represents the structure of the state used in graph
    """
    messages:Annotated[List[AnyMessage],add_messages]
