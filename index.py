Program 1 - Breadth first search 

def bfs(graph,start):
    visited = []
    queue=[start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node)
            visited.append(node)
            queue.extend(graph[node])
graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
print("Bfs traversal")
bfs(graph,'A')

Program 2 - Depth first search 

def dfs(graph,node,visited=None):
    if visited is None:
        visited=[]
    if node not in visited:
        print(node)
        visited.append(node)
        for neighbour in graph[node]:
            dfs(graph,neighbour,visited)

graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
print("Dfs traversal")
dfs(graph,'A')

program - 3 Tic tac toe game

board  = ['1','2','3','4','5','6','7','8','9']
player = 'X'
for turn in range(9):
    print(board[0],"|",board[1],"|",board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])

    choice  = int(input("Player "+player+" enter 1-9: "))
    board[choice-1] = player
    if board[0]==board[1]==board[2]:
        print("Player ",player,"wins")
        break
    if board[3] == board[4] == board[5]:
        print("Player ", player, "wins")
        break
    if board[6] == board[7] == board[8]:
        print("Player ", player, "wins")
        break
    if board[0] == board[3] == board[6]:
        print("Player ", player, "wins")
        break
    if board[1] == board[4] == board[7]:
        print("Player ", player, "wins")
        break
    if board[2] == board[5] == board[8]:
        print("Player ", player, "wins")
        break
    if board[0] == board[4] == board[8]:
        print("Player ", player, "wins")
        break
    if board[2] == board[4] == board[6]:
        print("Player ", player, "wins")
        break
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
else:
    print("Its a tie")

Program - 4 8 puzzle problem

from collections import deque
def solve(b):
    s = sum(b, [])
    if s == list(range(9)): return 0
    m = [[1, 3], [0, 2, 4], [1, 5], [0, 4, 6], [1, 3, 5, 7], [2, 4, 8], [3, 7],
         [4, 6, 8], [5, 7]]
    q = deque([(s, 0)])
    v = set()
    while q:
        t, c = q.popleft()
        if str(t) in v: continue
        v.add(str(t))
        z = t.index(0)

        for i in m[z]:
            n = t[:]
            n[z], n[i] = n[i], n[z]
            if n == list(range(9)): return c + 1
            q.append((n, c + 1))
    return -1
print(solve([[3, 1, 2], [4, 7, 5], [6, 8, 0]])) 

program - 5  Water Jug 

print("Water Jug problem") 
x = int(input("Enter X:")) 
y = int(input("Enter Y:")) 
 
while True: 
    rno = int(input("Enter the rule no:")) 
     
    if rno == 1: 
        if x < 4: 
            x = 4 
 
    if rno == 2: 
        if y < 3: 
            y = 3 
 
    if rno == 5: 
        if x > 0: 
            x = 0 
 
    if rno == 6: 
        if y > 0: 
            y = 0 
 
    if rno == 7: 
        if x + y >= 4 and y > 0: 
            x, y = 4, y - (4 - x) 
 
    if rno == 8: 
        if x + y >= 3 and x > 0: 
            x, y = x - (3 - y), 3 
 
    if rno == 9: 
        if x + y <= 4 and y > 0: 
            x, y = x + y, 0 
 
    if rno == 10: 
        if x + y <= 3 and x > 0: 
            x, y = 0, x + y 
 
    print("x =", x) 
    print("y =", y) 
 
    if x == 2: 
        print("The result is a goal state") 
        break 

Program 6 Salesman

from itertools import permutations
d = [[0,10,15,20], [10,0,35,25], [15,35,0,30], [20,25,30,0]]
best = 999
path = []
for trip in permutations([1,2,3]):
    a, b, c = trip
    cost = d[0][a] + d[a][b] + d[b][c] + d[c][0]
    if cost < best:
        best = cost
        path = trip
        print("Cost:", best, "Path:", path)

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


