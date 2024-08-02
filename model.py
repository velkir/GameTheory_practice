class Game:
    def __init__(self, player1, player2,
                 rounds=200,
                 betrayal_success=5,
                 betrayal_failed=1,
                 cooperation_success=3,
                 cooperation_failed=0):
        self.game_log = []
        self.player1 = player1
        self.player2 = player2
        self.total_rounds = rounds
        self.betrayal_success = betrayal_success
        self.betrayal_failed = betrayal_failed
        self.cooperation_success = cooperation_success
        self.cooperation_failed = cooperation_failed

    def next_round(self):
        self.calculate_round(self.player1.get_decision(self), self.player2.get_decision(self))

    def calculate_round(self, decision1, decision2):
        if decision1 and decision2:
            self.player1.score += self.cooperation_success
            self.player2.score += self.cooperation_success
        elif not decision1 and not decision2:
            self.player1.score += self.betrayal_failed
            self.player2.score += self.betrayal_failed
        elif decision1:
            self.player1.score += self.cooperation_failed
            self.player2.score += self.betrayal_success
        elif decision2:
            self.player1.score += self.betrayal_success
            self.player2.score += self.cooperation_failed
        if decision1:
            print("Player1 cooperated!")
        else:
            print("Player1 betrayed!")

        if decision2:
            print("Player2 cooperated!")
        else:
            print("Player2 betrayed!")

        self.game_log.append([decision1, decision2])

    def end_game(self):
        print("Game finished!")
        print(f"Score {self.player1.name}: {self.player1.score}")
        print(f"Score {self.player2.name}: {self.player2.score}")

    def process_game(self):
        for current_round in range(1, self.total_rounds+1):
            self.next_round()
        self.end_game()


class Player:
    def __init__(self, name=None, logics=None):
        self.name = name
        self.logics = logics
        self.score = 0

    def get_decision(self, game):
        if self.logics:
            return self.logics.get_decision(game.game_log, game.total_rounds)
        else:
            try:
                decision = int(input("0 for betrayal, 1 for cooperation"))
                if decision == 0 or decision == 1:
                    return decision
                else:
                    print("Wrong input")
                    return self.get_decision(game)
            except:
                print("Wrong input")
                return self.get_decision(game)

player1 = Player(name="Manual1")
player2 = Player(name="Manual2")
game = Game(player1, player2, rounds=3)
game.process_game()
print(game.game_log)
