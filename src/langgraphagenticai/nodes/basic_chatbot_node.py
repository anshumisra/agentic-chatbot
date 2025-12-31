from src.langgraphagenticai.state.state import State
class BasicChatbotNode:
    """
    Chatbot implementation
    """
    def __init__(self,model):
        self.llm=model
    
    def process(self,state:State)->dict:
        """
        Processes the ip stage and generates a chatbot response
        """
        return {"messages":self.llm.invoke(state["messages"])}
