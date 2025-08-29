from src.llm.groq import groqllm
from src.state.state import BlogState
from langchain_core.messages import SystemMessage, HumanMessage
from src.state.state import Blog
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
       
     
   def translation(self,state:BlogState):
      """
      Translate the content to the specifies language.
      
      """

      translation_prompt = """
      Translate the following content into {current_language}.
      - Maintaun the original tone, style and formatting.
      - Adapt cultural refrences and idioms to the a
   

      ORIGINAL CONTENT:
        {blog_content}

        """
      print(state["current_language"])
      blog_content=state["blog"]["content"]
      messages=[
      HumanMessage(translation_prompt.format(current_language=state["current_language"], blog_content=blog_content))

        ]
      transaltion_content = self.llm.with_structured_output(Blog).invoke(messages)
      return {"blog": {"content": transaltion_content}}
      



   
   def route(self, state: BlogState):
        return {"current_language": state['current_language'] }
      

   def route_decision(self, state: BlogState):
        """
        Route the content to the respective translation function.
        """
        if state["current_language"] == "hindi":
            return " hindi"
        elif state["current_language"] == "french": 
            return "french"
        else:
            return state['current_language']
