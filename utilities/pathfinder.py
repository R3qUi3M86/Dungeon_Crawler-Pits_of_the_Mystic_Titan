from sys import path
import pygame
from settings import screen
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
from utilities import movement_manager
from utilities import entity_manager

class Pathfinder:
    def __init__(self, matrix, monster_tile_index):
        
        self.monster_tile_index = monster_tile_index
        self.matrix = matrix
        self.grid = Grid(matrix = self.matrix)
        self.finder = AStarFinder(diagonal_movement = DiagonalMovement.always)
        self.path = []
    
    def create_path(self):
        start_grid = self.grid.node(self.monster_tile_index[1], self.monster_tile_index[0])
        end_grid = self.grid.node(movement_manager.player_tile_index[1], movement_manager.player_tile_index[0])
        self.path, _ = self.finder.find_path(start_grid, end_grid, self.grid)
        self.grid.cleanup()

    def update(self, monster_tile_index = None, pathfinding = False):
        if pathfinding:
            self.monster_tile_index = monster_tile_index
        elif self.path:
            self.path.clear()

    def draw_path(self):
        if self.path:
            points = []

            for path_grid in self.path:
                for level_tile in entity_manager.level_sprite_groups:
                    if level_tile.sprite.tile_index == (path_grid[1], path_grid[0]):
                        points.append((level_tile.sprite.position[0],level_tile.sprite.position[1]))

            pygame.draw.lines(screen,'#aa0000',False,points,5)