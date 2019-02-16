import pygame
import sys

from board import Board
from pygame.locals import *

pygame.init()

BOARD_SIZE = 4
WINDOW_DIMENSION = 500
BOARD = Board(BOARD_SIZE)
BOARD_RATIO = 0.8  # How much of the window the board takes up
BOARD_OFFSET = WINDOW_DIMENSION * (1 - BOARD_RATIO) / 2
BOARD_DIMENSION = WINDOW_DIMENSION * BOARD_RATIO
BORDER_DIMENSION = BOARD_DIMENSION + 2
BORDER_OFFSET = BOARD_OFFSET - 1
DISPLAY_SURF = pygame.display.set_mode((WINDOW_DIMENSION, WINDOW_DIMENSION))
LIGHT_GRAY = (225, 225, 225)
GRAY = (169,169,169)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TAN = (210, 180, 140)
ORANGE = (255, 178, 102)
DARK_ORANGE = (238, 99, 29)
PINK = (255, 102, 102)
RED = (204, 0, 0)
YELLOW = (255, 255, 51)
MUSTARD = (225, 225, 20)
LIME = (153, 255, 153)
CYAN = (153, 204, 255)
PERIWINKLE = (204, 153, 255)


BORDER_RECT = (BORDER_OFFSET, BORDER_OFFSET, BORDER_DIMENSION, BORDER_DIMENSION)
BOARD_RECT = (BOARD_OFFSET, BOARD_OFFSET, BOARD_DIMENSION, BOARD_DIMENSION)


FONT = pygame.font.SysFont("Arial", 12)

DISPLAY_SURF.fill(WHITE)

pygame.display.set_caption('2048')

pygame.draw.rect(DISPLAY_SURF, BLACK, BORDER_RECT)
pygame.draw.rect(DISPLAY_SURF, GRAY, BOARD_RECT)


def get_color(cell_value):
	if cell_value == 2:
		return TAN
	elif cell_value == 4:
		return LIGHT_GRAY
	elif cell_value == 8:
		return ORANGE
	elif cell_value == 16:
		return DARK_ORANGE
	elif cell_value == 32:
		return PINK
	elif cell_value == 64:
		return RED
	elif cell_value == 128:
		return YELLOW
	elif cell_value == 256:
		return MUSTARD
	elif cell_value == 512:
		return LIME
	elif cell_value == 1024:
		return CYAN
	elif cell_value == 2048:
		return PERIWINKLE
	else:
		return WHITE

def draw_board():
	cell_dimension = BOARD_DIMENSION / BOARD_SIZE

	for row in range(BOARD_SIZE):
		cell_top_offset = BOARD_OFFSET + ((row + 0.1) * cell_dimension)
		for col in range(BOARD_SIZE):
			cell_left_offset = BOARD_OFFSET + ((col + 0.1) * cell_dimension)
			cell_rect = (cell_left_offset,  cell_top_offset, cell_dimension * .8, cell_dimension * .8)

			cell = BOARD.get_cell_at(row, col)
			if cell.value is 0:
				pygame.draw.rect(DISPLAY_SURF, GRAY, cell_rect)
			else:
				color = get_color(cell.value)
				pygame.draw.rect(DISPLAY_SURF, color, cell_rect)
				text = FONT.render(cell.__str__(), True, BLACK)
				DISPLAY_SURF.blit(text, (cell_rect[0] + (cell_rect[2] / 2), cell_rect[1] + (cell_rect[2] / 2)))


draw_board()

while BOARD.game_not_over(): # main game loop

	for event in pygame.event.get():
		if event.type == KEYUP:
			if event.key == K_w or event.key == K_UP:
				if BOARD.move_up():
					draw_board()
			if event.key == K_a or event.key == K_LEFT:
				if BOARD.move_left():
					draw_board()
			if event.key == K_s or event.key == K_DOWN:
				if BOARD.move_down():
					draw_board()
			if event.key == K_d or event.key == K_RIGHT:
				if BOARD.move_right():
					draw_board()
			if event.key == K_r:
					BOARD.reset_game()
					draw_board()

		if event.type == QUIT:

			pygame.quit()

			sys.exit()

	pygame.display.update()