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

def check_guess(file_name,guess):
    with open(file_name, 'r') as file:
        dataset = file.read().splitlines()
        if guess in dataset:
            return True
        else:
            return False
        

target = random_word("dataset.txt")
print("You have 6 guesses")

for i in range(6):  #creates 6*5 grid
    print(f"Enter your guess no {i+1}")
    guess = enter_word()

    if check_guess("dataset.txt", guess):
        if guess == target:
            print("You've guessed the word correctly")
            break
        else:
            print("Incorrect guess")
    else:
        print("That word isn't in the dictionary")

else:
    print("Game over ---- you've used all your guesses")