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
    def lang_graph(self):
        """
        build a graph to generate blogs based on topic and language ..make it intresting to read 
        """
        self.blog_obj = blognode(self.llm)
        #nodes
        self.graph.add_node("title", self.blog_obj.title_creation)
        self.graph.add_node("creation", self.blog_obj.content_gen)
        self.graph.add_node("route",self.blog_obj.route)
        self.graph.add_node("hindi_trans",lambda state: self.blog_obj.translation({**state, "current_language": "hindi"}))
        self.graph.add_node("french_trans",lambda state: self.blog_obj.translation({**state, "current_language": "french"}))

        #edges
        self.graph.add_edge(START, "title")
        self.graph.add_edge("title", "creation")
        self.graph.add_edge("creation", "route")
        #conditonal edges
        self.graph.add_conditional_edges(
            "route",
            self.blog_obj.route_decision,
            {
                "hindi"  : "hindi_trans",
                "french" : "french_trans"
            }

        )
        self.graph.add_edge("hindi_trans", END)
        self.graph.add_edge("french_trans", END)

        return self.graph
    
    def setup_graph(self, usecase):
        if usecase == "topic":
            self.buildgraph()
        
        if usecase=="language":
            self.lang_graph()

        return self.graph.compile()

## below code is for langsmith langraph studio
llm=groqllm().getllm()

##get the graph
graph_builder=graphbuilder(llm)
graph = graph_builder.lang_graph().compile()