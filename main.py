from board import Board
from cell import Cell


def main():
	board = Board(4)
	cell = Cell(2)
	cella = Cell(4)
	cellb = Cell(8)
	board.place_cell(cell, 0, 1)
	board.place_cell(cell, 0, 2)
	board.place_cell(cella, 1, 0)
	board.place_cell(cellb, 1,1)
	board.place_cell(cella, 1, 3)
	board.place_cell(cellb, 3, 0)
	board.place_cell(cellb, 3, 3)
	print(board)
	board.move_left()
	print(board)
	board.move_right()
	print(board)


if __name__ == "__main__":
	main()
