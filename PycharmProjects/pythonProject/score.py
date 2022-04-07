scores_number_valor = {0: 'Love', 1: 'Fifteen', 2: 'Trirty',3: 'Forty'}
pontos_minimos_vantagem = 3
pontos_minimos_ganhar = 4
diferença_pontos_minimos_set = 2

class Score:
    def score(self):
        if self.is_game_empatado():
            result = self.is_player_set_point(self.p1points)
        elif self.is_player2_vantagem():
            result = "Advantage " + self.player2Name

        elif self.is_player1_vantagem():
            result = "Advantage " + self.player1Name

        elif self.is_player_set_point(self.p1points) and self.is_game_vencido(self.get_player1_player2_diferenca()):
            result = "Win for " + self.player1Name

        elif self.is_player_set_point(self.p2points) and self.is_game_vencido(self.get_player2_player1_diferenca()):
            result = "Win for " + self.player2Name
        else:
            player_1_pontuacao = self.get_pontuacao(self.p1points)
            player_2_pontuacao = self.get_pontuacao(self.p2points)
            result = player_1_pontuacao + "-" + player_2_pontuacao
        return result


    def is_game_vencido(self, diferenca):
        return diferenca >= diferença_pontos_minimos_set


    def get_player1_player2_diferenca(self):
        return self.p1points - self.p2points


    def get_player2_player1_diferenca(self):
        return self.p2points - self.p1points


    def is_game_empatado(self):
        return self.p1points == self.p2points and self.p1points < pontos_minimos_vantagem


    def is_player1_vantagem(self):
        return self.p1points > self.p2points >= pontos_minimos_vantagem


    def is_player2_vantagem(self):
        return self.p2points > self.p1points >= pontos_minimos_vantagem


    def is_player_set_point(self, points):
        return points >= pontos_minimos_ganhar


    def get_pontuacao_empatada(self, points):
        result = None
        if points >= pontos_minimos_vantagem:
            result = "Deuce"
            return result
        result = self.get_pontuacao(points)
        result += "-All"
        return result


    def get_pontuacao(self, points):
        return scores_number_valor[points]


    def set_player_1_pontuacao(self, number):
        for i in range(number):
            self.player_1_faz_ponto()


    def player_1_faz_ponto(self):
        self.p1points += 1


    def set_player_2_pontuacao(self, number):
        for i in range(number):
            self.player_2_faz_ponto()


    def player_2_faz_ponto(self):
        self.p2points += 1

