-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Create the database
DROP DATABASE tournament;

CREATE DATABASE tournament;

-- Tables: please look at the readme and the xls file
CREATE TABLE Register_player (Playername text, starting_tournament integer, Playerid serial PRIMARY KEY);

CREATE TABLE Tournaments (tournamentid serial PRIMARY KEY, tournamentname text);

CREATE TABLE Player (tournament integer REFERENCES Tournaments(tournamentid), 
					Playerid integer REFERENCES Register_player);

CREATE TABLE Matches (Matchid serial PRIMARY KEY, 
					  Player1 integer, 
					  Player2 integer, 
					  Roundnumber integer,
					  tournamentid integer REFERENCES Tournaments(tournamentid));


CREATE TABLE Results (Matchid integer REFERENCES Matches(Matchid),
					  Winnerid integer,
					  Loserid integer);

-- Views
	-- Return the current Tournament level
CREATE VIEW CurrentTournament AS SELECT max(tournamentid) as Latest from Tournaments;

	-- Return the last value
CREATE VIEW LastPlayerid AS SELECT max(Playerid) as Playerid from Register_player;

	-- Return the number of registered Player
CREATE VIEW CountPlayer AS SELECT count(*) as Numb FROM Player; 

	-- Return the players' standings 
CREATE VIEW Leadtable AS SELECT Register_player.Playerid as id, Register_player.Playername 
	as name, count(*) as matches, count(Results.Matchid) as wins
	FROM Register_player RIGHT JOIN Results ON Register_player.Playername = Results.Winnerid
	GROUP BY Results.Winnerid ORDER BY Win;