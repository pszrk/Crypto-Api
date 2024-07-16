def format(price):
    try:
        if(price >= 1000):
            return f"{price:.0f}"        
        if price >= 1:
            return f"{price:.02f}"
        return f"{price:.4g}"
    except:
        return price
    
