# ============================================================
# signal_engine.py
#
# Market Signal Engine
#
# Evaluates three independent dimensions:
# 1. Price Momentum
# 2. Volume Anomaly
# 3. Market Sentiment
#
# Produces:
# - Signal classification
# - Confidence
# - Reasoning
# - Signal breakdown
# - Data source information
# ============================================================


from market_data import get_stock_data


# ============================================================
# 1. CALCULATE PRICE MOMENTUM
# ============================================================

def calculate_momentum(data):

    current_price = data["price"]

    previous_price = data["previous_price"]

    momentum = (
        (current_price - previous_price)
        / previous_price
    ) * 100

    return momentum


# ============================================================
# 2. CONVERT MOMENTUM INTO SCORE
#
# Score range: 0 to 1
# ============================================================

def momentum_score(momentum):

    if momentum >= 3:
        return 1.0

    elif momentum >= 1:
        return 0.8

    elif momentum >= 0:
        return 0.6

    elif momentum >= -1:
        return 0.4

    elif momentum >= -3:
        return 0.2

    else:
        return 0.0


# ============================================================
# 3. CALCULATE VOLUME RATIO
#
# Current Volume / Average Volume
# ============================================================

def calculate_volume_ratio(data):

    current_volume = data["current_volume"]

    average_volume = data["average_volume"]

    ratio = current_volume / average_volume

    return ratio


# ============================================================
# 4. CONVERT VOLUME INTO SCORE
#
# Score range: 0 to 1
# ============================================================

def volume_score(ratio):

    if ratio >= 1.5:
        return 1.0

    elif ratio >= 1.2:
        return 0.8

    elif ratio >= 0.8:
        return 0.5

    elif ratio >= 0.5:
        return 0.3

    else:
        return 0.1


# ============================================================
# 5. GET SENTIMENT SCORE
#
# Sentiment is already between 0 and 1
# ============================================================

def calculate_sentiment(data):

    return data["sentiment"]


# ============================================================
# 6. CALCULATE FINAL SIGNAL SCORE
#
# Momentum  = 40%
# Volume    = 30%
# Sentiment = 30%
# ============================================================

def calculate_final_score(
    momentum,
    volume,
    sentiment
):

    score = (
        momentum * 0.40
        + volume * 0.30
        + sentiment * 0.30
    )

    return score


# ============================================================
# 7. CLASSIFY SIGNAL
#
# 0.65 - 1.00 -> BULLISH
# 0.40 - 0.64 -> NEUTRAL
# 0.00 - 0.39 -> BEARISH
# ============================================================

def classify_signal(score):

    if score >= 0.65:
        return "BULLISH"

    elif score >= 0.40:
        return "NEUTRAL"

    else:
        return "BEARISH"


# ============================================================
# 8. CALCULATE CONFIDENCE
#
# Converts score into percentage.
# ============================================================

def calculate_confidence(score):

    return round(score * 100)


# ============================================================
# 9. GENERATE EXPLAINABLE REASONING
# ============================================================

def generate_reasoning(
    momentum,
    volume_ratio,
    sentiment
):

    reasons = []


    # --------------------------------------------------------
    # Momentum reasoning
    # --------------------------------------------------------

    if momentum >= 1:

        reasons.append(
            "Positive price momentum"
        )

    elif momentum < 0:

        reasons.append(
            "Negative price momentum"
        )

    else:

        reasons.append(
            "Stable price movement"
        )


    # --------------------------------------------------------
    # Volume reasoning
    # --------------------------------------------------------

    if volume_ratio >= 1.2:

        reasons.append(
            "Trading volume is above average"
        )

    elif volume_ratio < 0.8:

        reasons.append(
            "Trading volume is below average"
        )

    else:

        reasons.append(
            "Trading volume is near average"
        )


    # --------------------------------------------------------
    # Sentiment reasoning
    # --------------------------------------------------------

    if sentiment >= 0.65:

        reasons.append(
            "Positive market sentiment"
        )

    elif sentiment <= 0.35:

        reasons.append(
            "Negative market sentiment"
        )

    else:

        reasons.append(
            "Neutral market sentiment"
        )


    return reasons


# ============================================================
# 10. MAIN STOCK ANALYSIS FUNCTION
# ============================================================

def analyze_stock(symbol):

    # Get market data
    data, used_fallback = get_stock_data(symbol)


    # --------------------------------------------------------
    # Stock not found
    # --------------------------------------------------------

    if data is None:

        return {

            "symbol": symbol,

            "signal": "UNAVAILABLE",

            "confidence": 0,

            "reasoning": [
                "Stock data could not be found"
            ],

            "data_source": "Unavailable",

            "data_warning": True
        }


    # --------------------------------------------------------
    # Calculate momentum
    # --------------------------------------------------------

    momentum = calculate_momentum(data)

    momentum_s = momentum_score(momentum)


    # --------------------------------------------------------
    # Calculate volume
    # --------------------------------------------------------

    volume_ratio = calculate_volume_ratio(data)

    volume_s = volume_score(volume_ratio)


    # --------------------------------------------------------
    # Calculate sentiment
    # --------------------------------------------------------

    sentiment = calculate_sentiment(data)


    # --------------------------------------------------------
    # Calculate final score
    # --------------------------------------------------------

    final_score = calculate_final_score(

        momentum_s,

        volume_s,

        sentiment
    )


    # --------------------------------------------------------
    # Classify signal
    # --------------------------------------------------------

    signal = classify_signal(final_score)


    # --------------------------------------------------------
    # Calculate confidence
    # --------------------------------------------------------

    confidence = calculate_confidence(final_score)


    # --------------------------------------------------------
    # Generate reasoning
    # --------------------------------------------------------

    reasoning = generate_reasoning(

        momentum,

        volume_ratio,

        sentiment
    )


    # --------------------------------------------------------
    # Reduce confidence when fallback data is used
    #
    # This makes the degraded-data scenario visible.
    # --------------------------------------------------------

    if used_fallback:

        confidence = round(confidence * 0.75)

        reasoning.append(
            "Primary market data unavailable; "
            "fallback data was used"
        )


    # --------------------------------------------------------
    # Determine data source
    # --------------------------------------------------------

    if used_fallback:

        data_source = "Fallback data"

    else:

        data_source = "Primary market data"


    # --------------------------------------------------------
    # Return complete structured result
    # --------------------------------------------------------

    return {

        "symbol": symbol,

        "price": data["price"],

        "momentum": round(
            momentum,
            2
        ),

        "volume_ratio": round(
            volume_ratio,
            2
        ),

        "sentiment": round(
            sentiment,
            2
        ),

        "signal": signal,

        "confidence": confidence,

        "signal_breakdown": {

            "momentum": round(
                momentum_s * 100
            ),

            "volume": round(
                volume_s * 100
            ),

            "sentiment": round(
                sentiment * 100
            )
        },

        "reasoning": reasoning,

        "data_source": data_source,

        "data_warning": used_fallback
    }


# ============================================================
# OPTIONAL: RUN DIRECTLY
#
# This allows you to run:
#
# python signal_engine.py
#
# ============================================================

if __name__ == "__main__":

    result = analyze_stock("RELIANCE")

    print("\n====================================")
    print("     FINANCIAL SIGNAL ENGINE")
    print("====================================")

    print(
        "Stock:",
        result["symbol"]
    )

    print(
        "Price:",
        result["price"]
    )

    print(
        "Momentum:",
        result["momentum"],
        "%"
    )

    print(
        "Volume Ratio:",
        result["volume_ratio"]
    )

    print(
        "Sentiment:",
        result["sentiment"]
    )

    print(
        "Signal:",
        result["signal"]
    )

    print(
        "Confidence:",
        result["confidence"],
        "%"
    )

    print(
        "Data Source:",
        result["data_source"]
    )

    print("\nSignal Breakdown:")

    print(
        "Momentum:",
        result["signal_breakdown"]["momentum"],
        "%"
    )

    print(
        "Volume:",
        result["signal_breakdown"]["volume"],
        "%"
    )

    print(
        "Sentiment:",
        result["signal_breakdown"]["sentiment"],
        "%"
    )

    print("\nReasoning:")

    for reason in result["reasoning"]:

        print(
            " -",
            reason
        )

    if result["data_warning"]:

        print(
            "\nWARNING:",
            "Fallback data is being used."
        )

    print("====================================")

