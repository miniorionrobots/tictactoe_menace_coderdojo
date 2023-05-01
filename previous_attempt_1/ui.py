"""Pygame UI for the game."""
from typing import Tuple

import pygame
import board
import menace

TILE_WIDTH = 100
TILE_HEIGHT = 100
TILE_PADDING = 5
LINE_WIDTH = 2
NOUGHT_COLOR = (255, 0, 0)
CROSS_COLOR = (0, 0, 255)
BOARD_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)

class Nought(pygame.sprite.Sprite):
    def __init__(self, *groups: pygame.sprite.AbstractGroup) -> None:
        super().__init__(*groups)
        # draw the nought onto a buffer, make this the image
        # and then blit the buffer onto the screen
        self.image = pygame.Surface((TILE_WIDTH, TILE_HEIGHT))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (TILE_WIDTH, TILE_HEIGHT)
        pygame.draw.circle(self.image, NOUGHT_COLOR, (TILE_WIDTH/2, TILE_HEIGHT/2), TILE_WIDTH/2 - TILE_PADDING, LINE_WIDTH)


class Cross(pygame.sprite.Sprite):
    def __init__(self, *groups: pygame.sprite.AbstractGroup) -> None:
        super().__init__(*groups)
        # draw the cross onto a buffer, make this the image
        # and then blit the buffer onto the screen
        self.image = pygame.Surface((TILE_WIDTH, TILE_HEIGHT))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (TILE_WIDTH, TILE_HEIGHT)
        pygame.draw.line(self.image, CROSS_COLOR, (TILE_PADDING, TILE_PADDING), (100 - TILE_PADDING, 100 - TILE_PADDING), LINE_WIDTH)
        pygame.draw.line(self.image, CROSS_COLOR, (100 - TILE_PADDING, TILE_PADDING), (TILE_PADDING, 100 - TILE_PADDING), LINE_WIDTH)


class BoardUI:
    def __init__(self, board: board.Board) -> None:
        self.board = board
        self.noughts = pygame.sprite.Group()
        self.crosses = pygame.sprite.Group()
        self.rect = pygame.Rect(0, 0, TILE_WIDTH * self.board.width, TILE_HEIGHT * self.board.height)        
    
    def update_board(self) -> None:
        self.noughts.empty()
        self.crosses.empty()
        for row in range(self.board.height):
            for column in range(self.board.width):
                if self.board.board[row][column] == board.Board.NOUGHT:
                    Nought(self.noughts).rect.center = (TILE_WIDTH * column + TILE_WIDTH/2, TILE_HEIGHT * row + TILE_HEIGHT/2)
                elif self.board.board[row][column] == board.Board.CROSS:
                    Cross(self.crosses).rect.center = (TILE_WIDTH * column + TILE_WIDTH/2, TILE_HEIGHT * row + TILE_HEIGHT/2)

    def draw(self, surface: pygame.Surface) -> None:
        # draw lines
        for row in range(self.board.height):
            pygame.draw.line(surface, BOARD_COLOR, (0, TILE_HEIGHT * row), (TILE_WIDTH * self.board.width, TILE_HEIGHT * row), LINE_WIDTH)

        for column in range(self.board.width):
            pygame.draw.line(surface, BOARD_COLOR, (TILE_WIDTH * column, 0), (TILE_WIDTH * column, TILE_HEIGHT * self.board.height), LINE_WIDTH)

        self.noughts.draw(surface)
        self.crosses.draw(surface)

    def get_position(self, x: int, y: int) -> Tuple[int, int]:
        return (x // TILE_WIDTH, y // TILE_HEIGHT)


class Game:
    def __init__(self) -> None:
        self.game_board = board.Board()
        self.board_ui = BoardUI(self.game_board)
        # self.menace = menace.Menace(self.game_board)
    
    def run(self) -> None:
        screen = pygame.display.set_mode((self.board_ui.rect.width, self.board_ui.rect.height))

        while True:
            screen.fill(BACKGROUND_COLOR)
            self.board_ui.update_board()
            self.board_ui.draw(screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        position = self.board_ui.get_position(*event.pos)
                        if self.game_board.board[position[1]][position[0]] == board.Board.EMPTY:
                            self.game_board.make_move(*position, self.game_board.turn)
                            self.game_board.next_turn()

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()
