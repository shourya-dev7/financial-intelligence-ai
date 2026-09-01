def technical_agent(data):

    momentum = data["momentum"]
    volume = data["volume_ratio"]

    if momentum > 0.6 and volume > 1.2:
        signal = "BULLISH"
        confidence = 85
        reason = "Positive momentum with above-average volume"

    elif momentum < 0.4 and volume < 0.8:
        signal = "BEARISH"
        confidence = 80
        reason = "Weak momentum and low trading volume"

    else:
        signal = "NEUTRAL"
        confidence = 60
        reason = "Technical indicators are mixed"

    return {
        "agent": "Technical Agent",
        "signal": signal,
        "confidence": confidence,
        "reason": reason,
        "evidence": [
            f"Momentum: {momentum}",
            f"Volume ratio: {volume}"
        ]
    }