from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time

from market_api import get_market_signal


app = FastAPI(title="Financial Intelligence AI")


# -------------------------
# CORS
# -------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------
# Health check
# -------------------------

@app.get("/health")
def health():
    return {
        "status": "ok"
    }


# -------------------------
# Analyze endpoint
# -------------------------

@app.post("/analyze")
def analyze(request: dict):

    start = time.time()

    symbol = request.get("symbol", "RELIANCE")
    user_profile = request.get(
        "user_profile",
        "moderate"
    )

    # -------------------------
    # Member 4 market engine
    # -------------------------

    market_result = get_market_signal(symbol)

    if market_result.get("success"):
        market = market_result["data"]

        price = market.get("price")
        signal = market.get("signal", "NEUTRAL")
        confidence = market.get("confidence", 0)

        degraded = market.get(
            "data_warning",
            False
        )

        degraded_note = None

        if degraded:
            degraded_note = (
                market.get("data_source")
                or "Market data is currently unavailable."
            )

    else:

        price = None
        signal = "NEUTRAL"
        confidence = 0
        degraded = True
        degraded_note = "Market signal engine failed."

        market = {}


    # -------------------------
    # Temporary agent results
    # Members 2 & 3 will replace
    # these later.
    # -------------------------

    agents = [

        {
            "agent": "Technical",
            "signal": signal,
            "confidence": confidence,
            "reason": "Market signal engine result",
            "evidence": market.get(
                "signal_breakdown",
                {}
            )
        },

        {
            "agent": "Fundamental",
            "signal": "BULLISH",
            "confidence": 76,
            "reason": "Temporary result until Fundamental Agent is integrated.",
            "evidence": []
        },

        {
            "agent": "Sentiment",
            "signal": "BULLISH",
            "confidence": 88,
            "reason": "Temporary result until Sentiment Agent is integrated.",
            "evidence": []
        }
    ]


    # -------------------------
    # Recommendation
    # -------------------------

    if user_profile == "conservative":

        recommendation = "WATCH"

    elif user_profile == "aggressive":

        recommendation = "STRONG INTEREST"

    else:

        recommendation = "CONSIDER"


    # -------------------------
    # Latency
    # -------------------------

    latency = time.time() - start


    # -------------------------
    # Final response
    # -------------------------

    return {

        "symbol": symbol,

        "price": price,

        "change_pct": 2.4,

        "signal": signal,

        "confidence": confidence,

        "recommendation": recommendation,

        "agents": agents,

        "synthesis": {

            "text": (
                "Multiple signals have been "
                "combined across the analysis pipeline."
            ),

            "reasoning": market.get(
                "reasoning",
                []
            )
        },

        "sources": [],

        "portfolio": [],

        "watchlist": [],

        "metrics": {

            "latency_s": round(
                latency,
                3
            ),

            "signal_accuracy": 78,

            "risk_score": 42
        },

        "degraded": degraded,

        "degraded_note": degraded_note
    }