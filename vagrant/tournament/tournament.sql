-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


-- Tables: please look at the readme and the xls file
CREATE TABLE Register_player (Playerid serial primary key, Playername text, starting_tournament integer);

CREATE TABLE Tournaments (tournamentid serial primary key, tournamentname text);

CREATE TABLE Player (tournament integer REFERENCES Tournaments(tournamentid), 
					Playerid integer REFERENCES Register_player);

CREATE TABLE Matches (Matchid serial primary key, 
					  Player1 integer REFERENCES Player(Playerid), 
					  Player2 integer REFERENCES Player(Playerid), 
					  Roundnumber integer
					  tournamentid integer REFERENCES Tournaments(tournamentid));


CREATE TABLE Results (Matchid integer REFERENCES Matches(Matchid),
					  Winnerid integer REFERENCES Player(Playerid),
					  Loserid integer REFERENCES Player(Playerid));

-- Views

CREATE VIEW CountPlayer AS SELECT count(*) as Numb FROM Player; 

	-- Return the players' standings 
CREATE VIEW Leadtable AS SELECT Register_player.Playerid as id, Register_player.Playername 
	as name, count(*) as matches, count(Results.Matchid) as wins
	FROM Register_player RIGHT JOIN Results ON Register_player.Playername = Results.Winnerid
	GROUP BY Results.Winnerid ORDER BY Win;