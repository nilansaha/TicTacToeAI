import numpy as np
from copy import deepcopy

class TicTacToe():
    def __init__(self):
        self.state = [-1] * 9
        self.turn = 1
        self.done = False
        self.winner = None
        self.move_history = []
        self.state_history = [[-1] * 9]

    def reset(self):
        self.state = [-1] * 9
        self.done = False
        self.turn = 1
        self.move_history = []
        self.state_history = [[-1] * 9]
        
    def check_win(self):
        state = np.array(self.state).reshape(3,3)
        for i in range(3):
            if all([self.turn == i for i in state[i]]):
                return True
            if all([self.turn == i for i in state[:,i]]):
                return True
        if all([self.turn == i for i in [self.state[0], self.state[4], self.state[8]]]):
            return True
        if all([self.turn == i for i in [self.state[2], self.state[4], self.state[6]]]):
            return True
        return False
        
    def move(self, idx):
        self.turn = 0 if self.turn == 1 else 1
        if self.state[idx] == -1:
            self.move_history.append(idx)
            self.state[idx] = self.turn
            self.state_history.append(deepcopy(self.state))
            if self.check_win():
                self.done = True
                self.winner = self.turn
                return (self.done, self.winner)
            else:
                if len(self.available_moves()) > 0:
                  self.done = False
                  return (self.done, self.winner)
                else:
                  self.done = True
                  self.winner = -1
                  return (self.done, self.winner)

        else:
            self.done = True
            self.winner = 'Illegal'
            return (self.done, self.winner)
        
    def available_moves(self):
        if self.done == True:
          return []
        return [idx for idx, x in enumerate(self.state) if x == -1]
    
    def render(self):
        for i in range(0,7,3):
            print('{:3d}{:3d}{:3d}'.format(self.state[i], self.state[i+1], self.state[i+2]))
