from ecommerce.pricing import calculate_discounted_price , calculate_total_tax
from ecommerce.order import calculate_total_order, generate_order_id


def main():
    items = [
        {'name': 'Laptop', 'price': calculate_total_tax(calculate_discounted_price(1000, 10),5)},
        {'name': 'phone', 'price': calculate_total_tax(calculate_discounted_price(500,5),5)},
        {'name': 'Headphone', 'price': calculate_total_tax(calculate_discounted_price(200,20),5)}

    ]

    total = calculate_total_order(items)
    order_id = generate_order_id()

    print('order summer:')
    for item in items:
        print(f"{item['name']}: ${item['price']:.2}")
        print(f'Total: ${total:.2}')
        print(f'Order ID: {order_id}')


if __name__ == '__main__':
    main()