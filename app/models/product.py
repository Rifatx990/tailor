from app import db

class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def save(self):
        cursor = db.cursor()
        query = "INSERT INTO products (name, description, price) VALUES (%s, %s, %s)"
        cursor.execute(query, (self.name, self.description, self.price))
        db.commit()
        cursor.close()
