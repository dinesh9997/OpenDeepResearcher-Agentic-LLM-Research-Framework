# 🧠 Agentic RAG Research System

> **An autonomous multi-agent research pipeline** that plans, retrieves, analyzes, and synthesizes technical documentation — powered by cloud-hosted LLMs and real-time web retrieval.

[![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Groq](https://img.shields.io/badge/Groq-LLM_Inference-F55036?style=for-the-badge)](https://groq.com/)
[![Tavily](https://img.shields.io/badge/Tavily-Search_API-0EA5E9?style=for-the-badge)](https://tavily.com/)

---

## 🎯 Project Objective

This system emulates a **professional research workflow** by combining planning, retrieval, and reasoning capabilities into a fully automated pipeline.

- 🔍 **Decompose** a research topic into structured, targeted questions
- 🌐 **Retrieve** real-time information from the web via Tavily Search API
- 🧠 **Reason** over retrieved context using cloud-hosted LLMs
- 📄 **Generate** high-quality, structured technical documentation
- 📤 **Export** research outputs in TXT, PDF, and Word formats

> Built as part of the **OpenDeepResearcher: Agentic LLM Research Framework** internship project.

---

## 🧩 System Architecture

The application follows a **sequential multi-agent workflow**, where each agent operates as an independent module with a clearly defined responsibility.

```
┌─────────────────────────────────────────────────────────────┐
│                     USER INPUT (Topic)                      │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              🧩 PLANNER AGENT  (planner_agent.py)           │
│  Analyzes the topic and generates targeted research         │
│  questions. Acts as the strategic blueprint for the         │
│  entire research process.                                   │
└─────────────────────┬───────────────────────────────────────┘
                      │  Research Questions
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              🔍 SEARCHER AGENT (searcher_agent.py)          │
│  Uses Tavily Search API for real-time web retrieval.        │
│  Collects contextual facts and reference sources to         │
│  supply grounded information to the Writer Agent.           │
└─────────────────────┬───────────────────────────────────────┘
                      │  Context + Sources
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              ✍️  WRITER AGENT   (main.py)                    │
│  Synthesizes planner questions and retrieved context        │
│  into a professional research report with structured        │
│  sections: Executive Summary, Technical Analysis,           │
│  Challenges & Ethics, and Strategic Conclusion.             │
└─────────────────────┬───────────────────────────────────────┘
                      │  Final Report
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              📤 EXPORT (TXT / PDF / Word)                   │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **LLM Inference** | [Groq](https://groq.com/) (Llama 3.1 8B) | Cloud-hosted, OpenAI-compatible LLM API |
| **Web Search** | [Tavily Search API](https://tavily.com/) | Real-time information retrieval |
| **Frontend** | [Streamlit](https://streamlit.io/) | Interactive web UI with dark/light mode |
| **PDF Export** | ReportLab | Professional PDF document generation |
| **Word Export** | python-docx | Word document generation |

---

## 📁 Project Structure

```
├── app.py                 # Streamlit UI — interactive research workflow
├── main.py                # Writer Agent + CLI entry point
├── planner_agent.py       # Planner Agent — generates research questions
├── searcher_agent.py      # Searcher Agent — retrieves web context via Tavily
├── llm_utils.py           # Shared utilities — LLM calls (Groq) & Tavily search
├── requirements.txt       # Python dependencies for deployment
├── .gitignore             # Protects .env and secrets from GitHub
├── .env                   # API keys (local only, never committed)
└── README.md              # Project documentation
```

---

## ⚡ Quick Start

### Prerequisites

- Python 3.10+
- [Groq API Key](https://console.groq.com/) (free)
- [Tavily API Key](https://app.tavily.com/) (free tier available)

### 1. Clone the Repository

```bash
git clone -b GUJJU-DINESH https://github.com/dinesh9997/OpenDeepResearcher-Agentic-LLM-Research-Framework.git
cd OpenDeepResearcher-Agentic-LLM-Research-Framework
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root:

```env
LLM_API_KEY=your_groq_api_key_here
LLM_BASE_URL=https://api.groq.com/openai/v1
LLM_MODEL_NAME=llama-3.1-8b-instant
TAVILY_API_KEY=your_tavily_api_key_here
```

### 4. Run the Application

```bash
streamlit run app.py
```

The app will be available at `http://localhost:8501`

---

## 🎨 User Interface

- **Dark Mode** & **Light (Gold) Mode** toggle
- Clean, card-based layout with gradient animations
- Guided research flow: `Topic → Planner → Writer → Export`
- One-click export to TXT, PDF, or Word

---

## 🚀 Deployment (Streamlit Cloud)

1. Push this repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository → Branch: `GUJJU-DINESH`
4. Set **Main file path**: `app.py`
5. Add secrets in **Settings → Secrets**:

```toml
LLM_API_KEY = "gsk_your_groq_key"
LLM_BASE_URL = "https://api.groq.com/openai/v1"
LLM_MODEL_NAME = "llama-3.1-8b-instant"
TAVILY_API_KEY = "tvly_your_tavily_key"
```

6. Click **Deploy** 🚀

---

## 📤 Export Formats

| Format | Library | Features |
|--------|---------|----------|
| 📄 **TXT** | Built-in | Plain text with markdown formatting |
| 📄 **PDF** | ReportLab | Professional layout with styled headings |
| 📄 **Word** | python-docx | Editable document with paragraph structure |

---

## 🔒 Security

- API keys are stored in `.env` (local) or **Streamlit Secrets** (cloud)
- `.gitignore` ensures `.env` is **never pushed** to GitHub
- No hardcoded credentials anywhere in the codebase

---

## ✅ Internship Alignment

This project fully aligns with the internship objectives by:

- ✅ Implementing a **complete agentic research pipeline**
- ✅ Using **cloud-hosted LLMs** via Groq for scalable deployment
- ✅ Integrating **real-time web retrieval** via Tavily Search API
- ✅ Delivering a **polished UI** with professional export capabilities
- ✅ Following **modular architecture** with separated agent responsibilities
- ✅ Demonstrating **end-to-end system design and execution**

---

## 👤 Author

**GUJJU DINESH**
B.Tech – CSE (Artificial Intelligence)

---