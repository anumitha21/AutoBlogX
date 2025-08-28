from langgraph.graph import START, END,StateGraph
from src.llm.groq import groqllm
from src.state.state import BlogState
from src.node.title_cre import blognode


class graphbuilder:
    def __init__(self, llm):
        self.llm = llm
        self.graph = StateGraph(BlogState)

    def buildgraph(self):
        """
        build a graph to generate blogs based on topic..make it intresting to read 
        """
        self.blog_obj = blognode(self.llm)
        #nodes
        self.graph.add_node("title", self.blog_obj.title_creation)
        self.graph.add_node("creation", self.blog_obj.content_gen)

        #edges
        self.graph.add_edge(START, "title")
        self.graph.add_edge("title", "creation")
        self.graph.add_edge("creation", END)

        return self.graph
    
    def setup_graph(self, usecase):
        if usecase == "topic":
            self.buildgraph()

        return self.graph.compile()
