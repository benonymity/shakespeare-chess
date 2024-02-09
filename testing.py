import chess.pgn
import os
import chess

pgn = open("/config/workspace/r3_Chess/pgn/Adams.pgn")

tally = 0
while True:
    game = chess.pgn.read_game(pgn)
    if not game:
        break
    tally += 1
    print(tally)

pgn.close()
