import chess.pgn
import os
import io
import chess

# READ ME:
# the reason why the original filter program didn't work was because if you put the pgn file into chess.pgn raw,
# it only grabs the first game and neglects all the others, so the old code only read the first game of each file.
# This code gets the raw text of the pgn file and then extracts each individual game from the text.
# The chess.pgn.read_game function doesn't accept raw text so the program encodes it into the format that it accepts.
#
# Can you make a function that takes in the read pgn game and puts out a board? so that we can check checkmate and stuff.
# Then I was thinking we search for games that are x moves long, and have a checkmate and white win
# and have the black queen captured on move 19
# (do you know which queen it is that dies? I suspect that it's richards queen, but idk. Black if it's richards queen, white if not)
# and then we could save every found game to a separate file

# NEW STUFF:
# To keep this file pristine I've moved my work to filter_old.py. It actually turns out to work, this module works in a strange way.
# If you open a file and keep calling chess.pgn.read_game(), it'll actually just read the next game in the pgn file instead of having
# to deal with text and such. At this point, filter_old.py filters every game in the entire database, but I'm trying to figure out
# how to deal with reading which pieces have been taken. I think it might be computationally expensive, because we might have to store
# every past move and track the existence of the queen. I think it is doable, and there might even be something built-in, but atm
# I'm trying to figure out how to get chess.pgn and plain old chess to talk nice, because the chess module has what we need.

# NEW NEW STUFF:
# Wow that explains a lot! That also makes things a lot simpler and cleaner!

# returns a board from a pgn read
def pgn_to_board(pgn):
    board = chess.Board()
    moves = pgn.mainline()
    # better name?
    list = str(moves).split(" ")
    # remove each turn number indicator "1.", "2." and so on
    for i in reversed(range(0, len(list), 3)):
        list.pop(i)
    # I was thinking of pushing each move from the pgn.mainline
    board.push(chess.Move.from_uci("g1f3"))
    return board


# save text from pgn file
with open("/config/workspace/r3_Chess/pgn/Adams.pgn") as f:
    pgn_file = f.read()

# Switch out for above logic to iterate through all pgn files:
# for file in os.listdir()

# split the file by breaks
pgn_file_split = pgn_file.split("\n\n")

# string for saving search results to later be saved to a file
search_res = ""

# loop
for i in range(0, len(pgn_file_split), 2):
    # save the text between every two double returns (which constitutes one pgn game)
    pgn_raw = "\n".join(pgn_file_split[0 + i : 2 + i])
    # encode it into the format that chess.pgn.read_game accepts
    pgn_enc = io.StringIO(pgn_raw)
    # read the game
    game = chess.pgn.read_game(pgn_enc)
    # convert pgn into board so that the moves can be read more easily
    board = pgn_to_board(game)

    break

    # if the game ends in checkmate
    if board.is_checkmate():
        # if white wins
        if game.headers["Result"] == "1-0":
            # save game to results
            search_res += game + "\n\n"
print(search_res)
