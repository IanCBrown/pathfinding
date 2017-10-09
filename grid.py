import pygame
import numpy as np


class Grid:
    
    rect_width = 20
    rect_height = 20 
    rect_margin = 5 

    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
   
    
    def __init__(self, grid):
        Grid.width = len(grid) 
        Grid.height = len(grid) 

        Grid.startX = 0
        Grid.startY = 0
        Grid.endX = self.width - 1
        Grid.endY = self.height - 1
              
        Grid.grid = np.zeros(shape=(self.width,self.height))
        #Start postion 
        Grid.grid[0][0] = 1
        Grid.grid[self.width - 1][self.height - 1] = 19

class Position:
    

    def __init__(self, x, y):
        Position.x = x
        Position.y = y
        Position.visited = np.zeros(shape=(Grid.width,Grid.height), dtype=bool)
        #Position.Neighbors = [None,None,None,None]
    def get_neighbors(Position):
        neighbors = []
        if Position.x < Grid.width - 1:
            neighbors.append(Position.x + 1, Position.y)
        if Position.x > 0: 
            neighbors.append(Position.x - 1, Position.y)
        if Position.y < Grid.height -1:
            neighbors.append(Position.x, Position.y + 1)
        if Position.y > 0:
            neighbors.append(Position.x, Position.y - 1)
        return neighbors
    def is_visited(Position):
        if Position.visited[Position.x][Position.y] is True:
            return True
        return False 
    def visit(Position):
        Position.visited[Position.x][Position.y] = True 


#controls the size of the grid
input_grid = np.zeros(shape=(20,20))
def make_grid(input_grid):
    grid = Grid(input_grid)
    return grid 

make_grid(input_grid)