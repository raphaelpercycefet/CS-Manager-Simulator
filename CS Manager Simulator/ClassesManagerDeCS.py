# -*- coding: utf-8 -*-
import random
class Player:
    def __init__(self, name, aim, teamwork, strategy):
        self.name = name
        self.aim = aim
        self.teamwork = teamwork
        self.strategy = strategy
        self.kills = 0
        self.deaths = 0
        self.deathstotal = 0
        self.killstotal = 0

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.map_preferences = {}
        self.tactic_preferences = {}
        self.strong_ct_point = None
        self.strong_tr_point = None
        
    def set_strong_points(self, strong_ct_point, strong_tr_point):
        self.strong_ct_point = strong_ct_point
        self.strong_tr_point = strong_tr_point

    def add_player(self, player):
        self.players.append(player)

    def set_map_preference(self, map_name, preference):
        self.map_preferences[map_name] = preference

    def set_tactic_preference(self, tactic, modifier):
        self.tactic_preferences[tactic] = modifier

class Match:
    def __init__(self, team1, team2, map_name, team1_tactic, team2_tactic, team1_tactic_modifier, 
                 team2_tactic_modifier, team1_strong_ct_point, team1_strong_tr_point, team2_strong_ct_point, team2_strong_tr_point):
        self.team1 = team1
        self.team2 = team2
        self.map_name = map_name
        self.team1_tactic = team1_tactic
        self.team2_tactic = team2_tactic
        self.team1_tactic_modifier = team1_tactic_modifier
        self.team2_tactic_modifier = team2_tactic_modifier
        self.team1_strong_ct_point = team1_strong_ct_point
        self.team1_strong_tr_point = team1_strong_tr_point
        self.team2_strong_ct_point = team2_strong_ct_point
        self.team2_strong_tr_point = team2_strong_tr_point

    def play_match(self, mapa, economia_time1, economia_time2, tatica_time1, tatica_time2, team1_strong_ct_point, team1_strong_tr_point, team2_strong_ct_point, team2_strong_tr_point):
        
        # Calculando a pontuação do time de acordo com a habilidade dos seus jogadores, táticas, mapas e com um pouco de aleatoriedade
        modificador_time1_pontoforte = 0
        modificador_time2_pontoforte = 0

        if team1_strong_ct_point == team2_strong_tr_point:
            
            modificador_time1_pontoforte += 8
            
        else:
            
            modificador_time2_pontoforte += 4

        if team1_strong_tr_point == team2_strong_ct_point:
            
            modificador_time2_pontoforte += 8
            
        else:
            modificador_time1_pontoforte += 4
            
        modificador_time1_tatica_mapa = 0
        modificador_time2_tatica_mapa = 0
        
        if mapa == "Mirage":
            
            if tatica_time1 == "Retake" or tatica_time1 == "Execute":
                modificador_time1_tatica_mapa += 5 
            elif tatica_time1 == "Bait" or tatica_time1 == "Rush":
                modificador_time1_tatica_mapa -= 5
                
            if tatica_time2 == "Retake" or tatica_time2 == "Execute":
                modificador_time2_tatica_mapa += 5 
            elif tatica_time2 == "Bait" or tatica_time2 == "Rush":
                modificador_time2_tatica_mapa -= 5
                
        if mapa == "Inferno":
            
            if tatica_time1 == "FK" or tatica_time1 == "Domínio":
                modificador_time1_tatica_mapa += 5 
            elif tatica_time1 == "Retake" or tatica_time1 == "Rush":
                modificador_time1_tatica_mapa -= 5
                
            if tatica_time2 == "FK" or tatica_time2 == "Domínio":
                modificador_time2_tatica_mapa += 5 
            elif tatica_time2 == "Retake" or tatica_time2 == "Rush":
                modificador_time2_tatica_mapa -= 5
                
        if mapa == "Overpass":
            
            if tatica_time1 == "Retake" or tatica_time1 == "Domínio":
                modificador_time1_tatica_mapa += 5 
            elif tatica_time1 == "FK" or tatica_time1 == "Bait":
                modificador_time1_tatica_mapa -= 5
                
            if tatica_time2 == "Retake" or tatica_time2 == "Domínio":
                modificador_time2_tatica_mapa += 5 
            elif tatica_time2 == "FK" or tatica_time2 == "Bait":
                modificador_time2_tatica_mapa -= 5
                
        if mapa == "Nuke":
            
            if tatica_time1 == "Rush" or tatica_time1 == "FK":
                modificador_time1_tatica_mapa += 5 
            elif tatica_time1 == "Execute" or tatica_time1 == "Retake":
                modificador_time1_tatica_mapa -= 5
                
            if tatica_time2 == "Rush" or tatica_time2 == "FK":
                modificador_time2_tatica_mapa += 5 
            elif tatica_time2 == "Execute" or tatica_time2 == "Retake":
                modificador_time2_tatica_mapa -= 5
                
        if mapa == "Vertigo":
            
            if tatica_time1 == "Rush" or tatica_time1 == "Bait":
                modificador_time1_tatica_mapa += 5 
            elif tatica_time1 == "FK" or tatica_time1 == "Domínio":
                modificador_time1_tatica_mapa -= 5
                
            if tatica_time2 == "Rush" or tatica_time2 == "Bait":
                modificador_time2_tatica_mapa += 5 
            elif tatica_time2 == "FK" or tatica_time2 == "Domínio":
                modificador_time2_tatica_mapa -= 5
                
        if mapa == "Ancient":
            
            if tatica_time1 == "Execute" or tatica_time1 == "Bait":
                modificador_time1_tatica_mapa += 5 
            elif tatica_time1 == "Domínio" or tatica_time1 == "Retake":
                modificador_time1_tatica_mapa -= 5
                
            if tatica_time2 == "Execute" or tatica_time2 == "Bait":
                modificador_time2_tatica_mapa += 5 
            elif tatica_time2 == "Domínio" or tatica_time2 == "Retake":
                modificador_time2_tatica_mapa -= 5
                
        if mapa == "Anubis":
            
            if tatica_time1 == "Retake" or tatica_time1 == "FK":
                modificador_time1_tatica_mapa += 5 
            elif tatica_time1 == "Execute" or tatica_time1 == "Bait":
                modificador_time1_tatica_mapa -= 5
                
            if tatica_time2 == "Retake" or tatica_time2 == "FK":
                modificador_time2_tatica_mapa += 5 
            elif tatica_time2 == "Execute" or tatica_time2 == "Bait":
                modificador_time2_tatica_mapa -= 5
        
        if economia_time1 == "Arriscada":
            aleatoriomin = -10
            aleatoriomax = 40
        elif economia_time1 == "Normal":
            aleatoriomin = 0
            aleatoriomax = 30
        if economia_time1 == "Conservadora":
            aleatoriomin = 6
            aleatoriomax = 10
            
        if economia_time2 == "Arriscada":
            aleatoriomin2 = -10
            aleatoriomax2 = 40
        elif economia_time2 == "Normal":
            aleatoriomin2 = 0
            aleatoriomax2 = 30
        if economia_time2 == "Conservadora":
            aleatoriomin2 = 6
            aleatoriomax2 = 10
        
        team1_score = (self.calculate_team_score(self.team1) + modificador_time1_pontoforte + modificador_time1_tatica_mapa) + random.uniform(aleatoriomin, aleatoriomax)
        team2_score = (self.calculate_team_score(self.team2) + modificador_time2_pontoforte + modificador_time2_tatica_mapa) + random.uniform(aleatoriomin2, aleatoriomax2)


        if team1_score > team2_score:
            winner = self.team1
            
            # Calcular a quantidade de rounds para o time perdedor com probabilidades maior para um stomp quanto maior a diferença entre os dois timnes
            score_difference = team1_score - team2_score

            if score_difference > 15:
                loser_rounds_distribution = [14] * 4 + [13] * 5 + [12] * 5 + [11] * 5 + [10] * 9 + [9] * 9 + [8] * 9 + [7] * 9 + [6] * 11 + [5] * 8 + [4] * 8 + [3] * 6 + [2] * 6 + [1] * 6
            elif score_difference > 10:
                loser_rounds_distribution = [14] * 8 + [13] * 8 + [12] * 9 + [11] * 10 + [10] * 9 + [9] * 10 + [8] * 9 + [7] * 9 + [6] * 9 + [5] * 8 + [4] * 3 + [3] * 2 + [2] * 2 + [1] * 1
            elif score_difference > 5:
                loser_rounds_distribution = [14] * 13 + [13] * 13 + [12] * 14 + [11] * 14 + [10] * 11 + [9] * 10 + [8] * 4 + [7] * 4 + [6] * 5 + [5] * 5 + [4] * 4 + [3] * 1 + [2] * 1 + [1] * 1
            else:
                loser_rounds_distribution = [14] * 16 + [13] * 16 + [12] * 16 + [11] * 15 + [10] * 10 + [9] * 8 + [8] * 3 + [7] * 3 + [6] * 5 + [5] * 3 + [4] * 2 + [3] * 1 + [2] * 1 + [1] * 1
            
            loser_rounds = random.choice(loser_rounds_distribution)

            return winner, loser_rounds
        
        elif team2_score >= team1_score:
            winner = self.team2
            
            # Calcular a quantidade de rounds para o time perdedor com probabilidades maior para um stomp quanto maior a diferença entre os dois timnes
            score_difference = abs(team2_score - team1_score)

            # Máximo 14 para o time perdedor
            # Mínimo 0 para o time perdedor


            if score_difference >= 15:
                loser_rounds_distribution = [14] * 4 + [13] * 5 + [12] * 5 + [11] * 5 + [10] * 9 + [9] * 9 + [8] * 9 + [7] * 9 + [6] * 11 + [5] * 8 + [4] * 8 + [3] * 6 + [2] * 6 + [1] * 6
            elif score_difference >= 10 and score_difference < 15:
                loser_rounds_distribution = [14] * 8 + [13] * 8 + [12] * 9 + [11] * 10 + [10] * 9 + [9] * 10 + [8] * 9 + [7] * 9 + [6] * 9 + [5] * 8 + [4] * 3 + [3] * 2 + [2] * 2 + [1] * 1
            elif score_difference >= 5 and score_difference < 10:
                loser_rounds_distribution = [14] * 13 + [13] * 13 + [12] * 14 + [11] * 14 + [10] * 11 + [9] * 10 + [8] * 4 + [7] * 4 + [6] * 5 + [5] * 5 + [4] * 4 + [3] * 1 + [2] * 1 + [1] * 1
            else:
                loser_rounds_distribution = [14] * 16 + [13] * 16 + [12] * 16 + [11] * 15 + [10] * 10 + [9] * 8 + [8] * 3 + [7] * 3 + [6] * 5 + [5] * 3 + [4] * 2 + [3] * 1 + [2] * 1 + [1] * 1

            loser_rounds = random.choice(loser_rounds_distribution)
            return winner, loser_rounds
            
        else:
            pass

    def set_tactics(self, team1_tactic, team2_tactic):
        
        self.team1_tactic = team1_tactic
        self.team2_tactic = team2_tactic

    def calculate_team_score(self, team):
        
        #Levando em conta a preferencia de cada time para cada mapa e das taticas escolhidas
        map_modifier = team.map_preferences.get(self.map_name, 1.0)
        tactic_modifier = self.team1_tactic_modifier if team == self.team1 else self.team2_tactic_modifier

        total_score = 0.0
        total_score += round(float(map_modifier), 2)  # Convert and round
        total_score += round(float(tactic_modifier), 2)  # Convert and round
       
       #Levando em conta os três jogadores com maior atributo de Aim, depois de teamwork e os dois maiores de strategy para entrar no calculo 
        aim_values = sorted([player.aim for player in team.players], reverse=True)[:3]
        teamwork_values = sorted([player.teamwork for player in team.players], reverse=True)[:3]
        strategy_values = sorted([player.strategy for player in team.players], reverse=True)[:2]

        if team == self.team1:
            total_score = (
            round(float(map_modifier), 2)
            + round(float(tactic_modifier), 2)
            + sum(aim_values)
            + sum(teamwork_values)
            + sum(strategy_values)
            )
        else:
            total_score = (
            round(float(map_modifier), 2)
            + round(float(tactic_modifier), 2)
            + sum(aim_values)
            + sum(teamwork_values)
            + sum(strategy_values)
            )

        return total_score / 9  # 9 é apenas uma escolha para deixar a escala perto de 100