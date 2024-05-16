import random

from utils.Constants import SIZE_OF_BOARD

from model.UltimateTicTacToe import UltimateTicTacToe


def get_free_positions(board):
    # TODO: algo recursivo daria para fazer não?
    free_positions = []
    for u_line in range(SIZE_OF_BOARD):
        for u_column in range(SIZE_OF_BOARD):
            if not board.get_childs()[u_line][u_column].get_value():
                for ttt_line in range(SIZE_OF_BOARD):
                    for ttt_column in range(SIZE_OF_BOARD):
                        if not board.get_childs()[u_line][u_column].get_childs()[ttt_line][ttt_column].get_value():
                            free_positions.append(((u_column, u_line), (ttt_column, ttt_line)))
    return free_positions[:]

def generate_game():
    moves = []
    winner = None
    board = UltimateTicTacToe()

    free_positions = get_free_positions(board)
    prev_position = random.choice(free_positions)
    u_position, ttt_position = prev_position
    board.get_childs()[u_position[1]][u_position[0]].get_childs()[ttt_position[1]][ttt_position[0]].set_value("X")
    symbol = "O"
    moves.append(prev_position)

    while not board.check_result():

        _, p_ttt_position = prev_position
        free_positions = get_free_positions(board)
        aux = [(u_position, ttt_position) for u_position, ttt_position in free_positions if u_position == p_ttt_position]
        
        if aux:
            prev_position = random.choice(aux)
        else:
            prev_position = random.choice(free_positions)

        u_position, ttt_position = prev_position
        board.get_childs()[u_position[1]][u_position[0]].get_childs()[ttt_position[1]][ttt_position[0]].set_value(symbol)

        symbol = "X" if symbol == "O" else "O"
        moves.append(prev_position)

    return moves, board

def main():
    moves, board = generate_game()

    print(moves)
    print(board)
    print(board.check_result())

if __name__ == "__main__":
    main()