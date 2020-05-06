import kivy
from random import random
from random import choice
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.factory import Factory
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from math import inf as infinity
import time

SIZE = 3
HUMAN = -1
COMP = +1
board = [[0 for i in range(SIZE)] for j in range(SIZE)]


def evaluate(state):
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score

def wins(state, player):
    
    win_state = []

    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    
    if [player for i in range(SIZE)] in win_state:
        return True
    else:
        return False


def game_over(state):
    return wins(state, HUMAN) or wins(state, COMP)

def empty_cells(state):
    
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def valid_move(x, y):
    if [x, y] in empty_cells(board):
        return True
    else:
        return False
    

def set_move(x, y, player):
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False
    

def minimax(state, depth, player):

    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score 
        else:
            if score[2] < best[2]:
                best = score  

    return best

def ai_turn():

    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return
    

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
        
    else:
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]
    
    
    set_move(x, y, COMP)
    a = [[1,2,3], [4,5,6], [7,8,9]]
    return a[x][y]
    

def human_turn(move):

    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    moves = {}
    x = 1
    for i in range(SIZE):
        for j in range(SIZE):
            moves[x] = [i,j]
            x += 1
        
    coord = moves[move]
    can_move = set_move(coord[0], coord[1], HUMAN)
    
    return move


h_choice = ''  # X or O
c_choice = ''
first = '.'

def update(self,n):
    if(n == 1):
        self.b1 = c_choice
        self.clr1 = (1.0, 0.0, 0.0, 1.0)
    
    elif(n == 2):
        self.b2 = c_choice
        self.clr2 = (1.0, 0.0, 0.0, 1.0)
        
    elif(n == 3):
        self.b3 = c_choice
        self.clr3 = (1.0, 0.0, 0.0, 1.0)
        
    elif(n == 4):
        self.b4 = c_choice
        self.clr4 = (1.0, 0.0, 0.0, 1.0)
        
    elif(n == 5):
        self.b5 = c_choice
        self.clr5 = (1.0, 0.0, 0.0, 1.0)
        
    elif(n == 6):
        self.b6 = c_choice
        self.clr6 = (1.0, 0.0, 0.0, 1.0)
        
    elif(n == 7):
        self.b7 = c_choice
        self.clr7 = (1.0, 0.0, 0.0, 1.0)
        
    elif(n == 8):
        self.b8 = c_choice
        self.clr8 = (1.0, 0.0, 0.0, 1.0)
        
    elif(n == 9):
        self.b9 = c_choice
        self.clr9 = (1.0, 0.0, 0.0, 1.0)
    
    time.sleep(0.5)
    
class FirstWindow(Screen):
    btn1 = ObjectProperty(None)
    btn2 = ObjectProperty(None)
    
    def variableInitialize(self):
        global SIZE, HUMAN, COMP, board, h_choice, c_choice, first
        SIZE = 3
        HUMAN = -1
        COMP = +1
        board = [[0 for i in range(SIZE)] for j in range(SIZE)]
        h_choice = ''  
        c_choice = ''
        first = '.'
        
    
    def symbol1(self):
        global h_choice,c_choice
        h_choice = 'X'
        c_choice = 'O'
    
    def symbol2(self):
        global h_choice,c_choice
        c_choice = 'X'
        h_choice = 'O'

class SecondWindow(Screen):
    btn1 = ObjectProperty(None)
    btn2 = ObjectProperty(None)
    def firstMove1(self):
        global first
        first = 'Y'
        
    def firstMove2(self):    
        global first
        first = 'N'
        
class FourthWindow(Screen):
    def StartLabel(self):
        if(first != 'N'):
            self.start_label.text = "You will take the first move !!!"
        else:
            self.start_label.text = "Computer will take the first move !!!"
        
        self.start_label.color = [1,0.0,0.0,1]
    

class ThirdWindow(Screen,App):
    b1 = StringProperty("-")    
    b2 = StringProperty("-")
    b3 = StringProperty("-")
    b4 = StringProperty("-")
    b5 = StringProperty("-")
    b6 = StringProperty("-")
    b7 = StringProperty("-")
    b8 = StringProperty("-")
    b9 = StringProperty("-")
    
    clr1 = ListProperty((1.0, 1.0, 1.0, 1.0))
    clr2 = ListProperty((1.0, 1.0, 1.0, 1.0))
    clr3 = ListProperty((1.0, 1.0, 1.0, 1.0))
    clr4 = ListProperty((1.0, 1.0, 1.0, 1.0))
    clr5 = ListProperty((1.0, 1.0, 1.0, 1.0))
    clr6 = ListProperty((1.0, 1.0, 1.0, 1.0))
    clr7 = ListProperty((1.0, 1.0, 1.0, 1.0))
    clr8 = ListProperty((1.0, 1.0, 1.0, 1.0))
    clr9 = ListProperty((1.0, 1.0, 1.0, 1.0))

    def on_start(self):
        
        
        if first  == 'N':
            self.chglabel.text = "Valid move"
            self.chglabel.color = [0.0,0.5,0.5,1]
            update(self,ai_turn())
        else:
            self.chglabel.text = "Take your move"
            self.chglabel.color = [0.9,0,0.4,1]
        
    def label_change1(self,event):
        if(self.b1 == "-" and len(empty_cells(board)) > 0 and not game_over(board)):
            self.b1 = str(h_choice)
            self.clr1 = (0, 1, 0, 1)
            self.chglabel.text = "Valid move"
            self.chglabel.color = [0.0,0.0,0.5,1]
            human_turn(1)
            update(self,ai_turn())
            result(self)
        else:
            self.chglabel.color = [1,0.0,0.0,1]
            self.chglabel.text = "Invalid Move"        
        
        
    def label_change2(self,event):
        if(self.b2 == "-" and len(empty_cells(board)) > 0 and not game_over(board)):
            self.b2 = str(h_choice)
            self.clr2 = (0, 1, 0, 1)
            self.chglabel.color = [0.0,0.0,0.5,1]
            self.chglabel.text = "Valid move"
            human_turn(2)
            update(self,ai_turn())
            result(self)
        else:
            self.chglabel.color = [1.0,0.0,0.0,1]
            self.chglabel.text = "Invalid Move"
    
    def label_change3(self,event):
        if(self.b3 == "-" and len(empty_cells(board)) > 0 and not game_over(board)):
            self.b3 = str(h_choice)
            self.clr3 = (0, 1, 0, 1)
            self.chglabel.color = [0.0,0.0,0.5,1]
            self.chglabel.text = "Valid move"
            human_turn(3)
            update(self,ai_turn())
            result(self)
        else:
            self.chglabel.color = [1,0,0.0,1]
            self.chglabel.text = "Invalid Move"
            
        
    def label_change4(self,event):
        if(self.b4 == "-" and len(empty_cells(board)) > 0 and not game_over(board)):
            self.b4 = str(h_choice)
            self.clr4 = (0, 1, 0, 1)
            self.chglabel.color = [0.0,0.0,0.5,1]
            self.chglabel.text = "Valid move"
            human_turn(4)
            update(self,ai_turn())
            result(self)
        else:
            self.chglabel.color = [1,0,0.0,1]
            self.chglabel.text = "Invalid Move"
            
        
    def label_change5(self,event):
        if(self.b5 == "-" and len(empty_cells(board)) > 0 and not game_over(board)):
            self.b5 = str(h_choice)
            self.clr5 = (0, 1, 0, 1)
            self.chglabel.color = [0.0,0.0,0.5,1]
            self.chglabel.text = "Valid move"
            human_turn(5)
            update(self,ai_turn())
            result(self)
        else:
            self.chglabel.color = [1,0,0.0,1]
            self.chglabel.text = "Invalid Move"
    
    def label_change6(self,event):
        if(self.b6 == "-" and len(empty_cells(board)) > 0 and not game_over(board)):
            self.b6 = str(h_choice)
            self.clr6 = (0, 1, 0, 1)
            self.chglabel.color = [0.0,0.0,0.5,1]
            self.chglabel.text = "Valid move"
            human_turn(6)
            update(self,ai_turn())
            result(self)
        else:
            self.chglabel.color = [1,0,0.0,1]
            self.chglabel.text = "Invalid Move"
            
            
            
        
    def label_change7(self,event):
        if(self.b7 == "-" and len(empty_cells(board)) > 0 and not game_over(board)):
            self.b7 = str(h_choice)
            self.clr7 = (0, 1, 0, 1)
            self.chglabel.color = [0.0,0.0,0.5,1]
            self.chglabel.text = "Valid move"
            human_turn(7)
            update(self,ai_turn())
            result(self)
        else:
            self.chglabel.color = [1.0,0.0,0.0,1]
            self.chglabel.text = "Invalid Move"
            
        
    def label_change8(self,event):
        if(self.b8 == "-"and len(empty_cells(board)) > 0 and not game_over(board)):
            self.b8 = str(h_choice)
            self.clr8 = (0, 1, 0, 1)
            self.chglabel.color = [0.0,0.0,0.5,1]
            self.chglabel.text = "Valid move"
            human_turn(8)
            update(self,ai_turn())
            result(self)
            
        else:
            self.chglabel.color = [1.0,0.0,0.0,1]
            self.chglabel.text = "Invalid Move"
           
        
    def label_change9(self,event):
        if(self.b9 == "-" and len(empty_cells(board)) > 0 and not game_over(board)):
            self.b9 = str(h_choice)
            self.clr9 = (0, 1, 0, 1)
            self.chglabel.color = [0.0,0.0,0.5,1]
            self.chglabel.text = "Valid move"
            human_turn(9)
            update(self,ai_turn())
            result(self)
        else:
            self.chglabel.color = [1.0,0.0,0.0,1]
            self.chglabel.text = "Invalid Move"
            
    def clear(self):
        self.b1 = "-"
        self.b2= "-"
        self.b3 = "-"
        self.b4 = "-"
        self.b5 = "-"
        self.b6 = "-"
        self.b7 = "-"
        self.b8 = "-"
        self.b9 = "-"
        
        self.clr1 = (1.0, 1.0, 1.0, 1.0)
        self.clr2 = (1.0, 1.0, 1.0, 1.0)
        self.clr3 = (1.0, 1.0, 1.0, 1.0)
        self.clr4 = (1.0, 1.0, 1.0, 1.0)
        self.clr5 = (1.0, 1.0, 1.0, 1.0)
        self.clr6 = (1.0, 1.0, 1.0, 1.0)
        self.clr7 = (1.0, 1.0, 1.0, 1.0)
        self.clr8 = (1.0, 1.0, 1.0, 1.0)
        self.clr9 = (1.0, 1.0, 1.0, 1.0)
        
        self.chglabel.text = ""
            

def result(self):
    if len(empty_cells(board)) == 0 or game_over(board):
        if wins(board, HUMAN):
            self.chglabel.text = "YOU WON"
        elif wins(board, COMP):
            self.chglabel.color = [1.0,0.0,1.0,1]
            self.chglabel.text = "Ooops YOU LOST !!!"
            
        else:
            self.chglabel.color = [0.0,0.0,1.0,1]
            self.chglabel.text = "Ohhh MATCH DRAW !!"
    

class WindowManager(ScreenManager):
    pass


class MyMainApp(App):
    def build(self):
        return kv    


kv = Builder.load_file("kivyeg.kv")

if __name__ == "__main__":
    MyMainApp().run()

