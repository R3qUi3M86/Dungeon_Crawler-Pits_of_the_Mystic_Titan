import pygame
from settings import screen
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from utilities import entity_manager

class Pathfinder:
    def __init__(self, matrix, monster_tile_index):
        
        self.position = 0,0
        self.monster_tile_index = monster_tile_index
        self.matrix = matrix
        self.grid = Grid(matrix = self.matrix)
        self.finder = AStarFinder()
        self.path = []
        self.points = []
    
    def create_path(self):
        start_grid = self.grid.node(self.monster_tile_index[1], self.monster_tile_index[0])
        end_grid = self.grid.node(entity_manager.hero.tile_index[1], entity_manager.hero.tile_index[0])
        self.path, _ = self.finder.find_path(start_grid, end_grid, self.grid)
        self.grid.cleanup()