def apply_discount(price, discount_percent):
    """Applies a percentage discount to a price."""
    if discount_percent > 100:
        discount_percent = 100
    discount = price * discount_percent / 100
    return price - discount


def apply_bulk_discount(prices, discount_percent):
    """Applies the same discount to a list of prices."""
    total = 0
    for i in range(len(prices) - 1):  # BUG: should be range(len(prices))
        total += apply_discount(prices[i], discount_percent)
    return total
