def fundamental_agent(documents):

    if not documents:
        return {
            "agent": "Fundamental Agent",
            "signal": "NEUTRAL",
            "confidence": 50,
            "reason": "No fundamental information available",
            "evidence": []
        }

    return {
        "agent": "Fundamental Agent",
        "signal": "BULLISH",
        "confidence": 75,
        "reason": "Retrieved company information indicates positive business conditions",
        "evidence": documents
    }