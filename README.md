Folder structure:-

main.py file: includes the main code of the wordle game (the functions and the main loop).

dataset.txt file: includes set of all 5-letter words in the dictionary, the program picks a random target word from here.

README.md file: text file includes folder layout, how the game works and explains the code logic.


Logical structure:-

Functions:
random_word: for the program to choose a random word from the dataset file and make it the target to be guessed.

enter_word: for input handling takes guessed word from user letter by letter.

check_guess: checks whether the guess provided by user is in the dataset or not.

feedback: compares each letter of the guess to the target and says if it’s in the correct place, in the wrong place, or not in the word at all.


Main game code: 
consists of a loop with 6 iterations to give the user 6 chances of guessing the word, the output of each iteration in the main loop will be one of the following:
1-when the guess is wrong but in the dataset: 'Incorrect guess' along with feedback
2-when the guess isn't in the dataset: 'That word isn't in the dictionary'
3-when the guess is correct:'Congratulations you've guessed the word correctly'

The game ends when the user correctly guesses the words or when the 6 loop iterations are done without reaching the correct guess <game over>

