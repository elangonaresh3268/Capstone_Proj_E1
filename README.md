# Insurance Advisor - AI-Powered Insurance Assistant

An intelligent, AI-driven application that helps users understand and navigate their insurance policies with ease. The Insurance Advisor combines advanced language models, retrieval-augmented generation (RAG), and document analysis to provide personalized insurance guidance and recommendations.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Use Cases](#use-cases)
- [Documentation](#documentation)

---

## 🎯 Overview

### Project Definition
The Insurance Advisor is a Streamlit-based intelligent assistant designed to simplify insurance policy comprehension for everyday users. It leverages artificial intelligence, natural language processing, and semantic document search to interpret complex insurance documents and answer user queries in plain, understandable language.

### Project Purpose
**Primary Goals:**
- Simplify insurance policy comprehension for non-technical users
- Enable users to quickly find relevant information from complex policy documents
- Provide AI-driven personalized insurance recommendations
- Create an interactive conversational interface for insurance queries
- Reduce confusion and empower informed insurance decisions

**Key Benefits:**
- User-friendly interface for policy document analysis
- Real-time AI responses to insurance questions
- Personalized recommendations based on user profile and documents
- Secure document upload and processing
- Conversation history tracking for reference

---

## ✨ Features

### 1. User Profile Management
- Create and manage user profiles with personal details
- Store insurance preferences and coverage needs
- Enable personalized recommendations based on profile data

### 2. Document Upload & Processing
- Secure upload of insurance policy documents
- Automatic text extraction and preprocessing
- Semantic document chunking for optimal analysis
- Vector embedding generation for fast retrieval

### 3. Conversational AI Chat
- Interactive chat interface for policy questions
- Real-time AI responses powered by OpenAI LLM
- RAG (Retrieval-Augmented Generation) for accurate, document-grounded answers
- Multi-turn conversation support with context awareness
- Complete conversation history tracking

### 4. Smart Recommendations Engine
- Analyzes user profile and uploaded documents
- Identifies coverage gaps and optimization opportunities
- Generates personalized insurance recommendations
- Considers user preferences discovered through chat interactions

### 5. RAG-Based Retrieval System
- Vector embeddings of policy documents
- Semantic similarity search for relevant policy sections
- Context-aware response generation grounded in actual policy text
- Prevents AI hallucinations with document-backed answers

---

## 🛠️ Technology Stack

### Frontend & UI
- **Streamlit** - Interactive web application framework for rapid UI development
- **Python 3.x** - Core programming language

### AI & Language Models
- **OpenAI API** - Large Language Model (LLM) for intelligent responses
- **LangChain** - Framework for LLM orchestration and chaining
- **Embeddings** - Semantic text representations for similarity search

### Data & Search
- **FAISS** (Facebook AI Similarity Search) - Efficient vector similarity search
- **LangChain Vector Stores** - Document embedding storage and retrieval
- **Pydantic** - Data validation and serialization

### Document Processing
- **PDF/Text Parsing** - Extract text from policy documents
- **Document Chunking** - Segment documents into meaningful units
- **Semantic Analysis** - Understand document context and meaning

### State Management
- **Streamlit Session State** - Maintain user session and conversation history
- **In-Memory Storage** - Efficient state tracking

### Testing & Quality
- **Python unittest** - Unit testing framework
- **pytest** - Advanced testing capabilities

### Report Generation
- **ReportLab** - PDF generation and document creation

---

## 📁 Project Structure

```
Capstone_Proj/
├── streamlit_app.py              # Main Streamlit application
├── llm.py                         # LLM connector and API integration
├── rag.py                         # RAG implementation and vector store
├── recommendation.py              # Recommendation engine and prompt builder
├── memory.py                      # Session state and memory management
├── graph.py                       # Workflow graph orchestration
├── models.py                      # Pydantic data models
├── generate_pdf_report.py         # PDF report generation script
├── test_llm.py                    # LLM smoke tests
├── requirements.txt               # Python dependencies
├── README.md                      # This file
├── screenshots/                   # Application screenshots
│   ├── User_Profile_Creation.png
│   ├── Profile_Creation_successfull.png
│   ├── Upload_documents.png
│   ├── Upload_document_successfull.png
│   ├── chat_screen.png
│   ├── Coversation_history.png
│   ├── recommendation.png
│   ├── recommendation_response.png
│   ├── AI_response.png
│   └── AI_response2.png
├── reports/                       # Generated PDF reports
│   └── insurance_advisor_project_report.pdf
├── uploads/                       # User uploaded documents
│   └── HealthSecurePlus_SOP.txt
├── tests/                         # Unit tests
│   └── test_recommendation_prompt.py
└── .venv/                         # Virtual environment
```

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment tool (venv or conda)

### Setup Steps

1. **Clone or Navigate to the Project**
   ```bash
   cd Capstone_Proj
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Keys**
   - Set your OpenAI API key as an environment variable:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

5. **Verify Installation**
   ```bash
   python test_llm.py
   ```

---

## 💻 Usage

### Running the Application

Start the Streamlit application:
```bash
streamlit run streamlit_app.py
```

The application will open in your default browser at `http://localhost:8501`

### Using the Application

1. **Step 1: Create Your Profile**
   - Navigate to the Profile Creation section
   - Enter your personal details and insurance preferences
   - Save your profile

2. **Step 2: Upload Insurance Documents**
   - Go to the Document Upload section
   - Select and upload your insurance policy documents
   - Wait for documents to be processed and indexed

3. **Step 3: Chat with AI Assistant**
   - Open the Chat section
   - Ask questions about your insurance policies
   - Review AI responses grounded in your documents
   - View conversation history anytime

4. **Step 4: Get Recommendations**
   - Navigate to the Recommendations section
   - Receive personalized insurance recommendations
   - Review recommendations based on your profile and documents

### Generating Reports

Generate a comprehensive PDF report:
```bash
python generate_pdf_report.py
```

Output: `reports/insurance_advisor_project_report.pdf`

---

## 🏗️ Architecture

### Application Workflow

The Insurance Advisor follows a structured 5-stage workflow:

**Stage 1: Profile Creation**
- Users enter personal information and insurance preferences
- Establishes foundation for personalized recommendations
- Validates input and confirms successful setup

**Stage 2: Document Upload & Processing**
- Secure document upload and preprocessing
- Text extraction from policy documents
- Semantic chunking and embedding generation
- Vector store indexing for fast retrieval

**Stage 3: Conversational Chat**
- User queries trigger RAG process
- System retrieves relevant policy sections from vector store
- LLM generates responses grounded in actual policy text
- Context preserved for multi-turn conversations

**Stage 4: Conversation Management**
- Complete conversation history maintained
- Previous context passed to LLM for continuity
- Users can review all past interactions

**Stage 5: Smart Recommendations**
- Analysis of user profile, documents, and conversation
- Identification of coverage gaps and optimization opportunities
- Generation of personalized insurance recommendations

### Core Components

- **Main App** (`streamlit_app.py`): User interface and orchestration
- **LLM Connector** (`llm.py`): OpenAI API integration
- **RAG Engine** (`rag.py`): Document retrieval and semantic search
- **Recommendation System** (`recommendation.py`): Personalized suggestion generation
- **Memory Manager** (`memory.py`): Session state and conversation tracking
- **Workflow Orchestration** (`graph.py`): Multi-step process coordination
- **Data Models** (`models.py`): Pydantic schemas for validation

---

## 🤖 AI Workflow & Processing Pipeline

### How the AI System Works

The Insurance Advisor uses a sophisticated AI pipeline combining multiple AI techniques to deliver accurate, personalized insurance guidance:

#### 1. **Document Ingestion & Preparation**

When a user uploads an insurance policy document:

```
User Document Upload
        ↓
    File Processing
        ↓
    Text Extraction (PDF → Plain Text)
        ↓
    Document Chunking (Split into meaningful segments ~500 tokens each)
        ↓
    Metadata Addition (Title, source, page info)
        ↓
    Storage in Memory
```

**Key Technologies:**
- PDF/Text parsing extracts raw content from policy documents
- Intelligent chunking ensures document segments retain semantic meaning
- Each chunk is labeled with metadata for traceability

#### 2. **Vector Embedding & Semantic Indexing**

After document preparation, the system creates searchable embeddings:

```
Document Chunks
        ↓
    OpenAI Embedding API
        ↓
    Generate Dense Vectors (1536-dimensional embeddings)
        ↓
    FAISS Vector Index Creation
        ↓
    In-Memory Vector Store
```

**How It Works:**
- Each document chunk is sent to OpenAI's embedding model
- Generates a mathematical representation (vector) capturing semantic meaning
- Vectors enable similarity search: semantically similar content has similar vectors
- FAISS indexes these vectors for fast retrieval (milliseconds, not seconds)

#### 3. **User Query & RAG (Retrieval-Augmented Generation)**

When a user asks a question about their insurance:

```
User Question
        ↓
    Session Context Loading (previous chat history)
        ↓
    Query Embedding Generation
        ↓
    FAISS Similarity Search
        ↓
    Retrieve Top-K Relevant Document Chunks (typically 3-5 chunks)
        ↓
    Construct Augmented Prompt
        ↓
    Send to OpenAI GPT LLM with:
        • User Question
        • Retrieved Policy Sections (Context)
        • Conversation History
        • System Instructions
        ↓
    LLM Processes & Generates Response
        ↓
    Response Returned to User
        ↓
    Store in Conversation History
```

**RAG Advantages:**
- **Accuracy**: Responses are grounded in actual policy documents, not AI hallucinations
- **Traceability**: Users can see which policy sections informed the answer
- **Currency**: Always uses current uploaded documents as source of truth
- **Context-Aware**: Maintains conversation history for natural multi-turn dialogue

#### 4. **LLM Processing & Response Generation**

The OpenAI GPT model processes queries with specialized prompts:

```
LLM Input Components:
├── System Prompt
│   └── "You are an insurance advisor. Answer using only the provided policy sections..."
├── Retrieved Context
│   └── Relevant policy excerpts from vector search
├── Conversation History
│   └── Previous Q&A for context continuity
└── User Question
    └── Current query

    ↓ (Processing in LLM)

LLM Output:
├── Clear, non-technical explanation
├── Direct answers to user questions
├── Policy references (where the answer comes from)
├── Clarifications and disclaimers
└── Suggested follow-up questions
```

**LLM Capabilities:**
- Interprets complex insurance language
- Translates policy text to plain language
- Handles multi-turn conversations naturally
- Provides contextual explanations
- Recognizes when insufficient information exists

#### 5. **Recommendation Generation**

Smart recommendations use AI to analyze holistically:

```
Recommendation Engine Input:
├── User Profile
│   ├── Age, health status
│   ├── Coverage needs
│   └── Preferences
├── Uploaded Documents
│   ├── Current policy details
│   ├── Coverage limits
│   └── Exclusions
└── Conversation History
    ├── Questions asked
    ├── Concerns expressed
    └── Coverage gaps identified

    ↓ (Analysis by Recommendation Prompt)

Analysis Process:
├── Identify Coverage Gaps
│   └── What's not covered by current policy?
├── Assess Risk Exposure
│   └── What scenarios leave user vulnerable?
├── Calculate Optimization Opportunities
│   └── Where can user improve coverage?
└── Generate Recommendations
    └── Prioritized, actionable suggestions

    ↓

Recommendations Returned:
├── Priority-ordered suggestions
├── Detailed explanations
├── Policy references
└── Expected impact assessment
```

#### 6. **Memory & Conversation Management**

The system maintains stateful interactions:

```
Streamlit Session State
├── user_profile (Current user data)
├── uploaded_documents (Cached document metadata)
├── vector_store (In-memory FAISS index)
├── conversation_history
│   ├── [Query 1] → [Response 1]
│   ├── [Query 2] → [Response 2]
│   └── ... (all interactions)
└── recommendations (Generated suggestions)

Benefits:
• Fast access to all conversation history
• No round-trips to database
• Seamless multi-turn conversations
• Instant recommendations regeneration
```

### Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                      INSURANCE ADVISOR                          │
│                      AI PROCESSING FLOW                         │
└─────────────────────────────────────────────────────────────────┘

                    ┌──────────────────────┐
                    │   User Interaction   │
                    │   (Streamlit UI)     │
                    └──────────┬───────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
                ▼              ▼              ▼
        ┌───────────────┐ ┌──────────┐ ┌──────────────┐
        │  Upload Doc   │ │Chat Ques │ │Get Recommend │
        └───────┬───────┘ └────┬─────┘ └──────┬───────┘
                │              │              │
                ▼              ▼              ▼
        ┌───────────────┐ ┌──────────┐ ┌──────────────┐
        │ Text Extract  │ │ Embedding│ │Profile Analy │
        │   Chunking    │ │Generation│ │sis & Prompt  │
        └───────┬───────┘ └────┬─────┘ └──────┬───────┘
                │              │              │
                ▼              ▼              ▼
        ┌───────────────┐ ┌──────────┐ ┌──────────────┐
        │  FAISS Index  │ │Vector    │ │LLM Process   │
        │  Storage      │ │Similarity│ │(GPT Model)   │
        └───────┬───────┘ │Search    │ └──────┬───────┘
                │         └────┬─────┘        │
                │              │              │
                └──────────────┼──────────────┘
                               │
                    ┌──────────▼───────────┐
                    │  LLM API Call        │
                    │  (OpenAI GPT-3.5+)   │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │  Response Generation │
                    │  with Context        │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │  Response Displayed  │
                    │  History Stored      │
                    └──────────────────────┘
```

### Key AI Technologies Used

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Embeddings** | OpenAI text-embedding-3-small | Convert text to semantic vectors |
| **Vector Search** | FAISS | Fast similarity search in embeddings |
| **Language Model** | OpenAI GPT-3.5-turbo / GPT-4 | Generate intelligent responses |
| **Orchestration** | LangChain | Chain AI components together |
| **State Management** | Streamlit Session State | Maintain conversation context |
| **Storage** | In-Memory Python Objects | Cache documents and history |

### How AI Prevents Hallucinations

Traditional LLMs can "hallucinate" - making up plausible-sounding but false information. The Insurance Advisor prevents this through:

1. **Context Grounding**: All responses must cite retrieved document sections
2. **Retrieval Validation**: Only information from uploaded documents is used
3. **Prompt Engineering**: Instructions explicitly prevent extrapolation beyond source material
4. **User Transparency**: Users can see which document sections informed responses
5. **Graceful Degradation**: System acknowledges when documents don't contain answer

---

## 📱 Use Cases

### For Individual Users
- Understand personal health insurance policy coverage and limitations
- Get answers to specific policy questions without contacting customer service
- Receive recommendations for policy optimization based on personal profile
- Clarify claim procedures and coverage scenarios
- Compare coverage options before renewal

### For Insurance Agents & Brokers
- Quickly explain policy details to clients
- Compare multiple policies and provide recommendations
- Assist clients in policy selection process
- Improve customer service efficiency
- Support policy counseling sessions

### For Enterprises & Insurance Companies
- Provide first-tier customer support for policy inquiries
- Reduce customer support ticket volume
- Improve customer satisfaction and engagement
- Support policy literacy and education initiatives
- Analyze common customer concerns and questions

### For Healthcare & Benefits Administration
- Help employees understand company health benefits
- Reduce HR department inquiries and support costs
- Support employee benefits onboarding
- Answer FAQs about coverage and enrollment
- Provide personalized benefits guidance

---

## 📊 Documentation

### Full Project Report
A comprehensive PDF report including:
- Project definition, purpose, and technology stack
- Detailed use cases and applications
- Application screenshots with descriptions
- Complete source code
- Test data and validation examples

**Location:** `reports/insurance_advisor_project_report.pdf`

### Running Tests

Execute unit tests:
```bash
python -m pytest tests/
python test_llm.py
```

### Configuration

Key configuration points in the code:
- `llm.py` - Configure LLM model and parameters
- `rag.py` - Adjust document chunking and retrieval settings
- `recommendation.py` - Customize recommendation prompts
- `streamlit_app.py` - Modify UI layout and styling

---

## 🔐 Security & Privacy

- Documents are processed securely
- User data is stored in secure sessions
- API keys should be managed using environment variables
- Sensitive information in documents is handled safely

---

## 🤝 Contributing

This is a capstone project. For modifications or improvements:
1. Create a feature branch
2. Make your changes with comprehensive testing
3. Ensure all tests pass
4. Document any new features or changes

---

## 📝 License

This project is created as part of a capstone program.

---

## 📞 Support & Questions

For issues, questions, or suggestions about the Insurance Advisor project:
- Review the PDF report in `reports/`
- Check the test files for usage examples
- Examine the source code documentation

---

**Last Updated:** July 14, 2026  
**Version:** 1.0.0
