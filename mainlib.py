import pygame as game
import itertools

#array to hold current board state

board_state = [0 for x in range(9)]

class Game:
    def __init__(self):
        self.size = 480
        self.grid = 3
        self.box_size = self.size/self.grid
        self.border = 5
        self.surface = game.display.set_mode((self.size+15, self.size+15))
        self.box_width = self.box_size - (2 * self.border)
        self.box_height = self.box_size - (2 * self.border)
        self.box_coords = None
        for i in range(9):
            board_state[i] = 0

    def create_board(self):
        game.display.set_caption("TicTacToe Game")
        self.surface.fill((255,255,255))

    def display_msg(self,str):
        self.surface.fill((255,255,255))
        font = game.font.Font(None, int(self.size/10))
        text = font.render(str, 1, (10, 10, 10))
        textpos = text.get_rect(centerx=self.surface.get_width()/2)
        self.surface.blit(text, textpos)
        game.display.update()

    def draw_lines(self):
        for i in range(1,3):
            start_position = ((self.box_size * i) + (5 * (i - 1))) + self.border
            width = self.surface.get_width() - (2 * self.border)
            game.draw.rect(self.surface,((0,0,0)), (start_position, self.border,5, width))
            game.draw.rect(self.surface,((0,0,0)), (self.border, start_position, width, 5))

    def create_boxes(self):        
        top_left_numbers = []
        for i in range(0, 3):
            num = ((i * self.box_size) + self.border + (i * 5))
            top_left_numbers.append(num)
        
        self.box_coords = list(itertools.product(top_left_numbers, repeat=2))

    def box_index(self,x,y):
        for idx,(a,b) in enumerate(self.box_coords):
            tile = game.Rect(a,b,self.box_width,self.box_height)
            if tile.collidepoint((x,y)) == 1 and board_state[idx] == 0:
                return idx
        return -1  

    def mark_x(self,idx):
        (x,y) = self.box_coords[idx]
        game.draw.line(self.surface,(25,25,200),((x+5),(y+5)),((x+5+self.box_width),(y+5+self.box_height)),4)
        game.draw.line(self.surface,(25,25,200),((x+5),(y+5+self.box_height)),((x+5+self.box_width),(y+5)),4)
        board_state[idx] = 2

    def mark_o(self,idx):
        (x , y) = self.box_coords[idx]
        x_pos = int(x + self.box_width / 2)
        y_pos = int(y + self.box_height / 2)
        radius = int(self.box_width / 2 - self.box_width / 8)
        game.draw.circle(self.surface, (200, 25, 25), (x_pos, y_pos), radius, 4)
        board_state[idx] = 1

    def human_turn(self, x, y):
        idx = self.box_index(x , y)
        if idx == -1:
            return False
        self.mark_x(idx)
        return True

    def check_status(self):
        # any vertical combination
        for i in range(0,9,3):
            if board_state[i]!=0 and board_state[i] == board_state[i+1]==board_state[i+2]:
                return board_state[i]
        # any horizontal combination    
        for i in range(3):
            if board_state[i]!=0 and board_state[i] == board_state[i+3] == board_state[i+6]:
                return board_state[i]    
        #for diagonal combination
        if board_state[0] != 0 and board_state[0] == board_state[4] == board_state[8]:
            return board_state[0]
        if board_state[2] != 0 and board_state[2] == board_state[4] == board_state[6]:
            return board_state[2]

        #if more moves possible
        #check for empty spaces
        for i in range(0, 9):
            if board_state[i] == 0:
                return -1
        #if no winner---tie
        return 0

    def minimax(self,isMax, alpha, beta):
        status=self.check_status()
        if status == 1:
            return 10
        elif status == 2:
            return -10
        elif status == 0:
            return 0

        if isMax:
            best = -1000000
            for i in range(0, 9):
                if board_state[i] == 0:
                    board_state[i] = 1
                    val = self.minimax(not isMax, alpha,beta)
                    board_state[i] = 0
                    best = max(best, val)
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        return alpha
            return alpha

        else:
            best = 1000000
            for i in range(0, 9):
                if board_state[i] == 0:
                    board_state[i] = 2
                    val = self.minimax(not isMax,alpha,beta)
                    board_state[i] = 0
                    best = min(best,val)
                    beta = min(beta,best)

                    if beta <= alpha:
                        return beta
            return beta

    def alphabeta (self):
        bestval = -1000000
        move = -1
        for i in range(9):
            if board_state[i] == 0:
                board_state[i] = 1
                moveval = self.minimax(False, -1000000, 1000000)
                board_state[i] = 0
                if moveval > bestval:
                    bestval = moveval
                    move = i
        return move

    def AI_turn(self):
        idx = self.alphabeta()
        self.mark_o(idx)



    
   
        





