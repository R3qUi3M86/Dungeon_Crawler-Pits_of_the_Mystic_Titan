import pygame
from settings import screen
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
from utilities import entity_manager
from entities.characters import unique_player_object

class Pathfinder:
    def __init__(self, matrix, monster_tile_index):
        
        self.position = 0,0
        self.monster_tile_index = monster_tile_index
        self.matrix = matrix
        self.grid = Grid(matrix = self.matrix)
        self.finder = AStarFinder(diagonal_movement = DiagonalMovement.always)
        self.path = []
        self.points = []
        self.pathfinding_collision_rect = pygame.Rect((self.position[0] - 2, self.position[1] -2),(4,4))
    
    def create_path(self):
        start_grid = self.grid.node(self.monster_tile_index[1], self.monster_tile_index[0])
        end_grid = self.grid.node(unique_player_object.HERO.tile_index[1], unique_player_object.HERO.tile_index[0])
        self.path, _ = self.finder.find_path(start_grid, end_grid, self.grid)
        self.grid.cleanup()

    def update(self, monster_tile_index = None, pathfinding = False):
        self.generate_points_path(self.path)
        if pathfinding:
            self.monster_tile_index = monster_tile_index
        elif self.path:
            self.path.clear()
            self.points.clear()

    def generate_points_path(self,path):
        self.points = []

        for path_grid in path:
            for level_tile in entity_manager.level_sprite_groups:
                if level_tile.sprite.tile_index == (path_grid[1], path_grid[0]):
                    self.points.append((level_tile.sprite.position[0],level_tile.sprite.position[1]))

    def draw_path(self):
        if self.points:
            pygame.draw.lines(screen,'#aa0000',False,self.points,5)

    def update_collision_rect_pos(self,position):
        self.pathfinding_collision_rect = pygame.Rect((self.position[0] - 2, self.position[1] -2),(4,4))