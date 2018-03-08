import random
from cell import Cell

class Board:
	EMPTY = Cell(0)

	def __init__(self, size):
		self.size = size
		self.board = [[self.EMPTY for col in range(size)] for row in range(size)]
		self.copy_board = [[self.EMPTY for col in range(size)] for row in range(size)]

	def __str__(self):
		string = ""
		for x in range(self.size):
			for y in range(self.size):
				string += str(self.board[x][y]) + " "
			string += "\n"
		return string

	def in_bounds(self, value):
		return 0 <= value < self.size

	def copy_over(self, original_board, copied_board):
		for row in range(self.size):
			for col in range(self.size):
				copied_board[row][col] = original_board[row][col]

	def move_left(self):
		self.copy_over(self.board, self.copy_board)

		for row in range(self.size):
			for col in range(1, self.size):
				left_col = col - 1
				finished = False
				while self.in_bounds(left_col) and not finished:
					if self.copy_board[row][left_col] == self.EMPTY:
						self.copy_board[row][left_col] = self.board[row][col]
						self.copy_board[row][left_col+1] = self.EMPTY
					elif self.copy_board[row][left_col] == self.board[row][col]:
						self.copy_board[row][left_col] = self.board[row][col] * 2
						self.copy_board[row][left_col+1] = self.EMPTY
						finished = True
					else:
						finished = True
					left_col -= 1

		self.copy_over(self.copy_board, self.board)

	def move_right(self):
		self.copy_over(self.board, self.copy_board)

		for row in range(self.size-1, -1, -1):
			for col in range(self.size-2, -1, -1):
				right_col = col + 1
				finished = False
				while self.in_bounds(right_col) and not finished:
					if self.copy_board[row][right_col] == self.EMPTY:
						self.copy_board[row][right_col] = self.board[row][col]
						self.copy_board[row][right_col-1] = self.EMPTY
					elif self.copy_board[row][right_col] == self.board[row][col]:
						self.copy_board[row][right_col] = self.board[row][col] * 2
						self.copy_board[row][right_col-1] = self.EMPTY
						finished = True
					else:
						finished = True
					right_col += 1

		self.copy_over(self.copy_board, self.board)

	def place_cell(self, cell, x, y):
		"""Places a given cell at a given location on the board"""
		self.board[x][y] = cell

	def place_random_cell(self):
		"""	Attempts to place a cell with value 2 or 4
			into an empty spot. Currently does not check
			if the board is filled or not
		"""

		# randint's bounds are inclusive
		num = random.randint(0, 1)
		if num is 0:
			cell = Cell(2)
		else:
			cell = Cell(4)

		placeSuccess = False
		while not placeSuccess:
			x = random.randint(0, self.size-1)
			y = random.randint(0, self.size-1)
			if self.board[x][y] == self.EMPTY:
				self.board[x][y] = cell
				placeSuccess = True

