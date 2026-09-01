from signal_engine import analyze_stock


def get_market_signal(symbol):
    """
    Wrapper function for the backend.

    Example:
        get_market_signal("RELIANCE")
    """

    try:
        result = analyze_stock(symbol.upper())

        return {
            "success": True,
            "data": result
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


if __name__ == "__main__":
    result = get_market_signal("RELIANCE")

    print(result)