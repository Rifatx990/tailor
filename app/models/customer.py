from app import db

class Customer:
    def __init__(self, name, email, password, phone):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone

    def save(self):
        cursor = db.cursor()
        query = "INSERT INTO customers (name, email, password, phone) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (self.name, self.email, self.password, self.phone))
        db.commit()
        cursor.close()
