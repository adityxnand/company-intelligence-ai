# 🧠 Company Intelligence AI

Company Intelligence AI is an AI-powered company research assistant that aims to make it easier to understand companies through their public filings and documents.

The long-term goal is to allow users to select a company such as **Apple, Microsoft, or NVIDIA** and ask questions about its business, financial performance, risks, and historical filings.

Instead of manually going through hundreds of pages of company reports, the system will retrieve the relevant information and use an LLM to generate a useful, source-grounded answer.

---

## 🚧 Current Progress

The project is currently in the **early development stage**.

### ✅ Completed

### Document Ingestion Pipeline

The first part of the system is the **ingestion pipeline**.

Its purpose is to take company documents and prepare them for the later stages of the AI pipeline.

```text
Company Documents
       ↓
     Loading
       ↓
  Document Processing
       ↓
    Chunking
       ↓
   Preparation
```

The ingestion layer is being organized into separate components for:

- Document loading
- Document processing
- Chunking
- Embedding preparation

The goal is to keep the ingestion process modular so that it can later be connected to the database, retrieval, and RAG layers.

---

## 🔮 What I Plan to Build

The ingestion pipeline is only the beginning.

The planned system will eventually look something like:

```text
SEC / EDGAR
     ↓
Company Documents
     ↓
Ingestion Pipeline        ← Current stage
     ↓
PostgreSQL + pgvector
     ↓
Retrieval
     ↓
RAG
     ↓
LLM
     ↓
Company Intelligence Assistant
```

The future goal is to build an assistant that can answer questions about companies using information retrieved directly from their filings and documents.

For example:

> "What are Apple's major business risks?"

> "How has Apple's revenue changed over the years?"

> "What does NVIDIA say about competition?"

The system should retrieve the relevant parts of the underlying documents before generating an answer.

---

## 🛠️ Current Tech Stack

- **Python**
- **SEC / EDGAR** for company filings
- **PostgreSQL** for data storage
- **pgvector** for vector search
- **LLMs** for the future RAG layer

---

## 📁 Project Structure

```text
company-intelligence-ai/
│
├── backend/
│   └── src/
│       └── company_ai/
│           │
│           ├── ingestion/
│           │   ├── loaders/
│           │   ├── chunking/
│           │   └── embedding/
│           │
│           ├── db/
│           ├── retrieval/
│           └── ...
│
└── README.md
```

The project is actively being developed, and the architecture will evolve as new parts of the system are built.

---

## 🚧 Status

**Currently working on:** Document ingestion pipeline

**Next:** Database and embedding layer

**Eventually:** Retrieval → RAG → Company Intelligence Assistant