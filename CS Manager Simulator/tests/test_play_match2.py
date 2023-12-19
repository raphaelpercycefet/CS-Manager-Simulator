import random

def create_team(team_name, player_data, tactic_preferences, map_preferences):
    team = Team(team_name)
    for player_name, abilities in player_data.items():
        aim, teamwork, strategy = abilities
        player = Player(player_name, aim, teamwork, strategy)      
        team.add_player(player)
    for tactic, modifier in tactic_preferences.items():
        team.set_tactic_preference(tactic, modifier)
    for map_name, preference in map_preferences.items():
        team.set_map_preference(map_name, preference)
    return team


def creating_teams_players():
    heroic_players = {
    "Cadian": (87, 84, 88),
    "Stavn": (87, 81, 76),
    "Jabbi": (85, 81, 73),
    "Teses": (83, 82, 76),
    "Sjuush": (73, 90, 84)}
    heroic_tactic_preferences = {
        "Retake": 42.0,
        "Domínio": 39.0,
        "Rush": 44.0,
        "FK": 35.0,
        "Execute": 40.0,
        "Bait": 36.0
    }
    heroic_map_preferences = {
        "Overpass": 16.8,
        "Mirage": 32.2,
        "Inferno": 29.1,
        "Nuke": 28.1,
        "Vertigo": 25.9,
        "Ancient": 29.0,
        "Anubis": 29.2
    }
    heroic_team = create_team("Heroic", heroic_players, heroic_tactic_preferences, heroic_map_preferences)

    vitality_players = {
    "Zywoo": (95, 86, 86),
    "Spinx": (87, 80, 78),
    "Flamez": (84, 79, 75),
    "Magisk": (82, 84, 83),
    "Apex": (70, 85, 88)}
    vitality_tactic_preferences = {
        "Retake": 45.0,
        "Domínio": 42.0,
        "Rush": 47.0,
        "FK": 31.0,
        "Execute": 37.0,
        "Bait": 33.0
    }
    vitality_map_preferences = {
        "Overpass": 31.1,
        "Mirage": 25.0,
        "Inferno": 31.2,
        "Nuke": 26.9,
        "Vertigo": 28.1,
        "Ancient": 25.8,
        "Anubis": 18.0
    }
    vitality_team = create_team("Vitality", vitality_players, vitality_tactic_preferences, vitality_map_preferences)

    teams = [heroic_team, vitality_team]
    maps = ["Overpass", "Mirage", "Inferno", "Nuke", "Vertigo", "Ancient", "Anubis"]
    tactics = [
        "Retake",
        "Domínio",
        "Rush",
        "FK",
        "Execute",
        "Bait"
    ]
    return teams, maps, tactics

      
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

teams, maps, tactics = creating_teams_players()

time1_nome = "Vitality"
time2_nome = "Heroic"

team1 = None
team2 = None

for team in teams:
    
    if team.name == time1_nome.title():
        team1 = team
    elif team.name == time2_nome.title():
        team2 = team

class Match:
    def __init__(self, team1, team2, mapa, team1_tactic, team2_tactic, team1_tactic_modifier, 
                 team2_tactic_modifier, team1_strong_ct_point, team1_strong_tr_point, team2_strong_ct_point, team2_strong_tr_point):
        self.team1 = team1
        self.team2 = team2
        self.mapa = mapa
        self.team1_tactic = team1_tactic
        self.team2_tactic = team2_tactic
        self.team1_tactic_modifier = team1_tactic_modifier
        self.team2_tactic_modifier = team2_tactic_modifier
        self.team1_strong_ct_point = team1_strong_ct_point
        self.team1_strong_tr_point = team1_strong_tr_point
        self.team2_strong_ct_point = team2_strong_ct_point
        self.team2_strong_tr_point = team2_strong_tr_point

    def test_play_match2(self, mapa, economia_time1, economia_time2, tatica_time1, tatica_time2, team1_strong_ct_point, team1_strong_tr_point, team2_strong_ct_point, team2_strong_tr_point):
        
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
            
        assert modificador_time1_pontoforte == 0
        
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
        
        assert aleatoriomin < 7 and aleatoriomax > 9
        assert aleatoriomax2 < 31 and aleatoriomin2 > -1
        
        team1_score = (self.calculate_team_score(self.team1) + modificador_time1_pontoforte + modificador_time1_tatica_mapa) + random.uniform(aleatoriomin, aleatoriomax)
        team2_score = (self.calculate_team_score(self.team2) + modificador_time2_pontoforte + modificador_time2_tatica_mapa) + random.uniform(aleatoriomin, aleatoriomax)

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
            assert loser_rounds < 15
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
            assert loser_rounds < 15
            return winner, loser_rounds
            
        else:
            pass

    def calculate_team_score(self, team):
        
        #Levando em conta a preferencia de cada time para cada mapa e das taticas escolhidas
        map_modifier = team.map_preferences.get(self.mapa, 1.0)
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


mapa = "Ancient"
economia_time1 = "Conservadora"
economia_time2 = "Normal"
tatica_time1 = "Execute"
tatica_time2 = "Rush"
team1_strong_ct_point = "A"
team1_strong_tr_point = "Meio"
team2_strong_ct_point = "Meio"
team2_strong_tr_point = "Meio"
team1_tactic_modifier = team1.tactic_preferences.get(tatica_time1, 1.0)
team2_tactic_modifier = team2.tactic_preferences.get(tatica_time2, 1.0)

match = Match(team1, team2, mapa, tatica_time1, tatica_time2, team1_tactic_modifier, team2_tactic_modifier,
              team1_strong_ct_point, team1_strong_tr_point, team2_strong_ct_point, team2_strong_tr_point)

# Simula a partida e retorna o ganhador e o numero de rounds do perdedor do mapa
winning_team, loser_rounds = match.test_play_match2(mapa, economia_time1, economia_time2, tatica_time1, tatica_time2, team1_strong_ct_point, team1_strong_tr_point, team2_strong_ct_point, team2_strong_tr_point)

assert winning_team.name == "Heroic"