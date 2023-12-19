-- Create e Use Database
create database CSPYTHON4;
use CSPYTHON4;

-- Criar Tabela Jogo, Campeonato, Mapa

CREATE TABLE IF NOT EXISTS StatsJogadoresPorPartida (
CODpartidajogador int auto_increment primary key,
Partidaidx int,
Nick VARCHAR (25) NULL,
Team VARCHAR(20) NULL,
Mapa VARCHAR (20) NULL,
Rounds INT NULL,
Kills Int NULL,
Deaths Int NULL,
Rating Float (3, 2) NULL);



CREATE TABLE Partidas (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    TimeVencedor VARCHAR(30),
    TimePerdedor VARCHAR(30),
    Mapa1 VARCHAR(20),
    Mapa1Vencedor VARCHAR(30),
    Mapa2 VARCHAR(20),
    Mapa2Vencedor VARCHAR(30),
    Mapa3 VARCHAR(20),
    Mapa3Vencedor VARCHAR(30));


CREATE TABLE IF NOT EXISTS PlayerGeralStats (
    PlayerID int auto_increment primary key,
    Nick VARCHAR (25) NULL,
    Team VARCHAR(20) NULL,
    TotalKills Int NULL,
    TotalDeaths Int NULL,
    KPR Float (3, 2) NULL,
    DPR Float (3, 2) NULL,
    Rounds INT NULL,
    AverageRating Float (3, 2) NULL,
    MapsPlayed Int NULL);
ALTER TABLE PlayerGeralStats
ADD CONSTRAINT uc_Nick UNIQUE (Nick);

DELIMITER $$
CREATE PROCEDURE AtualizarRegistros (IN nickjogador VARCHAR(25))
BEGIN
	DECLARE player_rating_total FLOAT(15, 2);
    DECLARE player_maps_played INT;
    DECLARE player_kills INT;
    DECLARE player_deaths INT;
    DECLARE player_exists INT;
    DECLARE player_rounds INT;
    DECLARE team VARCHAR(20);
    
    SELECT Team, SUM(Rating), COUNT(*), SUM(Kills), SUM(Deaths), SUM(Rounds) INTO team, player_rating_total, player_maps_played, player_kills, player_deaths, player_rounds
    FROM StatsJogadoresPorPartida
    WHERE Nick = nickjogador;
    
    SET @new_player_rating = IF(player_maps_played > 0, player_rating_total / player_maps_played, 0.00);
    
    SET @kpr = player_kills / player_rounds;
    SET @dpr = player_deaths / player_rounds;

    SELECT COUNT(*) INTO player_exists
    FROM PlayerGeralStats
    WHERE Nick = nickjogador;
    
    IF player_exists > 0 THEN
		UPDATE PlayerGeralStats
		SET Team = team, AverageRating = @new_player_rating , MapsPlayed = player_maps_played, TotalKills = player_kills, TotalDeaths = player_deaths, KPR = @kpr, DPR = @dpr, Rounds = player_rounds
		WHERE Nick = nickjogador;
	ELSE
        -- If player doesn't exist, insert a new record
        INSERT INTO PlayerGeralStats (Nick, Team, AverageRating, MapsPlayed, TotalKills, TotalDeaths, KPR, DPR, Rounds)
        VALUES (nickjogador, team, @new_player_rating, player_maps_played, player_kills, player_deaths, @kpr, @dpr, player_rounds);
    END IF;
END $$
DELIMITER ;
