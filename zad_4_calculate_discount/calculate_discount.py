def calculate_discount(price: float, discount: float) -> float:
    if 0 <= discount <= 1:
        return price*(1-discount)
    else:
        raise ValueError('Discount spoza zakresu 0-1!')
