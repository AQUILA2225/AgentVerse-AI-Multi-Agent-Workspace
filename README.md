# AgentVerse AI

## Overview

AgentVerse AI is a multi-agent AI workspace built using Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), memory systems, and vector databases. The project is designed to provide personalized AI assistance for multiple purposes such as career guidance, idea discussion, daily task planning, interview preparation, and resume analysis.

The application combines conversational AI with long-term memory and knowledge retrieval to create a more intelligent and context-aware user experience. Unlike a basic chatbot, AgentVerse AI can remember previous conversations, retrieve relevant information from stored knowledge, and provide personalized responses based on the user’s goals and interactions.

The project demonstrates the practical implementation of modern Generative AI concepts including memory-based AI systems, multi-agent architecture, prompt engineering, vector embeddings, semantic search, and AI-powered document analysis.

---

# Objectives

## Main Objectives

The main objective of this project is to build an intelligent AI assistant platform capable of:

- Maintaining conversation memory
- Retrieving personalized knowledge using RAG
- Supporting multiple AI agents for different tasks
- Providing career and learning guidance
- Generating daily learning tasks
- Assisting with resume analysis and ATS optimization
- Delivering a ChatGPT-style conversational experience

---

# Features

## Multi-Agent Architecture

The application contains multiple specialized AI agents, where each agent performs a specific role.

### Idea Discussion Agent
Helps users brainstorm ideas, improve concepts, compare solutions, and convert raw ideas into structured project plans.

### Career Mentor Agent
Provides career guidance, learning roadmaps, skill recommendations, and project suggestions for AI, ML, and GenAI domains.

### Daily Task Agent
Generates practical beginner-friendly daily learning tasks to help users maintain consistency and improve skills step by step.

### Resume Analyzer Agent
Analyzes uploaded resumes against job descriptions and provides ATS-style feedback, missing skills analysis, improvement suggestions, and optimized resume bullet points.

### Interview Preparation Agent
Helps users prepare for technical and HR interviews by generating interview questions and beginner-friendly answers.

---

# Memory System

## Persistent Conversation Memory

The project includes a persistent memory system that stores previous conversations in a JSON file. The AI can use previous interactions while generating new responses, allowing it to provide personalized and context-aware guidance.

### The Memory System Enables the Application To:
- Remember user goals
- Continue previous discussions
- Track learning interests
- Provide more relevant recommendations

---

# Retrieval-Augmented Generation (RAG)

## RAG Workflow

The project uses RAG to retrieve relevant information from a personal knowledge base before generating responses.

### Workflow Includes:
- Reading user notes and stored knowledge
- Converting text into vector embeddings
- Storing embeddings inside ChromaDB
- Performing semantic similarity search
- Supplying retrieved information to the LLM

This allows the AI to generate responses using both:
- Model knowledge
- User-specific stored knowledge

---

# Vector Database and Embeddings

## ChromaDB Integration

The project uses ChromaDB as a vector database for storing embeddings generated from user knowledge documents.

Text embeddings are created using OpenAI embedding models. These embeddings allow semantic similarity search, enabling the AI to retrieve relevant information based on meaning instead of exact keyword matching.

---

# Resume Analyzer System

## Key Features

The Resume Analyzer Agent supports:

- Resume PDF upload
- PDF text extraction using PyPDF2
- Job description input
- ATS-style resume analysis
- Skill matching
- Missing skills detection
- Resume improvement suggestions
- Suggested resume bullet points

The AI compares resume content with the job description and generates personalized feedback for improving resume quality and ATS compatibility.

---

# Technologies Used

## Core Technologies

- Python
- Streamlit
- GROK API
- LangChain
- ChromaDB
- PyPDF2
- RAG Architecture
- Vector Embeddings
- JSON Memory Storage

---

# Working Flow

## Application Workflow

1. User selects an AI agent from the sidebar.
2. The selected agent opens a dedicated chat session.
3. User interacts with the AI through a ChatGPT-style interface.
4. Previous memory is loaded from backend storage.
5. Relevant information is retrieved from the vector database using RAG.
6. The LLM generates a personalized response using:
   - Current user query
   - Previous conversation memory
   - Retrieved knowledge
   - Agent-specific instructions
7. The response is displayed in the UI and saved to memory.

---

# Learning Outcomes

## Skills Demonstrated

This project demonstrates practical implementation of:

- Generative AI applications
- Multi-agent AI systems
- Retrieval-Augmented Generation
- Prompt Engineering
- LLM Integration
- Vector Databases
- Semantic Search
- AI-powered Resume Analysis
- Persistent Memory Systems
- Streamlit-based AI interfaces

---

# Use Cases

## Real-World Applications

- AI career guidance
- Personalized learning assistance
- Resume optimization
- Interview preparation
- Project brainstorming
- Daily productivity assistance
- AI-powered mentoring systems