from board import Board


def main():

	board = Board(4)
	print(board)

	client_input = "s"

	while client_input is not "q" and board.game_not_over():
		client_input = input()
		if client_input is "u":
			board.move_up()
		elif client_input is "d":
			board.move_down()
		elif client_input is "l":
			board.move_left()
		elif client_input is "r":
			board.move_right()
		print(board)

	if board.has_2048():
		print("You win!")
	else:
		print("Game over!")


if __name__ == "__main__":
	main()
