# 💰 Financial Intelligence AI

> An AI-powered, explainable, and risk-aware financial analysis platform that combines market signals, specialized AI agents, RAG-based information retrieval, and personalized risk preferences.

---

## 📌 Problem

Financial analysis requires combining multiple factors such as:

* 📈 Market data
* 📊 Technical indicators
* 🏢 Company fundamentals
* 📰 News sentiment
* ⚠️ Investor risk preferences

These sources are often scattered across different platforms, making financial analysis time-consuming and difficult to understand.

---

## 💡 Solution

**Financial Intelligence AI** provides a unified platform that combines multiple financial signals and presents an **explainable, evidence-based, and risk-aware stock analysis**.

The user provides:

* A **stock symbol**
* A **risk profile**

The system then analyzes the stock and provides:

* 📊 Overall signal
* 🎯 Confidence score
* 💡 Personalized recommendation
* 📈 Technical analysis
* 🏢 Fundamental analysis
* 📰 Sentiment analysis
* 📚 Supporting evidence
* 🔗 Source information
* 💼 Portfolio information
* 👀 Watchlist information
* ⚠️ Risk metrics
* 🧠 Explainable reasoning

> ⚠️ **Disclaimer:** This system is designed as a decision-support prototype and does not provide financial advice.

---

# 🏗️ Architecture

```text
                         USER
                           |
                           v
                    React Frontend
                           |
                     POST /analyze
                           |
                           v
                    FastAPI Backend
                           |
           +---------------+---------------+
           |               |               |
           v               v               v
      Technical        Fundamental       Sentiment
        Agent             Agent            Agent
           |               |               |
           +---------------+---------------+
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

---

# ✨ Features

* 🤖 Multi-agent financial analysis
* 📈 Technical market analysis
* 🏢 Fundamental analysis
* 📰 News and sentiment analysis
* 📊 Market signal generation
* 📚 Retrieval-Augmented Generation (RAG)
* ⚠️ Risk-profile personalization
* 🧠 Explainable reasoning
* 🔍 Evidence-based analysis
* 🎯 Confidence scoring
* 📉 Risk scoring
* 💼 Portfolio information
* 👀 Watchlist information
* ⚡ FastAPI REST API
* 🌐 CORS-enabled backend
* 📖 Interactive API testing using Swagger

---

# 🛠️ Tech Stack

## Frontend

* React
* JavaScript
* HTML
* CSS

## Backend

* Python
* FastAPI
* Uvicorn

## AI & Intelligence

* Multi-agent architecture
* Retrieval-Augmented Generation (RAG)
* Technical signal analysis
* Fundamental analysis
* Sentiment analysis
* Risk personalization

## Development Tools

* Git
* GitHub
* VS Code

---

# 📁 Project Structure

```text
financial-intelligence-ai/
│
├── backend/
│   └── main.py
│
├── frontend/
│
├── agents/
│
├── rag/
│
├── data/
│
├── market_api.py
├── market_data.py
├── signal_engine.py
│
└── README.md
```

---

# ⚙️ How It Works

1. The user selects a **stock symbol**.
2. The user selects a **risk profile**.
3. The frontend sends a request to the `/analyze` endpoint.
4. The FastAPI backend receives the request.
5. The backend calls the **Market Signal Engine**.
6. Specialized AI agents evaluate different aspects of the stock.
7. The RAG component retrieves supporting financial information.
8. The system combines the available signals and reasoning.
9. The recommendation is personalized according to the user's risk profile.
10. The backend returns a structured JSON response.
11. The frontend displays the analysis to the user.

---

# 🤖 Multi-Agent Architecture

The system uses specialized agents to analyze different dimensions of a stock.

## 📈 Technical Agent

The Technical Agent focuses on market behavior and technical signals.

### It can analyze:

* Price momentum
* Trading volume
* Market movement
* Technical indicators

### The agent provides:

* Signal
* Confidence
* Reason
* Evidence

---

## 🏢 Fundamental Agent

The Fundamental Agent focuses on company and business information.

### It can analyze:

* Revenue growth
* Business performance
* Company disclosures
* Fundamental information

### The agent provides:

* Signal
* Confidence
* Reason
* Evidence

---

## 📰 Sentiment Agent

The Sentiment Agent focuses on the sentiment of relevant financial information and news.

### It can analyze:

* Positive news
* Negative news
* Overall sentiment
* Recent financial information

### The agent provides:

* Signal
* Confidence
* Reason
* Evidence

---

# 📊 Market Signal Engine

The **Market Signal Engine** provides market-level analysis used by the backend.

### Main Interface

```python
from market_api import get_market_signal

result = get_market_signal("RELIANCE")
```

### The interface returns:

* `symbol`
* `price`
* `momentum`
* `volume_ratio`
* `sentiment`
* `signal`
* `confidence`
* `signal_breakdown`
* `reasoning`
* `data_source`
* `data_warning`

### Example Response

```json
{
  "success": true,
  "data": {
    "symbol": "RELIANCE",
    "price": 2910,
    "momentum": 8.4,
    "volume_ratio": 1.4,
    "sentiment": "positive",
    "signal": "BULLISH",
    "confidence": 79,
    "signal_breakdown": {
      "momentum": 8.4,
      "volume": 1.4,
      "sentiment": "positive"
    },
    "reasoning": [],
    "data_source": "market data",
    "data_warning": false
  }
}
```

### Tested Stocks

The Market Signal Engine has been tested with:

* RELIANCE
* TCS
* INFY
* HDFC

### Possible Signal Values

| Signal     | Meaning                      |
| ---------- | ---------------------------- |
| 🟢 BULLISH | Positive market outlook      |
| 🟡 NEUTRAL | No strong directional signal |
| 🔴 BEARISH | Negative market outlook      |

---

# ⚠️ Risk Personalization

The system uses the user's **risk profile** when generating the final recommendation.

### Example

| Risk Profile | Recommendation     |
| ------------ | ------------------ |
| Conservative | 👀 WATCH           |
| Moderate     | 💡 CONSIDER        |
| Aggressive   | 🚀 STRONG INTEREST |

This allows the same underlying market analysis to produce different recommendations based on the user's risk preference.

---

# 📚 Retrieval-Augmented Generation (RAG)

The **RAG component** retrieves relevant financial information to provide supporting context for the analysis.

RAG can be used to:

* Retrieve relevant financial information
* Provide supporting evidence
* Improve explainability
* Support agent reasoning
* Connect analysis to source information

---

# 🔌 API Endpoints

## ❤️ Health Check

```http
GET /health
```

### Example Response

```json
{
  "status": "ok"
}
```

---

## 📊 Stock Analysis

```http
POST /analyze
```

The `/analyze` endpoint accepts a stock symbol and user risk profile and returns the complete financial analysis.

### Example Request

```json
{
  "symbol": "RELIANCE",
  "user_profile": "conservative"
}
```

### Example Response

```json
{
  "symbol": "RELIANCE",
  "price": 2910,
  "change_pct": 2.4,
  "signal": "BULLISH",
  "confidence": 82,
  "recommendation": "WATCH",
  "agents": [
    {
      "agent": "Technical",
      "signal": "BULLISH",
      "confidence": 84,
      "reason": "Positive price momentum with elevated volume",
      "evidence": [
        "20-day momentum: +8.4%",
        "Volume: 1.4x average"
      ]
    },
    {
      "agent": "Fundamental",
      "signal": "BULLISH",
      "confidence": 76,
      "reason": "Retrieved disclosure indicates improving revenue",
      "evidence": [
        "Revenue growth positive",
        "Retail segment expanding"
      ]
    },
    {
      "agent": "Sentiment",
      "signal": "BULLISH",
      "confidence": 88,
      "reason": "Recent news sentiment predominantly positive",
      "evidence": [
        "12 of 15 articles positive"
      ]
    }
  ],
  "synthesis": {
    "text": "Multiple positive signals align across all three dimensions.",
    "reasoning": [
      "Positive momentum",
      "Above-average volume",
      "Positive sentiment"
    ]
  },
  "sources": [
    {
      "file": "reliance.txt",
      "excerpt": "Revenue growth has remained positive..."
    }
  ],
  "portfolio": [
    {
      "symbol": "RELIANCE",
      "pct": 20
    },
    {
      "symbol": "TCS",
      "pct": 15
    },
    {
      "symbol": "CASH",
      "pct": 30
    }
  ],
  "watchlist": [
    {
      "symbol": "TCS",
      "signal": "BULLISH"
    },
    {
      "symbol": "INFOSYS",
      "signal": "NEUTRAL"
    }
  ],
  "metrics": {
    "latency_s": 2.43,
    "signal_accuracy": 78,
    "risk_score": 42
  },
  "degraded": false,
  "degraded_note": null
}
```

---

# 🧪 Testing

The backend can be tested using the FastAPI Swagger interface:

```text
http://127.0.0.1:8000/docs
```

## Health Test

```http
GET /health
```

Expected response:

```json
{
  "status": "ok"
}
```

## Analysis Test

```http
POST /analyze
```

Example request:

```json
{
  "symbol": "RELIANCE",
  "user_profile": "conservative"
}
```

### Market Signal Engine Testing

Tested stocks:

* RELIANCE
* TCS
* INFY
* HDFC

### Risk Personalization Testing

Supported profiles:

* Conservative
* Moderate
* Aggressive

---

# 👥 Team Contributions

## 👨‍💻 Member 1 — Frontend

* Built the dashboard interface
* Implemented frontend user interactions
* Integrated the frontend with the backend API
* Displays analysis results
* Handles API response data

## 🤖 Member 2 — AI / Agents

* Developed AI agent components
* Implemented financial reasoning
* Created specialized analysis outputs

## 📚 Member 3 — RAG

* Developed the RAG component
* Implemented financial information retrieval
* Provides supporting evidence and source context

## 📊 Member 4 — Market Signal Engine

* Developed the Market Signal Engine
* Implemented market indicators
* Created `market_api.py`
* Created `get_market_signal(symbol)`
* Implemented signal generation
* Tested RELIANCE, TCS, INFY, and HDFC

## ⚙️ Member 5 — Backend / Integration

* Developed the FastAPI backend
* Implemented `/analyze`
* Implemented `/health`
* Configured CORS
* Integrated the Market Signal Engine
* Maintained the API response contract
* Tested backend API endpoints
* Supported frontend/backend integration

---

# ⚠️ Limitations

This project is a **hackathon prototype**.

* Market data availability may vary.
* Some components may use prototype or limited data.
* Results depend on the quality and availability of the underlying data.
* The system does not guarantee investment outcomes.
* Production deployment would require additional security, monitoring, validation, and infrastructure.

---

# 🚀 Future Scope

* 📡 Real-time market data
* 🤖 Additional financial analysis agents
* 💼 Advanced portfolio optimization
* ⚠️ Improved risk modeling
* 📚 More financial document sources
* 📰 Advanced sentiment analysis
* 📊 Historical backtesting
* 📈 Model evaluation and monitoring
* 🔐 User authentication
* ☁️ Cloud deployment
* 🗄️ Production-grade database
* ⚡ Caching and performance optimization
* 🔔 Real-time alerts and notifications

---

# ⚠️ Disclaimer

**Financial Intelligence AI** is a hackathon prototype designed for financial analysis and decision-support purposes.

It does **not** provide guaranteed investment outcomes or professional financial advice.

Users should independently verify financial information before making financial decisions.

---

## ⭐ If you like this project

Give the repository a ⭐ on GitHub!
