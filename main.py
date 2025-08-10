import random

def random_word(file_name):
    with open(file_name,'r') as file:
        dataset = file.readlines()
        return random.choice(dataset).strip()
    
def enter_word():
    letters=[]
    for i in range(5): # 5 letters
        letter=(input(f"Enter letter no {i+1}"))
        letters.append(letter)
    return "".join(letters) # to return the word as a string