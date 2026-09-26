from discount import apply_discount, apply_bulk_discount

def test_single_discount():
    assert apply_discount(100, 10) == 90

def test_bulk_discount():
    prices = [100, 200, 300]
    # Expected: 90 + 180 + 270 = 540
    assert apply_bulk_discount(prices, 10) == 540

def test_discount_capped_at_100_percent():
    # Discount should never make price negative
    result = apply_discount(100, 150)
    assert result >= 0
