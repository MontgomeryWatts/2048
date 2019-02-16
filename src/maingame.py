import pygame
import sys

from board import Board
from pygame.locals import *

pygame.init()

WINDOW_DIMENSION = 500
BOARD = Board(4)
BOARD_RATIO = 0.8  # How much of the window the board takes up
BOARD_OFFSET = WINDOW_DIMENSION * (1 - BOARD_RATIO) / 2
BOARD_DIMENSION = WINDOW_DIMENSION * BOARD_RATIO
BORDER_DIMENSION = BOARD_DIMENSION + 2
BORDER_OFFSET = BOARD_OFFSET - 1
DISPLAY_SURF = pygame.display.set_mode((WINDOW_DIMENSION, WINDOW_DIMENSION))
GRAY = (169,169,169)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TAN = (210, 180, 140)
BORDER_RECT = (BORDER_OFFSET, BORDER_OFFSET, BORDER_DIMENSION, BORDER_DIMENSION)
BOARD_RECT = (BOARD_OFFSET, BOARD_OFFSET, BOARD_DIMENSION, BOARD_DIMENSION)

FONT = pygame.font.SysFont("Arial", 12)

DISPLAY_SURF.fill(TAN)

pygame.display.set_caption('Hello World!')

pygame.draw.rect(DISPLAY_SURF, BLACK, BORDER_RECT)
pygame.draw.rect(DISPLAY_SURF, GRAY, BOARD_RECT)




def draw_board(board):
	cell_dimension = BOARD_DIMENSION / board.size
	for row in range(board.size):
		for col in range(board.size):
			cell_top_offset = BOARD_OFFSET + (row * cell_dimension)
			cell_left_offset = BOARD_OFFSET + (col * cell_dimension)
			cell_rect = (cell_left_offset,  cell_top_offset, cell_dimension * .9, cell_dimension * .9)

			cell = board.get_cell_at(row, col)
			if cell.value is 0:
				pygame.draw.rect(DISPLAY_SURF, GRAY, cell_rect)
			else:
				pygame.draw.rect(DISPLAY_SURF, WHITE, cell_rect)
				text = FONT.render(cell.__str__(), True, BLACK)
				DISPLAY_SURF.blit(text, cell_rect)


draw_board(BOARD)

while BOARD.game_not_over(): # main game loop

	for event in pygame.event.get():
		if event.type == KEYUP:
			if event.key == K_w or event.key == K_UP:
				if BOARD.move_up():
					draw_board(BOARD)
			if event.key == K_a or event.key == K_LEFT:
				if BOARD.move_left():
					draw_board(BOARD)
			if event.key == K_s or event.key == K_DOWN:
				if BOARD.move_down():
					draw_board(BOARD)
			if event.key == K_d or event.key == K_RIGHT:
				if BOARD.move_right():
					draw_board(BOARD)

		if event.type == QUIT:

			pygame.quit()

			sys.exit()

	pygame.display.update()