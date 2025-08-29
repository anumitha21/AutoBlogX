import uvicorn
from fastapi import FastAPI, Request
from src.graph.gbuid import graphbuilder
from src.llm.groq import groqllm

import os
from dotenv import load_dotenv
load_dotenv()
app=FastAPI()

os.environ["LANGSMITH_API_KEY"]="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"

##API'S

@app.post("/blogs")
async def create_blog(request: Request):
    data = await request.json()
    topic = data.get("topic","")

    ##get the llm object
    groq_llm = groqllm()
    llm=groq_llm.getllm()

    ## get the graph

    graph_builder=graphbuilder(llm)

    if topic:
        graph=graph_builder.setup_graph(usecase="topic") #builds a workflow or processing pipeline.
        state = graph.invoke({"topic":topic})

    return {"data":state}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000,reload=True)