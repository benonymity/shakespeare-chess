import chess.pgn
import chess
import os

out = open("filtered.txt", "w")

for file in os.listdir("/config/workspace/r3_Chess/pgn"):
    pgn = open("/config/workspace/r3_Chess/pgn/" + file)
    try:
        while True:
            game = chess.pgn.read_game(pgn)
            if (
                int(str(game.end())[:2]) <= 30
                and int(str(game.end())[:2]) >= 25
                and game.headers["Result"][:-2] == "1"
            ):
                # print(game.next())
                # print(game)
                out.write(str(game))
                out.write("\n")
                print(game.fen())
                print(game.end().board())
                print()
    except:
        pass
