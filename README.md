# Swiss Tournament

Authors
----
* the [main part of program](https://github.com/udacity/fullstack-nanodegree-vm) was designed by the [udacity team with Karl Krueger as the intructor](https://discussions.udacity.com/users/karl/activity), this covers especially
	- the vagrant configuration as well as its internal setup
	- the testing file, **tournament_test.py**

* the **adaptation of the files** was done by **Guillaume Simler**, a Udacity Frontend Nanodegree graduate and Full Stack Web Developer Student, more information and contact details on my [Github profile](https://github.com/guillaumesimler)
	- the setup of the Postgr Database
	- the design of the SQL queries, stored in **tournament.sql**
	- the tournament management file, **tournament.py**


Project description
----

The aim is to design a program which manages a tournament working in [swiss-system](https://en.wikipedia.org/wiki/Swiss-system_tournament)


Data structure
----

## Database

The name of the database, **tournament**, as well as it is type, [psql](https://www.postgresql.org/), were given upfront.

## Tables

There are several table create:
1. **Register_player** (extra requirement): it enables the saving of the first tournament a participant enters.
2. **tournaments** (extra requirement): it saves the tournaments, so several might be possible. CAUTION!!! This is only the basis structure, two main views (Leadtable and Displayplayer) as well as the deletion logic of the Matches would require changes to be fully operational
3. **Player**: this is the list of the player of the tournament
4. **Matches**: the pairing of the matches are saved there (would be needed after the implementation of draws or irregular numbers of games, not yet active)
5. **Results**: here are store the results of the game (when game is won, score = 1 ; when lost, score = 0 - then draw, then it will be 0.5)

## Views
Out of the 5 views, the last two are the main one (and the fourth mostly in order to build the 5th). The first three are used once or twice in python and could have been replaced. They are mostly legacy.

They are quite self explaining as for the last two:
* **DisplayPlayer** enables to add the players names to the list of player in the tournament, which in turn allows the left join done in the next view
* **Leadtable** grants the output of the players' ranking in descending order. It widely uses the Score column of the Results table.
	- the number of matches are given by the __count__ of the entries grouped by player
	- the number of wins are given by their __sum__ (this would allow the use of draws.)


How to use
----

#### Initialize the project

1. Clone the [Repo](https://github.com/guillaumesimler/nanofsp3)
2. Set up your [vagrant machine and make sure to have a virtual machine](https://udacity.atlassian.net/wiki/display/BENDH/Vagrant+VM+Installation)
3. Once installed, use your terminal or git bash window to "cd" to the /vagrant/tournament
4. Run PSQL and **create the database** by typing

```shell
	psql -f tournament.sql
```

5. Run the test program by typing
```shell
	python tournament_test.py
```
Repository
----
* the [working project](https://github.com/guillaumesimler/nanofsp3)

License
----

The **current version** is under [_MIT License_](https://github.com/guillaumesimler/nanofsp3/blob/master/LICENSE.txt)