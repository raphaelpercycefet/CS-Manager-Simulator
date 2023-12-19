from Funcoes_Times_ManagerDeCS import creating_teams_players

txtTime1 = "o pLAno"
txtTime2 = "{^{:>^>"

def submit(txtTime1, txtTime2):
    
    teams, maps, tactics = creating_teams_players()
    
    time1_nome = txtTime1
    time2_nome = txtTime2
    
    team1 = None
    team2 = None
    
    for team in teams:
        
        if team.name == time1_nome.title():
            team1 = team
        elif team.name == time2_nome.title():
            team2 = team
        else:
            pass
            
    if team1 is None:
        txtTime1 = None
        
    assert team1.name == "O Plano"
    
    if team2 is None:
        txtTime2 = None
    
    assert txtTime2 == None

submit (txtTime1, txtTime2)