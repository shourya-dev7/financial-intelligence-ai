def adjust_for_risk(signal_data, risk_profile):
    """
    Adjust the market signal according to the user's risk profile.

    This is a hackathon personalization/demo layer.
    It does not provide financial advice.

    Risk profiles:
        conservative
        moderate
        aggressive
    """

    risk_profile = risk_profile.lower().strip()

    valid_profiles = ["conservative", "moderate", "aggressive"]

    if risk_profile not in valid_profiles:
        return {
            "success": False,
            "error": "Invalid risk profile. Use conservative, moderate, or aggressive."
        }

    signal = signal_data.get("signal", "NEUTRAL")
    confidence = signal_data.get("confidence", 0)

    # Default recommendation
    recommendation = "WATCH"

    # Conservative profile
    if risk_profile == "conservative":

        if signal == "BULLISH" and confidence >= 85:
            recommendation = "CONSIDER"
        elif signal == "BEARISH":
            recommendation = "WATCH"
        else:
            recommendation = "WATCH"

    # Moderate profile
    elif risk_profile == "moderate":

        if signal == "BULLISH" and confidence >= 70:
            recommendation = "CONSIDER"
        elif signal == "BEARISH" and confidence >= 70:
            recommendation = "WATCH"
        else:
            recommendation = "WATCH"

    # Aggressive profile
    elif risk_profile == "aggressive":

        if signal == "BULLISH" and confidence >= 70:
            recommendation = "STRONG INTEREST"
        elif signal == "BULLISH":
            recommendation = "CONSIDER"
        elif signal == "BEARISH":
            recommendation = "WATCH"
        else:
            recommendation = "CONSIDER"

    return {
        "success": True,
        "risk_profile": risk_profile,
        "market_signal": signal,
        "confidence": confidence,
        "personalized_recommendation": recommendation
    }


if __name__ == "__main__":
    # Example market signal
    example_signal = {
        "signal": "BULLISH",
        "confidence": 79
    }

    profiles = [
        "conservative",
        "moderate",
        "aggressive"
    ]

    for profile in profiles:
        result = adjust_for_risk(example_signal, profile)
        print(profile.upper(), "→", result["personalized_recommendation"])