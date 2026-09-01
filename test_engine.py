# ============================================================
# test_engine.py
#
# Testing file for the Market Signal Engine
# ============================================================


import market_data

from signal_engine import analyze_stock


# ============================================================
# FUNCTION TO DISPLAY RESULT
# ============================================================

def display_result(result):

    print("\n")
    print("============================================")
    print("          FINANCIAL INTELLIGENCE")
    print("============================================")


    print(
        "Stock:",
        result["symbol"]
    )


    # --------------------------------------------------------
    # Check whether stock data is available
    # --------------------------------------------------------

    if result["signal"] == "UNAVAILABLE":

        print(
            "Signal:",
            "UNAVAILABLE"
        )

        print(
            "Confidence:",
            "0%"
        )

        print("\nReason:")

        for reason in result["reasoning"]:

            print(
                " -",
                reason
            )

        return


    # --------------------------------------------------------
    # Basic information
    # --------------------------------------------------------

    print(
        "Price:",
        "₹" + str(result["price"])
    )

    print(
        "Momentum:",
        str(result["momentum"]) + "%"
    )

    print(
        "Volume Ratio:",
        result["volume_ratio"]
    )

    print(
        "Sentiment:",
        result["sentiment"]
    )


    # --------------------------------------------------------
    # Final signal
    # --------------------------------------------------------

    print("\n--------------------------------------------")

    print(
        "SIGNAL:",
        result["signal"]
    )

    print(
        "CONFIDENCE:",
        str(result["confidence"]) + "%"
    )

    print("--------------------------------------------")


    # --------------------------------------------------------
    # Signal breakdown
    # --------------------------------------------------------

    print("\nSIGNAL BREAKDOWN")

    print(
        "Momentum:",
        str(
            result["signal_breakdown"]["momentum"]
        ) + "%"
    )

    print(
        "Volume:",
        str(
            result["signal_breakdown"]["volume"]
        ) + "%"
    )

    print(
        "Sentiment:",
        str(
            result["signal_breakdown"]["sentiment"]
        ) + "%"
    )


    # --------------------------------------------------------
    # Reasoning
    # --------------------------------------------------------

    print("\nREASONING")

    for reason in result["reasoning"]:

        print(
            " ✓",
            reason
        )


    # --------------------------------------------------------
    # Data source
    # --------------------------------------------------------

    print("\nDATA SOURCE:")

    print(
        result["data_source"]
    )


    # --------------------------------------------------------
    # Warning
    # --------------------------------------------------------

    if result["data_warning"]:

        print("\n⚠ WARNING:")

        print(
            "Primary market data was unavailable."
        )

        print(
            "Fallback data was used."
        )

    else:

        print(
            "\n✓ Primary market data available."
        )


    print(
        "============================================"
    )


# ============================================================
# TEST 1
# NORMAL MARKET DATA
# ============================================================

print("\n\n")
print("############################################")
print("# TEST 1: PRIMARY MARKET DATA")
print("############################################")


# Make sure primary data is enabled

market_data.market_available = True


# Test RELIANCE

result = analyze_stock("RELIANCE")

display_result(result)


# ============================================================
# TEST 2
# TEST ALL STOCKS
# ============================================================

print("\n\n")
print("############################################")
print("# TEST 2: ALL STOCKS")
print("############################################")


stocks_to_test = [

    "RELIANCE",
    "TCS",
    "INFOSYS",
    "HDFC",
    "ICICIBANK"
]


for stock in stocks_to_test:

    result = analyze_stock(stock)

    print(
        stock,
        "→",
        result["signal"],
        "| Confidence:",
        str(result["confidence"]) + "%"
    )


# ============================================================
# TEST 3
# DEGRADED DATA SCENARIO
# ============================================================

print("\n\n")
print("############################################")
print("# TEST 3: DEGRADED DATA")
print("############################################")


# Simulate market data failure

market_data.market_available = False


# Analyze RELIANCE again

result = analyze_stock("RELIANCE")

display_result(result)


# ============================================================
# TEST 4
# UNKNOWN STOCK
# ============================================================

print("\n\n")
print("############################################")
print("# TEST 4: UNKNOWN STOCK")
print("############################################")


result = analyze_stock("UNKNOWN")

display_result(result)


# ============================================================
# FINISHED
# ============================================================

print("\n\n")
print("############################################")
print("# ALL TESTS COMPLETED")
print("############################################")

