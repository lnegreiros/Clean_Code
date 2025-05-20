def calculate_discount(price, customer_type):
    # VIP customers receive a 20% discount
    if customer_type == "VIP":
        return price * 0.8
    return price