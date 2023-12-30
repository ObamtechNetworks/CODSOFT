#!usr/bin/python3
"""thinking of using json serialization
Later project to work on
"""


import json


class FileStorage:
    """file storage class for hanlding storage"""
    def __init__(self, filename):
        self.filename = filename

    def save_data(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file)

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

# Example usage:
# storage = FileStorage('tasks.json')
# tasks = storage.load_data()
# tasks.append('New Task')
# storage.save_data(tasks)
