from src.llm.groq import groqllm
from src.state.state import BlogState

class blognode:
    """
    a classto represent the blog node
    """

    def __init__(self,llm):
      self.llm=llm


    def title_creation(self, state: BlogState):
       """
       Create the title for the blog.
        """

       if "topic" in state and state["topic"]:
           prompt = """
           You are an expert blog content writer. Use Markdown format.
           Write a blog title for the {topic}. This title should be catchy and engaging.
            """

           system_message = prompt.format(topic=state["topic"])
           response = self.llm.invoke(system_message)

           return {"blog": {"title": response.content}}
       
    
    def content_gen(self,state:BlogState):
       """
       Create blog content for the blog , it has to be detailed and informative and also intresting to read by user
       """
       if "topic" in state and state["topic"]:
          prompt ="""
                   You are an expert blog content writer. Use Markdown format.
                   Write a  detailed blog title for the {topic}. This content should be intresting and engaging.
                  """
          system_message = prompt.format(topic=state["topic"])
          response = self.llm.invoke(system_message)
          
          return {"blog": {"title": state['blog']['title'],"content":response.content}}
       
