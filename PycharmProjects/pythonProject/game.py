scores_number_valor = {0: 'Love', 1: 'Fifteen', 2: 'Trirty',3: 'Forty'}
pontos_minimos_vantagem = 3
pontos_minimos_ganhar = 4
diferença_pontos_minimos_set = 2

class Game:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.player_1_faz_ponto()
        else:
            self.player_2_faz_ponto()
