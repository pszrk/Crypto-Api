def format_price(price):
    if price >= 1:
        return f"{price:.02f}"
    return f"{price:.4g}"

print(f"{format_price(0.2341234)}")
print(f"{format_price(324534253425.23142314)}")
print(f"{format_price(2134)}")
print(f"{format_price(0.00000000000002341234)}")