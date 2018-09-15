import os
import string
import random


def generate_random_string(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
