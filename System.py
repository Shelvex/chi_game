import cvp_game
import pvp_game
import server
import client

def start():
    mode = cvp_game.explanation()
    if int(mode) == 0:
        cvp_game.initial_cvp_game()
    elif int(mode) == 1:
        pvp_game.initial_pvp_game()
    else :
        print("Something goes wrong")


if __name__ == '__main__':
    start()