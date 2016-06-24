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
    c.query("DELETE * FROM Results")
        # ... the matches themselves
    c.query("DELETE * FROM Matches")
    

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

    c.query("DELETE FROM player")
   

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

    count = c.query("SELECT * FROM Leadtable")
   

    # Generic database closing
    conn.commit()
    conn.close()

    # Return the value
    return count


def registerPlayer(name, newPlayer = False, oldPlayerid = ''):
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

    tournament = c.query("SELECT * FROM CurrentTournament")
    
    print tournament

    if newPlayer:
        # -- create: 
        # -- 1. a new Player 

        c.query("INSERT INTO Register_player %s, %s" %(name, tournament, ))

        # -- 2. a new player in the tournament

        playerid = c.query("SELECT * FROM LastPlayerid")
        
        c.query("INSERT INTO PLayer %s, %s" %(tournament, playerid, ))


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

    standings = c.query("SELECT * FROM Leadtable")
   
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


