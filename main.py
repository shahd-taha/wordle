import random

def random_word(file_name):
    with open(file_name,'r') as file:
        dataset = file.readlines()
        return random.choice(dataset).strip()