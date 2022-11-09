import numpy as np

start = np.array([672,  348])
goal = np.array([298 , 450])

grid = np.load('new_york.npy')

path = np.zeros([len(grid), len(grid[0])], dtype=float)
path -= 1000

heuristic=[0,0,0,0,0,0,0,0]

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
    # pos : current position
        u = np.array([-1, 0])
        d = np.array([1, 0])
        l = np.array([0, -1])
        r = np.array([0, 1])
        

        potential_moves = [pos + u, pos + d, pos + l, pos + r]

        # Diagonal moves
        potential_moves += [pos + u+r, pos + u+l, pos + d+r, pos + d+l]

        # print("Potential moves :",potential_moves)
        # print(potential_moves)
        
        return potential_moves
        
    
    def valid_moves(self,potential_moves):
                
        # Check if move is valid
        
        for move in potential_moves: 
            if move[0] < 0 or move[0] >= len(grid) or move[1] < 0 or move[1] >= len(grid[0]):
                potential_moves.remove(move)
            
            if self.grid[move[0],move[1],0] < 0.2:
                potential_moves.remove(move)
        valid_moves = potential_moves
        print("Valid moves :",potential_moves,"\n")
        # print(len(valid_moves))
        return valid_moves

    def next_move(self,valid_moves):
        
        # print(self.pos)
        for i,move in enumerate(valid_moves):
            
            heuristic[i]=(np.sqrt((move[0]-self.goal[0])**2 + (move[1]-self.goal[1])**2))
        
        minpos=heuristic.index(min(heuristic))
        self.explored_node.append(self.pos)
        self.pos=valid_moves[minpos]


obj= Astar(start,goal,grid,path)

while obj.pos[0]!=goal[0] or obj.pos[1]!=goal[1]:
    moves=obj.get_possible_moves(obj.pos)
    valid_moves=obj.valid_moves(moves)
    obj.next_move(valid_moves)
    
    

# obj.valid_moves(obj.get_possible_moves(start))
# obj.next_move(obj.valid_moves(obj.get_possible_moves(start)))
