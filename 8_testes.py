def calculate_discount(price, customer_type):
    if customer_type == "VIP":
        return price * 0.8
    return price

def test_should_return_discount_for_vip():
    assert calculate_discount(100, "VIP") == 80