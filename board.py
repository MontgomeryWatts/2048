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
				string += "{:<5}".format(str(self.board[x][y])) + " "
			string += "\n"
		return string

	def in_bounds(self, value):
		return 0 <= value < self.size

	def board_has_changed(self):
		for row in range(self.size):
			for col in range(self.size):
				if self.board[row][col] != self.copy_board[row][col]:
					return True
		return False

	def can_move(self):
		for row in range(self.size):
			for col in range(self.size):
				movable_cells = self.check_neighbors(row, col)
				if movable_cells == 1:
					return True
		return False

	def check_neighbors(self, row, col):
		for x in range(-1, 2):
			for y in range(-1, 2):
				if row + x != 0 or col + y != 0:
					if self.in_bounds(row + x) and self.in_bounds(col + y):
						if self.board[row+x][col+y] == self.EMPTY or self.board[row+x][col+x] == self.board[row][col]:
							return 1
		return 0

	def copy_over(self, original_board, copied_board):
		for row in range(self.size):
			for col in range(self.size):
				copied_board[row][col] = original_board[row][col]

	def get_cell_at(self, row, col):
		if self.in_bounds(row) and self.in_bounds(col):
			return self.board[row][col]

	def has_free_space(self):
		for row in range(self.size):
			for col in range(self.size):
				if self.board[row][col] == self.EMPTY:
					return True
		return False

	def move_left(self):
		return self.move_horizontal(row_start=0, row_end=self.size, col_start=1, col_end=self.size, delta=1)

	def move_right(self):
		return self.move_horizontal(row_start=self.size-1, row_end=-1, col_start=self.size-2, col_end=-1, delta=-1)

	def move_horizontal(self, row_start, row_end, col_start, col_end, delta):
		if not self.can_move():
			return False

		self.copy_over(self.board, self.copy_board)

		for row in range(row_start, row_end, delta):
			for col in range(col_start, col_end, delta):
				next_col = col - delta
				finished = False
				while self.in_bounds(next_col) and not finished:
					if self.copy_board[row][next_col] == self.EMPTY:
						self.copy_board[row][next_col] = self.board[row][col]
						self.copy_board[row][next_col + delta] = self.EMPTY
					elif self.copy_board[row][next_col] == self.board[row][col]:
						self.copy_board[row][next_col] = self.board[row][col] * 2
						self.copy_board[row][next_col + delta] = self.EMPTY
						finished = True
					else:
						finished = True
					next_col -= delta

		if self.board_has_changed():
			self.copy_over(self.copy_board, self.board)
			return True
		return False

	def move_up(self):
		return self.move_vertical(row_start=1, row_end=self.size, col_start=0, col_end=self.size, delta=1)

	def move_down(self):
		return self.move_vertical(row_start=self.size-2, row_end=-1, col_start=self.size-1, col_end=-1, delta=-1)

	def move_vertical(self, row_start, row_end, col_start, col_end, delta):
		if not self.can_move():
			return False

		self.copy_over(self.board, self.copy_board)

		for row in range(row_start, row_end, delta):
			for col in range(col_start, col_end, delta):
				next_row = row - delta
				finished = False
				while self.in_bounds(next_row) and not finished:
					if self.copy_board[next_row][col] == self.EMPTY:
						self.copy_board[next_row][col] = self.board[row][col]
						self.copy_board[next_row + delta][col] = self.EMPTY
					elif self.copy_board[next_row][col] == self.board[row][col]:
						self.copy_board[next_row][col] = self.board[row][col] * 2
						self.copy_board[next_row + delta][col] = self.EMPTY
						finished = True
					else:
						finished = True
					next_row -= delta

		if self.board_has_changed():
			self.copy_over(self.copy_board, self.board)
			return True
		return False

	def place_cell(self, cell, x, y):
		"""Places a given cell at a given location on the board"""
		self.board[x][y] = cell

	def place_random_cell(self):
		"""	Attempts to place a cell with value 2 or 4
			into an empty spot. Currently does not check
			if the board is filled or not
		"""
		if not self.has_free_space():
			return

		# randint's bounds are inclusive
		num = random.randint(0, 1)
		if num is 0:
			cell = Cell(2)
		else:
			cell = Cell(4)

		successful = False
		while not successful:
			x = random.randint(0, self.size-1)
			y = random.randint(0, self.size-1)
			if self.board[x][y] == self.EMPTY:
				self.board[x][y] = cell
				successful = True
