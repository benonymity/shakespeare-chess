import chess.pgn
import os
import chess
from time import sleep

# READ ME:
# Wow that explains a lot! That also makes things a lot simpler and cleaner!
# I integrated your code from filter_old here, and moved an archive of my old code used extracted text shenanigans to filter_old_old.py
#
# Instead of try and except, I found out that read_game() returns null when there are none left, so I used that for more pythonic code.
# I figured out how to get a chess.Board object from the pgn! I put it all in pgn_to_board
# I changed str(game.end()[:2]) to str(game.end()).split('.')[0] because of an edge case where the turn number was 1 digit and thus included a period in the first two chars
#
# now all we need to do is filter out the queen captures and whatnot!


# NEW: Very nice! See more comments at end. But I think we'll probably have to give up this whole database combing thing if she wants a 12-15 move game :(
# If I find a game that is that, I'll let you know!


# returns a board from a pgn read
def pgn_to_board(pgn):
    # make empty board
    board = chess.Board()
    # get string of moves from pgn
    moves = pgn.mainline()
    movelist = str(moves).split(" ")
    # remove each turn number indicator "1.", "2." and so on
    for i in reversed(range(0, len(movelist), 3)):
        movelist.pop(i)
    # push each move to board
    for i in movelist:
        board.push_san(i)
    return board


# Just a counter to track how long this has been running!
game_number = 0
filtered = []

# Info printing
os.system("clear")
print(
    "This program will search through all pgn files in /pgn for games < 16 turns long. When completeled it will print out all found games. Will take some time to run, use CTRL+Z to force stop."
)
sleep(5)

# iterate through each pgn file
for file in os.listdir("/config/workspace/r3_Chess/pgn"):

    # Sorry, had to use one of these because I got a weird error. I believe that one of the pgns was mislabelled,
    # so it took headers as the game and as this can't parse a string it panicked. Oh well. ¯\_(ツ)_/¯
    try:
        pgn_file = open("/config/workspace/r3_Chess/pgn/" + file)
        while True:
            pgn = chess.pgn.read_game(pgn_file)
            # when it reaches the final game, it returns null. if there are no more games, break the loop.      NEW: Brilliant!! Much nicer logic than waiting for errors ;)
            if not pgn:
                break

            # More sanity checks when running, to make this program marginally more exciting than watching paint dry ;)
            os.system("clear")
            game_number += 1
            print("Game number: " + str(game_number))
            print("Matches found: " + str(len(filtered)))
            print("Currently searching " + str(file))
            print("Game's move count: " + str(pgn.end()).split(".")[0])
            # print(filtered)

            # Moved pgn_to_board into first if loop, otherwise unnessecary and time-consuming computation is being done

            # if the games length is 25-30 moves, not turns
            if int(str(pgn.end()).split(".")[0]) < 16:
                # convert pgn to board
                board = pgn_to_board(pgn)

                # In 15k games, not one that ended in checkmate and was < 16 turns :( Might as well find short ones though.
                # if board.is_checkmate():

                # These have been supersceded and are handled elsewhere, not really needed
                # print(pgn.headers)
                # print(board)

                # Tracks filtered games across console clears--don't laugh at the absurd amount of str()s,
                # I didn't want to take any chances of errors after spending this much time running it! ;)
                filtered.append(
                    str(pgn.headers)
                    + "/n"
                    + str(pgn)
                    + "/n"
                    + str(board)
                    + "/n"
                    + str(game_number)
                )

                # Saves good games to new pgn
                with open("filtered.pgn", "a") as f:
                    f.write(str(pgn))
                    f.write("\n")
                    f.write("\n")
                    f.close()
    except:
        pass

# To make sure that hard work doesn't get erased!
print("Games searched: " + str(game_number))
print("Found " + str(len(filtered)) + " matching games, which are:")
for i in filtered:
    print(i)
    print()
out.close()

# NEWER READ ME: Okay, I spent an embarrasing amount of time trying to debug this, but turns out there is no output because there
# are almost no games that are 12 moves long. I'll let this run while I do other things and see if anything gets printed.
# If not, I think that historical games are out. Do something ourselves? Should we attempt that programatically? Or just by hand? Hmmmm...
