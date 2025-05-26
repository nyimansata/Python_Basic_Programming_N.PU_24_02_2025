import uuid

def calculate_total_order(items):
    total = 0
    for item in items:
        total += item['price']
        return total
    
def generate_order_id():
    return str(uuid.uuid4())