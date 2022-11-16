import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
start = np.array([672,  348])
goal = np.array([600, 417])
grid = np.load('new_york.npy')

path = np.zeros([len(grid), len(grid[0])], dtype=float)

print("VAL :",grid[600,417,0])

node_count = 0
step_count = 0


class Astar:
    def __init__(self, start, goal, grid, path):
        self.start = start
        self.pos = start
        self.goal = goal
        self.explored_node = [[0, 0]]
        self.path = path
        self.grid = grid

    def get_possible_moves(self, pos):

        # print("Get possible moves")
        # Get all moves possible
        # pos : current position
        u = np.array([-1, 0])
        d = np.array([1, 0])
        l = np.array([0, -1])
        r = np.array([0, 1])

        potential_moves = [pos + u, pos + d, pos + l, pos + r]

        # Diagonal moves
        potential_moves += [pos + u+r, pos + u+l, pos + d+r, pos + d+l]
        # print("Potential moves: ", potential_moves)

        return potential_moves

    def valid_moves(self, potential_moves):

        # print("Potential moves: ", potential_moves)

        # print("Valid moves check")
        # Check if move is within grid
        valid_moves = []
        for move in potential_moves:
            if move[0] >= 0 and move[0] < len(self.grid) and move[1] >= 0 and move[1] < len(self.grid[0]) and self.grid[move[0], move[1], 0] >= 0.1 :
                valid_moves.append(move)

        
    
    # and self.grid[move[0], move[1], 0] >= 0.2
              
        return valid_moves

    def next_move(self, valid_moves):

        # print("Valid moves: ", valid_moves)

        heuristic=[]

        # print("Current position: ", self.pos)

        for move in valid_moves:

            heuristic.append(np.sqrt((move[0]-self.goal[0]) **
                        2 + (move[1]-self.goal[1])**2))
    

        # print("Heuristic :", heuristic)
        # print("Lowest heuristic :", min(heuristic))
        
        minpos = heuristic.index(min(heuristic))
        print("Next move: ", valid_moves[minpos])
        self.pos = valid_moves[minpos]

obj = Astar(start, goal, grid, path)

while True :

    if obj.pos[0] == obj.goal[0] and obj.pos[1] == obj.goal[1]:
        for i in range(len(obj.explored_node)):
            # print(obj.explored_node[i], "\n")
            print("Goal Reached")
            print("Total nodes explored :", node_count)
        break
    else:
        obj.next_move(obj.valid_moves(obj.get_possible_moves(obj.pos)))
        # print(obj.explored_node)
        # print(node_count)
        node_count += 1

        obj.path[obj.pos[0], obj.pos[1]] = 1

plt.imshow(obj.path,cmap='jet',alpha=0.75)
plt.tight_layout()
plt.show()

