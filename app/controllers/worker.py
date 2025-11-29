from flask import request, jsonify
from app.models.worker import Worker

class WorkerController:
    def create(self):
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']
        role = request.json['role']
        worker = Worker(name, email, password, role)
        worker.save()
        return jsonify({'message': 'Worker created successfully'}), 201

    def get_all(self):
        cursor = db.cursor()
        query = "SELECT * FROM workers"
        cursor.execute(query)
        workers = cursor.fetchall()
        cursor.close()
        return jsonify([{'id': worker[0], 'name': worker[1], 'email': worker[2], 'role': worker[3]} for worker in workers]), 200
