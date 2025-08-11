import random

def random_word(file_name):
    with open(file_name,'r') as file:
        dataset = file.readlines()
        return random.choice(dataset).strip()
    
def enter_word():
    letters=[]
    for i in range(5): # 5 letters
        letter=(input(f"Enter letter no {i+1}: "))
        letters.append(letter)
    return "".join(letters) # to return the word as a string

def check_guess(file_name,guess):
    with open(file_name, 'r') as file:
        dataset = file.read().splitlines()
        if guess in dataset:
            return True
        else:
            return False
        
### function for game logic
def feedback(guess, target):
    result = []
    for i in range(len(guess)):
        if guess[i] == target[i]:
            result.append(guess[i] + " is in the right position")
        elif guess[i] in target:
            result.append(guess[i] + " is in the word but in the wrong position")
        else:
            result.append(guess[i] + " is not in the word")
    return "\n".join(result)
        

target = random_word("dataset.txt")
print("You have 6 guesses")

for i in range(6):  #creates 6*5 grid
    print(f"\nEnter guess no {i+1}:-")
    guess = enter_word()

    if check_guess("dataset.txt", guess):
        if guess == target:
            print("Congratulations you've guessed the word correctly!")
            break
        else:
            print("\nIncorrect guess")
            print("\nfeedback:\n" + feedback(guess,target))

    else:
        print("That word isn't in the dictionary")

else:
    print("Game over ---- you've used all your guesses")