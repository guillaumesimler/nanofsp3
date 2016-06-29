#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    # Generic database start
    conn = connect()
    c = conn.cursor()
    # --  Main programm

        # Kick the matches'results, then...
    c.execute("DELETE FROM Results;")
        # ... the matches themselves
    c.execute("DELETE FROM matches;")
    

    # Generic database closing
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""

    # Generic database start
    conn = connect()
    c = conn.cursor()

    # --  Main programm

        # Kick the tournaments' player

    t = c.execute("DELETE FROM player")
   

    # Generic database closing
    conn.commit()
    conn.close()

def countPlayers():
    """Returns the number of players currently registered."""

    # Generic database start
    conn = connect()
    c = conn.cursor()

    # --  Main programm

        # Kick the tournaments' player

    query = "SELECT * FROM CountPlayer;"

    c.execute(query)
    result = c.fetchall()


    # Generic database closing
    conn.close()

    result = result[0][0]

    # Return the value
    return result


def registerPlayer(name, newPlayer = True, oldPlayerid = ''):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    
    !!! Deviation to fit multiple tournaments and inherited player name!!!
    Args:
      name: the player's full name (need not be unique).
      !!Deviation!!
      newPlayer (Boolean, per default True) 
    """
    
    # Generic database start
    conn = connect()
    c = conn.cursor()

    # --  Main programm

    name = name.replace("'", "''")
    
        # -- get the tournament id

    tournament = getCurrentTournament(c)

    if newPlayer:
        # -- create: 
        # -- 1. a new Player 

        query = "INSERT INTO Register_player (Playername, starting_tournament) VALUES ('%s', %s)" %(name, tournament, )

        c.execute(query)

        # -- 2. a new player in the tournament

        c.execute("SELECT * FROM LastPlayerid")

        playerid = c.fetchall()[0][0] 

    else:
        playerid = oldPlayerid

    c.execute("INSERT INTO PLayer (tournament, Playerid) VALUES ('%s', %s)" %(tournament, playerid, ))

    # Generic database closing
    conn.commit()
    conn.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    # Generic database start
    conn = connect()
    c = conn.cursor()

    # --  Main programm

    c.execute("SELECT * FROM Leadtable")
    standings = c.fetchall()

    result = []

    for standing in standings:
        if standing[2] == None:
            standing = list(standing)
          
            standing[2] = 0
            print standing

            standing = tuple(standing)

            result.append(standing)

    # Generic database closing
    conn.commit()
    conn.close()

    # Return the value
    return result

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    createPairing(winner, loser, 3)

    # Generic database start
    conn = connect()
    c = conn.cursor()

    # --  Main programm

    matchid = getMatchID(c, winner, loser)

    # first insert the winner
    query = 'INSERT INTO RESULTS values (%s, %s, 1)' %(matchid, winner, )
    c.execute(query)
    # first insert the loser
    query = 'INSERT INTO RESULTS values (%s, %s, 0)' %(matchid, loser, )
    c.execute(query)

    # Generic database closing
    conn.commit()
    conn.close()

    # Finish Report
    print 'Match between players %s and %s successfully reported !' %(winner, loser)
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    print 'Hello AGAIN'



# Guillaume's own formula

def createPairing(winner, loser, roundnb):
    """ Create a game pairing""" 

    # Generic database start
    conn = connect()
    c = conn.cursor()

    tournament = getCurrentTournament(c)
    # --  Main programm

    query = 'INSERT INTO Matches values (%s, %s, %s, %s)' %(winner, loser, roundnb, tournament, )
    c.execute(query)

    # Generic database closing
    conn.commit()
    conn.close()

def getMatchID(c, winner, loser):

    query = 'SELECT Matchid FROM Matches where ((player1 = %s) and (player2 = %s)) \
             or ((player1 = %s) and (player2 = %s))' %(winner, loser, loser, winner, )

    c.execute(query)

    matchid = c.fetchall()[0][0]

    return matchid


def getCurrentTournament(c):
    c.execute("SELECT * FROM CurrentTournament;")
    tournament =  c.fetchall()[0][0]

    return tournament


# registerPlayer('Heinrich')
# registerPlayer('Gargamel', False, 1)
# displayPlayer()

playerStandings()