# 📝 AutoBlogX 

A powerful, production-ready FastAPI service for generating engaging blog posts. This project leverages LangGraph for stateful workflows and Groq's high-performance LLMs to deliver AI-generated blogs with multi-language support out of the box.
- Blog Generation API with LangGraph + Groq LLM
  
🔗  Features

AI-Powered Blog Generation – Automatically generate high-quality blog posts with titles and well-structured content.

 Multi-Language Support – Built-in translation to Hindi and French (easily extendable to other languages).

LangGraph Workflows – State-based workflow management for better control and modularity.

 RESTful API – Clean, documented FastAPI endpoints for smooth integration.

 Postman-Ready – Standardized JSON responses for quick testing and automation.

 Visual Debugging – LangGraph Studio integration for workflow visualization and debugging.

 Markdown-Formatted Output – Ready-to-publish content for blogs or CMS systems.

📦 Prerequisites

Python 3.8+

Groq API Key – Get yours from Groq Console

(Optional) LangSmith API Key – For observability and tracing

⚙️ Installation & Setup

Clone the repository

git clone <your-repo-url>
cd blog-generation


Install dependencies

uv add -r requirements.txt


Configure environment variables
Create a .env file at the root:

GROQ_API_KEY=your_groq_api_key_here
LANGSMITH_API_KEY=your_langsmith_api_key_here


Install extra tools for development

uv add langgraph-cli[inmem]

📂 Project Structure
blog-generation/
├── app.py                 # FastAPI entry point
├── main.py                # Application startup logic
├── requirements.txt       # Dependencies
├── langgraph.json         # LangGraph workflow config
├── uv.lock                # Lock file (optional)
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

🚀 Running the API

Start the FastAPI server locally:

python app.py


Server runs at: http://localhost:8000

📡 API Usage
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

🧪 Testing with Postman

Create a new POST request
http://localhost:8000/blogs

Set headers:

Content-Type: application/json


Body (raw JSON):

{
  "topic": "Climate Change Solutions",
  "language": "french"
}


Send request → You’ll receive a translated, AI-generated blog.

🖼️ Visualize Workflows with LangGraph Studio

Install CLI:

uv add langgraph-cli


Run:

langgraph dev


🏗️ Architecture Overview
Workflow Nodes

Title Creation → Generates engaging titles

Content Generation → Produces full blog content

Routing Node → Decides if translation is needed

Translation Node → Converts content into target language

State Management

The app uses a BlogState object to track:

topic

blog (title & content)

current_language

🔧 Customization

Add a New Language

In src/graph/gbuid.py, add:

self.graph.add_node(
  "spanish_trans",
  lambda state: self.blog_obj.translation({**state, "current_language": "spanish"})
)


Then update routing logic in title_cre.py.

📖 API Documentation

FastAPI provides auto-generated docs:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

📜 License

This project is licensed under MIT License – see the LICENSE file for details.

🤝 Contributions
Contributions are welcome 🎉! Feel free to fork, open issues, and submit PRs 🚀

