def format_price(price):
    try:
        if price >= 1:
            return f"{price:.02f}"
        return f"{price:.4g}"
    except:
        return price