from app import db

class Worker:
    def __init__(self, name, email, password, role):
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def save(self):
        cursor = db.cursor()
        query = "INSERT INTO workers (name, email, password, role) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (self.name, self.email, self.password, self.role))
        db.commit()
        cursor.close()
