import random
from ClassesManagerDeCS import Player, Team 


def update_player_stats(winning_team, losing_team, rounds):
    
    if rounds >= 28:
        # Calculando o número de kills dos times de forma aleatória com base no número de rounds
        total_winning_killsv = random.randint(105, 115)
        total_losing_deathsp = total_winning_killsv
        total_winning_killsp = random.randint(95, total_winning_killsv - 5)
        total_losing_deathsv = total_winning_killsp
        total_winning_killsv = max(total_winning_killsv, 10)
        min_kills=13
        max_kills=34
        kills_distribution = generate_random_values(total_winning_killsv, len(winning_team.players), min_kills, max_kills, rounds)
        players = winning_team.players

        probabilidades = [
                0.40,  # Maior probabilidade para o índice 0
                0.30, # 0.32
                0.15, # 0.16
                0.10, # 0.07
                0.5  # Menor probabilidade para o índice 4
                ]

        # Criação da lista de elementos com probabilidades

        # Criar uma lista ponderada com base nas probabilidades
        weighted_players = [player for player, weight in zip(players, probabilidades) for _ in range(int(weight * 100))]
        
        
        # Obter uma amostra sem reposição usando random.sample
        jogadores_baseada_probabilidade = []

        while len(jogadores_baseada_probabilidade) < 5:
            jogador = random.choice(weighted_players)
            if jogador not in jogadores_baseada_probabilidade:
                jogadores_baseada_probabilidade.append(jogador)

        
        
        for i, jogador in enumerate(jogadores_baseada_probabilidade):
            jogador_selecionado = next((player for player in players if player.name == jogador.name), None)
            if jogador_selecionado:
                jogador_selecionado.kills = kills_distribution[i]
                jogador_selecionado.killstotal = jogador_selecionado.kills + jogador_selecionado.killstotal
                
                

        min_kills=15
        max_kills=27
        deaths_distribution = generate_random_values(total_losing_deathsp, len(losing_team.players), min_kills, max_kills, rounds)
        players = losing_team.players
        probabilidades = [
                0.15,  # Maior probabilidade para o índice 0
                0.15, # 0.32
                0.20, # 0.16
                0.20, # 0.07
                0.30  # Menor probabilidade para o índice 4
                ]

        # Criar uma lista ponderada com base nas probabilidades
        weighted_players = [player for player, weight in zip(players, probabilidades) for _ in range(int(weight * 100))]
        
        
        # Obter uma amostra sem reposição usando random.sample
        jogadores_baseada_probabilidade = []

        while len(jogadores_baseada_probabilidade) < 5:
            jogador = random.choice(weighted_players)
            if jogador not in jogadores_baseada_probabilidade:
                jogadores_baseada_probabilidade.append(jogador)

        

        for i, jogador in enumerate(jogadores_baseada_probabilidade):
            
            jogador_selecionado = next((player for player in players if player.name == jogador.name), None)
            
            if jogador_selecionado:
                jogador_selecionado.deaths = deaths_distribution[i]
                jogador_selecionado.deathstotal = jogador_selecionado.deathstotal + jogador_selecionado.deaths
                
            
        min_kills=10
        max_kills=32
        kills_distribution = generate_random_values(total_winning_killsp, len(losing_team.players), min_kills, max_kills, rounds)
        players = losing_team.players

        probabilidades = [
                0.40,  # Maior probabilidade para o índice 0
                0.30, # 0.32
                0.15, # 0.16
                0.10, # 0.07
                0.5  # Menor probabilidade para o índice 4
                ]

        # Criação da lista de elementos com probabilidades
        
# Criar uma lista ponderada com base nas probabilidades
        weighted_players = [player for player, weight in zip(players, probabilidades) for _ in range(int(weight * 100))]
        
        
        # Obter uma amostra sem reposição usando random.sample
        jogadores_baseada_probabilidade = []

        while len(jogadores_baseada_probabilidade) < 5:
            jogador = random.choice(weighted_players)
            if jogador not in jogadores_baseada_probabilidade:
                jogadores_baseada_probabilidade.append(jogador)

        

        for i, jogador in enumerate(jogadores_baseada_probabilidade):
            
            jogador_selecionado = next((player for player in players if player.name == jogador.name), None)
            
            if jogador_selecionado:
                jogador_selecionado.kills = kills_distribution[i]
                jogador_selecionado.killstotal = jogador_selecionado.kills + jogador_selecionado.killstotal
                
        min_kills = 14
        max_kills = 26
        deaths_distribution = generate_random_values(total_losing_deathsv, len(winning_team.players), min_kills, max_kills, rounds)
        players = winning_team.players
        probabilidades = [
                0.15,  # Maior probabilidade para o índice 0
                0.15, # 0.32
                0.20, # 0.16
                0.20, # 0.07
                0.30  # Menor probabilidade para o índice 4
                ]

        # Criar uma lista ponderada com base nas probabilidades
        weighted_players = [player for player, weight in zip(players, probabilidades) for _ in range(int(weight * 100))]
        
        
        # Obter uma amostra sem reposição usando random.sample
        jogadores_baseada_probabilidade = []

        while len(jogadores_baseada_probabilidade) < 5:
            jogador = random.choice(weighted_players)
            if jogador not in jogadores_baseada_probabilidade:
                jogadores_baseada_probabilidade.append(jogador)

        

        for i, jogador in enumerate(jogadores_baseada_probabilidade):
            
            jogador_selecionado = next((player for player in players if player.name == jogador.name), None)
            
            if jogador_selecionado:
                jogador_selecionado.deaths = deaths_distribution[i]
                jogador_selecionado.deathstotal = jogador_selecionado.deathstotal + jogador_selecionado.deaths
                
            
    elif rounds >= 25 and rounds < 28:
        total_winning_killsv = random.randint(90, 100)
        total_losing_deathsp = total_winning_killsv
        total_winning_killsp = random.randint(75, total_winning_killsv - 10)
        total_losing_deathsv = total_winning_killsp
        total_winning_killsv = max(total_winning_killsv, 10)
        min_kills=8
        max_kills=30
        kills_distribution = generate_random_values(total_winning_killsv, len(winning_team.players), min_kills, max_kills, rounds)
        players = winning_team.players

        probabilidades = [
                0.40,  # Maior probabilidade para o índice 0
                0.30, # 0.32
                0.15, # 0.16
                0.10, # 0.07
                0.5  # Menor probabilidade para o índice 4
                ]

        # Criar uma lista ponderada com base nas probabilidades
        weighted_players = [player for player, weight in zip(players, probabilidades) for _ in range(int(weight * 100))]
        
        
        # Obter uma amostra sem reposição usando random.sample
        jogadores_baseada_probabilidade = []

        while len(jogadores_baseada_probabilidade) < 5:
            jogador = random.choice(weighted_players)
            if jogador not in jogadores_baseada_probabilidade:
                jogadores_baseada_probabilidade.append(jogador)

        
        for i, jogador in enumerate(jogadores_baseada_probabilidade):
            
            jogador_selecionado = next((player for player in players if player.name == jogador.name), None)
            
            if jogador_selecionado:
                jogador_selecionado.kills = kills_distribution[i]
                jogador_selecionado.killstotal = jogador_selecionado.kills + jogador_selecionado.killstotal
                

        min_kills = 14
        max_kills = 25
        deaths_distribution = generate_random_values(total_losing_deathsp, len(losing_team.players), min_kills, max_kills, rounds)
        players = losing_team.players
        probabilidades = [
                0.15,  # Maior probabilidade para o índice 0
                0.15, # 0.32
                0.20, # 0.16
                0.20, # 0.07
                0.30  # Menor probabilidade para o índice 4
                ]
        # Criar uma lista ponderada com base nas probabilidades
        weighted_players = [player for player, weight in zip(players, probabilidades) for _ in range(int(weight * 100))]
        
        
        # Obter uma amostra sem reposição usando random.sample
        jogadores_baseada_probabilidade = []

        while len(jogadores_baseada_probabilidade) < 5:
            jogador = random.choice(weighted_players)
            if jogador not in jogadores_baseada_probabilidade:
                jogadores_baseada_probabilidade.append(jogador)

        

        for i, jogador in enumerate(jogadores_baseada_probabilidade):
            
            jogador_selecionado = next((player for player in players if player.name == jogador.name), None)
            
            if jogador_selecionado:
                jogador_selecionado.deaths = deaths_distribution[i]
                jogador_selecionado.deathstotal = jogador_selecionado.deathstotal + jogador_selecionado.deaths
                
            
        min_kills = 6
        max_kills = 28
        kills_distribution = generate_random_values(total_winning_killsp, len(losing_team.players), min_kills, max_kills, rounds)
        players = losing_team.players

        probabilidades = [
                0.40,  # Maior probabilidade para o índice 0
                0.30, # 0.32
                0.15, # 0.16
                0.10, # 0.07
                0.5  # Menor probabilidade para o índice 4
                ]

        # Criar uma lista ponderada com base nas probabilidades
        weighted_players = [player for player, weight in zip(players, probabilidades) for _ in range(int(weight * 100))]
        
        
        # Obter uma amostra sem reposição usando random.sample
        jogadores_baseada_probabilidade = []

        while len(jogadores_baseada_probabilidade) < 5:
            jogador = random.choice(weighted_players)
            if jogador not in jogadores_baseada_probabilidade:
                jogadores_baseada_probabilidade.append(jogador)

        

        for i, jogador in enumerate(jogadores_baseada_probabilidade):
            
            jogador_selecionado = next((player for player in players if player.name == jogador.name), None)
            
            if jogador_selecionado:
                jogador_selecionado.kills = kills_distribution[i]
                jogador_selecionado.killstotal = jogador_selecionado.kills + jogador_selecionado.killstotal
                
            
        min_kills = 10
        max_kills = 22
        deaths_distribution = generate_random_values(total_losing_deathsv, len(winning_team.players), min_kills, max_kills, rounds)
        players = winning_team.players
        probabilidades = [
                0.10,
                0.13,
                0.18,
                0.22,
                0.37
                ]

        # Criar uma lista ponderada com base nas probabilidades
        weighted_players = [player for player, weight in zip(players, probabilidades) for _ in range(int(weight * 100))]
        
        
        # Obter uma amostra sem reposição usando random.sample
        jogadores_baseada_probabilidade = []

        while len(jogadores_baseada_probabilidade) < 5:
            jogador = random.choice(weighted_players)
            if jogador not in jogadores_baseada_probabilidade:
                jogadores_baseada_probabilidade.append(jogador)

        

        for i, jogador in enumerate(jogadores_baseada_probabilidade):
            
            jogador_selecionado = next((player for player in players if player.name == jogador.name), None)
            
            if jogador_selecionado:
                jogador_selecionado.deaths = deaths_distribution[i]
                jogador_selecionado.deathstotal = jogador_selecionado.deathstotal + jogador_selecionado.deaths
            
    elif rounds >= 22 and rounds < 25:
        total_winning_killsv = random.randint(80, 95)
        total_losing_deathsp = total_winning_killsv
        total_winning_killsp = random.randint(60, total_winning_killsv - 7)
        total_losing_deathsv = total_winning_killsp
        total_winning_killsv = max(total_winning_killsv, 10)
        min_kills = 7
        max_kills = 29
        kills_distribution = generate_random_values(total_winning_killsv, len(winning_team.players), min_kills, max_kills, rounds)
        players = winning_team.players

        probabilidades = [
                0.40,  # Maior probabilidade para o índice 0
                0.30, # 0.32
                0.15, # 0.16
                0.10, # 0.07
                0.5  # Menor probabilidade para o índice 4
                ]

        # Criar uma lista ponderada com base nas probabilidades
        weighted_players = [player for player, weight in zip(players, probabilidades) for _ in range(int(weight * 100))]
        
        
        # Obter uma amostra sem reposição usando random.sample
        jogadores_baseada_probabilidade = []

        while len(jogadores_baseada_probabilidade) < 5:
            jogador = random.choice(weighted_players)
            if jogador not in jogadores_baseada_probabilidade:
                jogadores_baseada_probabilidade.append(jogador)

        
        
        for i, jogador in enumerate(jogadores_baseada_probabilidade):
            
            jogador_selecionado = next((player for player in players if player == jogador), None)
            
            if jogador_selecionado:
                jogador_selecionado.kills = kills_distribution[i]
                jogador_selecionado.killstotal = jogador_selecionado.kills + jogador_selecionado.killstotal
                
            
        min_kills = 8
        max_kills = 21
        deaths_distribution = generate_random_values(total_losing_deathsp, len(losing_team.players), min_kills, max_kills, rounds)
        players = losing_team.players
        probabilidades = [
                0.10,
                0.13,
                0.18,
                0.22,
                0.37
                ]

        # Criar uma lista ponderada com base nas probabilidades
        weighted_players = [player for player, weight in zip(players, probabilidades) for _ in range(int(weight * 100))]
        
        
        # Obter uma amostra sem reposição usando random.sample
        jogadores_baseada_probabilidade = []

        while len(jogadores_baseada_probabilidade) < 5:
            jogador = random.choice(weighted_players)
            if jogador not in jogadores_baseada_probabilidade:
                jogadores_baseada_probabilidade.append(jogador)

        

        for i, jogador in enumerate(jogadores_baseada_probabilidade):
            
            jogador_selecionado = next((player for player in players if player.name == jogador.name), None)
            
            if jogador_selecionado:
                jogador_selecionado.deaths = deaths_distribution[i]
                jogador_selecionado.deathstotal = jogador_selecionado.deathstotal + jogador_selecionado.deaths
                

        min_kills = 6
        max_kills = 26
        kills_distribution = generate_random_values(total_winning_killsp, len(losing_team.players), min_kills, max_kills, rounds)
        players = losing_team.players

        probabilidades = [
                0.40,  # Maior probabilidade para o índice 0
                0.30, # 0.32
                0.15, # 0.16
                0.10, # 0.07
                0.5  # Menor probabilidade para o índice 4
                ]

        # Criar uma lista ponderada com base nas probabilidades
        weighted_players = [player for player, weight in zip(players, probabilidades) for _ in range(int(weight * 100))]
        
        
        # Obter uma amostra sem reposição usando random.sample
        jogadores_baseada_probabilidade = []

        while len(jogadores_baseada_probabilidade) < 5:
            jogador = random.choice(weighted_players)
            if jogador not in jogadores_baseada_probabilidade:
                jogadores_baseada_probabilidade.append(jogador)

        
        
        for i, jogador in enumerate(jogadores_baseada_probabilidade):
            
            jogador_selecionado = next((player for player in players if player.name == jogador.name), None)
            
            if jogador_selecionado:
                jogador_selecionado.kills = kills_distribution[i]
                jogador_selecionado.killstotal = jogador_selecionado.kills + jogador_selecionado.killstotal
                

        # Distribuir deaths no time vencedor
        min_kills = 7
        max_kills = 19
        deaths_distribution = generate_random_values(total_losing_deathsv, len(winning_team.players), min_kills, max_kills, rounds)
        players = winning_team.players
        probabilidades = [
                0.10,
                0.13,
                0.18,
                0.22,
                0.37
                ]

        # Criar uma lista ponderada com base nas probabilidades
        weighted_players = [player for player, weight in zip(players, probabilidades) for _ in range(int(weight * 100))]
        
        
        # Obter uma amostra sem reposição usando random.sample
        jogadores_baseada_probabilidade = []

        while len(jogadores_baseada_probabilidade) < 5:
            jogador = random.choice(weighted_players)
            if jogador not in jogadores_baseada_probabilidade:
                jogadores_baseada_probabilidade.append(jogador)

        

        for i, jogador in enumerate(jogadores_baseada_probabilidade):
            
            jogador_selecionado = next((player for player in players if player.name == jogador.name), None)
            
            if jogador_selecionado:
                jogador_selecionado.deaths = deaths_distribution[i]
                jogador_selecionado.deathstotal = jogador_selecionado.deathstotal + jogador_selecionado.deaths
                
            
    elif rounds >= 14 and rounds < 22:
        total_winning_killsv = random.randint(65, 70)
        total_losing_deathsp = total_winning_killsv
        total_winning_killsp = random.randint(35, total_winning_killsv - 8)
        total_losing_deathsv = total_winning_killsp
        total_winning_killsv = max(total_winning_killsv, 10)
        min_kills = 6
        max_kills = 22
        # Distribuir kills no time vencedor
        kills_distribution = generate_random_values(total_winning_killsv, len(winning_team.players), min_kills, max_kills, rounds)
        players = winning_team.players

        probabilidades = [
                0.40,  # Maior probabilidade para o índice 0
                0.30, # 0.32
                0.15, # 0.16
                0.10, # 0.07
                0.5  # Menor probabilidade para o índice 4
                ]

        # Criar uma lista ponderada com base nas probabilidades
        weighted_players = [player for player, weight in zip(players, probabilidades) for _ in range(int(weight * 100))]
        
        
        # Obter uma amostra sem reposição usando random.sample
        jogadores_baseada_probabilidade = []

        while len(jogadores_baseada_probabilidade) < 5:
            jogador = random.choice(weighted_players)
            if jogador not in jogadores_baseada_probabilidade:
                jogadores_baseada_probabilidade.append(jogador)

        
        
        for i, jogador in enumerate(jogadores_baseada_probabilidade):
            
            jogador_selecionado = next((player for player in players if player.name == jogador.name), None)
            
            if jogador_selecionado:
                jogador_selecionado.kills = kills_distribution[i]
                jogador_selecionado.killstotal = jogador_selecionado.kills + jogador_selecionado.killstotal
                
            
        min_kills = 8
        max_kills = 16
        deaths_distribution = generate_random_values(total_losing_deathsp, len(losing_team.players), min_kills, max_kills, rounds)
        players = losing_team.players
        probabilidades = [
                0.10,
                0.13,
                0.18,
                0.22,
                0.37
                ]

        # Criar uma lista ponderada com base nas probabilidades
        weighted_players = [player for player, weight in zip(players, probabilidades) for _ in range(int(weight * 100))]
        
        
        # Obter uma amostra sem reposição usando random.sample
        jogadores_baseada_probabilidade = []

        while len(jogadores_baseada_probabilidade) < 5:
            jogador = random.choice(weighted_players)
            if jogador not in jogadores_baseada_probabilidade:
                jogadores_baseada_probabilidade.append(jogador)

        

        for i, jogador in enumerate(jogadores_baseada_probabilidade):
            
            jogador_selecionado = next((player for player in players if player.name == jogador.name), None)
            
            if jogador_selecionado:
                jogador_selecionado.deaths = deaths_distribution[i]
                jogador_selecionado.deathstotal = jogador_selecionado.deathstotal + jogador_selecionado.deaths
                
            
        min_kills = 3
        max_kills = 17
        kills_distribution = generate_random_values(total_winning_killsp, len(losing_team.players), min_kills, max_kills, rounds)
        players = losing_team.players

        probabilidades = [
                0.40,  # Maior probabilidade para o índice 0
                0.30, # 0.32
                0.15, # 0.16
                0.10, # 0.07
                0.5  # Menor probabilidade para o índice 4
                ]

        # Criar uma lista ponderada com base nas probabilidades
        weighted_players = [player for player, weight in zip(players, probabilidades) for _ in range(int(weight * 100))]
        
        
        # Obter uma amostra sem reposição usando random.sample
        jogadores_baseada_probabilidade = []

        while len(jogadores_baseada_probabilidade) < 5:
            jogador = random.choice(weighted_players)
            if jogador not in jogadores_baseada_probabilidade:
                jogadores_baseada_probabilidade.append(jogador)

        

        for i, jogador in enumerate(jogadores_baseada_probabilidade):
            
            jogador_selecionado = next((player for player in players if player.name == jogador.name), None)
            
            if jogador_selecionado:
                jogador_selecionado.kills = kills_distribution[i]
                jogador_selecionado.killstotal = jogador_selecionado.kills + jogador_selecionado.killstotal
                
            
        min_kills = 4
        max_kills = 16
        deaths_distribution = generate_random_values(total_losing_deathsv, len(winning_team.players), min_kills, max_kills, rounds)
        players = winning_team.players
        probabilidades = [
                0.10,
                0.13,
                0.18,
                0.22,
                0.37
                ]

        # Criar uma lista ponderada com base nas probabilidades
        weighted_players = [player for player, weight in zip(players, probabilidades) for _ in range(int(weight * 100))]
        
        
        # Obter uma amostra sem reposição usando random.sample
        jogadores_baseada_probabilidade = []

        while len(jogadores_baseada_probabilidade) < 5:
            jogador = random.choice(weighted_players)
            if jogador not in jogadores_baseada_probabilidade:
                jogadores_baseada_probabilidade.append(jogador)

        

        for i, jogador in enumerate(jogadores_baseada_probabilidade):
            
            jogador_selecionado = next((player for player in players if player.name == jogador.name), None)
            
            if jogador_selecionado:
                jogador_selecionado.deaths = deaths_distribution[i]
                jogador_selecionado.deathstotal = jogador_selecionado.deathstotal + jogador_selecionado.deaths
                
            
def generate_random_values(total_value, num_players, min_kills, max_kills, rounds):
    values = []
    guardandoovalortotal = total_value
    while total_value >= 0 and num_players >=1:
        if total_value < min_kills:
            values.clear()
            values = []
            num_players = 5
            total_value = guardandoovalortotal
        value = random.randint(min_kills, min(total_value, max_kills))
        if num_players == 1 and total_value <= max_kills:
            value = total_value
        elif num_players == 1 and total_value > max_kills:
            values.clear()
            values = []
            num_players = 5
            total_value = guardandoovalortotal
            value = random.randint(min_kills, min(total_value, max_kills))
        elif num_players == 2 and total_value <= max_kills:
            total_value = guardandoovalortotal
            values.clear()
            value = random.randint(min_kills, min(total_value, max_kills))
            values = []
            num_players = 5
        values.append(value)
        total_value -= value
        num_players -= 1
        for value in values:
            if value > max_kills:
                total_value = guardandoovalortotal
                num_players = 5
    values.sort(reverse=True)
    return values

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
    o_plano_players = {
    "Kng": (86, 75, 79),
    "Vsm": (86, 74, 77),
    "Leo Drk": (80, 82, 85),
    "Trk": (78, 73, 85),
    "Lucas1": (70, 80, 75)}
    o_plano_tactic_preferences = {
        "Retake": 40.0,
        "Domínio": 36.0,
        "Rush": 50.0,
        "FK": 45.0,
        "Execute": 38.0,
        "Bait": 42.0
    }
    o_plano_map_preferences = {
        "Overpass": 30.0,
        "Mirage": 30.0,
        "Inferno": 16.0,
        "Nuke": 35.0,
        "Vertigo": 26.0,
        "Ancient": 29.0,
        "Anubis": 22.0
    }
    o_plano_team = create_team("O Plano", o_plano_players, o_plano_tactic_preferences, o_plano_map_preferences)

    furia_players = {
    "Kscerato": (93, 71, 81),
    "Yuurih": (90, 79, 78),
    "Chelo": (86, 71, 74),
    "Art": (85, 82, 83),
    "Fallen": (79, 94, 90)}
    furia_tactic_preferences = {
        "Retake": 50.0,
        "Domínio": 40.0,
        "Rush": 42.0,
        "FK": 33.0,
        "Execute": 46.0,
        "Bait": 37.0
    }
    furia_map_preferences = {
        "Overpass": 30.0,
        "Mirage": 30.0,
        "Inferno": 26.0,
        "Nuke": 30.0,
        "Vertigo": 28.0,
        "Ancient": 24.0,
        "Anubis": 22.1
    }
    furia_team = create_team("Furia", furia_players, furia_tactic_preferences, furia_map_preferences)

    mibr_players = {
    "Insani": (87, 76, 73),
    "Brnz4n": (87, 80, 79),
    "Saffee": (84, 77, 74),
    "Exit": (74, 84, 81),
    "Drop": (72, 88, 83)}
    mibr_tactic_preferences = {
        "Retake": 38.0,
        "Domínio": 30.0,
        "Rush": 44.0,
        "FK": 48.0,
        "Execute": 39.0,
        "Bait": 41.0
    }
    mibr_map_preferences = {
        "Overpass": 24.9,
        "Mirage": 25.2,
        "Inferno": 12.9,
        "Nuke": 28.8,
        "Vertigo": 31.1,
        "Ancient": 24.0,
        "Anubis": 30.0
    }
    mibr_team = create_team("Mibr", mibr_players, mibr_tactic_preferences, mibr_map_preferences)
    
    Imperial_players = {
    "Noway": (83, 71, 62),
    "Hen1": (83, 75, 72),
    "Boltz": (81, 85, 79),
    "Felps": (80, 80, 74),
    "Vini": (78, 86, 83)}
    Imperial_tactic_preferences = {
        "Retake": 41.0,
        "Domínio": 44.0,
        "Rush": 41.0,
        "FK": 48.0,
        "Execute": 35.0,
        "Bait": 30.0
    }
    Imperial_map_preferences = {
        "Overpass": 25.9,
        "Mirage": 20.2,
        "Inferno": 30.9,
        "Nuke": 21.8,
        "Vertigo": 28.1,
        "Ancient": 15.0,
        "Anubis": 30.0
    }
    imperial_team = create_team("Imperial", Imperial_players, Imperial_tactic_preferences, Imperial_map_preferences)

    pain_players = {
    "Skullz": (88, 75, 73),
    "Kauez": (84, 71, 73),
    "Cass1n": (82, 80, 79),
    "Lux": (82, 86, 76),
    "Biguzera": (77, 83, 88)}
    pain_tactic_preferences = {
        "Retake": 45.0,
        "Domínio": 39.0,
        "Rush": 37.0,
        "FK": 33.0,
        "Execute": 52.0,
        "Bait": 39.0
    }
    pain_map_preferences = {
        "Overpass": 25.9,
        "Mirage": 12.2,
        "Inferno": 25.9,
        "Nuke": 34.8,
        "Vertigo": 23.1,
        "Ancient": 29.0,
        "Anubis": 29.0
    }
    pain_team = create_team("Pain", pain_players, pain_tactic_preferences, pain_map_preferences)
    
    Mongolz_players = {
    "Blitz": (84, 77, 75),
    "Techno": (83, 81, 75),
    "Bart4k": (78, 75, 82),
    "Hasteka": (77, 83, 75),
    "Annihilation": (77, 74, 72)}
    Mongolz_tactic_preferences = {
        "Retake": 45.0,
        "Domínio": 39.0,
        "Rush": 37.0,
        "FK": 33.0,
        "Execute": 52.0,
        "Bait": 39.0
    }
    Mongolz_map_preferences = {
        "Overpass": 21.9,
        "Mirage": 24.2,
        "Inferno": 38.9,
        "Nuke": 24.8,
        "Vertigo": 33.1,
        "Ancient": 27.0,
        "Anubis": 24.0
    }
    mongolz_team = create_team("Mongolz", Mongolz_players, Mongolz_tactic_preferences, Mongolz_map_preferences)
    
    Grayhound_players= {
    "Vexite": (82, 81, 75),
    "Liazz": (82, 83, 75),
    "INS": (81, 76, 80),
    "Sico": (75, 73, 82),
    "AliStair": (72, 77, 72)}
    Grayhound_tactic_preferences = {
        "Retake": 35.0,
        "Domínio": 42.0,
        "Rush": 32.0,
        "FK": 37.0,
        "Execute": 32.0,
        "Bait": 45.0
    }
    Grayhound_map_preferences = {
        "Overpass": 29.9,
        "Mirage": 24.2,
        "Inferno": 38.9,
        "Nuke": 31.8,
        "Vertigo": 24.1,
        "Ancient": 23.0,
        "Anubis": 19.0
    }
    grayhound_team = create_team("Grayhound", Grayhound_players, Grayhound_tactic_preferences, Grayhound_map_preferences)
    
    Nip_players = {
    "Brollan": (86, 79, 75),
    "Headtrick": (85, 73, 69),
    "Konfig": (84, 71, 80),
    "Rez": (80, 76, 79),
    "Hampus": (79, 82, 82)}
    Nip_tactic_preferences = {
        "Retake": 41.0,
        "Domínio": 34.0,
        "Rush": 52.0,
        "FK": 36.0,
        "Execute": 50.0,
        "Bait": 31.0
    }
    Nip_map_preferences = {
        "Overpass": 14.7,
        "Mirage": 31.0,
        "Inferno": 29.2,
        "Nuke": 28.1,
        "Vertigo": 25.8,
        "Ancient": 31.1,
        "Anubis": 26.0
    }
    nip_team = create_team("Nip", Nip_players, Nip_tactic_preferences, Nip_map_preferences)
    
    Complexity_players= {
    "Grim": (85, 78, 73),
    "Floppy": (80, 84, 79),
    "Fang": (79, 84, 74),
    "Hallzerk": (79, 74, 77),
    "JT": (74, 80, 83)}
    Complexity_tactic_preferences = {
        "Retake": 41.0,
        "Domínio": 44.0,
        "Rush": 41.0,
        "FK": 48.0,
        "Execute": 35.0,
        "Bait": 30.0
    }
    Complexity_map_preferences = {
        "Overpass": 29.9,
        "Mirage": 19.2,
        "Inferno": 28.9,
        "Nuke": 26.8,
        "Vertigo": 32.1,
        "Ancient": 24.0,
        "Anubis": 25.0
    }
    complexity_team = create_team("Complexity", Complexity_players, Complexity_tactic_preferences, Complexity_map_preferences)

    Gamerlegion_players = {
    "iM": (86, 80, 73),
    "Keoz": (82, 75, 72),
    "Siuhy": (82, 83, 87),
    "Acor": (80, 81, 79),
    "Isak": (76, 80, 74)}
    Gamerlegion_tactic_preferences = {
        "Retake": 43.0,
        "Domínio": 38.0,
        "Rush": 42.0,
        "FK": 41.0,
        "Execute": 39.0,
        "Bait": 36.0
    }
    Gamerlegion_map_preferences = {
        "Overpass": 14.7,
        "Mirage": 29.0,
        "Inferno": 24.2,
        "Nuke": 30.1,
        "Vertigo": 29.8,
        "Ancient": 24.1,
        "Anubis": 32.0
    }
    gamerlegion_team = create_team("Gamerlegion", Gamerlegion_players, Gamerlegion_tactic_preferences, Gamerlegion_map_preferences)
    

    g2_players = {
    "Niko": (95, 81, 80),
    "Monesy": (92, 70, 72),
    "Hunter": (85, 78, 76),
    "Jks": (80, 81, 74),
    "Hooxi": (65, 86, 90)}
    g2_tactic_preferences = {
        "Retake": 41.0,
        "Domínio": 34.0,
        "Rush": 52.0,
        "FK": 36.0,
        "Execute": 50.0,
        "Bait": 31.0
    }
    g2_map_preferences = {
        "Overpass": 14.7,
        "Mirage": 31.0,
        "Inferno": 29.2,
        "Nuke": 28.1,
        "Vertigo": 25.8,
        "Ancient": 31.1,
        "Anubis": 26.0
    }
    g2_team = create_team("G2", g2_players, g2_tactic_preferences, g2_map_preferences)
    
    liquid_players = {
    "Yekindar": (90, 74, 83),
    "Elige": (88, 79, 80),
    "Naf": (87, 91, 81),
    "Osee": (76, 75, 73),
    "Nitro": (61, 83, 84),}
    liquid_tactic_preferences = {
        "Retake": 43.0,
        "Domínio": 41.0,
        "Rush": 46.0,
        "FK": 32.0,
        "Execute": 38.0,
        "Bait": 35.0
    }
    liquid_map_preferences = {
        "Overpass": 27.9,
        "Mirage": 30.1,
        "Inferno": 30.2,
        "Nuke": 26.0,
        "Vertigo": 12.0,
        "Ancient": 24.9,
        "Anubis": 24.8
    }
    liquid_team = create_team("Liquid", liquid_players, liquid_tactic_preferences, liquid_map_preferences)

    navi_players = {
    "Simple": (95, 75, 85),
    "Bit": (87, 79, 80),
    "Electronic": (86, 61, 82),
    "Perfecto": (74, 94, 81),
    "Boombl4": (67, 82, 93),}
    navi_tactic_preferences = {
        "Retake": 46.0,
        "Domínio": 40.0,
        "Rush": 48.0,
        "FK": 30.0,
        "Execute": 42.0,
        "Bait": 34.0
    }
    navi_map_preferences = {
        "Overpass": 27.2,
        "Mirage": 25.1,
        "Inferno": 25.0,
        "Nuke": 29.9,
        "Vertigo": 11.1,
        "Ancient": 27.2,
        "Anubis": 31.0
    }
    navi_team = create_team("Navi", navi_players, navi_tactic_preferences, navi_map_preferences)
    
    faze_players = {
    "Ropz": (90, 73, 78),
    "Twistzz": (89, 85, 75),
    "Broky": (89, 77, 73),
    "Rain": (82, 89, 79),
    "Karrigan": (62, 89, 96)}
    faze_tactic_preferences = {
        "Retake": 45.0,
        "Domínio": 42.0,
        "Rush": 47.0,
        "FK": 31.0,
        "Execute": 37.0,
        "Bait": 33.0
    }
    faze_map_preferences = {
        "Overpass": 24.1,
        "Mirage": 29.0,
        "Inferno": 29.2,
        "Nuke": 26.9,
        "Vertigo": 12.1,
        "Ancient": 31.8,
        "Anubis": 23.0
    }
    faze_team = create_team("Faze", faze_players, faze_tactic_preferences, faze_map_preferences)

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

    teams = [furia_team, mibr_team, imperial_team, pain_team, mongolz_team, grayhound_team, nip_team, complexity_team, gamerlegion_team, g2_team, liquid_team, navi_team, heroic_team, faze_team, vitality_team, o_plano_team]
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