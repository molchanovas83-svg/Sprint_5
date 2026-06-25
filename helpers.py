import random


class Helpers:
    @staticmethod
    def generate_email():
        return f'mail_{random.randint(100, 999)}@gmail.com'
