from agents.technical_agent import technical_agent
from agents.fundamental_agent import fundamental_agent
from agents.sentiment_agent import sentiment_agent
from agents.synthesis_agent import synthesis_agent


# Sample market data
market_data = {
    "symbol": "RELIANCE",
    "price": 2910,
    "momentum": 0.72,
    "volume_ratio": 1.45,
    "sentiment": 0.68
}


# Fundamental information
documents = [
    {
        "source": "reliance_report.txt",
        "text": "Revenue growth remained positive."
    }
]


# Run the three agents
technical = technical_agent(market_data)

fundamental = fundamental_agent(documents)

sentiment = sentiment_agent(market_data)


# Synthesis agent combines their results
final_result = synthesis_agent(
    technical,
    fundamental,
    sentiment
)


print("\n--- TECHNICAL AGENT ---")
print(technical)

print("\n--- FUNDAMENTAL AGENT ---")
print(fundamental)

print("\n--- SENTIMENT AGENT ---")
print(sentiment)

print("\n--- FINAL SYNTHESIS ---")
print(final_result)