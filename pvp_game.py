import cvp_game


class pvp_game:
    def __init__(self, number_of_player):
        self.player_list = []
        for i in range(0, number_of_player):
            self.player_list.append(cvp_game.player())

    def print_operation(self, player):
        if player.get_operation() == 0:
            print('get CHI!')

        elif 1 <= player.get_operation() < 3:
            if player.get_operation() == 1:
                print('Small Attack to Player ' + str(player.get_opponent()))
                if self.player_list[player.get_opponent()].get_operation() == 4:
                    player.small_damage()
                #         get reflect
                elif self.player_list[player.get_opponent()].get_operation() < 3:
                    self.player_list[player.get_opponent()].small_damage()

            if player.get_operation() == 2:
                print('BIG Attack to Player ' + str(player.get_opponent()))
                if self.player_list[player.get_opponent()].get_operation() < 3:
                    self.player_list[player.get_opponent()].dead()

        elif player.get_operation() == 3:
            print('BOOOOOOOOOOOOM!')
            for the_player in self.player_list:
                if not the_player == player:
                    if not the_player.get_operation() == 5:
                        the_player.dead()
        #                 不防御 死

        elif player.get_operation() == 4:
            print('Reflect! ))>')

        elif player.get_operation() == 5:
            print('DEFEND! ]]]]')

    def print_each_operation(self):
        for i in range(0, len(self.player_list)):
            print("Player " + str(i) + "'s operation")
            self.print_operation(self.player_list[i])

    def print_player_status(self):
        for i in range(0, len(self.player_list)):
            print("Player " + str(i) + "'s status")
            print("Health: " + str(self.player_list[i].health))
            print("Chi: " + str(self.player_list[i].chi))

    def judge(self):
        # print each player's operation, and calculate the operation result
        self.print_each_operation()

        self.print_player_status()
        # show after judge status

        # judge done, operation initialized
        for player in self.player_list:
            player.operation_status = -1

        return

    def get_health_status(self):
        for j in range(0, len(self.player_list)):
            if self.player_list[j].health <= 0:
                return False
        #     end the game
        return True

    #     continue the game

    def get_operation_status(self):
        for j in range(0, len(self.player_list)):
            if self.player_list[j].operation_status == -1:
                return True
        #     end the game
        return False

    #     continue the game
    def do_one_round_operation(self):
        while self.get_operation_status():
            for player in self.player_list:
                if player.operation_status == -1:
                    # player.operate()
                    player.pvp_operate()

    def get_loser_and_winner(self):
        print("***************RESULT****************")
        for j in range(0, len(self.player_list)):
            if self.player_list[j].health <= 0:
                print("Player " + str(j) + ", you fuckin' loser...")
            else:
                print("Player " + str(j) + ", congrats, you beat others by your chance...")

        #     end the game


def initial_pvp_game():
    number_of_people = int(input('How many people are to play the chi game?'))
    my_pvp_game = pvp_game(number_of_people)

    for i in range(0, number_of_people):
        print(my_pvp_game.player_list[i])

    while my_pvp_game.get_health_status():
        my_pvp_game.do_one_round_operation()
        my_pvp_game.judge()

    my_pvp_game.get_loser_and_winner()


# if __name__ == '__main__':



