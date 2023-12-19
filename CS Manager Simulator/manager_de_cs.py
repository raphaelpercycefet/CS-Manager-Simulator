import sys
import copy  # Importe a biblioteca copy para usar o deepcopy
from rich import print
from rich.console import Console
from ClassesManagerDeCS import Match
from Funcoes_Times_ManagerDeCS import update_player_stats, creating_teams_players
import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.patheffects import withStroke
import mysql.connector
import random
import csv
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from pathlib import Path

database = {
    "host": "localhost",
    "user": "root",
    "database": "CSPYTHON4"
}

conn = mysql.connector.connect(**database)
console = Console()
print(sys.version)
def toggle_fullscreen(Pagina):
        Pagina.attributes('-fullscreen', not Pagina.attributes('-fullscreen')) # Coloca em Tela Cheia se não estiver

def Abrir_Pagina_Inicial():
    Pagina_Inicial = tk.Tk()
    Pagina_Inicial.title("Página Inicial")
 
    lbl_começar_font = ("Dotum", 20)
    lbl_começar = tk.Label(Pagina_Inicial, text= "Simulador de Manager de CS por Raphael Percy", bg= "azure1", height= 5, font= lbl_começar_font)
    btn_comecar_font = ("Dotum", 20)
    btn_começar = tk.Button(Pagina_Inicial, text= "Começar", width= 12, height= 3, bg= "khaki2", fg= "black", font= btn_comecar_font, command = lambda : Abrir_Pagina_Escolha_Time(Pagina_Inicial)) # Lambda para que só seja executada a função quando o botão for clicado

    btn_começar.place(relx=0.5, rely=0.5, anchor=CENTER)
    lbl_começar.place(relx=0, rely=0, anchor=N)
    lbl_começar.pack(side="top", fill="x")
        
    Pagina_Inicial.configure(bg="darkgoldenrod")
        
    Pagina_Inicial.after(0, toggle_fullscreen, Pagina_Inicial)
    
    Pagina_Inicial.mainloop()
    

def Abrir_Pagina_Escolha_Time(Pagina_Escolha_Modo):
    Pagina_Escolha_Time = tk.Tk()
    Pagina_Escolha_Time.title("Escolha de Time")
    
    teams, maps, tactics = creating_teams_players()
    
    frm = tk.Frame(Pagina_Escolha_Time)
    frm.grid()
    frm.configure(bg="azure1")
    
    Pagina_Escolha_Time.configure(bg="darkgoldenrod")
    
    lbl_começar_font = ("Dotum", 18)
    lbl_começar = tk.Label(Pagina_Escolha_Time, text= "Times Disponíveis:", bg= "azure1", height=2, font= lbl_começar_font)
    
    column = []
    header_text = ['Times']
    
    for i, team in enumerate(teams):
        
        column.append(tk.Label(frm, text= team.name, bg= "azure1", font= lbl_começar_font))
        column[i].grid()
    
    frm.place(relx=0.5, rely=0.32, anchor= CENTER)
    lbl_começar.place(relx=0, rely=0, anchor= N)
    lbl_começar.pack(side= "top", fill= "x")
    
    lbl_times_font = ("Dotum", 16)
    
    lbl_time1 = tk.Label(Pagina_Escolha_Time, text= "Seu Time:", bg= "azure1", height=2, font= lbl_times_font)
    lbl_time2 = tk.Label(Pagina_Escolha_Time, text= "Time da CPU:", bg= "azure1", height=2, font= lbl_times_font)
    lbl_manager = tk.Label(Pagina_Escolha_Time, text= "Nome do Usuario:", bg= "azure1", height=2, font= lbl_times_font)
    
    txtTime1 = tk.Entry(Pagina_Escolha_Time, textvariable= tk.StringVar(), font= lbl_times_font)
    txtTime2 = tk.Entry(Pagina_Escolha_Time, textvariable= tk.StringVar(), font= lbl_times_font)
    txtmanager = tk.Entry(Pagina_Escolha_Time, textvariable= tk.StringVar(), font= lbl_times_font)
    
    btn_subTimes_font = ("Dotum", 14)
    btn_subTimes = tk.Button(Pagina_Escolha_Time, width= 10, height= 4, text= 'Confirmar', font= btn_subTimes_font, command=lambda: submit(txtTime1, txtTime2, txtmanager, Pagina_Escolha_Time))
    
    lbl_time1.place(relx=0.5, rely=0.60, anchor= CENTER)
    lbl_time2.place(relx=0.5, rely=0.70, anchor= CENTER)
    lbl_manager.place(relx=0.5, rely=0.80, anchor= CENTER)
     
    txtTime1.place(relx=0.5, rely=0.65, anchor= CENTER)
    txtTime2.place(relx=0.5, rely=0.75, anchor= CENTER)
    txtmanager.place(relx=0.5, rely=0.85, anchor= CENTER) 
    
    btn_subTimes.place(relx=0.5, rely=0.94, anchor= CENTER)
    
    def submit(txtTime1, txtTime2, txtmanager, Pagina_Escolha_Time):
        
        teams, maps, tactics = creating_teams_players()
        
        time1_nome = txtTime1.get()
        time2_nome = txtTime2.get()
        usuario = txtmanager.get()
        
        team1 = None
        team2 = None
        
        for team in teams:
            
            if team.name == time1_nome.title():
                team1 = team
            elif team.name == time2_nome.title():
                team2 = team
                
        if team1 is None:
            
            messagebox.showerror(title="Escolha de Times", message="Escolha os times com base nos times na lista apresentada.")
            txtTime1.delete(0, tk.END)
            
            return 0
        
        elif team2 is None:
            
            messagebox.showerror(title="Escolha de Times", message="Escolha os times com base nos times na lista apresentada.")
            txtTime2.delete(0, tk.END)
            
            return 0
        
        elif not str(usuario):

            messagebox.showerror(title="Nome de Usuário", message="Escreva apenas letras no nome de usuário.")
            txtmanager.delete(0, tk.END)
            
            return 0   
        
        else:
            
            return Abrir_Pagina_Vetos(team1, team2, usuario, Pagina_Escolha_Time)

    if Pagina_Escolha_Modo == "Sem":
        pass
    
    else:
        Pagina_Escolha_Modo.destroy()
    
    Pagina_Escolha_Time.after(0, toggle_fullscreen, Pagina_Escolha_Time)
    Pagina_Escolha_Time.mainloop()

def Abrir_Pagina_Vetos(team1, team2, usuario, Pagina_Escolha_Time):
    Pagina_Vetos = tk.Tk()
    Pagina_Vetos.title("Escolha de Time")
    
    teams, maps, tactics = creating_teams_players()
    
    mapas_restantes = maps
    mapas_do_jogo = []
    
    Pagina_Vetos.configure(bg="darkgoldenrod")
    
    
    lbl_top_font = ("Dotum", 16)
    lbl_top = tk.Label(Pagina_Vetos, text= "Escolha um Mapa para BANIR:", bg= "tomato3", height= 2, font= lbl_top_font)

    lbl_top.place(relx=0, rely=0, anchor= N)
    lbl_top.pack(side= "top", fill= "x")
    
    btn_font = ("Dotum", 18)
    
    lbl_banners = ("Dotum", 17)
    
    btn_mirage = tk.Button(Pagina_Vetos, text= "Mirage", width=20, height=7, font= btn_font, command=lambda: changeColor(btn_mirage, "Mirage", mapas_restantes, mapas_do_jogo, team1, team2, usuario, Pagina_Vetos, lbl_banners))
    btn_anubis = tk.Button(Pagina_Vetos, text= "Anubis", width=20, height=7, font= btn_font, command=lambda: changeColor(btn_anubis, "Anubis", mapas_restantes, mapas_do_jogo, team1, team2, usuario, Pagina_Vetos, lbl_banners))
    btn_ancient = tk.Button(Pagina_Vetos, text= "Ancient", width=20, height=7, font= btn_font, command=lambda: changeColor(btn_ancient, "Ancient", mapas_restantes, mapas_do_jogo, team1, team2, usuario, Pagina_Vetos, lbl_banners))
    btn_inferno = tk.Button(Pagina_Vetos, text= "Inferno", width=20, height=7, font= btn_font, command=lambda: changeColor(btn_inferno, "Inferno", mapas_restantes, mapas_do_jogo, team1, team2, usuario, Pagina_Vetos, lbl_banners))
    btn_overpass = tk.Button(Pagina_Vetos, text= "Overpass", width=20, height=7, font= btn_font,command=lambda: changeColor(btn_overpass, "Overpass", mapas_restantes, mapas_do_jogo, team1, team2, usuario, Pagina_Vetos, lbl_banners))
    btn_nuke = tk.Button(Pagina_Vetos, text= "Nuke", width=20, height=7, font= btn_font, command=lambda: changeColor(btn_nuke, "Nuke", mapas_restantes, mapas_do_jogo, team1, team2, usuario, Pagina_Vetos, lbl_banners))
    btn_vertigo = tk.Button(Pagina_Vetos, text= "Vertigo", width=20, height=7, font= btn_font,command=lambda: changeColor(btn_vertigo, "Vertigo", mapas_restantes, mapas_do_jogo, team1, team2, usuario, Pagina_Vetos, lbl_banners))
    
    btn_mirage.place(relx=0.2, rely=0.17, anchor= CENTER)
    btn_overpass.place(relx=0.5, rely=0.17, anchor= CENTER)
    btn_inferno.place(relx=0.8, rely=0.17, anchor= CENTER)
    btn_nuke.place(relx=0.15, rely=0.40, anchor= CENTER)
    btn_vertigo.place(relx=0.40, rely=0.40, anchor= CENTER)
    btn_ancient.place(relx=0.60, rely=0.40, anchor= CENTER)
    btn_anubis.place(relx=0.85, rely=0.40, anchor= CENTER)

    def changeColor(button, mapa, mapas_restantes, mapas_do_jogo, team1, team2, usuario, Pagina_Vetos, lbl_banners):
        
        if button.cget("bg") == "mediumpurple1" or len(mapas_restantes) == 0:
            
            messagebox.showerror(title="Veto", message = "O processo de vetar mapas já acabou, prossiga quando quiser.")
            return 0
        
        elif button.cget("bg") == "tomato3" or button.cget("bg") == "mediumseagreen":
            
            messagebox.showerror(title="Veto", message = "Este Mapa já foi escolhido ou banido, tente outro.")
            return 0

        
        else:
            
            verificador = "x"
            
            if len(mapas_restantes) == 6:
                lbl_top.config(text="Escolha um Mapa para PICKAR", bg="mediumseagreen")
                
            elif len(mapas_restantes) == 4:
                    lbl_top.config(text="Escolha um Mapa para BANIR", bg="mediumseagreen")
            else:
                pass
            
            if len(mapas_restantes) == 5:
                verificador = "pick"
                
            elif len(mapas_restantes) == 1:
                verificador = "decider"
                
            else:
                verificador = "ban"
            
            
            if verificador == "ban":
                
                button.configure(bg="tomato3")
                mapas_restantes.remove(mapa)
                return loop(mapas_restantes, mapas_do_jogo, team1, team2, usuario, Pagina_Vetos, lbl_banners)

            elif verificador == "pick":
                
                button.configure(bg="mediumseagreen")
                mapas_restantes.remove(mapa)
                mapas_do_jogo.append(mapa)
                return loop(mapas_restantes, mapas_do_jogo, team1, team2, usuario, Pagina_Vetos, lbl_banners)
            
            elif verificador == "decider":
                
                button.configure(bg="mediumpurple1")
                mapas_restantes.remove(mapa)
                mapas_do_jogo.append(mapa)
                return loop(mapas_restantes, mapas_do_jogo, team1, team2, usuario, Pagina_Vetos, lbl_banners)
            
            else:
                pass
                sys.exit()
            
    
    def loop (mapas_restantes, mapas_do_jogo, team1, team2, usuario, Pagina_Vetos, lbl_banners):
        
        buttons_by_map = {
            "Mirage": btn_mirage,
            "Anubis": btn_anubis,
            "Ancient": btn_ancient,
            "Inferno": btn_inferno,
            "Overpass": btn_overpass,
            "Nuke": btn_nuke,
            "Vertigo": btn_vertigo,
            }
    
        while len(mapas_restantes) < 7:         
            
            while len(mapas_restantes) == 6:
                
                maps_cpu = dict(sorted(team2.map_preferences.items(), key=lambda x: x[1], reverse=False))
                find_map = False
            
                while not find_map:
                
                    find_map = False
                    
                    for map in maps_cpu:
                        
                        if map in mapas_restantes:
                            
                            mapas_restantes.remove(map)
                            
                            button = buttons_by_map.get(map)
                            button.configure(bg="tomato3")
                            
                            lbl_cpu_ban1 = tk.Label(Pagina_Vetos, text= f"{team2.name} Baniu: {map}", bg= "tomato3", height= 2, font= lbl_banners)
                            lbl_cpu_ban1.place(relx=0.5, rely=0.55, anchor= CENTER, relwidth=1.0)
                            
                            find_map = True
                            
                            lbl_top.config(text="Escolha um Mapa para PICKAR", bg="mediumseagreen")
                            
                            break # Quebra o For apenas
                            
                    if not find_map:
                        
                        find_map = True
                        
                return mapas_restantes, mapas_do_jogo
            
                break
                    
            while len(mapas_restantes) == 5: # Usuario Picka um Mapa
        
                break
                
            while len(mapas_restantes) == 4: # Cpu Bane um Mapa
                
                maps_cpu = dict(sorted(team2.map_preferences.items(), key=lambda x: x[1], reverse=True)) # CPU Pickar um Mapa
                find_map = False
                
                while not find_map:
                    
                    find_map = False
                    
                    for map_pick_adv in maps_cpu:
                        if map_pick_adv in mapas_restantes:
                            
                            mapas_do_jogo.append(map_pick_adv)
                            mapas_restantes.remove(map_pick_adv)
                            
                            button = buttons_by_map.get(map_pick_adv)
                            button.configure(bg="mediumseagreen")
                            
                            lbl_cpu_pick = tk.Label(Pagina_Vetos, text= f"{team2.name} Pickou: {map_pick_adv}", bg= "mediumseagreen", height= 2, font= lbl_banners)
                            lbl_cpu_pick.place(relx=0.5, rely=0.62, anchor= CENTER, relwidth=1.0)
                            
                            find_map = True

                            lbl_top.config(text="Escolha um Mapa para BANIR", bg="tomato3")
                            
                            break # Quebra o For apenas
                            
                    if not find_map:
                        
                        find_map = True
                        
                return mapas_restantes, mapas_do_jogo
            
                break
            
            while len(mapas_restantes) == 3: # Usuario Bane um Mapa 
            
                break
            
            while len(mapas_restantes) == 2: # CPU Bane um Mapa
                
                maps_cpu = dict(sorted(team2.map_preferences.items(), key=lambda x: x[1], reverse=False))
                find_map = False
            
                while not find_map:
                    
                    find_map = False
                    
                    for map in maps_cpu:
                        
                        if map in mapas_restantes:
                            
                            mapas_restantes.remove(map)
                            button = buttons_by_map.get(map)
                            button.configure(bg="tomato3")
                            
                            lbl_cpu_ban2 = tk.Label(Pagina_Vetos, text= f"{team2.name} Baniu: {map}", bg= "tomato3", height= 2, font= lbl_banners)
                            lbl_cpu_ban2.place(relx=0.5, rely=0.69, anchor= CENTER, relwidth=1.0)
                            
                            find_map = True
                            
                            map_decider = mapas_restantes[0]
                            mapas_do_jogo.append(map_decider)
                            mapas_restantes.remove(map_decider)
                            
                            button = buttons_by_map.get(map_decider)
                            button.configure(bg="mediumpurple1")
                            
                            lbl_top.config(text="Boa Sorte!!!!!", bg="mediumpurple1")               
                            
                            lbl_mapas_jogo_font = ("Dotum", 22)
                            lbl_mapas_jogo = tk.Label(Pagina_Vetos, text= f"Mapas do confronto em ordem: {', '.join(mapas_do_jogo)}", bg= "mediumpurple1", height= 3, font= lbl_mapas_jogo_font)
                            lbl_mapas_jogo.place(relx=0.5, rely=0.78, anchor= CENTER, relwidth=1.0)
                            
                            btn_confirmar = tk.Button(Pagina_Vetos, text= "Confirmar", width=10, height=4, font= btn_font, bg= "deepskyblue2", command=lambda: submit(mapas_do_jogo, team1, team2, usuario, Pagina_Vetos))
                            btn_confirmar.place(relx=0.50, rely=0.97, anchor= S)
                            
                            break # Quebra o For apenas
                            
                    if not find_map:
                        
                        find_map = True

                return mapas_restantes, mapas_do_jogo
            
                break
            
            if len(mapas_restantes) == 1:
                
                break
            
    def submit(mapas_do_jogo, team1, team2, usuario, Pagina_Vetos):
        
        if len(mapas_do_jogo) != 3:
            
            del mapas_do_jogo
            
            return Abrir_Pagina_Vetos(team1, team2, "Sem")
        
        else:
            
            mapa = mapas_do_jogo[0]

            return Abrir_Pagina_Taticas_Pontos_Fortes_Simulação(team1, team2, usuario, Pagina_Vetos, mapa, mapas_do_jogo, "Sem", 0, 0, "Sem")
            
    if Pagina_Escolha_Time == "Sem":
        
        pass
        
    else:
        
        Pagina_Escolha_Time.destroy()
    
    Pagina_Vetos.after(0, toggle_fullscreen, Pagina_Vetos)
    Pagina_Vetos.mainloop()
    

def Abrir_Pagina_Taticas_Pontos_Fortes_Simulação(team1, team2, usuario, Pagina_Vetos, mapa, mapas_do_jogo, mapas_results, team1_wins, team2_wins, Pagina_Resultado_Mapa):
    PTPFSM2 = tk.Tk()
    PTPFSM2.title("Pontos e Táticas")

    def changeColor_2(PTPFSM2, button, nome_tatica_ponto, verificador_ponto_tatica, verificador_lado):
        
            if verificador_ponto_tatica == "Tatica":
                
                if 'tatica_time1' not in globals():
                    global tatica_time1

                Buttons_Taticas = {
                    "Retake": btn_retake,
                    "Domínio": btn_dominio,
                    "Rush": btn_rush,
                    "FK": btn_fk,
                    "Execute": btn_execute,
                    "Bait": btn_bait
                    }
                
                for nome, button in Buttons_Taticas.items():
                    
                    if nome == nome_tatica_ponto:
                        button.configure(bg="mediumseagreen")
                        tatica_time1 = nome
                    
                    else:
                        button.configure(bg="tomato3")
                
                return 0
            
            elif verificador_ponto_tatica == "Ponto":
                
                if 'pontoforte_time1_tr' not in globals():
                    global pontoforte_time1_tr
                if 'pontoforte_time1_ct' not in globals():
                    global pontoforte_time1_ct
                    
                Buttons_Pontos_CT = {
                    "A": btn_bomb_a_ct,
                    "B": btn_bomb_b_ct,
                    "Meio": btn_meio_ct,
                    "Pontas": btn_pontas_ct
                    }
                Buttons_Pontos_TR = {
                    "A": btn_bomb_a_tr,
                    "B": btn_bomb_b_tr,
                    "Meio": btn_meio_tr,
                    "Pontas": btn_pontas_tr
                    }

                if verificador_lado == "CT":
                    
                    for nome, button in Buttons_Pontos_CT.items(): 
                        
                        if nome == nome_tatica_ponto:
                            
                            button.configure(bg="mediumseagreen")
                            pontoforte_time1_ct = nome
                            
                        else:
                            button.configure(bg="tomato3")
                else:
                    
                    for nome, button in Buttons_Pontos_TR.items(): 
                        
                        if nome == nome_tatica_ponto:
                            
                            button.configure(bg="mediumseagreen")
                            pontoforte_time1_tr = nome
                    
                        else:
                            button.configure(bg="tomato3")
                            
            elif verificador_ponto_tatica == "Economia":
                if 'economia_time1' not in globals():
                    global economia_time1
                
                Buttons_Economia = {"Arriscada": btn_economia_arriscada,
                                    "Conservadora": btn_economia_conservadora,
                                    "Normal": btn_economia_normal
                                    }
                
                for nome, button in Buttons_Economia.items(): 
                    
                    if nome == nome_tatica_ponto:
                        
                        button.configure(bg="mediumseagreen")
                        economia_time1 = nome
                        
                    else:
                        button.configure(bg="tomato3")
                        
                return 0
    

    PTPFSM2.configure(bg="darkgoldenrod")
    
    lbl_top_font = ("Dotum", 24)
    lbl_top = tk.Label(PTPFSM2, text= "Escolha a tática e o ponto forte de sua Equipe para esse mapa:", bg= "cadetblue3", height= 1, font= lbl_top_font)

    lbl_top.place(relx=0, rely=0, anchor= N)
    lbl_top.pack(side= "top", fill= "x")

    mapa = mapas_do_jogo[0]
    
    lbl_map_font = ("Dotum", 25)
    lbl_map = tk.Label(PTPFSM2, text= f"{mapa}:", bg= "darkseagreen3", height= 1, font= lbl_map_font)
    
    lbl_map.place(relx=0, rely=0.10, anchor= N)
    lbl_map.pack(side= "top", fill= "x")

    btn_font = ("Dotum", 20)
    
    btn_retake = tk.Button(PTPFSM2, text= "Retake", width=10, height=2, font= btn_font, command=lambda: changeColor_2(PTPFSM2, btn_retake, "Retake", "Tatica", "0"))
    btn_dominio = tk.Button(PTPFSM2, text= "Domínio", width=10, height=2, font= btn_font, command=lambda: changeColor_2(PTPFSM2, btn_dominio, "Domínio", "Tatica", "0"))
    btn_rush = tk.Button(PTPFSM2, text= "Rush", width=10, height=2, font= btn_font, command=lambda: changeColor_2(PTPFSM2, btn_rush, "Rush", "Tatica", "0"))
    btn_fk = tk.Button(PTPFSM2, text= "FK", width=10, height=2, font= btn_font, command=lambda: changeColor_2(PTPFSM2, btn_fk, "FK", "Tatica", "0"))
    btn_execute = tk.Button(PTPFSM2, text= "Execute", width=10, height=2, font= btn_font,command=lambda: changeColor_2(PTPFSM2, btn_execute, "Execute", "Tatica", "0"))
    btn_bait = tk.Button(PTPFSM2, text= "Bait", width=10, height=2, font= btn_font, command=lambda: changeColor_2(PTPFSM2, btn_bait, "Bait", "Tatica", "0"))

    
    btn_bomb_a_ct = tk.Button(PTPFSM2, text= "Bomb A", width=10, height=2, font= btn_font, command=lambda: changeColor_2(PTPFSM2, btn_bomb_a_ct, "A", "Ponto", "CT"))
    btn_bomb_b_ct = tk.Button(PTPFSM2, text= "Bomb B", width=10, height=2, font= btn_font, command=lambda: changeColor_2(PTPFSM2, btn_bomb_b_ct, "B", "Ponto", "CT"))
    btn_meio_ct = tk.Button(PTPFSM2, text= "Meio", width=10, height=2, font= btn_font, command=lambda: changeColor_2(PTPFSM2, btn_meio_ct, "Meio", "Ponto", "CT"))
    btn_pontas_ct = tk.Button(PTPFSM2, text= "Pontas", width=10, height=2, font= btn_font, command=lambda: changeColor_2(PTPFSM2, btn_pontas_ct, "Pontas", "Ponto", "CT"))
    
    btn_bomb_a_tr = tk.Button(PTPFSM2, text= "Bomb A", width=10, height=2, font= btn_font, command=lambda: changeColor_2(PTPFSM2, btn_bomb_a_tr, "A", "Ponto", "TR"))
    btn_bomb_b_tr = tk.Button(PTPFSM2, text= "Bomb B", width=10, height=2, font= btn_font, command=lambda: changeColor_2(PTPFSM2, btn_bomb_b_tr, "B", "Ponto", "TR"))
    btn_meio_tr = tk.Button(PTPFSM2, text= "Meio", width=10, height=2, font= btn_font, command=lambda: changeColor_2(PTPFSM2, btn_meio_tr, "Meio", "Ponto", "TR"))
    btn_pontas_tr = tk.Button(PTPFSM2, text= "Pontas", width=10, height=2, font= btn_font, command=lambda: changeColor_2(PTPFSM2, btn_pontas_tr, "Pontas", "Ponto", "TR"))
    
    btn_economia_arriscada = tk.Button(PTPFSM2, text= "Arriscada", width=15, height=2, font= btn_font, command=lambda: changeColor_2(PTPFSM2, btn_economia_arriscada, "Arriscada", "Economia", "0"))
    btn_economia_normal = tk.Button(PTPFSM2, text= "Normal", width=15, height=2, font= btn_font, command=lambda: changeColor_2(PTPFSM2, btn_economia_normal, "Normal", "Economia", "0"))
    btn_economia_conservadora = tk.Button(PTPFSM2, text= "Conservadora", width=15, height=2, font= btn_font, command=lambda: changeColor_2(PTPFSM2, btn_economia_conservadora, "Conservadora", "Economia", "0"))
    
    lbl_taticas_font = ("Dotum", 22)
    lbl_taticas = tk.Label(PTPFSM2, text= "Táticas", bg= "deepskyblue2", width= 90, height= 1, font= lbl_taticas_font)
    lbl_taticas.place(relx=0.5, rely=0.09, anchor= N)
    
    lbl_ponto_font = ("Dotum", 22)
    lbl_ponto_ct = tk.Label(PTPFSM2, text= "Ponto Forte CT", bg= "deepskyblue2", width= 90, height= 1, font= lbl_ponto_font)
    lbl_ponto_ct.place(relx=0.5, rely=0.24, anchor= N)
    
    lbl_ponto_tr = tk.Label(PTPFSM2, text= "Ponto Forte TR", bg= "deepskyblue2", width= 90, height= 1, font= lbl_ponto_font)
    lbl_ponto_tr.place(relx=0.5, rely=0.39, anchor= N)
    
    lbl_economia = tk.Label(PTPFSM2, text= "Economia", bg= "deepskyblue2", width= 90, height= 1, font= lbl_ponto_font)
    lbl_economia.place(relx=0.5, rely=0.59, anchor= N)
    
    btn_retake.place(relx=0.15, rely=0.18, anchor= CENTER)
    btn_dominio.place(relx=0.29, rely=0.18, anchor= CENTER)
    btn_rush.place(relx=0.43, rely=0.18, anchor= CENTER)
    btn_fk.place(relx=0.57, rely=0.18, anchor= CENTER)
    btn_execute.place(relx=0.71, rely=0.18, anchor= CENTER)
    btn_bait.place(relx=0.85, rely=0.18, anchor= CENTER)

    btn_bomb_a_ct.place(relx=0.15, rely=0.33, anchor= CENTER)
    btn_bomb_b_ct.place(relx=0.35, rely=0.33, anchor= CENTER)
    btn_meio_ct.place(relx=0.65, rely=0.33, anchor= CENTER)
    btn_pontas_ct.place(relx=0.85, rely=0.33, anchor= CENTER)
    
    btn_bomb_a_tr.place(relx=0.15, rely=0.48, anchor= CENTER)
    btn_bomb_b_tr.place(relx=0.35, rely=0.48, anchor= CENTER)
    btn_meio_tr.place(relx=0.65, rely=0.48, anchor= CENTER)
    btn_pontas_tr.place(relx=0.85, rely=0.48, anchor= CENTER)
    
    btn_economia_arriscada.place(relx=0.20, rely=0.67, anchor= CENTER)
    btn_economia_normal.place(relx=0.50, rely=0.67, anchor= CENTER)
    btn_economia_conservadora.place(relx=0.80, rely=0.67, anchor= CENTER)
    
    btn_confirmar_font = ("Dotum", 24)
    btn_confirmar = tk.Button(PTPFSM2, text= "Simular Mapa", width=11, height=4, font= btn_confirmar_font, command=lambda: SimularPartida(PTPFSM2, team1, team2, usuario, mapa, mapas_results, economia_time1, tatica_time1 if "tatica_time1" in globals() else None, pontoforte_time1_tr if "pontoforte_time1_tr" in globals() else None, pontoforte_time1_ct if "pontoforte_time1_ct" in globals() else None, team1_wins, team2_wins, mapas_do_jogo))
    btn_confirmar.place(relx=0.5, rely=0.83, anchor= CENTER)
    
    
    lbl_obs_font = ("Dotum", 15)
    lbl_obs = tk.Label(PTPFSM2, text= "(Escolha uma Tática e um Ponto Forte antes):", bg= "azure1", height=1, font= lbl_obs_font)
    lbl_obs.place(relx=0.5, rely=0.94, anchor= CENTER)
    
    
    def SimularPartida(PTPFMS2, team1, team2, usuario, mapa, mapas_results, economia_time1, tatica_time1, pontoforte_time1_tr, pontoforte_time1_ct, team1_wins, team2_wins, mapas_do_jogo):
        
            Buttons_Taticas = [btn_retake, btn_dominio, btn_rush, btn_fk, btn_execute, btn_bait]
            Buttons_PF_CT = [btn_bomb_a_ct, btn_bomb_b_ct, btn_meio_ct, btn_pontas_ct]
            Buttons_PF_TR = [btn_bomb_a_tr, btn_bomb_b_tr, btn_meio_tr, btn_pontas_tr]
            Buttons_Economia = [btn_economia_arriscada, btn_economia_conservadora, btn_economia_normal]
            
            def Verificar_Tatica_Definida():

                for button in Buttons_Taticas:
                    if button.cget("bg") == "mediumseagreen":
                        return True

                return False
            
            def Verificar_PF_CT_Definida():
 
                for button in Buttons_PF_CT:
                    if button.cget("bg") == "mediumseagreen":
                        return True

                return False
            
            def Verificar_PF_TR_Definida():

                for button in Buttons_PF_TR:
                    if button.cget("bg") == "mediumseagreen":
                        return True

                return False
            
            def Verificar_Economia_Definida():

                for button in Buttons_Economia:
                    if button.cget("bg") == "mediumseagreen":
                        return True

                return False
            
            if not Verificar_Tatica_Definida():
                
                return messagebox.showerror(title="Tática", message="Escolha uma tática.")
            
            elif not Verificar_PF_CT_Definida():
                
                return messagebox.showerror(title="Ponto Forte CT", message="Escolha um Ponto Forte de CT.")
            
            elif not Verificar_PF_TR_Definida():
                
                return messagebox.showerror(title="Ponto Forte TR", message="Escolha um Ponto Forte de TR.")
            
            elif not Verificar_Economia_Definida():
                
                return messagebox.showerror(title="Economia", message="Escolha uma estratégia de economia.")
            
            else:
                pass           
        
            player_stats = {}  # O dicionário terá o formato: {nome_do_jogador: (total_kills, total_deaths)}
        
            if mapas_results == "Sem":
            
                mapas_results = []
        
            else:
            
                pass
        
            try:
                
                cursor = conn.cursor()
                cursor.execute("SELECT MAX(Partidaidx) FROM StatsJogadoresPorPartida")
                partidaidx = cursor.fetchone()[0]
                cursor.close()
                
                # Assegura que o ID exista e está certo, ele é a chave primária da tabela de partida
                if partidaidx is None:
                    
                    partidaidx = 0
                    partidaidx = partidaidx + 1
                    
                else:
                    
                    partidaidx = partidaidx + 1
                    
            except Exception as e:
                print("Erro: ", e)
                
            team1_copy = copy.deepcopy(team1)
            team2_copy = copy.deepcopy(team2)       
                
            taticas_cpu = dict(sorted(team2.tactic_preferences.items(), key=lambda x: x[1], reverse=True))        
                    
            probabilidades = {
                0: 0.25,  # Maior probabilidade para o índice 0
                1: 0.22,
                2: 0.17,
                3: 0.15,
                4: 0.13,
                5: 0.08,
                }
                
            numero_probabilidade = random.choices(list(probabilidades.keys()), weights=list(probabilidades.values()), k=1)[0] # Escolhe uma tática somente
            taticas_cpu_lista = list(taticas_cpu.values())

            tatica_time2 = taticas_cpu_lista[numero_probabilidade]
            
            team1_tactic_modifier = team1.tactic_preferences.get(tatica_time1, 1.0)
            team2_tactic_modifier = team2.tactic_preferences.get(tatica_time2, 1.0)

            team1_copy.set_tactic_preference(tatica_time1, team1_tactic_modifier)
            team2_copy.set_tactic_preference(tatica_time2, team2_tactic_modifier)
            
            team1_forte_tr = pontoforte_time1_ct
            team1_forte_ct = pontoforte_time1_tr
           
            pontoforte_cpu = ["A", "B", "Meio", "Pontas"]
            
            numero_probabilidade = random.randint(0, 3)
            team2_forte_tr = pontoforte_cpu[numero_probabilidade]
            
            team2_forte_ct = pontoforte_cpu[numero_probabilidade]
            
            numero_probabilidade = random.randint(0, 2)
            economia_cpu = ["Arriscada", "Normal", "Conservadora"]
            economia_time2 = economia_cpu[numero_probabilidade]
            
            
            
            match = Match(team1_copy, team2_copy, mapa, tatica_time1, tatica_time2, team1_tactic_modifier, team2_tactic_modifier,
                          team1_forte_ct, team1_forte_tr, team2_forte_ct, team2_forte_tr)

            # Simula a partida e retorna o ganhador e o numero de rounds do perdedor do mapa
            winning_team, loser_rounds = match.play_match(mapa, economia_time1, economia_time2, tatica_time1, tatica_time2, team1_forte_ct, team1_forte_tr, team2_forte_ct, team2_forte_tr)
            
            del tatica_time1
            del pontoforte_time1_tr
            del pontoforte_time1_ct

            
            if winning_team:
                
                rounds_total = loser_rounds + 16

                mapa_nome = mapa
                
                if team1_copy == winning_team:
                    
                    losing_team = team2_copy
                    mapas_results.append((mapa_nome, winning_team.name, losing_team.name, loser_rounds))
                    update_player_stats(winning_team, losing_team, rounds_total)
                    team1_wins += 1
                    
                else:
                    
                    losing_team = team1_copy
                    mapas_results.append((mapa_nome, winning_team.name, losing_team.name, loser_rounds))
                    update_player_stats(winning_team, losing_team, rounds_total)
                    team2_wins += 1
            
            for player in team1_copy.players + team2_copy.players:
                
                if player.name not in player_stats:
                    
                    player_stats[player.name] = (player.kills, player.deaths)
                    
                else:
                    
                    total_kills, total_deaths = player_stats[player.name]
                    player_stats[player.name] = (total_kills + player.kills, total_deaths + player.deaths)
                    
            try:
                
                for player in team1_copy.players + team2_copy.players:
                    
                    if player in team1_copy.players:
                        
                        player_time = team1_copy.name
                        
                    else:
                        
                        player_time = team2_copy.name

                    rating = player.kills / player.deaths if player.deaths != 0 else player.kills
                    Cursor = conn.cursor()
                    InsertQRY = "INSERT INTO StatsJogadoresPorPartida (Partidaidx, Nick, Team, Mapa, Rounds, Kills, Deaths, Rating) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    Dados = (partidaidx, player.name, player_time, mapa, rounds_total, player.kills, player.deaths, rating)
                    Cursor.execute(InsertQRY, Dados)
                    conn.commit()
                    Cursor.close()
                    Cursor = conn.cursor()
                    CallProcedure = "CALL AtualizarRegistros(%s)"
                    Cursor.execute(CallProcedure, (player.name,))
                    conn.commit()
                    Cursor.close()

            except Exception as e:
                    print("Erro: ", e)   
                    
            most_kills_player = max(team1_copy.players + team2_copy.players, key=lambda p: p.kills)
            most_deaths_player = max(team1_copy.players + team2_copy.players, key=lambda p: p.deaths)

            return Abrir_Pagina_Resultado_Mapa(team1_copy, team2_copy, usuario, mapa, mapas_do_jogo, mapas_results, winning_team, losing_team, loser_rounds, team1_wins, team2_wins, PTPFSM2)    
    
    if Pagina_Vetos == "Sem":
        
        pass
        
    else:
        
        Pagina_Vetos.destroy()
        
    if Pagina_Resultado_Mapa == "Sem":
        
         pass
         
    else:
        
         Pagina_Resultado_Mapa.destroy()
    
    PTPFSM2.after(0, toggle_fullscreen, PTPFSM2)
    PTPFSM2.mainloop()

def Abrir_Pagina_Resultado_Mapa(team1_copy, team2_copy, usuario, mapa, mapas_do_jogo, mapas_results, winning_team, losing_team, loser_rounds, team1_wins, team2_wins, PTPFSM2):
    Pagina_Resultado_Mapa = tk.Tk()
    Pagina_Resultado_Mapa.title(f"Resultado {mapa}")
    
    Pagina_Resultado_Mapa.configure(bg="darkgoldenrod")
    
    lbl_placar_font = ("Dotum", 36)
    lbl_placar = tk.Label(Pagina_Resultado_Mapa, text= f"{winning_team.name} 16 x {loser_rounds} {losing_team.name}", bg= "cadetblue3", width= 50, height= 2, font= lbl_placar_font)
    lbl_placar.place(relx=0.5, rely=0.19, anchor= CENTER)


    lbl_map_font = ("Dotum", 36)
    lbl_map = tk.Label(Pagina_Resultado_Mapa, text= f"{mapa}:", bg= "darkseagreen3", width= 70, height= 2, font= lbl_map_font)
    lbl_map.place(relx=0.5, rely=0, anchor= N)


    lbl_time1_scoreboard_font = ("Dotum", 28)
    lbl_time1_scoreboard = tk.Label(Pagina_Resultado_Mapa, text= f"{winning_team.name}", bg= "#FCE6C9", width= 46, height= 2, bd=4, relief="solid", font= lbl_time1_scoreboard_font)
    lbl_time1_scoreboard.place(relx=0.2, rely=0.30, anchor= CENTER)
    
    winning_players_stats = {}

    for player in winning_team.players:
        winning_players_stats[player.name] = {
            "Kills": player.kills,
            "Deaths": player.deaths,
            "Rating": player.kills / player.deaths if player.deaths != 0 else player.kills
        }
        
    win_player_stats = dict(sorted(winning_players_stats.items(), key=lambda x: x[1]['Rating'], reverse=True))
    
    win_melhor = list(win_player_stats.keys())[0] if win_player_stats else None
    win_melhor_stats = win_player_stats[win_melhor]
    win_melhor_kills = win_melhor_stats["Kills"]
    win_melhor_deaths = win_melhor_stats["Deaths"]
    win_melhor_rating = round(win_melhor_stats["Rating"], 2)
    
    win_segundo = list(win_player_stats.keys())[1] if win_player_stats else None
    win_segundo_stats = win_player_stats[win_segundo]
    win_segundo_kills = win_segundo_stats["Kills"]
    win_segundo_deaths = win_segundo_stats["Deaths"]
    win_segundo_rating = round(win_segundo_stats["Rating"], 2)
    
    win_terceiro = list(win_player_stats.keys())[2] if win_player_stats else None
    win_terceiro_stats = win_player_stats[win_terceiro]
    win_terceiro_kills = win_terceiro_stats["Kills"]
    win_terceiro_deaths = win_terceiro_stats["Deaths"]
    win_terceiro_rating = round(win_terceiro_stats["Rating"], 2)
    
    win_quarto = list(win_player_stats.keys())[3] if win_player_stats else None
    win_quarto_stats = win_player_stats[win_quarto]
    win_quarto_kills = win_quarto_stats["Kills"]
    win_quarto_deaths = win_quarto_stats["Deaths"]
    win_quarto_rating = round(win_quarto_stats["Rating"], 2)
    
    win_ultimo = list(win_player_stats.keys())[4] if win_player_stats else None
    win_ultimo_stats = win_player_stats[win_ultimo]
    win_ultimo_kills = win_ultimo_stats["Kills"]
    win_ultimo_deaths = win_ultimo_stats["Deaths"]
    win_ultimo_rating = round(win_ultimo_stats["Rating"], 2)
    
    lbl_time1_jogador_font = ("Dotum", 22)
    lbl_header_time1 = tk.Label(Pagina_Resultado_Mapa, text= "Nick", bg= "#FCE6C9", width= 35, height= 1, bd=4, relief="solid", font= lbl_time1_jogador_font)
    lbl_header_time1.place(relx=0.1, rely=0.36, anchor= CENTER)
    lbl_header_time1_kills = tk.Label(Pagina_Resultado_Mapa, text= "K", bg= "#A2CD5A", width= 5, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
    lbl_header_time1_kills.place(relx=0.28, rely=0.36, anchor= CENTER)
    lbl_header_time1_deaths = tk.Label(Pagina_Resultado_Mapa, text= "D", bg= "tomato1", width= 5, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
    lbl_header_time1_deaths.place(relx=0.33, rely=0.36, anchor= CENTER)
    lbl_header_time1_rating = tk.Label(Pagina_Resultado_Mapa, text= "Rating", bg= "#FCE6C9", width= 12, height= 1, bd=4, relief="solid", font= lbl_time1_jogador_font)
    lbl_header_time1_rating.place(relx=0.41, rely=0.36, anchor= CENTER)
    
    lbl_melhor_time1 = tk.Label(Pagina_Resultado_Mapa, text= f"{win_melhor}", bg= "#FCE6C9", width= 35, height= 1, bd=4, relief="solid", font= lbl_time1_jogador_font)
    lbl_melhor_time1.place(relx=0.1, rely=0.40, anchor= CENTER)
    lbl_melhor_time1_kills = tk.Label(Pagina_Resultado_Mapa, text= f"{win_melhor_kills}", bg= "#A2CD5A", width= 5, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
    lbl_melhor_time1_kills.place(relx=0.28, rely=0.40, anchor= CENTER)
    lbl_melhor_time1_deaths = tk.Label(Pagina_Resultado_Mapa, text= f"{win_melhor_deaths}", bg= "tomato1", width= 5, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
    lbl_melhor_time1_deaths.place(relx=0.33, rely=0.40, anchor= CENTER)
    lbl_melhor_time1_rating = tk.Label(Pagina_Resultado_Mapa, text= f"{win_melhor_rating}", bg= "#FCE6C9", width= 12, height= 1, bd=4, relief="solid", font= lbl_time1_jogador_font, fg="darkgreen" if win_melhor_rating > 1.10 else ("yellow3" if win_melhor_rating >= 0.90 else "red4"))
    lbl_melhor_time1_rating.place(relx=0.41, rely=0.40, anchor= CENTER)
    
    lbl_segundo_time1 = tk.Label(Pagina_Resultado_Mapa, text= f"{win_segundo}", bg= "#FCE6C9", width= 35, height= 1, bd=4, relief="solid", font= lbl_time1_jogador_font)
    lbl_segundo_time1.place(relx=0.1, rely=0.44, anchor= CENTER)
    lbl_segundo_time1_kills = tk.Label(Pagina_Resultado_Mapa, text= f"{win_segundo_kills}", bg= "#A2CD5A", width= 5, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
    lbl_segundo_time1_kills.place(relx=0.28, rely=0.44, anchor= CENTER)
    lbl_segundo_time1_deaths = tk.Label(Pagina_Resultado_Mapa, text= f"{win_segundo_deaths}", bg= "tomato1", width= 5, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
    lbl_segundo_time1_deaths.place(relx=0.33, rely=0.44, anchor= CENTER)
    lbl_segundo_time1_rating = tk.Label(Pagina_Resultado_Mapa, text= f"{win_segundo_rating}", bg= "#FCE6C9", width= 12, height= 1, bd=4, relief="solid", font= lbl_time1_jogador_font, fg="darkgreen" if win_segundo_rating > 1.10 else ("yellow3" if win_segundo_rating >= 0.90 else "red4"))
    lbl_segundo_time1_rating.place(relx=0.41, rely=0.44, anchor= CENTER)
    
    lbl_terceiro_time1 = tk.Label(Pagina_Resultado_Mapa, text= f"{win_terceiro}", bg= "#FCE6C9", width= 35, height= 1, bd=4, relief="solid", font= lbl_time1_jogador_font)
    lbl_terceiro_time1.place(relx=0.1, rely=0.48, anchor= CENTER)
    lbl_terceiro_time1_kills = tk.Label(Pagina_Resultado_Mapa, text= f"{win_terceiro_kills}", bg= "#A2CD5A", width= 5, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
    lbl_terceiro_time1_kills.place(relx=0.28, rely=0.48, anchor= CENTER)
    lbl_terceiro_time1_deaths = tk.Label(Pagina_Resultado_Mapa, text= f"{win_terceiro_deaths}", bg= "tomato1", width= 5, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
    lbl_terceiro_time1_deaths.place(relx=0.33, rely=0.48, anchor= CENTER)
    lbl_terceiro_time1_rating = tk.Label(Pagina_Resultado_Mapa, text= f"{win_terceiro_rating}", bg= "#FCE6C9", width= 12, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font, fg="darkgreen" if win_terceiro_rating > 1.10 else ("yellow3" if win_terceiro_rating >= 0.90 else "red4"))
    lbl_terceiro_time1_rating.place(relx=0.41, rely=0.48, anchor= CENTER)
    
    lbl_quarto_time1 = tk.Label(Pagina_Resultado_Mapa, text= f"{win_quarto}", bg= "#FCE6C9", width= 35, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
    lbl_quarto_time1.place(relx=0.1, rely=0.52, anchor= CENTER)
    lbl_quarto_time1_kills = tk.Label(Pagina_Resultado_Mapa, text= f"{win_quarto_kills}", bg= "#A2CD5A", width= 5, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
    lbl_quarto_time1_kills.place(relx=0.28, rely=0.52, anchor= CENTER)
    lbl_quarto_time2_deaths = tk.Label(Pagina_Resultado_Mapa, text= f"{win_quarto_deaths}", bg= "tomato1", width= 5, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
    lbl_quarto_time2_deaths.place(relx=0.33, rely=0.52, anchor= CENTER)
    lbl_quarto_time1_rating = tk.Label(Pagina_Resultado_Mapa, text= f"{win_quarto_rating}", bg= "#FCE6C9", width= 12, height= 1, bd=4, relief="solid", font= lbl_time1_jogador_font, fg="darkgreen" if win_quarto_rating > 1.10 else ("yellow3" if win_quarto_rating >= 0.90 else "red4"))
    lbl_quarto_time1_rating.place(relx=0.41, rely=0.52, anchor= CENTER)
    
    lbl_quinto_time1 = tk.Label(Pagina_Resultado_Mapa, text= f"{win_ultimo}", bg= "#FCE6C9", width= 35, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
    lbl_quinto_time1.place(relx=0.1, rely=0.56, anchor= CENTER)
    lbl_quinto_time1_kills = tk.Label(Pagina_Resultado_Mapa, text= f"{win_ultimo_kills}", bg= "#A2CD5A", width= 5, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
    lbl_quinto_time1_kills.place(relx=0.28, rely=0.56, anchor= CENTER)
    lbl_quinto_time1_deaths = tk.Label(Pagina_Resultado_Mapa, text= f"{win_ultimo_deaths}", bg= "tomato1", width= 5, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
    lbl_quinto_time1_deaths.place(relx=0.33, rely=0.56, anchor= CENTER)
    lbl_quinto_time1_rating = tk.Label(Pagina_Resultado_Mapa, text= f"{win_ultimo_rating}", bg= "#FCE6C9", width= 12, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font, fg="darkgreen" if win_ultimo_rating > 1.10 else ("yellow3" if win_ultimo_rating >= 0.90 else "red4"))
    lbl_quinto_time1_rating.place(relx=0.41, rely=0.56, anchor= CENTER)
    
    
    
    
    
    
    lbl_time2_scoreboard_font = ("Dotum", 28)
    lbl_time2_scoreboard = tk.Label(Pagina_Resultado_Mapa, text= f"{losing_team.name}", bg= "#FCE6C9", width= 46, height= 2, bd=4, relief="solid", font= lbl_time2_scoreboard_font)
    lbl_time2_scoreboard.place(relx=0.8, rely=0.30, anchor= CENTER)
    
    losing_players_stats = {}

    for player in losing_team.players:
        losing_players_stats[player.name] = {
            "Kills": player.kills,
            "Deaths": player.deaths,
            "Rating": player.kills / player.deaths if player.deaths != 0 else player.kills
        }
        
    loss_player_stats = dict(sorted(losing_players_stats.items(), key=lambda x: x[1]['Rating'], reverse=True))
    
    loss_melhor = list(loss_player_stats.keys())[0] if loss_player_stats else None
    loss_melhor_stats = loss_player_stats[loss_melhor]
    loss_melhor_kills = loss_melhor_stats["Kills"]
    loss_melhor_deaths = loss_melhor_stats["Deaths"]
    loss_melhor_rating = round(loss_melhor_stats["Rating"], 2)
    
    loss_segundo = list(loss_player_stats.keys())[1] if loss_player_stats else None
    loss_segundo_stats = loss_player_stats[loss_segundo]
    loss_segundo_kills = loss_segundo_stats["Kills"]
    loss_segundo_deaths = loss_segundo_stats["Deaths"]
    loss_segundo_rating = round(loss_segundo_stats["Rating"], 2)
    
    loss_terceiro = list(loss_player_stats.keys())[2] if loss_player_stats else None
    loss_terceiro_stats = loss_player_stats[loss_terceiro]
    loss_terceiro_kills = loss_terceiro_stats["Kills"]
    loss_terceiro_deaths = loss_terceiro_stats["Deaths"]
    loss_terceiro_rating = round(loss_terceiro_stats["Rating"], 2)
    
    loss_quarto = list(loss_player_stats.keys())[3] if loss_player_stats else None
    loss_quarto_stats = loss_player_stats[loss_quarto]
    loss_quarto_kills = loss_quarto_stats["Kills"]
    loss_quarto_deaths = loss_quarto_stats["Deaths"]
    loss_quarto_rating = round(loss_quarto_stats["Rating"], 2)
    
    loss_ultimo = list(loss_player_stats.keys())[4] if loss_player_stats else None
    loss_ultimo_stats = loss_player_stats[loss_ultimo]
    loss_ultimo_kills = loss_ultimo_stats["Kills"]
    loss_ultimo_deaths = loss_ultimo_stats["Deaths"]
    loss_ultimo_rating = round(loss_ultimo_stats["Rating"], 2)
    
    lbl_time2_jogador_font = ("Dotum", 22)
    
    lbl_header_time2 = tk.Label(Pagina_Resultado_Mapa, text= "Nick", bg= "#FCE6C9", width= 35, height= 1, bd=4, relief="solid", font= lbl_time1_jogador_font)
    lbl_header_time2.place(relx=0.9, rely=0.36, anchor= CENTER)
    lbl_header_time2_kills = tk.Label(Pagina_Resultado_Mapa, text= "K", bg= "#A2CD5A", width= 6, height= 1, bd=4, relief="solid", font= lbl_time1_jogador_font)
    lbl_header_time2_kills.place(relx=0.72, rely=0.36, anchor= CENTER)
    lbl_header_time2_deaths = tk.Label(Pagina_Resultado_Mapa, text= "D", bg= "tomato1", width= 5, height= 1, bd=4, relief="solid", font= lbl_time1_jogador_font)
    lbl_header_time2_deaths.place(relx=0.67, rely=0.36, anchor= CENTER)
    lbl_header_time2_rating = tk.Label(Pagina_Resultado_Mapa, text= "Rating", bg= "#FCE6C9", width= 12, height= 1, bd=4, relief="solid", font= lbl_time1_jogador_font)
    lbl_header_time2_rating.place(relx=0.59, rely=0.36, anchor= CENTER)
    
    lbl_melhor_time2 = tk.Label(Pagina_Resultado_Mapa, text= f"{loss_melhor}", bg= "#FCE6C9", width= 35, height= 1, bd=4, relief="solid", font= lbl_time2_jogador_font)
    lbl_melhor_time2.place(relx=0.9, rely=0.40, anchor= CENTER)
    lbl_melhor_time2_kills = tk.Label(Pagina_Resultado_Mapa, text= f"{loss_melhor_kills}", bg= "#A2CD5A", width= 6, height= 1, bd=4, relief="solid", font= lbl_time2_jogador_font)
    lbl_melhor_time2_kills.place(relx=0.72, rely=0.40, anchor= CENTER)
    lbl_melhor_time2_deaths = tk.Label(Pagina_Resultado_Mapa, text= f"{loss_melhor_deaths}", bg= "tomato1", width= 5, height= 1, bd=4, relief="solid", font= lbl_time2_jogador_font)
    lbl_melhor_time2_deaths.place(relx=0.67, rely=0.40, anchor= CENTER)
    lbl_melhor_time2_rating = tk.Label(Pagina_Resultado_Mapa, text= f"{loss_melhor_rating}", bg= "#FCE6C9", width= 12, height= 1, bd=4, relief="solid", font= lbl_time2_jogador_font, fg="darkgreen" if loss_melhor_rating > 1.10 else ("yellow3" if loss_melhor_rating >= 0.90 else "red4"))
    lbl_melhor_time2_rating.place(relx=0.59, rely=0.40, anchor= CENTER)
    
    lbl_segundo_time2 = tk.Label(Pagina_Resultado_Mapa, text= f"{loss_segundo}", bg= "#FCE6C9", width= 35, height= 1, bd=4, relief="solid", font= lbl_time2_jogador_font)
    lbl_segundo_time2.place(relx=0.9, rely=0.44, anchor= CENTER)
    lbl_segundo_time2_kills = tk.Label(Pagina_Resultado_Mapa, text= f"{loss_segundo_kills}", bg= "#A2CD5A", width= 6, height= 1, bd=4, relief="solid", font= lbl_time2_jogador_font)
    lbl_segundo_time2_kills.place(relx=0.72, rely=0.44, anchor= CENTER)
    lbl_segundo_time2_deaths = tk.Label(Pagina_Resultado_Mapa, text= f"{loss_segundo_deaths}", bg= "tomato1", width= 5, height= 1, bd=4, relief="solid", font= lbl_time2_jogador_font)
    lbl_segundo_time2_deaths.place(relx=0.67, rely=0.44, anchor= CENTER)
    lbl_segundo_time2_rating = tk.Label(Pagina_Resultado_Mapa, text= f"{loss_segundo_rating}", bg= "#FCE6C9", width= 12, height= 1, bd=4, relief="solid", font= lbl_time2_jogador_font, fg="darkgreen" if loss_segundo_rating > 1.10 else ("yellow3" if loss_segundo_rating >= 0.90 else "red4"))
    lbl_segundo_time2_rating.place(relx=0.59, rely=0.44, anchor= CENTER)
    
    lbl_terceiro_time2 = tk.Label(Pagina_Resultado_Mapa, text= f"{loss_terceiro}", bg= "#FCE6C9", width= 35, height= 1, bd=4, relief="solid", font= lbl_time2_jogador_font)
    lbl_terceiro_time2.place(relx=0.9, rely=0.48, anchor= CENTER)
    lbl_terceiro_time2_kills = tk.Label(Pagina_Resultado_Mapa, text= f"{loss_terceiro_kills}", bg= "#A2CD5A", width= 6, height= 1, bd=5, relief="solid", font= lbl_time2_jogador_font)
    lbl_terceiro_time2_kills.place(relx=0.72, rely=0.48, anchor= CENTER)
    lbl_terceiro_time2_deaths = tk.Label(Pagina_Resultado_Mapa, text= f"{loss_terceiro_deaths}", bg= "tomato1", width= 5, height= 1, bd=5, relief="solid", font= lbl_time2_jogador_font)
    lbl_terceiro_time2_deaths.place(relx=0.67, rely=0.48, anchor= CENTER)
    lbl_terceiro_time2_rating = tk.Label(Pagina_Resultado_Mapa, text= f"{loss_terceiro_rating}", bg= "#FCE6C9", width= 12, height= 1, bd=5, relief="solid", font= lbl_time2_jogador_font, fg="darkgreen" if loss_terceiro_rating > 1.10 else ("yellow3" if loss_terceiro_rating >= 0.90 else "red4"))
    lbl_terceiro_time2_rating.place(relx=0.59, rely=0.48, anchor= CENTER)
    
    lbl_quarto_time2 = tk.Label(Pagina_Resultado_Mapa, text= f"{loss_quarto}", bg= "#FCE6C9", width= 35, height= 1, bd=5, relief="solid", font= lbl_time2_jogador_font)
    lbl_quarto_time2.place(relx=0.9, rely=0.52, anchor= CENTER)
    lbl_quarto_time2_kills = tk.Label(Pagina_Resultado_Mapa, text= f"{loss_quarto_kills}", bg= "#A2CD5A", width= 6, height= 1, bd=5, relief="solid", font= lbl_time2_jogador_font)
    lbl_quarto_time2_kills.place(relx=0.72, rely=0.52, anchor= CENTER)
    lbl_quarto_time2_deaths = tk.Label(Pagina_Resultado_Mapa, text= f"{loss_quarto_deaths}", bg= "tomato1", width= 5, height= 1, bd=5, relief="solid", font= lbl_time2_jogador_font)
    lbl_quarto_time2_deaths.place(relx=0.67, rely=0.52, anchor= CENTER)
    lbl_quarto_time2_rating = tk.Label(Pagina_Resultado_Mapa, text= f"{loss_quarto_rating}", bg= "#FCE6C9", width= 12, height= 1, bd=5, relief="solid", font= lbl_time2_jogador_font, fg="darkgreen" if loss_quarto_rating > 1.10 else ("yellow3" if loss_quarto_rating >= 0.90 else "red4"))
    lbl_quarto_time2_rating.place(relx=0.59, rely=0.52, anchor= CENTER)
    
    lbl_quinto_time2 = tk.Label(Pagina_Resultado_Mapa, text= f"{loss_ultimo}", bg= "#FCE6C9", width= 35, height= 1, bd=5, relief="solid", font= lbl_time2_jogador_font)
    lbl_quinto_time2.place(relx=0.9, rely=0.56, anchor= CENTER)
    lbl_quinto_time2_kills = tk.Label(Pagina_Resultado_Mapa, text= f"{loss_ultimo_kills}", bg= "#A2CD5A", width= 6, height= 1, bd=5, relief="solid", font= lbl_time2_jogador_font)
    lbl_quinto_time2_kills.place(relx=0.72, rely=0.56, anchor= CENTER)
    lbl_quinto_time2_deaths = tk.Label(Pagina_Resultado_Mapa, text= f"{loss_ultimo_deaths}", bg= "tomato1", width= 5, height= 1, bd=5, relief="solid", font= lbl_time2_jogador_font)
    lbl_quinto_time2_deaths.place(relx=0.67, rely=0.56, anchor= CENTER)
    lbl_quinto_time2_rating = tk.Label(Pagina_Resultado_Mapa, text= f"{loss_ultimo_rating}", bg= "#FCE6C9", width= 12, height= 1, bd=5, relief="solid", font= lbl_time2_jogador_font, fg="darkgreen" if loss_ultimo_rating > 1.10 else ("yellow3" if loss_ultimo_rating >= 0.90 else "red4"))
    lbl_quinto_time2_rating.place(relx=0.59, rely=0.56, anchor= CENTER)
    
    
    most_kills_player = max(winning_team.players + losing_team.players, key=lambda p: p.kills)
    most_deaths_player = max(winning_team.players + losing_team.players, key=lambda p: p.deaths)
    
    lbl_mais_kills = tk.Label(Pagina_Resultado_Mapa, text= f"Mais Kills: {most_kills_player.name} ({most_kills_player.kills})", bg= "#FCE6C9", width= 25, height= 2, bd=3, relief="solid", font= lbl_time1_jogador_font)
    lbl_mais_kills.place(relx=0.5, rely=0.64, anchor= CENTER)
    lbl_mais_deaths = tk.Label(Pagina_Resultado_Mapa, text= f"Mais Mortes: {most_deaths_player.name} ({most_deaths_player.deaths})", bg= "#FCE6C9", width= 25, height= 2, bd=3, relief="solid", font= lbl_time1_jogador_font)
    lbl_mais_deaths.place(relx=0.5, rely=0.72, anchor= CENTER)
    
    lbl_vs_font = ("Dotum", 28)
    lbl_vs = tk.Label(Pagina_Resultado_Mapa, text= "X", bg= "darkgoldenrod", width= 5, height= 2, font= lbl_vs_font)
    lbl_vs.place(relx=0.5, rely=0.30, anchor= CENTER)
    
    btn_confirmar_font = ("Dotum", 24)
    btn_confirmar = tk.Button(Pagina_Resultado_Mapa, text= "Próximo Mapa", width=11, height=4, font= btn_confirmar_font, command=lambda: Verificar_Se_Acabou(team1_copy, team2_copy, usuario, mapa, winning_team, losing_team, loser_rounds, team1_wins, team2_wins))
    btn_confirmar.place(relx=0.5, rely=0.85, anchor= CENTER)    
        
    if PTPFSM2 == "Sem":
        pass
    
    else:
        PTPFSM2.destroy()
        
    def Verificar_Se_Acabou(team1_copy, team2_copy, usuario, mapa, winning_team, losing_team, loser_rounds, team1_wins, team2_wins):
        
        if team1_wins >= 2:
            
            final_winner = team1_copy
            final_loser = team2_copy
                
        elif team2_wins >=2:
            
            final_winner = team2_copy
            final_loser = team1_copy
            
        if winning_team:
            
            if team1_wins == 2 or team2_wins == 2:   
                  
                Abrir_Pagina_Final(team1_copy, team2_copy, usuario, mapas_results, final_winner, final_loser, loser_rounds, team1_wins, team2_wins, Pagina_Resultado_Mapa)
                
            else:

                Abrir_Pagina_Taticas_Pontos_Fortes_Simulação(team1_copy, team2_copy, usuario, "Sem", mapa, mapas_do_jogo, mapas_results, team1_wins, team2_wins, Pagina_Resultado_Mapa)
                
        else:
            pass
    

    Pagina_Resultado_Mapa.after(0, toggle_fullscreen, Pagina_Resultado_Mapa)
    mapas_do_jogo.remove(mapa)
    Pagina_Resultado_Mapa.mainloop()

def Abrir_Pagina_Final(team1_copy, team2_copy, usuario, mapas_results, final_winner, final_loser, loser_rounds, team1_wins, team2_wins, Pagina_Resultado_Mapa):
        Pagina_Final = tk.Tk()
        Pagina_Final.title(f"Resultado {team1_copy.name} x {team2_copy.name}")
        
        Pagina_Final.configure(bg="darkgoldenrod")
        
        StatsUsuarios = "statsusuarios.csv"
        Estatísticas_Usuarios = {}
        
        try:
            
            dados = []
            
            if final_winner == team1_copy:
                
                dados.append([usuario, team1_copy.name, "win"])
                
            if final_loser == team1_copy:

                dados.append([usuario, team1_copy.name, "loss"])
    
            cabeçalho = ['Nome', 'Time', 'Resultado']
            
            verificar_arquivo = Path(StatsUsuarios).is_file()

            with open(StatsUsuarios, 'a', newline='') as arquivo:
                
                  
                escritor_csv = csv.writer(arquivo)
                escritor_header = csv.writer(arquivo)
                
                if not verificar_arquivo: # Verificando se o arquivo já existe para não escrever header duas vezes

                    escritor_header.writerow(cabeçalho)
                    
                for linha in dados:

                    escritor_csv.writerow(linha)
            
            with open(StatsUsuarios, 'r') as arquivo:
                
                leitor = csv.reader(arquivo)
                next(leitor)  # pula a primeira linha (cabeçalho)
                
                for linha in leitor:
                    
                    usuario = linha[0]
                    time = linha[1]
                    resultado = linha[2]
                    chave = (usuario, time)

                    if chave not in Estatísticas_Usuarios:
                        Estatísticas_Usuarios[chave] = []

                    Estatísticas_Usuarios[chave].append(resultado)


                Estatísticas_Usuarios_Final = []


                for chave, resultado in Estatísticas_Usuarios.items():
                    
                    usuario, time = chave
                    jogos = len(resultado)
                    vitorias = resultado.count('win')
                    derrotas = resultado.count('loss')

                    # Criando um dicionário para auxiliar a inserir na lista final

                    Insert_Estatísticas_Usuarios = {
                        'Nome': usuario,
                        'Time': time,
                        'Jogos': jogos,
                        'Vitorias': vitorias,
                        'Derrotas': derrotas
                    }

                    Estatísticas_Usuarios_Final.append(Insert_Estatísticas_Usuarios)
                print(Estatísticas_Usuarios_Final)
                    
        except Exception as e:
            print("Erro: ", e)
            
        try:
            
            player_stats = {}
            
            for player in team1_copy.players + team2_copy.players: 
                
                if player.name not in player_stats:
                    
                    player_stats[player.name] = player
                    
                else:
                    
                    pass
            
            # Calcula Maximos e Minimos de estatísticas
            max_kills_player = max(player_stats.values(), key=lambda player: player.killstotal)
            min_kills_player = min(player_stats.values(), key=lambda player: player.killstotal)
            max_deaths_player = max(player_stats.values(), key=lambda player: player.deathstotal)
            min_deaths_player = min(player_stats.values(), key=lambda player: player.deathstotal)
            max_rating_player = max(player_stats.values(), key=lambda player: player.killstotal / player.deathstotal if player.deaths != 0 else player.killstotal)
            min_rating_player = min(player_stats.values(), key=lambda player: player.killstotal / player.deathstotal if player.deaths != 0 else player.killstotal)
            
            max_rating_player_valor = round(max_rating_player.killstotal / max_rating_player.deathstotal, 2)
            min_rating_player_valor = round(min_rating_player.killstotal / min_rating_player.deathstotal, 2)
            
            winning_team_map_wins = 0
            losing_team_map_wins = 0
            
            if final_winner == team1_copy:
                
                winning_team_map_wins = team1_wins
                losing_team_map_wins = team2_wins

            elif final_winner == team2_copy:
                
                winning_team_map_wins = team2_wins
                losing_team_map_wins = team1_wins
                

            lbl_placar_font = ("Dotum", 36)
            lbl_placar = tk.Label(Pagina_Final, text= f"{final_winner.name} {winning_team_map_wins} x {losing_team_map_wins} {final_loser.name}", bg= "cadetblue3", width= 100, height= 2, font= lbl_placar_font)

            lbl_placar.place(relx=0.5, rely=0.20, anchor= CENTER)
            
            resultado_mapas = "\n".join([
                f"{mapa_nome}: {winner_name} 16 x {loser_rounds} {loser_name}" for mapa_nome, winner_name, loser_name, loser_rounds in mapas_results
                ])
            
            lbl_map_font = ("Dotum", 30)
            lbl_map = tk.Label(Pagina_Final, text= f"{resultado_mapas}", bg= "darkseagreen3", width= 100, height= 3, font= lbl_map_font)
            lbl_map.place(relx=0.5, rely=0, anchor= N)
            
            lbl_max_min = ("Dotum", 25)
            lbl_max_kills = tk.Label(Pagina_Final, text= f"Mais Kills: {max_kills_player.name} ({max_kills_player.killstotal})", bg= "cadetblue3", width= 25, height= 2, font= lbl_max_min)
            lbl_max_kills.place(relx=0.12, rely=0.63, anchor= S)
            lbl_min_kills = tk.Label(Pagina_Final, text= f"Menos Kills: {min_kills_player.name} ({min_kills_player.killstotal})", bg= "cadetblue3", width= 25, height= 2, font= lbl_max_min)
            lbl_min_kills.place(relx=0.36, rely=0.63, anchor= S)
            
            lbl_max_deaths = tk.Label(Pagina_Final, text= f"Mais Mortes: {max_deaths_player.name} ({max_deaths_player.deathstotal})", bg= "cadetblue3", width= 25, height= 2, font= lbl_max_min)
            lbl_max_deaths.place(relx=0.12, rely=0.70, anchor= S)
            lbl_min_deaths = tk.Label(Pagina_Final, text= f"Menos Mortes: {min_deaths_player.name} ({min_deaths_player.deathstotal})", bg= "cadetblue3", width= 25, height= 2, font= lbl_max_min)
            lbl_min_deaths.place(relx=0.36, rely=0.70, anchor= S)
            
            lbl_max_rating = tk.Label(Pagina_Final, text= f"Maior Rating: {max_rating_player.name} ({max_rating_player_valor})", bg= "cadetblue3", width= 25, height= 2, font= lbl_max_min)
            lbl_max_rating.place(relx=0.12, rely=0.77, anchor= S)
            lbl_min_rating = tk.Label(Pagina_Final, text= f"Menor Rating: {min_rating_player.name} ({min_rating_player_valor})", bg= "cadetblue3", width= 25, height= 2, font= lbl_max_min)
            lbl_min_rating.place(relx=0.36, rely=0.77, anchor= S)
            
            lbl_usuario_tabela_font = ("Dotum", 22)
            frm = tk.Frame(Pagina_Final)
            frm.grid()
            frm.configure(bg="azure1")       
            column = []
            
            for i, dado in zip(range(5), Estatísticas_Usuarios_Final):
                
                label = tk.Label(frm, text= f"Usuario: {dado['Nome']}, Time: {dado['Time']}, Jogos: {dado['Jogos']}, Vitórias: {dado['Vitorias']}, Derrotas: {dado['Derrotas']}", bg="azure1", bd= 1, font= lbl_usuario_tabela_font)
                label.grid(row=i, column=0, sticky="n", padx=5, pady=5)
            
            frm.place(relx=0.76, rely=0.60, anchor= CENTER)
            
            
            lbl_time1_scoreboard_font = ("Dotum", 28)
            lbl_time1_scoreboard = tk.Label(Pagina_Final, text= f"{final_winner.name}", bg= "#FCE6C9", width= 46, height= 1, bd=4, relief="solid", font= lbl_time1_scoreboard_font)
            lbl_time1_scoreboard.place(relx=0.2, rely=0.28, anchor= CENTER)
            
            btn_font = ("Dotum", 23)
            btn_sair = tk.Button(Pagina_Final, text= "Fechar Aplicação", width=25, height=2, font= btn_font, command= lambda: (Pagina_Final.destroy(), sys.exit()))
            btn_sair.place(relx=0.3, rely=0.85, anchor= CENTER)
            btn_recomecar = tk.Button(Pagina_Final, text= "Recomeçar Aplicação", width=25, height=2, font= btn_font, command= lambda: Recomecar())
            btn_recomecar.place(relx=0.7, rely=0.85, anchor= CENTER)
            
            winning_players_stats = {}

            for player in final_winner.players:
                    winning_players_stats[player.name] = {
                    "Kills": player.killstotal,
                    "Deaths": player.deathstotal,
                    "Rating": player.killstotal / player.deathstotal if player.deathstotal != 0 else player.killstotal
                    }
                    
            win_player_stats = dict(sorted(winning_players_stats.items(), key=lambda x: x[1]['Rating'], reverse=True))
            
            win_melhor = list(win_player_stats.keys())[0] if win_player_stats else None
            win_melhor_stats = win_player_stats[win_melhor]
            win_melhor_kills = win_melhor_stats["Kills"]
            win_melhor_deaths = win_melhor_stats["Deaths"]
            win_melhor_rating = round(win_melhor_stats["Rating"], 2)
            
            win_segundo = list(win_player_stats.keys())[1] if win_player_stats else None
            win_segundo_stats = win_player_stats[win_segundo]
            win_segundo_kills = win_segundo_stats["Kills"]
            win_segundo_deaths = win_segundo_stats["Deaths"]
            win_segundo_rating = round(win_segundo_stats["Rating"], 2)
            
            win_terceiro = list(win_player_stats.keys())[2] if win_player_stats else None
            win_terceiro_stats = win_player_stats[win_terceiro]
            win_terceiro_kills = win_terceiro_stats["Kills"]
            win_terceiro_deaths = win_terceiro_stats["Deaths"]
            win_terceiro_rating = round(win_terceiro_stats["Rating"], 2)
            
            win_quarto = list(win_player_stats.keys())[3] if win_player_stats else None
            win_quarto_stats = win_player_stats[win_quarto]
            win_quarto_kills = win_quarto_stats["Kills"]
            win_quarto_deaths = win_quarto_stats["Deaths"]
            win_quarto_rating = round(win_quarto_stats["Rating"], 2)
            
            win_ultimo = list(win_player_stats.keys())[4] if win_player_stats else None
            win_ultimo_stats = win_player_stats[win_ultimo]
            win_ultimo_kills = win_ultimo_stats["Kills"]
            win_ultimo_deaths = win_ultimo_stats["Deaths"]
            win_ultimo_rating = round(win_ultimo_stats["Rating"], 2)
            
            lbl_time1_jogador_font = ("Dotum", 22)
            lbl_header_time1 = tk.Label(Pagina_Final, text= "Nick", bg= "#FCE6C9", width= 35, height= 1, bd=4, relief="solid", font= lbl_time1_jogador_font)
            lbl_header_time1.place(relx=0.1, rely=0.32, anchor= CENTER)
            lbl_header_time1_kills = tk.Label(Pagina_Final, text= "K", bg= "#A2CD5A", width= 5, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
            lbl_header_time1_kills.place(relx=0.28, rely=0.32, anchor= CENTER)
            lbl_header_time1_deaths = tk.Label(Pagina_Final, text= "D", bg= "tomato1", width= 5, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
            lbl_header_time1_deaths.place(relx=0.33, rely=0.32, anchor= CENTER)
            lbl_header_time1_rating = tk.Label(Pagina_Final, text= "Rating", bg= "#FCE6C9", width= 12, height= 1, bd=4, relief="solid", font= lbl_time1_jogador_font)
            lbl_header_time1_rating.place(relx=0.41, rely=0.32, anchor= CENTER)
            
            lbl_melhor_time1 = tk.Label(Pagina_Final, text= f"{win_melhor}", bg= "#FCE6C9", width= 35, height= 1, bd=4, relief="solid", font= lbl_time1_jogador_font)
            lbl_melhor_time1.place(relx=0.1, rely=0.36, anchor= CENTER)
            lbl_melhor_time1_kills = tk.Label(Pagina_Final, text= f"{win_melhor_kills}", bg= "#A2CD5A", width= 5, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
            lbl_melhor_time1_kills.place(relx=0.28, rely=0.36, anchor= CENTER)
            lbl_melhor_time1_deaths = tk.Label(Pagina_Final, text= f"{win_melhor_deaths}", bg= "tomato1", width= 5, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
            lbl_melhor_time1_deaths.place(relx=0.33, rely=0.36, anchor= CENTER)
            lbl_melhor_time1_rating = tk.Label(Pagina_Final, text= f"{win_melhor_rating}", bg= "#FCE6C9", width= 12, height= 1, bd=4, relief="solid", font= lbl_time1_jogador_font, fg="darkgreen" if win_melhor_rating > 1.10 else ("yellow3" if win_melhor_rating >= 0.90 else "red4"))
            lbl_melhor_time1_rating.place(relx=0.41, rely=0.36, anchor= CENTER)
            
            lbl_segundo_time1 = tk.Label(Pagina_Final, text= f"{win_segundo}", bg= "#FCE6C9", width= 35, height= 1, bd=4, relief="solid", font= lbl_time1_jogador_font)
            lbl_segundo_time1.place(relx=0.1, rely=0.40, anchor= CENTER)
            lbl_segundo_time1_kills = tk.Label(Pagina_Final, text= f"{win_segundo_kills}", bg= "#A2CD5A", width= 5, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
            lbl_segundo_time1_kills.place(relx=0.28, rely=0.40, anchor= CENTER)
            lbl_segundo_time1_deaths = tk.Label(Pagina_Final, text= f"{win_segundo_deaths}", bg= "tomato1", width= 5, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
            lbl_segundo_time1_deaths.place(relx=0.33, rely=0.40, anchor= CENTER)
            lbl_segundo_time1_rating = tk.Label(Pagina_Final, text= f"{win_segundo_rating}", bg= "#FCE6C9", width= 12, height= 1, bd=4, relief="solid", font= lbl_time1_jogador_font, fg="darkgreen" if win_segundo_rating > 1.10 else ("yellow3" if win_segundo_rating >= 0.90 else "red4"))
            lbl_segundo_time1_rating.place(relx=0.41, rely=0.40, anchor= CENTER)
            
            lbl_terceiro_time1 = tk.Label(Pagina_Final, text= f"{win_terceiro}", bg= "#FCE6C9", width= 35, height= 1, bd=4, relief="solid", font= lbl_time1_jogador_font)
            lbl_terceiro_time1.place(relx=0.1, rely=0.44, anchor= CENTER)
            lbl_terceiro_time1_kills = tk.Label(Pagina_Final, text= f"{win_terceiro_kills}", bg= "#A2CD5A", width= 5, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
            lbl_terceiro_time1_kills.place(relx=0.28, rely=0.44, anchor= CENTER)
            lbl_terceiro_time1_deaths = tk.Label(Pagina_Final, text= f"{win_terceiro_deaths}", bg= "tomato1", width= 5, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
            lbl_terceiro_time1_deaths.place(relx=0.33, rely=0.44, anchor= CENTER)
            lbl_terceiro_time1_rating = tk.Label(Pagina_Final, text= f"{win_terceiro_rating}", bg= "#FCE6C9", width= 12, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font, fg="darkgreen" if win_terceiro_rating > 1.10 else ("yellow3" if win_terceiro_rating >= 0.90 else "red4"))
            lbl_terceiro_time1_rating.place(relx=0.41, rely=0.44, anchor= CENTER)
            
            lbl_quarto_time1 = tk.Label(Pagina_Final, text= f"{win_quarto}", bg= "#FCE6C9", width= 35, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
            lbl_quarto_time1.place(relx=0.1, rely=0.48, anchor= CENTER)
            lbl_quarto_time1_kills = tk.Label(Pagina_Final, text= f"{win_quarto_kills}", bg= "#A2CD5A", width= 5, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
            lbl_quarto_time1_kills.place(relx=0.28, rely=0.48, anchor= CENTER)
            lbl_quarto_time2_deaths = tk.Label(Pagina_Final, text= f"{win_quarto_deaths}", bg= "tomato1", width= 5, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
            lbl_quarto_time2_deaths.place(relx=0.33, rely=0.48, anchor= CENTER)
            lbl_quarto_time1_rating = tk.Label(Pagina_Final, text= f"{win_quarto_rating}", bg= "#FCE6C9", width= 12, height= 1, bd=4, relief="solid", font= lbl_time1_jogador_font, fg="darkgreen" if win_quarto_rating > 1.10 else ("yellow3" if win_quarto_rating >= 0.90 else "red4"))
            lbl_quarto_time1_rating.place(relx=0.41, rely=0.48, anchor= CENTER)
            
            lbl_quinto_time1 = tk.Label(Pagina_Final, text= f"{win_ultimo}", bg= "#FCE6C9", width= 35, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
            lbl_quinto_time1.place(relx=0.1, rely=0.52, anchor= CENTER)
            lbl_quinto_time1_kills = tk.Label(Pagina_Final, text= f"{win_ultimo_kills}", bg= "#A2CD5A", width= 5, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
            lbl_quinto_time1_kills.place(relx=0.28, rely=0.52, anchor= CENTER)
            lbl_quinto_time1_deaths = tk.Label(Pagina_Final, text= f"{win_ultimo_deaths}", bg= "tomato1", width= 5, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font)
            lbl_quinto_time1_deaths.place(relx=0.33, rely=0.52, anchor= CENTER)
            lbl_quinto_time1_rating = tk.Label(Pagina_Final, text= f"{win_ultimo_rating}", bg= "#FCE6C9", width= 12, height= 1, bd=5, relief="solid", font= lbl_time1_jogador_font, fg="darkgreen" if win_ultimo_rating > 1.10 else ("yellow3" if win_ultimo_rating >= 0.90 else "red4"))
            lbl_quinto_time1_rating.place(relx=0.41, rely=0.52, anchor= CENTER)
            
            
            
            
            
            
            lbl_time2_scoreboard_font = ("Dotum", 28)
            lbl_time2_scoreboard = tk.Label(Pagina_Final, text= f"{final_loser.name}", bg= "#FCE6C9", width= 46, height= 1, bd=4, relief="solid", font= lbl_time2_scoreboard_font)
            lbl_time2_scoreboard.place(relx=0.8, rely=0.28, anchor= CENTER)
            
            losing_players_stats = {}

            for player in final_loser.players:
                losing_players_stats[player.name] = {
                    "Kills": player.killstotal,
                    "Deaths": player.deathstotal,
                    "Rating": player.killstotal / player.deathstotal if player.deathstotal != 0 else player.killstotal
                }
                
            loss_player_stats = dict(sorted(losing_players_stats.items(), key=lambda x: x[1]['Rating'], reverse=True))
            
            loss_melhor = list(loss_player_stats.keys())[0] if loss_player_stats else None
            loss_melhor_stats = loss_player_stats[loss_melhor]
            loss_melhor_kills = loss_melhor_stats["Kills"]
            loss_melhor_deaths = loss_melhor_stats["Deaths"]
            loss_melhor_rating = round(loss_melhor_stats["Rating"], 2)
            
            loss_segundo = list(loss_player_stats.keys())[1] if loss_player_stats else None
            loss_segundo_stats = loss_player_stats[loss_segundo]
            loss_segundo_kills = loss_segundo_stats["Kills"]
            loss_segundo_deaths = loss_segundo_stats["Deaths"]
            loss_segundo_rating = round(loss_segundo_stats["Rating"], 2)
            
            loss_terceiro = list(loss_player_stats.keys())[2] if loss_player_stats else None
            loss_terceiro_stats = loss_player_stats[loss_terceiro]
            loss_terceiro_kills = loss_terceiro_stats["Kills"]
            loss_terceiro_deaths = loss_terceiro_stats["Deaths"]
            loss_terceiro_rating = round(loss_terceiro_stats["Rating"], 2)
            
            loss_quarto = list(loss_player_stats.keys())[3] if loss_player_stats else None
            loss_quarto_stats = loss_player_stats[loss_quarto]
            loss_quarto_kills = loss_quarto_stats["Kills"]
            loss_quarto_deaths = loss_quarto_stats["Deaths"]
            loss_quarto_rating = round(loss_quarto_stats["Rating"], 2)
            
            loss_ultimo = list(loss_player_stats.keys())[4] if loss_player_stats else None
            loss_ultimo_stats = loss_player_stats[loss_ultimo]
            loss_ultimo_kills = loss_ultimo_stats["Kills"]
            loss_ultimo_deaths = loss_ultimo_stats["Deaths"]
            loss_ultimo_rating = round(loss_ultimo_stats["Rating"], 2)
            
            lbl_time2_jogador_font = ("Dotum", 22)
            
            lbl_header_time2 = tk.Label(Pagina_Final, text= "Nick", bg= "#FCE6C9", width= 35, height= 1, bd=4, relief="solid", font= lbl_time1_jogador_font)
            lbl_header_time2.place(relx=0.9, rely=0.32, anchor= CENTER)
            lbl_header_time2_kills = tk.Label(Pagina_Final, text= "K", bg= "#A2CD5A", width= 6, height= 1, bd=4, relief="solid", font= lbl_time1_jogador_font)
            lbl_header_time2_kills.place(relx=0.72, rely=0.32, anchor= CENTER)
            lbl_header_time2_deaths = tk.Label(Pagina_Final, text= "D", bg= "tomato1", width= 5, height= 1, bd=4, relief="solid", font= lbl_time1_jogador_font)
            lbl_header_time2_deaths.place(relx=0.67, rely=0.32, anchor= CENTER)
            lbl_header_time2_rating = tk.Label(Pagina_Final, text= "Rating", bg= "#FCE6C9", width= 12, height= 1, bd=4, relief="solid", font= lbl_time1_jogador_font)
            lbl_header_time2_rating.place(relx=0.59, rely=0.32, anchor= CENTER)
            
            lbl_melhor_time2 = tk.Label(Pagina_Final, text= f"{loss_melhor}", bg= "#FCE6C9", width= 35, height= 1, bd=4, relief="solid", font= lbl_time2_jogador_font)
            lbl_melhor_time2.place(relx=0.9, rely=0.36, anchor= CENTER)
            lbl_melhor_time2_kills = tk.Label(Pagina_Final, text= f"{loss_melhor_kills}", bg= "#A2CD5A", width= 6, height= 1, bd=4, relief="solid", font= lbl_time2_jogador_font)
            lbl_melhor_time2_kills.place(relx=0.72, rely=0.36, anchor= CENTER)
            lbl_melhor_time2_deaths = tk.Label(Pagina_Final, text= f"{loss_melhor_deaths}", bg= "tomato1", width= 5, height= 1, bd=4, relief="solid", font= lbl_time2_jogador_font)
            lbl_melhor_time2_deaths.place(relx=0.67, rely=0.36, anchor= CENTER)
            lbl_melhor_time2_rating = tk.Label(Pagina_Final, text= f"{loss_melhor_rating}", bg= "#FCE6C9", width= 12, height= 1, bd=4, relief="solid", font= lbl_time2_jogador_font, fg="darkgreen" if loss_melhor_rating > 1.10 else ("yellow3" if loss_ultimo_rating >= 0.90 else "red4"))
            lbl_melhor_time2_rating.place(relx=0.59, rely=0.36, anchor= CENTER)
            
            lbl_segundo_time2 = tk.Label(Pagina_Final, text= f"{loss_segundo}", bg= "#FCE6C9", width= 35, height= 1, bd=4, relief="solid", font= lbl_time2_jogador_font)
            lbl_segundo_time2.place(relx=0.9, rely=0.40, anchor= CENTER)
            lbl_segundo_time2_kills = tk.Label(Pagina_Final, text= f"{loss_segundo_kills}", bg= "#A2CD5A", width= 6, height= 1, bd=4, relief="solid", font= lbl_time2_jogador_font)
            lbl_segundo_time2_kills.place(relx=0.72, rely=0.40, anchor= CENTER)
            lbl_segundo_time2_deaths = tk.Label(Pagina_Final, text= f"{loss_segundo_deaths}", bg= "tomato1", width= 5, height= 1, bd=4, relief="solid", font= lbl_time2_jogador_font)
            lbl_segundo_time2_deaths.place(relx=0.67, rely=0.40, anchor= CENTER)
            lbl_segundo_time2_rating = tk.Label(Pagina_Final, text= f"{loss_segundo_rating}", bg= "#FCE6C9", width= 12, height= 1, bd=4, relief="solid", font= lbl_time2_jogador_font, fg="darkgreen" if loss_segundo_rating > 1.10 else ("yellow3" if loss_segundo_rating >= 0.90 else "red4"))
            lbl_segundo_time2_rating.place(relx=0.59, rely=0.40, anchor= CENTER)
            
            lbl_terceiro_time2 = tk.Label(Pagina_Final, text= f"{loss_terceiro}", bg= "#FCE6C9", width= 35, height= 1, bd=4, relief="solid", font= lbl_time2_jogador_font)
            lbl_terceiro_time2.place(relx=0.9, rely=0.44, anchor= CENTER)
            lbl_terceiro_time2_kills = tk.Label(Pagina_Final, text= f"{loss_terceiro_kills}", bg= "#A2CD5A", width= 6, height= 1, bd=5, relief="solid", font= lbl_time2_jogador_font)
            lbl_terceiro_time2_kills.place(relx=0.72, rely=0.44, anchor= CENTER)
            lbl_terceiro_time2_deaths = tk.Label(Pagina_Final, text= f"{loss_terceiro_deaths}", bg= "tomato1", width= 5, height= 1, bd=5, relief="solid", font= lbl_time2_jogador_font)
            lbl_terceiro_time2_deaths.place(relx=0.67, rely=0.44, anchor= CENTER)
            lbl_terceiro_time2_rating = tk.Label(Pagina_Final, text= f"{loss_terceiro_rating}", bg= "#FCE6C9", width= 12, height= 1, bd=5, relief="solid", font= lbl_time2_jogador_font, fg="darkgreen" if loss_terceiro_rating > 1.10 else ("yellow3" if loss_terceiro_rating >= 0.90 else "red4"))
            lbl_terceiro_time2_rating.place(relx=0.59, rely=0.44, anchor= CENTER)
            
            lbl_quarto_time2 = tk.Label(Pagina_Final, text= f"{loss_quarto}", bg= "#FCE6C9", width= 35, height= 1, bd=5, relief="solid", font= lbl_time2_jogador_font)
            lbl_quarto_time2.place(relx=0.9, rely=0.48, anchor= CENTER)
            lbl_quarto_time2_kills = tk.Label(Pagina_Final, text= f"{loss_quarto_kills}", bg= "#A2CD5A", width= 6, height= 1, bd=5, relief="solid", font= lbl_time2_jogador_font)
            lbl_quarto_time2_kills.place(relx=0.72, rely=0.48, anchor= CENTER)
            lbl_quarto_time2_deaths = tk.Label(Pagina_Final, text= f"{loss_quarto_deaths}", bg= "tomato1", width= 5, height= 1, bd=5, relief="solid", font= lbl_time2_jogador_font)
            lbl_quarto_time2_deaths.place(relx=0.67, rely=0.48, anchor= CENTER)
            lbl_quarto_time2_rating = tk.Label(Pagina_Final, text= f"{loss_quarto_rating}", bg= "#FCE6C9", width= 12, height= 1, bd=5, relief="solid", font= lbl_time2_jogador_font, fg="darkgreen" if loss_quarto_rating > 1.10 else ("yellow3" if loss_quarto_rating >= 0.90 else "red4"))
            lbl_quarto_time2_rating.place(relx=0.59, rely=0.48, anchor= CENTER)
            
            lbl_quinto_time2 = tk.Label(Pagina_Final, text= f"{loss_ultimo}", bg= "#FCE6C9", width= 35, height= 1, bd=5, relief="solid", font= lbl_time2_jogador_font)
            lbl_quinto_time2.place(relx=0.9, rely=0.52, anchor= CENTER)
            lbl_quinto_time2_kills = tk.Label(Pagina_Final, text= f"{loss_ultimo_kills}", bg= "#A2CD5A", width= 6, height= 1, bd=5, relief="solid", font= lbl_time2_jogador_font)
            lbl_quinto_time2_kills.place(relx=0.72, rely=0.52, anchor= CENTER)
            lbl_quinto_time2_deaths = tk.Label(Pagina_Final, text= f"{loss_ultimo_deaths}", bg= "tomato1", width= 5, height= 1, bd=5, relief="solid", font= lbl_time2_jogador_font)
            lbl_quinto_time2_deaths.place(relx=0.67, rely=0.52, anchor= CENTER)
            lbl_quinto_time2_rating = tk.Label(Pagina_Final, text=f"{loss_ultimo_rating}", bg="#FCE6C9", width=12, height=1, bd=5, relief="solid", font=lbl_time2_jogador_font, fg="darkgreen" if loss_ultimo_rating > 1.10 else ("yellow3" if loss_ultimo_rating >= 0.90 else "red4"))
            lbl_quinto_time2_rating.place(relx=0.59, rely=0.52, anchor= CENTER)
            
            
            most_kills_player = max(final_winner.players + final_loser.players, key=lambda p: p.killstotal)
            most_deaths_player = max(final_winner.players + final_loser.players, key=lambda p: p.deathstotal)
            
            map_data = []
            
            for mapa_nome, winner_name, loser_name, loser_rounds in mapas_results:
                map_data.append((mapa_nome, winner_name))
            
            # Chamando o Cursor para poder executar as queries no mysql
            Cursor = conn.cursor()

            # Montando a query "dinamica"
            insert_query = "INSERT INTO Partidas (TimeVencedor, TimePerdedor"

            for i, (mapa_nome, winner_name) in enumerate(map_data, start=1):
                insert_query += f", Mapa{i}, Mapa{i}Vencedor"

            insert_query += ") VALUES (%s, %s"

            for _ in map_data:
                insert_query += ", %s, %s"

            insert_query += ")"

            data = [final_winner.name, final_loser.name]
            
            for map_nome, winner_name in map_data:
                data.extend([map_nome, winner_name])

            # Execute a query completa
            Cursor.execute(insert_query, data)
            conn.commit()
            
            # Execute a query para retirar dados que serao usados no grafico
            Cursor.execute("select MapsPlayed from PlayerGeralStats where MapsPlayed >= 0;")
            result = Cursor.fetchall()

            Qnt_Mapas_Jogados = []
         
            for i in result:
                Qnt_Mapas_Jogados.append(i[0])

            Media_Mapas_Jogados = sum(Qnt_Mapas_Jogados) / len(Qnt_Mapas_Jogados) if len(Qnt_Mapas_Jogados) > 0 else 0
            Media_Busca = round(Media_Mapas_Jogados - (Media_Mapas_Jogados * 0.7))
            print(Media_Busca, Media_Mapas_Jogados)
            
            Cursor.execute(f"select Nick, Team, AverageRating, KPR, DPR, MapsPlayed, Rounds from PlayerGeralStats where MapsPlayed >= {Media_Busca};")
            result = Cursor.fetchall

            Nicks = []
            KPR = []
            DPR = []
         
            for i in Cursor:
                Nicks.append(i[0])
                KPR.append(i[3])
                DPR.append(i[4])
                
            fig, ax = plt.subplots(figsize=(35, 35))
            
            # Defina os limites da área do gráfico (left, bottom, width, height)
            left, bottom, width, height = 0.05, 0.05, 0.90, 0.90
            ax = fig.add_axes([left, bottom, width, height])
            try:
                
                # Define os pontos
                ax.scatter = ax.scatter(KPR, DPR, marker='o', color='black')
            
                max_kpr = max(KPR)
                min_kpr = min(KPR)
                min_dpr = min(DPR)
                max_dpr = max(DPR)
                
                # Defina o limite máximo dos eixos com margem de 0.01
                
                max_dprtick = max_dpr + 0.01
                max_kprtick = max_kpr + 0.01
                min_dprtick = min_dpr - 0.01
                min_kprtick = min_kpr - 0.01
                
                ax.set_xlim(min_kprtick, max_kprtick)
                ax.set_ylim(min_dprtick, max_dprtick)
            
                # Separando os ticks para uma melhor vizualização, dependendo dos limites.
            
                if max_dprtick >= 0.60:
                            refmax_dprtick = max_dprtick
                if max_dprtick >= 0.90:
                    if min_dprtick < 0.10:
                        refmin_dprtick = min_dprtick
                        DPRticks = [max_dprtick, 0.90, 0.80, 0.70, 0.60, 0.50, 0.40, 0.30, 0.20, 0.10, min_dprtick]
                    elif min_dprtick < 0.20 and min_dprtick >= 0.10:
                        refmin_dprtick = 0.10
                        DPRticks = [max_dprtick, 0.90, 0.80, 0.70, 0.60, 0.50, 0.40, 0.30, 0.20, min_dprtick]
                    elif min_dprtick < 0.30 and min_dprtick >= 0.20:
                        refmin_dprtick = 0.20
                        DPRticks = [max_dprtick, 0.90, 0.80, 0.70, 0.60, 0.50, 0.40, 0.30, min_dprtick]
                    elif min_dprtick < 0.40 and min_dprtick >= 0.30:
                        refmin_dprtick = 0.30
                        DPRticks = [max_dprtick, 0.90, 0.80, 0.70, 0.60, 0.50, 0.40, min_dprtick]
                    elif min_dprtick < 0.50 and min_dprtick >= 0.40:
                        refmin_dprtick = 0.40
                        DPRticks = [max_dprtick, 0.90, 0.80, 0.70, 0.60, 0.50, min_dprtick]
                    elif min_dprtick < 0.60 and min_dprtick >= 0.50:
                        refmin_dprtick = 0.50
                        DPRticks = [max_dprtick, 0.90, 0.80, 0.70, 0.60, min_dprtick]
                    elif min_dprtick < 0.70 and min_dprtick >= 0.60:
                        refmin_dprtick = 0.60
                        DPRticks = [max_dprtick, 0.90, 0.80, 0.70, min_dprtick]
                elif max_dprtick >= 0.80:
                    if min_dprtick < 0.10:
                        refmin_dprtick = min_dprtick
                        DPRticks = [max_dprtick, 0.80, 0.70, 0.60, 0.50, 0.40, 0.30, 0.20, 0.10, min_dprtick]
                    elif min_dprtick < 0.20 and min_dprtick >= 0.10:
                        refmin_dprtick = 0.10
                        DPRticks = [max_dprtick, 0.80, 0.70, 0.60, 0.50, 0.40, 0.30, 0.20, min_dprtick]
                    elif min_dprtick < 0.30 and min_dprtick >= 0.20:
                        refmin_dprtick = 0.20
                        DPRticks = [max_dprtick, 0.80, 0.70, 0.60, 0.50, 0.40, 0.30, min_dprtick]
                    elif min_dprtick < 0.40 and min_dprtick >= 0.30:
                        refmin_dprtick = 0.30
                        DPRticks = [max_dprtick, 0.80, 0.70, 0.60, 0.50, 0.40, min_dprtick]
                    elif min_dprtick < 0.50 and min_dprtick >= 0.40:
                        refmin_dprtick = 0.40
                        DPRticks = [max_dprtick, 0.80, 0.70, 0.60, 0.50, min_dprtick]
                    elif min_dprtick < 0.60 and min_dprtick >= 0.50:
                        refmin_dprtick = 0.50
                        DPRticks = [max_dprtick, 0.80, 0.70, 0.60, min_dprtick]
                    elif min_dprtick < 0.70 and min_dprtick >= 0.60:
                        refmin_dprtick = 0.60
                        DPRticks = [max_dprtick, 0.80, 0.70, min_dprtick]
                        
                elif max_dprtick >= 0.70:
                    if min_dprtick < 0.10:
                        refmin_dprtick = min_dprtick
                        DPRticks = [max_dprtick, 0.70, 0.60, 0.50, 0.40, 0.30, 0.20, 0.10, min_dprtick]
                    elif min_dprtick < 0.20 and min_dprtick >= 0.10:
                        refmin_dprtick = 0.10
                        DPRticks = [max_dprtick, 0.70, 0.60, 0.50, 0.40, 0.30, 0.20, min_dprtick]
                    elif min_dprtick < 0.30 and min_dprtick >= 0.20:
                        refmin_dprtick = 0.20
                        DPRticks = [max_dprtick, 0.70, 0.60, 0.50, 0.40, 0.30, min_dprtick]
                    elif min_dprtick < 0.40 and min_dprtick >= 0.30:
                        refmin_dprtick = 0.30
                        DPRticks = [max_dprtick, 0.70, 0.60, 0.50, 0.40, min_dprtick]
                    elif min_dprtick < 0.50 and min_dprtick >= 0.40:
                        refmin_dprtick = 0.40
                        DPRticks = [max_dprtick, 0.70, 0.60, 0.50, min_dprtick]
                    elif min_dprtick < 0.60 and min_dprtick >= 0.50:
                        refmin_dprtick = 0.50
                        DPRticks = [max_dprtick, 0.70, 0.60, min_dprtick]
                    elif min_dprtick < 0.70 and min_dprtick >= 0.60:
                        refmin_dprtick = 0.60
                        DPRticks = [max_dprtick, 0.70, min_dprtick]
                        
                elif max_dprtick >= 0.60:
                    if min_dprtick < 0.10:
                        refmin_dprtick = min_dprtick
                        DPRticks = [max_dprtick, 0.60, 0.50, 0.40, 0.30, 0.20, 0.10, min_dprtick]
                    elif min_dprtick < 0.20 and min_dprtick >= 0.10:
                        refmin_dprtick = 0.10
                        DPRticks = [max_dprtick, 0.60, 0.50, 0.40, 0.30, 0.20, min_dprtick]
                    elif min_dprtick < 0.30 and min_dprtick >= 0.20:
                        refmin_dprtick = 0.20
                        DPRticks = [max_dprtick, 0.60, 0.50, 0.40, 0.30, min_dprtick]
                    elif min_dprtick < 0.40 and min_dprtick >= 0.30:
                        refmin_dprtick = 0.30
                        DPRticks = [max_dprtick, 0.60, 0.50, 0.40, min_dprtick]
                    elif min_dprtick < 0.50 and min_dprtick >= 0.40:
                        refmin_dprtick = 0.40
                        DPRticks = [max_dprtick, 0.60, 0.50, min_dprtick]
                    elif min_dprtick < 0.60 and min_dprtick >= 0.50:
                        refmin_dprtick = 0.50
                        DPRticks = [max_dprtick, 0.60, min_dprtick]
                    elif min_dprtick < 0.70 and min_dprtick >= 0.60:
                        refmin_dprtick = 0.60
                        DPRticks = [max_dprtick, min_dprtick]
                    
                    
                if max_kprtick > 0.90:
                    refmax_kprtick = max_kprtick
                else:
                    refmax_kprtick = max_kprtick

                if min_kprtick < 0.10:
                    refmin_kprtick = min_kprtick
                    if max_kprtick <= 0.60:
                        KPRticks = [max_kprtick, 0.50, 0.40, 0.30, 0.20, 0.10, min_kprtick]
                        refmax_kprtick = 1.0
                    elif max_kprtick <= 0.70:
                        KPRticks = [max_kprtick, 0.60, 0.50, 0.40, 0.30, 0.20, 0.10, min_kprtick]
                    elif max_kprtick <= 0.80:
                        KPRticks = [max_kprtick, 0.70, 0.60, 0.50, 0.40, 0.30, 0.20, 0.10, min_kprtick]
                    elif max_kprtick <= 0.90:
                        KPRticks = [max_kprtick, 0.80, 0.70, 0.60, 0.50, 0.40, 0.30, 0.20, 0.10, min_kprtick]  
                    else:
                        KPRticks = [max_kprtick, 0.90, 0.80, 0.70, 0.60, 0.50, 0.40, 0.30, 0.20, 0.10, min_kprtick]
                        
                elif min_kprtick < 0.20 and min_kprtick >= 0.10:
                    refmin_kprtick = min_kprtick
                    if max_kprtick <= 0.60:
                        KPRticks = [max_kprtick, 0.50, 0.40, 0.30, 0.20, min_kprtick]
                        refmax_kprtick = 1.0
                    elif max_kprtick <= 0.70:
                        KPRticks = [max_kprtick, 0.60, 0.50, 0.40, 0.30, 0.20, min_kprtick]
                    elif max_kprtick <= 0.80:
                        KPRticks = [max_kprtick, 0.70, 0.60, 0.50, 0.40, 0.30, 0.20, min_kprtick]
                    elif max_kprtick <= 0.90:
                        KPRticks = [max_kprtick, 0.80, 0.70, 0.60, 0.50, 0.40, 0.30, 0.20, min_kprtick]
                    else:
                        KPRticks = [max_kprtick, 0.90, 0.80, 0.70, 0.60, 0.50, 0.40, 0.30, 0.20, min_kprtick]
                        
                elif min_kprtick < 0.30 and min_kprtick >= 0.20:
                    refmin_kprtick = min_kprtick
                    if max_kprtick <= 0.60:
                        KPRticks = [max_kprtick, 0.50, 0.40, 0.30, min_kprtick]
                        refmax_kprtick = 1.0
                    elif max_kprtick <= 0.70:
                        KPRticks = [max_kprtick, 0.60, 0.50, 0.40, 0.30, min_kprtick]
                    elif max_kprtick <= 0.80:
                        KPRticks = [max_kprtick, 0.70, 0.60, 0.50, 0.40, 0.30, min_kprtick]
                    elif max_kprtick <= 0.90:
                        KPRticks = [max_kprtick, 0.80, 0.70, 0.60, 0.50, 0.40, 0.30, min_kprtick]   
                    else:
                        KPRticks = [max_kprtick, 0.90, 0.80, 0.70, 0.60, 0.50, 0.40, 0.30, min_kprtick]
                        
                elif min_kprtick < 0.40 and min_kprtick >= 0.30:
                    refmin_kprtick = min_kprtick
                    if max_kprtick <= 0.60:
                        KPRticks = [max_kprtick, 0.50, 0.40, min_kprtick]
                        refmax_kprtick = 1.0
                    elif max_kprtick <= 0.70:
                        KPRticks = [max_kprtick, 0.60, 0.50, 0.40, min_kprtick]
                    elif max_kprtick <= 0.80:
                        KPRticks = [max_kprtick, 0.70, 0.60, 0.50, 0.40, min_kprtick]
                    elif max_kprtick <= 0.90:
                        KPRticks = [max_kprtick, 0.80, 0.70, 0.60, 0.50, 0.40, min_kprtick]
                    else:
                        KPRticks = [max_kprtick, 0.90, 0.80, 0.70, 0.60, 0.50, 0.40, min_kprtick]
                        
                elif min_kprtick < 0.50 and min_kprtick >= 0.40:
                    refmin_kprtick = min_kprtick
                    if max_kprtick <= 0.60:
                        KPRticks = [max_kprtick, 0.50, min_kprtick]
                        refmax_kprtick = 1.0
                    elif max_kprtick <= 0.70:
                        KPRticks = [max_kprtick, 0.60, 0.50, min_kprtick]
                    elif max_kprtick <= 0.80:
                        KPRticks = [max_kprtick, 0.70, 0.60, 0.50, min_kprtick]
                    elif max_kprtick <= 0.90:
                        KPRticks = [max_kprtick, 0.80, 0.70, 0.60, 0.50, min_kprtick]   
                    else:
                        KPRticks = [max_kprtick, 0.90, 0.80, 0.70, 0.60, 0.50, min_kprtick]
                        
                elif min_kprtick < 0.60 and min_kprtick >= 0.50:
                    refmin_kprtick = min_kprtick
                    if max_kprtick <= 0.60:
                        KPRticks = [max_kprtick, min_kprtick]
                        refmax_kprtick = 1.0
                    elif max_kprtick <= 0.70:
                        KPRticks = [max_kprtick, 0.60, min_kprtick]
                    elif max_kprtick <= 0.80:
                        KPRticks = [max_kprtick, 0.70, 0.60, min_kprtick]
                    elif max_kprtick <= 0.90:
                        KPRticks = [max_kprtick, 0.80, 0.70, 0.60, min_kprtick]
                    else:
                        KPRticks = [max_kprtick, 0.90, 0.80, 0.70, 0.60, min_kprtick]
                    
                elif min_kprtick >= 0.60:
                    refmin_kprtick = min_kprtick
                    if max_kprtick <= 0.70:
                        KPRticks = [max_kprtick, min_kprtick]
                    elif max_kprtick <= 0.80:
                        KPRticks = [max_kprtick, 0.70, min_kprtick]
                    elif max_kprtick <= 0.90:
                        KPRticks = [max_kprtick, 0.80, 0.70, min_kprtick]
                    else:
                        KPRticks = [max_kprtick, 0.90, 0.80, 0.70, min_kprtick]
            
                all_y_ticks = DPRticks
                all_x_ticks = KPRticks

                ax.set_yticks(all_y_ticks)
                ax.set_xticks(all_x_ticks)
            
                #Fundo do Gráfico
                import matplotlib.image as mpimg

                # Carregar a imagem
                background_img = mpimg.imread('E:/@Raphael/Futebol/fotos/RESIZE.jpg')
                ax.imshow(background_img, extent=[refmin_kprtick, refmax_kprtick, refmax_dprtick, refmin_dprtick], aspect='auto', zorder=-1, interpolation='none')

                #Fundo das label de fora do titulo etc
                fig.set_facecolor("black")

                ax.set_ylabel('DPR', fontsize=12, color="white")

                ax.set_xlabel('KPR', fontsize=12, color="white")

                ax.set_title('KPR e DPR CSGO', fontsize=17, color="white")
                
                # Array da lista de pontos
                x = np.array(KPR)
                y = np.array(DPR)
            
                #Linha de tendência (1, Reta)
                slope, intercept = np.polyfit(x, y, 1)
                trend_line = slope * x + intercept
                
                # Media do Gráfico
                average_dpr = np.mean(y)
                average_kpr = np.mean(x)
                
                plt.plot(KPR, trend_line, color='gray', label='Trend Line', alpha = 1, zorder=2)
                
                ax.grid(True, linestyle='dotted', color='black', alpha=0.2, zorder=16)
                ax.axhline(average_dpr, color='b', linestyle='--', label='Average DPR')
                ax.axvline(average_kpr, color='b', linestyle='--', label='Average KPR')

                # Cor dos valores que ficam ao lado como referencia
                ax.tick_params(axis='both', colors='white')
                
                # Adicione as anotações (Nome do Jogador) após desenhar a trend line
                for i, (nome, KPR_val, DPR_val) in enumerate(zip(Nicks, KPR, DPR)):
                    
                    if len(nome) > 11:
                        xytext = (KPR_val - 0.011, DPR_val - 0.0027)
                    elif len(nome) > 9:
                        xytext = (KPR_val - 0.0086, DPR_val - 0.0027)
                    elif len(nome) > 7:
                        xytext = (KPR_val - 0.008, DPR_val - 0.0027)
                    elif len(nome) > 5:
                        xytext = (KPR_val - 0.007, DPR_val - 0.0027)
                    elif len(nome) > 3:
                        xytext = (KPR_val - 0.0047, DPR_val - 0.0027)
                    else:
                        xytext = (KPR_val - 0.0023, DPR_val - 0.0027)
                        
                    # Escrever no ponto o Nome e Valor do Rating
                    annotation_text = f'{nome}'  # Inclua o Nome na anotação
                    ax.annotate(
                            annotation_text,
                            xy=(KPR_val, DPR_val),
                            xytext = xytext,
                            color="black",
                            fontsize=9,
                            alpha=1,
                            zorder=5,
                            fontweight='bold',  
                            path_effects=[withStroke(linewidth=3, foreground='white')]
                            )
                
                # Inverter o eixo Y porque Deaths é uma estatística negativa
                ax.invert_yaxis()
                
                Cursor.close()
                
            except Exception as e:
                print("Erro: ", e)
            
        except Exception as e:
           print("Erro: ", e)


        def Recomecar():
            Pagina_Final.destroy() 
            Abrir_Pagina_Inicial()
        
        Pagina_Resultado_Mapa.destroy() 
        
        Pagina_Final.after(0, toggle_fullscreen, Pagina_Final)
        plt.show()
        Pagina_Final.mainloop()
    
Abrir_Pagina_Inicial()