
from collections import namedtuple
from bs4 import BeautifulSoup
import sqlite3 as sl

class DiscGolfDatabase:
    def __init__(self):
        con = sl.connect('DiscGolf.db')

    with con:
        con.execute("""
        CREATE TABLE ProPlayers (
            team TEXT,
            rating INTEGER,
            name TEXT,
            age INTEGER,
            primaryHand TEXT,
            pdgaNum INTEGER,
            careerEvents INTEGER,
            careerWins INTEGER,
            location TEXT
            );
            """)

    with con:
        con.execute("""
        CREATE TABLE Discs (
            name TEXT,
            ...
        );
            """)









class Disc:
  
  def getStats():
    #gets stats for disc for constructor
       Stats = namedtuple("Stats", ["speed", "glide", "turn", "fade"])
       DO THIS?@!?#?!@#?!@#?
       return Stats

   #Function that uses disc name to scrape all other info about the disc.
   def getAllInfo(self):


       return

  def __init__(self, tab):

    self.name = name
    self.stability = stability
    self.weightRange = weightRange
    self.discType = discType
    self.cost = cost
    self.inStock = inStock
    self.company = company
    self.stats = getStats()     #function to set stats




#Professional PDGA players
class Player:
    def __init__(self, name, age, team, bag, careerEarnings, tournamentsWon):
        self.name = name
        self.age = age
        self.team = team
        self.bag = bag
        self.careerEarnings = careerEarnings
        self.tournamentsWon = tournamentsWon



##Users logging into the shop
#class User:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age



class Team:
    def __init__(self, teamName, yearFounded, location):
        self.name = teamName
        self.yearFounded = yearFounded
        self.location = location





#---------------------------------------------------------HELPER FUNCTIONS----------------------------------------------------------

#does webscraping from https://alldiscs.com/ to autofill database of discs
def getAllDiscs():

    return 


#does webscraping from ____________________________ to autofill database of pro players
def getAllPros():

    return


#does webscraping from ____________________________ to autofill database of disc golf teams 
def getAllTeams():

    return



