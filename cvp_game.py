"""
boom > big attack
can only reflect small attack
can defend all attack
big attack can kill

"""
import random


class player:
    def __init__(self):
        self.health = 1
        # 0为未操作 1为已操作
        self.operation_status = -1
        # 0 get chi 1 small attack 2 big attack 3 boom 4 reflect 5 defend
        # judge 结束 清零

        # energy chi default 0
        self.chi = 0
        self.opponent = None

    def get_opponent(self):
        return self.opponent

    def get_operation(self):
        return self.operation_status

    def get_chi(self):
        return self.chi

    def pvp_operate(self):
        prompt = 'Choose operation:'
        prompt2 = 'Choose an Opponent:'
        x = input(prompt)
        operation = int(x)
        if operation == 0:
            self.chi = self.chi + 1
            self.operation_status = operation

        elif self.chi >= operation:
            print('fuck')
            self.chi = self.chi - operation
            self.operation_status = operation
            # 要缩进进来啊 兄弟
            if operation < 3:
                opponent = int(input(prompt2))
                self.opponent = opponent

        elif 4 <= operation <=5:
            self.operation_status = operation

        else:
            print('no enough chi OR wrong status')


    def operate(self):
        # 在这里判断 可行 与 打气 ? 是否最优？
        prompt = 'Choose operation:'
        operation = int(input(prompt))

        # real player
        # 0 get chi 1 small attack 2 big attack 3 boom 4 reflect 5 defend
        if operation == 0:
            self.chi = self.chi + 1
            self.operation_status = operation

        elif self.chi >= operation:
            self.chi = self.chi - operation
            self.operation_status = operation

        elif 4 <= operation <= 5:
            self.operation_status = operation

        else:
            print('no enough chi OR wrong status')

    def comp_operate(self, operation):

        # real player
        # 0 get chi 1 small attack 2 big attack 3 boom 4 reflect 5 defend
        if operation == 0:
            self.chi = self.chi + 1
            self.operation_status = operation

        elif self.chi >= 1 and operation == 1:
            self.chi = self.chi - 1
            self.operation_status = operation

        elif self.chi >= 2 and operation == 2:
            self.chi = self.chi - 2
            self.operation_status = operation

        elif self.chi >= 3 and operation == 3:
            self.chi = self.chi - 3
            self.operation_status = operation

        elif operation == 4:
            self.operation_status = operation

        elif operation == 5:
            self.operation_status = operation

        else:
            print('no enough chi OR wrong status')

    def print_status(self, name):
        print('Status of ' + name)
        print('Health: ' + str(self.health) + '   chi: ' + str(self.chi))

    def small_damage(self):
        self.health = self.health - 0.5

    def dead(self):
        self.health = self.health - 1


class CvP_game:
    def __init__(self):
        self.player_a = player()
        self.player_b = player()

    def judge(self):
        me = int(self.player_a.operation_status)
        comp = int(self.player_b.operation_status)
        # if me == 0 and comp == 1:
        #     return
        # if me > 3 and comp > 3:
        #     return

        if me == 1:
            if comp == 0:
                self.player_b.small_damage()
            elif comp == 1:
                self.player_a.small_damage()
                self.player_b.small_damage()
            elif comp == 2 or comp == 3:
                self.player_a.dead()
                self.player_b.small_damage()

            elif comp == 4:
                self.player_a.small_damage()

            #    格挡加气？
            # elif comp == 5:
            #     self.player_b.chi = self.player_b.chi + 1

        elif me == 2:
            if comp == 1:
                self.player_a.small_damage()
                self.player_b.dead()
            elif comp == 2 or comp == 3:
                self.player_a.dead()
                self.player_b.dead()

            elif comp == 4 or comp == 0:
                self.player_b.dead()

        elif me == 3:
            if not comp == 5:
                self.player_b.dead()

        elif me == 4:
            if comp == 1:
                self.player_b.small_damage()
            elif comp == 2 or comp == 3:
                self.player_a.dead()

        if me == 0:
            if comp == 1:
                self.player_a.small_damage()

            elif comp == 2:
                self.player_a.dead()

            elif comp == 3:
                self.player_a.dead()

        self.player_a.operation_status = -1
        self.player_b.operation_status = -1

        return

def computer_operation(chi):
    if chi == 0:
        return 0
    # 没气打气
    rand = random.random()
    bigRand = random.random()
    # print(rand)
    # print(bigRand)
    if bigRand < 0.3:
        if bigRand < 0.15:
            return 4
        #     reflect
        else:
            return 5
    #     defend


#     打气
    if chi <= 2:
        if rand < 0.25:
            return 0
    #     1/3 打气
        elif rand < 0.66 and chi >=1:
            return 1
        else:
            if chi == 2:
                return 2
            else:
                return 0
    #        不完整

    elif chi >= 3:
        return 3
    #     boom

    # 默认打气
    return 0

def print_operation(number):
    if number == 0:
        print('get CHI!')

    elif number == 1:
        print('Small Attack! ')

    elif number == 2:
        print('BIG Attack!')

    elif number == 3:
        print('BOOOOOOOOOOOOM!')

    elif number == 4:
        print('Reflect! ))>')

    elif number == 5:
        print('DEFEND! ]]]]')

def explanation():
    print('Welcome to chi game')
    print('*************************************')
    print("Belows are instructions: CHI 1.1.2")
    print("Get chi and kill the computer (input 0)")
    print("Or you can try pvp mode by inputting 1")
    print()
    mode = input()

    print("0: Get chi(used  for attack operation)")
    print("1: Small Attack(need 1 chi), deal 0.5 damage")
    print("2: BIG Attack(need 2 chi), deal 1 damage(can kill directly)")
    print("3: BOOOOOOOOOM!(need 3 chi), deal aoe damage, prior to BIG attack")
    print("4: Reflect, can reflect small attack to opponent")
    print("5: Defend, can defend all attack including BOOOOOM!")

    return mode

def initial_cvp_game():
    mygame = CvP_game()

    while mygame.player_a.health > 0 and mygame.player_b.health > 0:
        mygame.player_a.print_status(name='ME')
        mygame.player_b.print_status(name='Computer')

        while mygame.player_a.get_operation() < 0:
            # variable type need to convert
            mygame.player_a.operate()

        # 电脑暂时一直打气
        com_operation = int(computer_operation(mygame.player_b.chi))
        mygame.player_b.comp_operate(com_operation)

        print('My operation:')
        print_operation(mygame.player_a.get_operation())
        print('Computer operation:')
        print_operation(mygame.player_b.get_operation())

        mygame.judge()

    if mygame.player_a.health == 0:
        print('Oh no, you fucking loser...')

    else:
        print('Great job, defeating a programme..,')

    input("Would you like another round? (if so just restart the game)")


# if __name__ == '__main__':
