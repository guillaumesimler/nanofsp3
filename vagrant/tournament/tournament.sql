-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


-- Initialize and select the Database
--
-- Thanks to reviewer n1 for the 
--  * IF EXIST Statement
--  * the simple \c tournament (to select the database, an element I missed so I kicked the 
--    two first lines from an previous not reviewed version)

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;


-- Tables: please look at the readme and the xls file
CREATE TABLE Register_player (Playername text,
							  starting_tournament integer,
							  Playerid serial PRIMARY KEY);

CREATE TABLE Tournaments (tournamentname text,
						  tournamentid serial PRIMARY KEY);

CREATE TABLE Player (tournament integer REFERENCES Tournaments(tournamentid),
					Playerid integer REFERENCES Register_player);


-- Thanks to reviewer n1 for the correction:
--    I was aware that Player1 and 2 (now winner and loser) were foreign key
--    I thought it was more logical to put on Player. Yet PSQL did not like the 
--    foreign key on a foreign key.

CREATE TABLE Matches (Player1 integer REFERENCES Register_player(Playerid),
					  Player2 integer REFERENCES Register_player(Playerid),
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
								ORDER BY wins DESC;


-- Fill the tournament DB (enabling the start)

INSERT INTO Tournaments VALUES ('Queen''s own');
INSERT INTO Tournaments VALUES ('Schuertzenjaegerturnier');