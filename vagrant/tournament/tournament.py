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
        # -- First get the match id

    c.execute("SELECT * FROM CurrentTournament;")
    tournament =  c.fetchall()[0][0]

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

    standings = c.execute("SELECT * FROM Leadtable")
   
    # Generic database closing
    conn.commit()
    conn.close()

    # Return the value
    return standings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    print 'Hello'
 
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


def displayPlayer():
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    
    !!! Deviation to fit multiple tournaments and inherited player name!!!
    Args:
      name: the player's full name (need not be unique).
      !!Deviation!!
      newPlayer (Boolean, per default False) 
    """
    
    # Generic database start
    conn = connect()
    c = conn.cursor()

    # --  Main programm
        # -- First get the match id

    c.execute("SELECT * FROM Player;")
    tournament =  c.fetchall()

    print tournament

    
    # Generic database closing
    conn.commit()
    conn.close()

registerPlayer('Heinrich')
registerPlayer('Gargamel', False, 1)
displayPlayer()
