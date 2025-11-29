from app import db

class Order:
    def __init__(self, customer_id, order_date, total):
        self.customer_id = customer_id
        self.order_date = order_date
        self.total = total

    def save(self):
        cursor = db.cursor()
        query = "INSERT INTO orders (customer_id, order_date, total) VALUES (%s, %s, %s)"
        cursor.execute(query, (self.customer_id, self.order_date, self.total))
        db.commit()
        cursor.close()
