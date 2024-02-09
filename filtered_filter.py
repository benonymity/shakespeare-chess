import chess.pgn
import os
import chess


def pgn_to_board(pgn):
    board = chess.Board()
    moves = pgn.mainline()
    movelist = str(moves).split(" ")
    for i in reversed(range(0, len(movelist), 3)):
        movelist.pop(i)
    for i in movelist:
        board.push_san(i)
    return board


try:
    pgn_file = open("/config/workspace/r3_Chess/filtered.pgn")
    while True:
        pgn = chess.pgn.read_game(pgn_file)
        if not pgn:
            break
        board = pgn_to_board(pgn)
        if board.is_checkmate():
            print(pgn.headers)
            print(board)
            with open("final.pgn", "a") as f:
                f.write(str(pgn))
                f.write("\n")
                f.write("\n")
                f.close()

except:
    pass
