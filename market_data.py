# ============================================================
# market_data.py
# Market data and fallback data for the Financial Intelligence
# System
# ============================================================


# ============================================================
# PRIMARY MARKET DATA
# ============================================================

stocks = {

    "RELIANCE": {
        "price": 2910,
        "previous_price": 2840,
        "average_volume": 1000000,
        "current_volume": 1450000,
        "sentiment": 0.78
    },

    "TCS": {
        "price": 3890,
        "previous_price": 3920,
        "average_volume": 900000,
        "current_volume": 700000,
        "sentiment": 0.42
    },

    "INFOSYS": {
        "price": 1510,
        "previous_price": 1490,
        "average_volume": 800000,
        "current_volume": 1200000,
        "sentiment": 0.65
    },

    "HDFC": {
        "price": 1680,
        "previous_price": 1700,
        "average_volume": 1100000,
        "current_volume": 1300000,
        "sentiment": 0.38
    },

    "ICICIBANK": {
        "price": 1320,
        "previous_price": 1280,
        "average_volume": 950000,
        "current_volume": 1600000,
        "sentiment": 0.82
    }
}


# ============================================================
# FALLBACK DATA
#
# This data is used when the primary market data source
# becomes unavailable.
# ============================================================

fallback_stocks = {

    "RELIANCE": {
        "price": 2900,
        "previous_price": 2850,
        "average_volume": 1000000,
        "current_volume": 1100000,
        "sentiment": 0.60
    },

    "TCS": {
        "price": 3870,
        "previous_price": 3900,
        "average_volume": 900000,
        "current_volume": 800000,
        "sentiment": 0.50
    },

    "INFOSYS": {
        "price": 1500,
        "previous_price": 1490,
        "average_volume": 800000,
        "current_volume": 900000,
        "sentiment": 0.55
    },

    "HDFC": {
        "price": 1670,
        "previous_price": 1690,
        "average_volume": 1100000,
        "current_volume": 1000000,
        "sentiment": 0.45
    },

    "ICICIBANK": {
        "price": 1300,
        "previous_price": 1285,
        "average_volume": 950000,
        "current_volume": 1000000,
        "sentiment": 0.65
    }
}


# ============================================================
# MARKET DATA STATUS
#
# True  -> Primary market data is available
# False -> Simulate market data failure
#
# Keep this TRUE for the normal demo.
# Change to FALSE to demonstrate the fallback scenario.
# ============================================================

market_available = True


# ============================================================
# GET STOCK DATA
# ============================================================

def get_stock_data(symbol):

    # --------------------------------------------------------
    # PRIMARY DATA AVAILABLE
    # --------------------------------------------------------

    if market_available:

        data = stocks.get(symbol)

        if data is not None:
            return data, False

        return None, False


    # --------------------------------------------------------
    # PRIMARY DATA UNAVAILABLE
    # Use fallback data
    # --------------------------------------------------------

    fallback_data = fallback_stocks.get(symbol)

    if fallback_data is not None:
        return fallback_data, True

    return None, True

