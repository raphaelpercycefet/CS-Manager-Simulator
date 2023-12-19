-- Create e Use Database
DELIMITER // begin;
create database CSPYTHON4;
use CSPYTHON4;
end; DELIMITER;

-- Criar Tabela Jogo, Campeonato, Mapa
DELIMITER //
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
DELIMITER;

DELIMITER //
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
DELIMITER;

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

Call AtualizarRegistros('Niko');

select * from PlayerGeralStats;
select Nick, AverageRating, KPR, DPR, MapsPlayed, Rounds from PlayerGeralStats where MapsPlayed >= 0 and MapsPlayed < 25;
select * from Partidas;
select * from StatsJogadoresPorPartida;

truncate PlayerGeralStats;
truncate partidas;
truncate statsjogadoresporpartida;

SELECT * FROM PlayerGeralStats WHERE Nick = 'Keoz' OR Nick = 'Isak' OR Nick = 'iM' OR Nick = 'Siuhy' OR Nick = 'Acor';
SELECT * FROM PlayerGeralStats WHERE Nick = 'Fallen' OR Nick = 'Art' OR Nick = 'Kscerato' OR Nick = 'Yuurih' OR Nick = 'Chelo';
SELECT * FROM PlayerGeralStats WHERE Nick = 'Brnz4n' OR Nick = 'Insani' OR Nick = 'Drop' OR Nick = 'Saffee' OR Nick = 'Exit';
SELECT * FROM PlayerGeralStats WHERE Nick = 'Stavn' OR Nick = 'Cadian' OR Nick = 'Sjuush' OR Nick = 'Teses' OR Nick = 'Jabbi';
SELECT * FROM PlayerGeralStats WHERE Nick = 'Simple' OR Nick = 'Boombl4' OR Nick = 'Bit' OR Nick = 'Electronic' OR Nick = 'Perfecto';
SELECT * FROM PlayerGeralStats WHERE Nick = 'Flamez' OR Nick = 'Spinx' OR Nick = 'Apex' OR Nick = 'Zywoo' OR Nick = 'Magisk';

select * from PlayerGeralStats WHERE Nick = 'Twistzz' OR Nick = 'Rain'OR Nick = 'Ropz' OR Nick = 'Karrigan' OR Nick = 'Broky';

drop table StatsJogadoresPorPartida;
drop table Partidas;
drop table PlayerGeralStats;

drop procedure AtualizarRegistros;

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

SELECT * FROM statsjogadoresporpartida;

SELECT COUNT(*)
    FROM PlayerGeralStats
    WHERE Nick = "Niko";

Call AtualizarRegistros("Niko");

SELECT * FROM playergeralstats;

SELECT Nick, SUM(Rating)/COUNT(*) as Rating, COUNT(*) as Mapas, SUM(Kills) as Kills, SUM(Deaths) as Deaths, SUM(Rounds) as Rounds, SUM(Kills)/SUM(Rounds) as KPR FROM StatsJogadoresPorPartida group by Nick order by KPR DESC;

SELECT SUM(Rating), COUNT(*) FROM StatsJogadoresPorPartida Where Nick = "Cadian";

-- Stats Gerais PLayers
SELECT
    Nick AS Nick,
    SUM(Kills) AS TotalKills,
    SUM(Deaths) AS TotalDeaths,
    ROUND(AVG(Rating), 2) AS AverageRating,
    COUNT(*) AS MapsPlayed
FROM StatsJogadoresPorPartida
GROUP BY Nick ORDER BY AverageRating DESC;

-- Stats Gerais por Mapa
SELECT
    Nick AS Nick,
    SUM(Kills) AS TotalKills,
    SUM(Deaths) AS TotalDeaths,
    ROUND(AVG(Rating), 2) AS AverageRating,
    COUNT(*) AS MapsPlayed
FROM StatsJogadoresPorPartida where Mapa = "Mirage"
GROUP BY Nick ORDER BY AverageRating DESC;

SELECT
    Nick AS Nick,
    SUM(Kills) AS TotalKills,
    SUM(Deaths) AS TotalDeaths,
    ROUND(AVG(Rating), 2) AS AverageRating,
    COUNT(*) AS MapsPlayed
FROM StatsJogadoresPorPartida where Mapa = "Inferno"
GROUP BY Nick ORDER BY AverageRating DESC;

SELECT
    Nick AS Nick,
    SUM(Kills) AS TotalKills,
    SUM(Deaths) AS TotalDeaths,
    ROUND(AVG(Rating), 2) AS AverageRating,
    COUNT(*) AS MapsPlayed
FROM StatsJogadoresPorPartida where Mapa = "Overpass"
GROUP BY Nick ORDER BY AverageRating DESC;

SELECT
    Nick AS Nick,
    SUM(Kills) AS TotalKills,
    SUM(Deaths) AS TotalDeaths,
    ROUND(AVG(Rating), 2) AS AverageRating,
    COUNT(*) AS MapsPlayed
FROM StatsJogadoresPorPartida where Mapa = "Ancient"
GROUP BY Nick ORDER BY AverageRating DESC;

SELECT
    Nick AS Nick,
    SUM(Kills) AS TotalKills,
    SUM(Deaths) AS TotalDeaths,
    ROUND(AVG(Rating), 2) AS AverageRating,
    COUNT(*) AS MapsPlayed
FROM StatsJogadoresPorPartida where Mapa = "Anubis"
GROUP BY Nick ORDER BY AverageRating DESC;

SELECT
    Nick AS Nick,
    SUM(Kills) AS TotalKills,
    SUM(Deaths) AS TotalDeaths,
    ROUND(AVG(Rating), 2) AS AverageRating,
    COUNT(*) AS MapsPlayed
FROM StatsJogadoresPorPartida where Mapa = "Vertigo"
GROUP BY Nick ORDER BY AverageRating DESC;

SELECT
    Nick AS Nick,
    SUM(Kills) AS TotalKills,
    SUM(Deaths) AS TotalDeaths,
    ROUND(AVG(Rating), 2) AS AverageRating,
    COUNT(*) AS MapsPlayed
FROM StatsJogadoresPorPartida where Mapa = "Nuke"
GROUP BY Nick ORDER BY AverageRating DESC;

-- Stats Gerais Times
SELECT
    TeamName,
    SUM(MatchPlayed) AS MatchesPlayed,
    SUM(MatchWon) AS MatchesWon,
    CONCAT(truncate((SUM(MatchWon)/SUM(MatchPlayed))*100, 0), '%') AS Porcentagem
FROM
    (
        SELECT TimeVencedor AS TeamName, 1 AS MatchPlayed, 1 AS MatchWon FROM Partidas
        UNION ALL
        SELECT TimePerdedor AS TeamName, 1 AS MatchPlayed, 0 AS MatchWon FROM Partidas
    ) AS Teams
GROUP BY TeamName;


-- Stats Times Mapa1
SELECT
    TeamName,
    SUM(MapPlayed) AS Map1Played,
    SUM(MapWon) AS Map1Won,
    CONCAT(truncate((SUM(MapWon)/SUM(MapPlayed))*100, 0), '%') AS Porcentagem
FROM
    (
        SELECT Mapa1Vencedor AS TeamName, 0 AS MapPlayed, 1 AS MapWon FROM Partidas
        UNION ALL
        SELECT TimePerdedor AS TeamName, 1 AS MapPlayed, 0 AS MapWon FROM Partidas
        UNION ALL
        SELECT TimeVencedor AS TeamName, 1 AS MapPlayed, 0 AS MapWon FROM Partidas
    ) AS Teams
GROUP BY TeamName;

-- Stats Gerais Times Mapa2
SELECT
    TeamName,
    SUM(MapPlayed) AS Map2Played,
    SUM(MapWon) AS Map2Won,
    CONCAT(truncate((SUM(MapWon)/SUM(MapPlayed))*100, 0), '%') AS Porcentagem
FROM
    (
        SELECT Mapa2Vencedor AS TeamName, 0 AS MapPlayed, 1 AS MapWon FROM Partidas
        UNION ALL
        SELECT TimePerdedor AS TeamName, 1 AS MapPlayed, 0 AS MapWon FROM Partidas
        UNION ALL
        SELECT TimeVencedor AS TeamName, 1 AS MapPlayed, 0 AS MapWon FROM Partidas
    ) AS Teams
GROUP BY TeamName;

-- Stats Gerais Times Mapa3
SELECT
    TeamName,
    SUM(MapPlayed) AS Map3Played,
    SUM(MapWon) AS Map3Won,
    CONCAT(truncate((SUM(MapWon) / SUM(MapPlayed) * 100), 0), '%') AS Porcentagem
FROM
    (
        SELECT Mapa3Vencedor AS TeamName, 0 AS MapPlayed, 1 AS MapWon FROM Partidas WHERE Mapa3 IS NOT NULL
        UNION ALL
        SELECT TimePerdedor AS TeamName, 1 AS MapPlayed, 0 AS MapWon FROM Partidas WHERE Mapa3 IS NOT NULL
        UNION ALL
        SELECT TimeVencedor AS TeamName, 1 AS MapPlayed, 0 AS MapWon FROM Partidas WHERE Mapa3 IS NOT NULL
    ) AS Teams
GROUP BY TeamName ORDER BY CAST(SUBSTRING(Porcentagem, 1, LENGTH(Porcentagem) - 1) AS SIGNED) DESC;

-- Juntando todos e vendo por mapa
-- Anubis
SELECT
    TeamName,
    SUM(MapPlayed) AS AnubisMapPlayed,
    SUM(MapWon) AS AnubisMapWon,
    CONCAT(truncate((SUM(MapWon) / SUM(MapPlayed) * 100), 0), '%') AS PorcentagemAnubis
FROM
    (
        SELECT Mapa3Vencedor AS TeamName, 0 AS MapPlayed, 1 AS MapWon FROM Partidas WHERE Mapa3 IS NOT NULL And Mapa3 = "Anubis"
        UNION ALL
        SELECT Mapa1Vencedor AS TeamName, 0 AS MapPlayed, 1 AS MapWon FROM Partidas WHERE Mapa1 = "Anubis"
        UNION ALL
        SELECT Mapa2Vencedor AS TeamName, 0 AS MapPlayed, 1 AS MapWon FROM Partidas WHERE Mapa2 = "Anubis"
        UNION ALL
        SELECT TimePerdedor AS TeamName, 1 AS MapPlayed, 0 AS MapWon FROM Partidas WHERE Mapa3 = "Anubis" or Mapa2 = "Anubis" or Mapa1 = "Anubis"
        UNION ALL
        SELECT TimeVencedor AS TeamName, 1 AS MapPlayed, 0 AS MapWon FROM Partidas WHERE Mapa3 = "Anubis" or Mapa2 = "Anubis" or Mapa1 = "Anubis"
    ) AS Teams
GROUP BY TeamName ORDER BY CAST(SUBSTRING(PorcentagemAnubis, 1, LENGTH(PorcentagemAnubis) - 1) AS SIGNED) DESC;

-- Mirage
SELECT
    TeamName,
    SUM(MapPlayed) AS MirageMapPlayed,
    SUM(MapWon) AS MirageMapWon,
    CONCAT(truncate((SUM(MapWon) / SUM(MapPlayed) * 100), 0), '%') AS PorcentagemMirage
FROM
    (
        SELECT Mapa3Vencedor AS TeamName, 0 AS MapPlayed, 1 AS MapWon FROM Partidas WHERE Mapa3 IS NOT NULL And Mapa3 = "Mirage"
        UNION ALL
        SELECT Mapa1Vencedor AS TeamName, 0 AS MapPlayed, 1 AS MapWon FROM Partidas WHERE Mapa1 = "Mirage"
        UNION ALL
        SELECT Mapa2Vencedor AS TeamName, 0 AS MapPlayed, 1 AS MapWon FROM Partidas WHERE Mapa2 = "Mirage"
        UNION ALL
        SELECT TimePerdedor AS TeamName, 1 AS MapPlayed, 0 AS MapWon FROM Partidas WHERE Mapa3 = "Mirage" or Mapa2 = "Mirage" or Mapa1 = "Mirage"
        UNION ALL
        SELECT TimeVencedor AS TeamName, 1 AS MapPlayed, 0 AS MapWon FROM Partidas WHERE Mapa3 = "Mirage" or Mapa2 = "Mirage" or Mapa1 = "Mirage"
    ) AS Teams
GROUP BY TeamName ORDER BY CAST(SUBSTRING(PorcentagemMirage, 1, LENGTH(PorcentagemMirage) - 1) AS SIGNED) DESC;

-- Overpass
SELECT
    TeamName,
    SUM(MapPlayed) AS OverpassMapPlayed,
    SUM(MapWon) AS OverpassMapWon,
    CONCAT(truncate((SUM(MapWon) / SUM(MapPlayed) * 100), 0), '%') AS PorcentagemOverpass
FROM
    (
        SELECT Mapa3Vencedor AS TeamName, 0 AS MapPlayed, 1 AS MapWon FROM Partidas WHERE Mapa3 IS NOT NULL And Mapa3 = "Overpass"
        UNION ALL
        SELECT Mapa1Vencedor AS TeamName, 0 AS MapPlayed, 1 AS MapWon FROM Partidas WHERE Mapa1 = "Overpass"
        UNION ALL
        SELECT Mapa2Vencedor AS TeamName, 0 AS MapPlayed, 1 AS MapWon FROM Partidas WHERE Mapa2 = "Overpass"
        UNION ALL
        SELECT TimePerdedor AS TeamName, 1 AS MapPlayed, 0 AS MapWon FROM Partidas WHERE Mapa3 = "Overpass" or Mapa2 = "Overpass" or Mapa1 = "Overpass"
        UNION ALL
        SELECT TimeVencedor AS TeamName, 1 AS MapPlayed, 0 AS MapWon FROM Partidas WHERE Mapa3 = "Overpass" or Mapa2 = "Overpass" or Mapa1 = "Overpass"
    ) AS Teams
GROUP BY TeamName ORDER BY CAST(SUBSTRING(PorcentagemOverpass, 1, LENGTH(PorcentagemOverpass) - 1) AS SIGNED) DESC;

-- Vertigo
SELECT
    TeamName,
    SUM(MapPlayed) AS VertigoMapPlayed,
    SUM(MapWon) AS VertigoMapWon,
    CONCAT(truncate((SUM(MapWon) / SUM(MapPlayed) * 100), 0), '%') AS PorcentagemVertigo
FROM
    (
        SELECT Mapa3Vencedor AS TeamName, 0 AS MapPlayed, 1 AS MapWon FROM Partidas WHERE Mapa3 IS NOT NULL And Mapa3 = "Vertigo"
        UNION ALL
        SELECT Mapa1Vencedor AS TeamName, 0 AS MapPlayed, 1 AS MapWon FROM Partidas WHERE Mapa1 = "Vertigo"
        UNION ALL
        SELECT Mapa2Vencedor AS TeamName, 0 AS MapPlayed, 1 AS MapWon FROM Partidas WHERE Mapa2 = "Vertigo"
        UNION ALL
        SELECT TimePerdedor AS TeamName, 1 AS MapPlayed, 0 AS MapWon FROM Partidas WHERE Mapa3 = "Vertigo" or Mapa2 = "Vertigo" or Mapa1 = "Vertigo"
        UNION ALL
        SELECT TimeVencedor AS TeamName, 1 AS MapPlayed, 0 AS MapWon FROM Partidas WHERE Mapa3 = "Vertigo" or Mapa2 = "Vertigo" or Mapa1 = "Vertigo"
    ) AS Teams
GROUP BY TeamName ORDER BY CAST(SUBSTRING(PorcentagemVertigo, 1, LENGTH(PorcentagemVertigo) - 1) AS SIGNED) DESC;

-- Inferno
SELECT
    TeamName,
    SUM(MapPlayed) AS InfernoMapPlayed,
    SUM(MapWon) AS InfernoMapWon,
    CONCAT(truncate((SUM(MapWon) / SUM(MapPlayed) * 100), 0), '%') AS PorcentagemInferno
FROM
    (
        SELECT Mapa3Vencedor AS TeamName, 0 AS MapPlayed, 1 AS MapWon FROM Partidas WHERE Mapa3 IS NOT NULL And Mapa3 = "Inferno"
        UNION ALL
        SELECT Mapa1Vencedor AS TeamName, 0 AS MapPlayed, 1 AS MapWon FROM Partidas WHERE Mapa1 = "Inferno"
        UNION ALL
        SELECT Mapa2Vencedor AS TeamName, 0 AS MapPlayed, 1 AS MapWon FROM Partidas WHERE Mapa2 = "Inferno"
        UNION ALL
        SELECT TimePerdedor AS TeamName, 1 AS MapPlayed, 0 AS MapWon FROM Partidas WHERE Mapa3 = "Inferno" or Mapa2 = "Inferno" or Mapa1 = "Inferno"
        UNION ALL
        SELECT TimeVencedor AS TeamName, 1 AS MapPlayed, 0 AS MapWon FROM Partidas WHERE Mapa3 = "Inferno" or Mapa2 = "Inferno" or Mapa1 = "Inferno"
    ) AS Teams
GROUP BY TeamName ORDER BY CAST(SUBSTRING(PorcentagemInferno, 1, LENGTH(PorcentagemInferno) - 1) AS SIGNED) DESC;

select * from StatsJogadoresPorPartida;
select * from Partidas;
select * from PlayerGeralStats;

select Nick, AverageRating, KPR, DPR, MapsPlayed from PlayerGeralStats;

select * from StatsJogadoresPorPartida where Kills > 30;
select * from StatsJogadoresPorPartida where Deaths > 25;
select * from StatsJogadoresPorPartida where Rating > 3.00;
select * from StatsJogadoresPorPartida where Rating < 0.30;

SELECT MAX(Partidaidx) FROM StatsJogadoresPorPartida;

select Nick, AverageRating, MapsPlayed from PlayerGeralStats where MapsPlayed >= 0 and MapsPlayed < 25;

drop database CSPYTHON4;
DROP DATABASE IF EXISTS CSPYTHON4;
drop table PlayerGeralStats;
