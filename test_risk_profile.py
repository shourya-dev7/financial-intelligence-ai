from market_api import get_market_signal
from risk_profile import adjust_for_risk


symbol = "RELIANCE"

market_result = get_market_signal(symbol)

if market_result["success"]:

    signal_data = market_result["data"]

    print("\nSTOCK:", symbol)
    print("MARKET SIGNAL:", signal_data["signal"])
    print("CONFIDENCE:", signal_data["confidence"])

    print("\nPERSONALIZED RESULTS:")

    profiles = [
        "conservative",
        "moderate",
        "aggressive"
    ]

    for profile in profiles:

        result = adjust_for_risk(
            signal_data,
            profile
        )

        print(
            profile.upper(),
            "→",
            result["personalized_recommendation"]
        )

else:

    print("Market signal failed:")
    print(market_result["error"])