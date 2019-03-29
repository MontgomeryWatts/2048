import pygame
import sys

from board import Board
from pygame.locals import *

pygame.init()

# Control Variables: All other constants depend on these
BOARD_SIZE = 4  # How many cells are in the n x n board
WINDOW_DIMENSION = 500  # The square dimensions of the window
BOARD_RATIO = 0.8  # How much of the window the board takes up

BOARD = Board(BOARD_SIZE)
OFFSET_RATIO = ((1 - BOARD_RATIO) / 2)
BOARD_OFFSET = WINDOW_DIMENSION * OFFSET_RATIO
BOARD_DIMENSION = WINDOW_DIMENSION * BOARD_RATIO
BORDER_DIMENSION = BOARD_DIMENSION + 2  # 1 pixel border
BORDER_OFFSET = BOARD_OFFSET - 1
DISPLAY_SURF = pygame.display.set_mode((WINDOW_DIMENSION, WINDOW_DIMENSION))
BORDER_RECT = (BORDER_OFFSET, BORDER_OFFSET, BORDER_DIMENSION, BORDER_DIMENSION)
BOARD_RECT = (BOARD_OFFSET, BOARD_OFFSET, BOARD_DIMENSION, BOARD_DIMENSION)
CELL_DIMENSION = BOARD_DIMENSION / BOARD_SIZE
FONT = pygame.font.SysFont("Arial", int(CELL_DIMENSION * OFFSET_RATIO * 2))

LIGHT_GRAY = (225, 225, 225)
GRAY = (169,169,169)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TAN = (210, 180, 140)
PASTEL_RED = (255, 179, 186)
PASTEL_ORANGE = (255, 223, 186)
PASTEL_YELLOW = (255, 255, 186)
PASTEL_GREEN = (186, 255, 201)
PASTEL_BLUE = (186, 225, 255)
PASTEL_PURPLE = (149, 125, 173)
LIME = (153, 255, 153)
CYAN = (153, 204, 255)
PERIWINKLE = (204, 153, 255)

pygame.display.set_caption('2048')
DISPLAY_SURF.fill(WHITE)
pygame.draw.rect(DISPLAY_SURF, BLACK, BORDER_RECT)  # Draw game border and board
pygame.draw.rect(DISPLAY_SURF, GRAY, BOARD_RECT)


def get_color(cell_value):
	if cell_value == 2:
		return TAN
	elif cell_value == 4:
		return LIGHT_GRAY
	elif cell_value == 8:
		return PASTEL_RED
	elif cell_value == 16:
		return PASTEL_ORANGE
	elif cell_value == 32:
		return PASTEL_YELLOW
	elif cell_value == 64:
		return PASTEL_GREEN
	elif cell_value == 128:
		return PASTEL_BLUE
	elif cell_value == 256:
		return PASTEL_PURPLE
	elif cell_value == 512:
		return LIME
	elif cell_value == 1024:
		return CYAN
	elif cell_value == 2048:
		return PERIWINKLE
	else:  # Placeholder for now, granted I do not allow players to continue after reaching 2048
		return WHITE


def draw_board():
	for row in range(BOARD_SIZE):
		cell_top_offset = BOARD_OFFSET + ((row + OFFSET_RATIO) * CELL_DIMENSION)
		for col in range(BOARD_SIZE):
			cell_left_offset = BOARD_OFFSET + ((col + OFFSET_RATIO) * CELL_DIMENSION)
			cell_rect = (cell_left_offset,  cell_top_offset, CELL_DIMENSION * BOARD_RATIO, CELL_DIMENSION * BOARD_RATIO)

			cell = BOARD.get_cell_at(row, col)
			if cell.value is 0:
				pygame.draw.rect(DISPLAY_SURF, GRAY, cell_rect)
			else:
				color = get_color(cell.value)
				pygame.draw.rect(DISPLAY_SURF, color, cell_rect)
				text = FONT.render(cell.__str__(), True, BLACK)

				# Centers the text of the cell's value
				text_rect = text.get_rect(center=(cell_rect[0] + (cell_rect[2] / 2), cell_rect[1] + (cell_rect[2] / 2)))

				DISPLAY_SURF.blit(text, text_rect)


draw_board()

while BOARD.game_not_over():  # main game loop

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
