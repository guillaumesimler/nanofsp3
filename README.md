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

Thanks
----

* to the first **reviewer** and its [great, awesome, terrific (& etc.) input](https://review.udacity.com/#!/reviews/175505)
* to the co-students and their [discussion in the forum](https://discussions.udacity.com/t/p2-normalized-table-design/19927/2)

Project description
----

The aim is to design a program which manages a tournament working in [swiss-system](https://en.wikipedia.org/wiki/Swiss-system_tournament)


Data structure
----

## Database

The name of the database, **tournament**, as well as it is type, [psql](https://www.postgresql.org/), were given upfront.

## Tables

There are several table create:
* **Register_player** (extra requirement): it enables the saving of the first tournament a participant enters.
* **tournaments** (extra requirement): it saves the tournaments, so several might be possible. CAUTION!!! This is only the basis structure, two main views (Leadtable and Displayplayer) as well as the deletion logic of the Matches would require changes to be fully operational
* **Player**: this is the list of the player of the tournament
* **Matches**: the pairing of the matches are saved there (would be needed after the implementation of draws or irregular numbers of games, not yet active)
* **Results**: here are store the results of the game (when game is won, score = 1 ; when lost, score = 0 - then draw, then it will be 0.5)

## Views
Out of the 5 views, the last two are the main one (and the fourth mostly in order to build the 5th). The first three are used once or twice in python and could have been replaced. They are mostly legacy.

They are quite self explaining as for the last two:
* **DisplayPlayer** enables to add the players names to the list of player in the tournament, which in turn allows the left join done in the next view
* **Leadtable** grants the output of the players' ranking in descending order. It widely uses the Score column of the Results table. It is build with a two subqueries to count the results

How to use
----

#### Initialize the project

* Clone the [Repo](https://github.com/guillaumesimler/nanofsp3)
* Set up your [vagrant machine and make sure to have a virtual machine](https://udacity.atlassian.net/wiki/display/BENDH/Vagrant+VM+Installation)
* Once installed, use your terminal or git bash window to "cd" to the /vagrant/tournament
* Run PSQL and **create the database** by typing

```shell
	psql -f tournament.sql
```

* Run the test program by typing
```shell
	python tournament_test.py
```
Repository
----
* the [working project](https://github.com/guillaumesimler/nanofsp3)

License
----

The **current version** is under [_MIT License_](https://github.com/guillaumesimler/nanofsp3/blob/master/LICENSE.txt)