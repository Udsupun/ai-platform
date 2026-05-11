# AI Notes RAG Platform

A full-stack AI-powered semantic note search and Retrieval-Augmented Generation (RAG) application built with FastAPI, React, PostgreSQL, Qdrant, and Ollama.

---

# Features

* JWT authentication
* Semantic note search using embeddings
* Vector database integration with Qdrant
* Retrieval-Augmented Generation (RAG)
* Local LLM inference using Ollama
* PostgreSQL for structured data
* React frontend chat interface
* Dockerized development environment
* Unit testing with pytest
* Code formatting and linting
* Type checking support

---

# Tech Stack

## Backend

* Python 3.12
* FastAPI
* SQLAlchemy
* PostgreSQL
* Alembic
* JWT Authentication
* Sentence Transformers
* Qdrant Vector Database
* Ollama

## Frontend

* React
* Vite
* Axios

## DevOps & Tooling

* Docker
* Docker Compose
* pytest
* Ruff
* Black
* MyPy
* Makefile

---

# Architecture

```text
React Frontend
    ↓
FastAPI Backend
    ↓
Service Layer
    ↓
Repository Layer
    ↓
PostgreSQL

AI Pipeline:
User Question
    ↓
Embedding Generation
    ↓
Qdrant Vector Search
    ↓
Relevant Context Retrieval
    ↓
LLM Prompt Construction
    ↓
Ollama Response
```
---

# Setup Instructions

## Prerequisites

Install:

* Docker Desktop
* Node.js
* npm

---

# Backend Setup

## 1. Clone Repository

```bash
git clone <repository-url>
cd <project-folder>
```

---

## 2. Environment Variables

Copy:

```text
backend/.env.example -> backend/.env
```

---

## 3. Start Docker Containers

```bash
docker compose up -d --build
```

---

## 4. Run Database Migrations

```bash
docker compose exec backend alembic upgrade head
```

---

## 5. Pull Ollama Model

```bash
docker compose exec ollama ollama pull phi3:mini
```

---

# Frontend Setup

## 1. Install Dependencies

```bash
cd frontend
npm install
```

---

## 2. Frontend Environment Variables

Copy:

```text
frontend/.env.example -> frontend/.env
```
---

## 3. Start Frontend

```bash
npm run dev
```

---
# Makefile Commands

## Run Tests

```bash
make test
```

## Run Linting

```bash
make lint
```

## Run Formatting

```bash
make format
```

## Run Full Quality Pipeline

```bash
make quality
```

---
