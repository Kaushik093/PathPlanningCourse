from turtle import distance
from matplotlib.pyplot import grid
import numpy as np

grid = [[1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

start = np.array([0, 0])
goal = np.array([7, 9])

path = np.zeros([len(grid), len(grid)], dtype=int)

# heuristic : Euclidean distance


class Astar:
    def __init__(self,start,goal,grid,path):
        self.start= start
        self.pos = start
        self.goal=goal
        self.explored_node = [[0,0]]
        self.next_node = []
        self.path = path
        self.grid = grid

    def get_possible_moves(self,pos):

    # Get all moves possible 

        u = np.array([-1, 0])
        d = np.array([1, 0])
        l = np.array([0, -1])
        r = np.array([0, 1])
        diag_r_lower = np.array([1,1])
        diag_l_lower=np.array([1,-1])
        diag_r_upper=np.array([-1,1])
        diag_l_upper=np.array([-1,-1])


        potential_moves = [pos + u, pos + d, pos + l, pos + r, pos+diag_l_lower, pos+diag_l_upper, pos+diag_r_lower, pos+diag_r_upper]

        # print(potential_moves)
        return potential_moves
    
    def valid_moves(self,potential_moves):
                
        # Check if move is valid
        for move in potential_moves: 
            if move[0] < 0 or move[0] >= len(self.grid) or move[1] < 0 or move[1] >= len(self.grid):
                print("out of bounds")
                potential_moves.remove(move)
                    
                                    
        # print(potential_moves)

                            

    # def next_move(self):
    #     potential_moves=self.get_possible_moves(self.pos)

    #     for move in potential_moves:
    #         if move not in self.valid_moves(move):
    #             potential_moves.remove(move)
    #     print(potential_moves)

astar = Astar(start,goal,grid,path)

astar.get_possible_moves(start)
astar.valid_moves(astar.get_possible_moves(start))
            
            
        










        























 