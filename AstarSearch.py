from turtle import distance
from matplotlib.pyplot import grid
import numpy as np

grid = [[1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
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
        self.goal=goal
        self.explored_node = [[0,0]]
        self.next_node = []
        self.path = path
        self.grid = grid

        # def get_possible_moves():
        # Get all moves possible and check heuristic and add shortest path onto list

        























 