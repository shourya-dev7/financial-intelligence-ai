# Financial Intelligence AI

## Problem

Financial analysis requires combining multiple factors such as market data, technical indicators, company fundamentals, news sentiment, and investor risk preferences.

These sources are often scattered across different places, making financial analysis time-consuming and difficult to understand.

Our project provides a unified platform that combines these signals and presents an explainable, risk-aware stock analysis.

## Solution

Financial Intelligence AI is an AI-powered financial analysis platform that combines market signals, multiple specialized agents, RAG-based information retrieval, and risk personalization.

The user provides a stock symbol and risk profile. The system analyzes the stock and returns:

- Overall signal
- Confidence score
- Personalized recommendation
- Technical analysis
- Fundamental analysis
- Sentiment analysis
- Supporting evidence
- Sources
- Portfolio information
- Watchlist information
- Risk metrics
- Explainable reasoning

The system is designed as a decision-support prototype and not as financial advice.

## Architecture

```text
                         USER
                           |
                           v
                    React Frontend
                           |
                           | POST /analyze
                           v
                    FastAPI Backend
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
     Technical        Fundamental       Sentiment
       Agent             Agent            Agent
          |                |                |
          +----------------+----------------+
                           |
                           v
                 Market Signal Engine
                           |
                           v
                           RAG
                           |
                           v
                  Signal Synthesis
                           |
                           v
                 Risk Personalization
                           |
                           v
                  Structured JSON
                           |
                           v
                    React Frontend
```

##Features
Multi-agent financial analysis
Technical market analysis
Fundamental analysis
News and sentiment analysis
Market signal generation
Retrieval-Augmented Generation (RAG)
Risk-profile personalization
Explainable reasoning
Evidence-based analysis
Confidence scoring
Risk scoring
Portfolio information
Watchlist information
FastAPI REST API
CORS-enabled backend
Interactive API testing through Swagger

##Tech Stack
###Frontend
React
JavaScript
HTML
CSS
###Backend
Python
FastAPI
Uvicorn
###AI and Intelligence
Multi-agent architecture
Retrieval-Augmented Generation (RAG)
Technical signal analysis
Fundamental analysis
Sentiment analysis
Risk personalization
###Development
Git
GitHub
VS Code
