#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import math

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
    c.execute("DELETE FROM results")
        # ... the matches themselves
    c.execute("DELETE FROM matches")
    

    # Generic database closing
    conn.commit()
    conn.close()

    # Finish Report
    print 'Status: '
    print 'All match records are deleted'
  

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

    # Finish Report
    print 'Status: '
    print 'All players are deleted'

def countPlayers():
    """Returns the number of players currently registered."""

    # Generic database start
    conn = connect()
    c = conn.cursor()

    # --  Main programm

        # Kick the tournaments' player

    query = "SELECT * FROM countplayer;"

    c.execute(query)
    result = c.fetchall()


    # Generic database closing
    conn.close()

    result = result[0][0]

    # Finish Report
    print 'Status: '
    print 'The players were counted.'

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

        # -- enable the use of apostrophe

    name = name.replace("'", "''")
    
        # -- get the tournament id

    tournament = getCurrentTournament(c)

    if newPlayer:
        # -- create: 
        # -- 1. a new Player 

        query = "INSERT INTO Register_player (Playername, starting_tournament) \
                VALUES ('%s', %s)" %(name, tournament, )

        c.execute(query)

        # -- 2. a new player in the tournament

        c.execute("SELECT * FROM LastPlayerid")

        playerid = c.fetchall()[0][0] 

    else:
        # in case of an existing player, simply take its value
        playerid = oldPlayerid

    c.execute("INSERT INTO PLayer (tournament, Playerid) \
               VALUES ('%s', %s)" %(tournament, playerid, ))

    # Generic database closing
    conn.commit()
    conn.close()

    # Finish Report
    print 'Status: '
    print 'Player %s (%s) successfully registered !' %(name, playerid)


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

        # This function is rebuild 'standings', especially when 
        # there is no matches.
        #
        # The DB would return a 'None' value for the wins which would 
        # fail in the tests 

    result = []

    for standing in standings:
        if standing[2] == None:
            standing = list(standing)
          
            standing[2] = 0
            standing = tuple(standing)

        result.append(standing)

    # Generic database closing
    conn.commit()
    conn.close()

    # Finish Report
    print 'Status: '
    print 'Standing edited !'

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
    print 'Status: '
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

    # 1. get the player field
    field = playerStandings()

    
    # Check the round numbers
    conn = connect()
    c = conn.cursor()

    roundnb = getCurrentRound(c) + 1

    conn.commit()
    conn.close()
    
    maxround = getMaxRound(field)


    #3. get the pairs

    if roundnb <= maxround:

        result = []

        i = 0
        
        while i < len(field):
            # create the game 
            pair1 = list(field[i])
            pair2 = list(field[i + 1])

            # create the pair to report

            pair = (pair2[0], pair2[0], pair1[0], pair1[0])
            result.append(pair)

            # create the match

            createPairing(pair1[0], pair2[0], roundnb)

            i = i + 2
         
        return result

    else:
        print 'The tournament is OVER !!'
        print 'Hail the players in the following order '
        print field




# Guillaume's own methods

def createPairing(winner, loser, roundnb):
    """ Creates a game pairing""" 

    # Generic database start
    conn = connect()
    c = conn.cursor()

    tournament = getCurrentTournament(c)
    # --  Main programm

    query = 'INSERT INTO Matches values (%s, %s, %s, %s)' \
             %(winner, loser, roundnb, tournament, )
    
    c.execute(query)

    # Generic database closing
    conn.commit()
    conn.close()

def getMatchID(c, winner, loser):
    """ Returns the current Tournament ID"""

    query = 'SELECT Matchid FROM Matches where ((player1 = %s) and (player2 = %s)) \
             or ((player1 = %s) and (player2 = %s))' %(winner, loser, loser, winner, )

    c.execute(query)

    matchid = c.fetchall()[0][0]

    return matchid


def getCurrentTournament(c):
    """ Returns the current Tournament ID"""
    c.execute("SELECT * FROM CurrentTournament;")
    tournament =  c.fetchall()[0][0]

    return tournament

def getCurrentRound(c):
    """ Returns the current round number """
    
    query = 'SELECT max(matches) FROM Leadtable'
    c.execute(query)

    roundnb = c.fetchall()[0][0]

    # in the starting face the query should return 'None'
    if not roundnb: 
        roundnb = 0


    return roundnb


def getMaxRound(field):
    """Get the maximal number of rounds """
    maxround = math.log( len(field), 2)
    
    return maxround

