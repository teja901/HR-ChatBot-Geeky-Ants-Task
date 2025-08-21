# HR Resource Query Chatbot

## Overview
The **HR Resource Query Chatbot** is an AI-powered assistant designed to help HR teams quickly find suitable employees for projects by processing natural language queries. It uses **FAISS for vector similarity search**, **sentence-transformer embeddings**, and **Groq LLaMA LLM** to generate natural and contextual responses. The system is served with **FastAPI** for backend APIs and a **modern web UI** for interaction.

## Features
- 🔍 **Semantic Search with FAISS** (retrieves best employee matches using embeddings)
- 🤖 **Groq LLaMA LLM** for natural language responses
- 📂 **Sample Employee Dataset** with realistic skills, projects, and availability
- 🌐 **FastAPI Backend** with REST APIs
- 💻 **Frontend (HTML/CSS/JS)** with modern UI design
- 🚀 Easy local setup with `uvicorn`
- 📊 Clear API docs (via FastAPI `/docs`)

## Architecture
```
User → Frontend (HTML/JS) → FastAPI Backend → FAISS Retrieval + LLaMA → Response
```
- **Frontend**: Chat interface (index.html, CSS styling, JS fetch API)
- **Backend**: FastAPI serving `/chat` and `/employees/search`
- **Data Layer**: Employee dataset in JSON
- **RAG Component**: Sentence-Transformer embeddings + FAISS retrieval
- **LLM**: Groq-hosted LLaMA for generating professional recommendations

## Setup & Installation
```bash
# 1. Clone repository
git clone https://github.com/your-username/hr-resource-chatbot.git


# 2. Install dependencies
pip install -r requirements.txt

# 3. Set Groq API key
setx GROQ_API_KEY "your_api_key_here" (Windows)


# 4. Run FastAPI server
uvicorn main:app --reload

# 5. Open in browser
http://127.0.0.1:8000/
```

## API Documentation
### `POST /chat`
**Request Body:**
```json
{
  "query": "Find Python developers with 3+ years experience"
}
```
**Response:**
```json
{
  "query": "Find Python developers with 3+ years experience",
  "llm_response": "Based on your query, Alice Johnson and John Doe are strong candidates...",
  "results": [
    {
      "name": "Alice Johnson",
      "skills": ["Python", "React", "AWS"],
      "experience": 5,
      "projects": ["E-commerce Platform", "Healthcare Dashboard"],
      "availability": "available"
    }
  ]
}
```

### `GET /employees/search?query=React Native`
Returns top-matched employees.

## AI Development Process
- **AI Coding Assistants Used**: ChatGPT (for code scaffolding, debugging help, documentation), GitHub Copilot (inline code suggestions).
- **AI Contributions**:
  - Dataset generation (15 realistic employees)
  - RAG design (FAISS + embeddings)
  - Groq LLaMA integration for natural language responses
  - Frontend design (modern chat interface)
- **Human Work**: API design, fine-tuning retrieval logic, CSS polishing.
- **Ratio**: ~70% AI-assisted, ~30% manually refined.
- **Interesting AI Outputs**: Suggested embedding model `all-MiniLM-L6-v2`, recommended `faiss.IndexFlatL2` setup.
- **Challenges**: Handling multi-turn memory was solved manually (AI suggested stateless approach first).

## Technical Decisions
- **Groq LLaMA**: Chosen for speed + cost-effective inference.
- **FAISS**: Fast similarity search over embeddings.
- **Sentence-Transformers**: Provides lightweight embeddings for employee profiles.
- **FastAPI**: Auto-generated docs, async support, simple API development.
- **HTML/JS frontend**: Lightweight and easy to customize.

**Trade-offs**:
- Cloud LLMs (Groq) provide high-quality output but require API keys.
- Local LLMs (Ollama) could reduce costs but may impact speed/accuracy.
- Privacy: On-premise embeddings with FAISS keep sensitive employee data local.

## Future Improvements
-  Multi-turn memory (track conversation context)
-  Role-based filtering (availability, department, seniority)
-  Enhanced dataset with 100+ employees
-  Richer UI (avatars, filters, advanced search)

## Demo
- **Local Demo**: Run via `uvicorn main:app --reload` → open browser
- Google Drive Video mp4 ====>  https://drive.google.com/file/d/1-D_7ATKQ8hV92Vzdq2uwjt6fuoyR9Gze/view?usp=sharing
