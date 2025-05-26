def calculate_discounted_price(price,discout_percent):
    discout_amount = price * (discout_percent / 100)
    return price - discout_amount




def calculate_total_tax(price, tax_percent):
    tax_amount = price * (tax_percent / 100)
    return price + tax_amount