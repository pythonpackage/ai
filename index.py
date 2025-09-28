program - 7 Tower of hanoi

def tower_of_hanoi(n, source, aux, dest):
    if n == 0:
        return
    tower_of_hanoi(n - 1, source, dest, aux)
    print(f"Move disk {n} from source {source} to destination {dest}")
    tower_of_hanoi(n - 1, aux, source, dest)
n=3
tower_of_hanoi(n,"A","B","C")

program - 8  Monkey Banana Problem

def monkey_banana_problem(n):
    climb = 0
    bananas = 0
    hungry = True
    for i in range(n):
        if hungry:
            climb += 1
            bananas += 1
            hungry = False
        else:
            climb += 1
    return climb, bananas
n = 10
climb, bananas = monkey_banana_problem(n)
print(f"The monkey made {climb} climbs and get {bananas} bananas.")

program - 9 Alpha Beta Pruning

MAX, MIN = 1000, -1000


def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]
    if maximizingPlayer:
        best = MIN
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = MAX
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break
        return best


values = [3, 5, 6, 9, 1, 2, 0, -1]
print("The optimal value is:", minimax(0, 0, True, values, MIN, MAX)) 

program - 10  8 queens problem

global N
N=4
def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j],end=" ")
        print()
def isSafe(board,row,col):
    for i in range(col):
        if board[row][i]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    for i,j in zip(range(row,N,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    return True
def solveNQUtil(board,col):
    if col>=N:
        return True
    for i in range(N):
        if isSafe(board,i,col):
            board[i][col]=1
            if solveNQUtil(board,col+1)==True:
                return True
            board[i][col]=0
    return False
def solveNQ():
    board=[
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
    if solveNQUtil(board,0)==False:
        print("Solution Does not exist")
        return False
    printSolution(board)
    return True
solveNQ() 

program - 11   Simple Chatbot

import random
responses=["Hello,how can I help you?",
    "What do you want to talk about?",
    "I'm not sure what you mean.",
    "Can you repeat that?",
    "I'm sorry,I don't understand.",
    "Goodbye!"]
def get_response():
    return random.choice(responses)
def start_chatbot():
    print("Hello,I'm a chatbot.What do you want to talk about?")
    while True:
        user_input=input()
        response=get_response()
        print(response)
start_chatbot()

program - 12  Hangman Game
import random
import string

def choose_word():
    words = ["python", "hangman", "programming", "developer", "artificial", "intelligence"]
    return random.choice(words)

def get_available_letters(letters_guessed):
    return ''.join([ch for ch in string.ascii_lowercase if ch not in letters_guessed])

def get_guessed_word(secret_word, letters_guessed):
    return ''.join([ch if ch in letters_guessed else '_' for ch in secret_word])

def is_word_guessed(secret_word, letters_guessed):
    return all(ch in letters_guessed for ch in secret_word)

def hangman(secret_word):
    guesses_left = 8
    letters_guessed = []

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print("-------------")

    while guesses_left > 0:
        print(f"You have {guesses_left} guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        guess = input("Please guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
        elif guess in letters_guessed:
            print("Oops! You've already guessed that letter:", get_guessed_word(secret_word, letters_guessed))
        elif guess in secret_word:
            letters_guessed.append(guess)
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed.append(guess)
            guesses_left -= 1
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))

        print("-------------")

        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            break
    else:  # runs if while loop ends without break
        print(f"Sorry, you ran out of guesses. The word was '{secret_word}'.")

if __name__ == "__main__":
    word = choose_word()
    hangman(word)


program - 13  Remove stopwords using NLTK

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')  # ✅ important for newer NLTK
text = "This is a simple example to remove stop words using NLTK."
words = word_tokenize(text)
filtered = [w for w in words if w.lower() not in stopwords.words('english')]
print(filtered)

