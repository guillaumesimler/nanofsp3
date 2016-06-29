-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Tables: please look at the readme and the xls file
CREATE TABLE Register_player (Playername text, 
							  starting_tournament integer, 
							  Playerid serial PRIMARY KEY);

CREATE TABLE Tournaments (tournamentname text, 
						  tournamentid serial PRIMARY KEY);

CREATE TABLE Player (tournament integer REFERENCES Tournaments(tournamentid), 
					Playerid integer REFERENCES Register_player);

CREATE TABLE Matches (Player1 integer, 
					  Player2 integer, 
					  Roundnumber integer,
					  tournamentid integer REFERENCES Tournaments(tournamentid),
					  Matchid serial PRIMARY KEY);


CREATE TABLE Results (Matchid integer REFERENCES Matches(Matchid),
					  Playerid integer,
					  Score integer);

-- Views
	-- Return the current Tournament level
CREATE VIEW CurrentTournament AS SELECT max(tournamentid) as Latest from Tournaments;

	-- Return the last value
CREATE VIEW LastPlayerid AS SELECT max(Playerid) as Playerid from Register_player;

	-- Return the number of registered Player
CREATE VIEW CountPlayer AS SELECT count(*) as Numb FROM Player; 

	-- Return the number of registered Player
CREATE VIEW DisplayPlayer AS SELECT Player.playerid as playerid, 
									Register_player.Playername as playername,
									Player.tournament as tournamentid 
						     FROM Player, Register_player 
						     WHERE player.playerid = Register_player.playerid; 

	-- Return the players' standings 
CREATE VIEW Leadtable AS SELECT DisplayPlayer.Playerid as id, 
								DisplayPlayer.Playername as name,
								sum(Results.Score) as wins,
								count(Results.Score) as matches
								FROM DisplayPlayer LEFT JOIN Results 
								ON DisplayPlayer.Playerid = Results.Playerid
								GROUP BY DisplayPlayer.Playerid, DisplayPlayer.Playername
								ORDER BY wins;


-- Fill the tournament DB

INSERT INTO Tournaments VALUES ('Queen''s own');
INSERT INTO Tournaments VALUES ('Schuertzenjaegerturnier');