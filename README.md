# 📝 AutoBlogX

A production-ready FastAPI service for generating engaging blog posts. AutoBlogX uses LangGraph for stateful workflows and Groq's high-performance LLMs to create AI-generated blogs with multi-language support out of the box.

## 🔗 Features

 AI-Powered Blog Generation – Automatically generate high-quality blog posts with titles and well-structured content.

 Multi-Language Support – Built-in translation to Hindi and French (easily extendable to other languages).

 LangGraph Workflows – State-based workflow management for modular and scalable pipelines.

 RESTful API – Clean, well-documented FastAPI endpoints for seamless integration.

 Postman-Ready – Standardized JSON responses for quick testing and automation.

 Visual Debugging – LangGraph Studio integration for workflow visualization and debugging.

 Markdown Output – Ready-to-publish content for blogs or CMS platforms.

## 📦 Prerequisites

Python 3.8+

Groq API Key – Get yours here

(Optional) LangSmith API Key – For observability and tracing

## ⚙️ Installation & Setup

Clone the repository

git clone <your-repo-url>
cd blog-generation


Install dependencies

uv add -r requirements.txt


Set environment variables
Create a .env file in the root directory:

GROQ_API_KEY=your_groq_api_key_here
LANGSMITH_API_KEY=your_langsmith_api_key_here


Install extra tools (for development)

uv add langgraph-cli[inmem]

## 📂 Project Structure

blog-generation/
├── app.py                 # FastAPI entry point
├── main.py                # Application startup logic
├── requirements.txt       # Dependencies
├── langgraph.json         # LangGraph workflow config
├── uv.lock                # Lock file
├── pyproject.toml         # Project metadata
├── src/
│   ├── graph/
│   │   └── gbuid.py       # Graph builder & workflow definition
│   ├── llm/
│   │   └── groq.py        # Groq LLM integration
│   ├── node/
│   │   └── title_cre.py   # Nodes for title/content generation
│   └── state/
│       └── state.py       # TypedDict state definitions
└── README.md

## 🚀 Running the API

Start the FastAPI server locally:

python app.py


Server runs at: http://localhost:8000

## 📡 API Usage
POST /blogs

Generate a blog post for a given topic and optional target language.

Request:

{
  "topic": "Artificial Intelligence in Healthcare",
  "language": "hindi"   // optional: "hindi", "french", or omit for English
}


Response:

{
  "data": {
    "blog": {
      "title": "The Future of Healthcare: How AI is Revolutionizing Patient Care",
      "content": "# The Future of Healthcare: How AI is Revolutionizing Patient Care\n\nArtificial Intelligence is transforming healthcare in unprecedented ways...",
      "current_language": "hindi"
    }
  }
}

## 🧪 Testing with Postman

Create a new POST request
http://localhost:8000/blogs

Set headers:

Content-Type: application/json


Body (raw JSON):

{
  "topic": "Climate Change Solutions",
  "language": "french"
}


Send request → Get translated, AI-generated blog content instantly.

## 🖼️ Visualize Workflows with LangGraph Studio
uv add langgraph-cli
langgraph dev


Then open http://localhost:3000
 in your browser to visualize and debug workflows.

## 🏗️ Architecture Overview

Workflow Nodes:

Title Creation → Generates engaging titles

Content Generation → Produces detailed blog content

Routing Node → Decides if translation is needed

Translation Node → Translates into target language

State Management:
Uses BlogState to track:

topic

blog (title & content)

current_language

## 🔧 Customization
Adding a New Language

In src/graph/gbuid.py:

self.graph.add_node(
  "spanish_trans",
  lambda state: self.blog_obj.translation({**state, "current_language": "spanish"})
)


Then update routing logic in title_cre.py.

## 📖 API Documentation

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

## 📜 License

Licensed under the MIT License – see the LICENSE file for details.

## 🤝 Contributions

Contributions are welcome 🎉 — fork the repo, make your changes, and open a PR 🚀
