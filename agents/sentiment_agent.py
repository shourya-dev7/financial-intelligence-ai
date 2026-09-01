def sentiment_agent(data):

    sentiment = data["sentiment"]

    if sentiment > 0.65:
        signal = "BULLISH"
        confidence = int(sentiment * 100)
        reason = "Overall news sentiment is positive"

    elif sentiment < 0.35:
        signal = "BEARISH"
        confidence = int((1 - sentiment) * 100)
        reason = "Overall news sentiment is negative"

    else:
        signal = "NEUTRAL"
        confidence = 60
        reason = "News sentiment is mixed"

    return {
        "agent": "Sentiment Agent",
        "signal": signal,
        "confidence": confidence,
        "reason": reason,
        "evidence": [
            f"Sentiment score: {sentiment}"
        ]
    }