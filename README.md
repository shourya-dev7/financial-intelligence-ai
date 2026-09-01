# Financial Intelligence AI

An AI-powered financial analysis platform that combines market signals, multi-agent reasoning, risk personalization, and retrieval-augmented generation (RAG) to provide explainable stock insights.

---

## Problem

Investors often need to analyze multiple sources of information before making an investment decision.

Market data, technical indicators, company fundamentals, news sentiment, and risk preferences are usually scattered across different sources.

This makes financial analysis time-consuming and difficult to interpret, especially for users with different risk profiles.

---

## Solution

Financial Intelligence AI brings these signals together into a single analysis pipeline.

A user provides:

- Stock symbol
- Risk profile

The system analyzes the stock using multiple intelligence components and returns:

- Market signal
- Confidence score
- Personalized recommendation
- Agent-level reasoning
- Supporting evidence
- Portfolio/watchlist information
- Risk metrics

The system is designed to make financial analysis more explainable rather than simply producing a BUY/SELL-style result.

---

## Architecture

```text
                    User
                      |
                      v
                React Frontend
                      |
                      | POST /analyze
                      v
                FastAPI Backend
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
     Technical   Fundamental   Sentiment
       Agent        Agent        Agent
          |           |           |
          +-----------+-----------+
                      |
                      v
              Market Signal Engine
                      |
                      v
                 RAG Layer
                      |
                      v
              Synthesis / Decision
                      |
                      v
             Risk Personalization
                      |
                      v
                JSON Response
                      |
                      v
                  Frontend
