from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

class groqllm:
    def __init__(self):
        load_dotenv()

    def getllm(self): # to access the models
        try:
            os.environ["GROQ_API_KEY"]=self.groq_api_key=os.getenv("GROQ_API_KEY")
            llm=ChatGroq(api_key=self.groq_api_key,model="llama-3.1-8b-instant")
            return llm
        except Exception as e:
          raise ValueError("error occured with excpetion :{e}")
