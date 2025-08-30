# 📝 AutoBlogX

> ⚡️ A powerful **production-ready FastAPI service** for generating engaging blog posts.  
> Built with **LangGraph workflows** and **Groq's high-performance LLMs**, AutoBlogX delivers AI-generated blogs with **multi-language support** out of the box.

---

## ✨ Features

- **AI-Powered Blog Generation** – Automatically generate high-quality blog posts with titles and well-structured content  
- **Multi-Language Support** – Built-in translation to Hindi and French (easily extendable to other languages)  
- **LangGraph Workflows** – State-based workflow management for better control and modularity  
- **RESTful API** – Clean, documented FastAPI endpoints for smooth integration  
- **Postman-Ready** – Standardized JSON responses for quick testing and automation  
- **Visual Debugging** – LangGraph Studio integration for workflow visualization and debugging  
- **Markdown-Formatted Output** – Ready-to-publish content for blogs or CMS systems  

---

## 🛠️ Prerequisites

- Python **3.8+**  
- Groq API Key – [Get from Groq Console](https://console.groq.com/)  
- (Optional) LangSmith API Key – For observability and tracing  

---

## ⚡ Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd blog-generation

# Install dependencies
uv add -r requirements.txt

## ⚙️ Setup

GROQ_API_KEY=your_groq_api_key_here
LANGSMITH_API_KEY=your_langsmith_api_key_here

uv add langgraph-cli[inmem]

▶️ Usage

  Running the API

  python app.py
  Server runs at: http://localhost:8000


📡 API Endpoint: POST /blogs

Generate a blog post for a given topic and optional target language.

Request

{
  "topic": "Artificial Intelligence in Healthcare",
  "language": "hindi"   // optional: "hindi", "french", or omit for English
}

Response

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

Create a new POST request → http://localhost:8000/blogs

Set headers → Content-Type: application/json

Set body →

