#!/usr/bin/python3
import requests
from collections import namedtuple
from bs4 import BeautifulSoup
import sqlite3 as sl

class DiscGolfDatabase:
    con = sl.connect('DiscGolf.db')
    num_discs = 0
    
    def __init__(self):
        #con = sl.connect('DiscGolf.db')

        with self.con:
            self.con.execute("""
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

        with self.con:
            self.con.execute("""
        CREATE TABLE Discs (
            name TEXT,
            speed INTEGER,
            glide INTEGER,
            turn INTEGER,
            fade INTEGER,
            type TEXT,
            brand TEXT,
            stability TEXT,
            );
            """)

        with self.con:
            self.con.execute("""
        CREATE TABLE Companies (
            name TEXT,
            location TEXT,
            type TEXT,
            yearFounded INTEGER,
            );
            """)

     #does webscraping from https://alldiscs.com/ to autofill single entry of disc
    def addOneDisc(self):

         sql = 'INSERT INTO Discs (name, speed, glide, turn, fade, type, brand, stability) values(?, ?, ?, ?, ?, ?, ?,?)'
         
         url = 'https://alldiscs.com/'
         data = requests.get(url)

         lst = []

         soup = BeautifulSoup(page.text, 'lxml')

         #finds number of discs for 
         num_disc_div = soup.find("div", {"id": "table_1_info"})
         num_disc_string_list = num_disc_div.string.split()
         self.num_discs = num_disc_string_list[3]

         tab = soup.find("table", attrs={"class": "table1"})
         tab_data = tab.tbody.find_all("tr")  # contains 2 rows

         for i in range(0,self.num_discs):
             lst.append(?)       #name
             lst.append(?)       #speed
             lst.append(?)       #glide
             lst.append(?)       #turn
             lst.append(?)       #fade
             lst.append(?)       #type
             lst.append(?)       #brand
             lst.append(?)       #stability
             
         lst_tuple = [x for x in zip(*[iter(list)] * 8)]     # *8 because 8 parameters for each disc

         #data = [
         #       (1, 'Alice', 21),
         #       (2, 'Bob', 22),
         #       (3, 'Chris', 23)
         #   ]

         with self.con:
            self.con.executemany(sql, lst_tuple)
         return


        #adds all discs to Discs table
    def addDiscs():

        return


        #does webscraping from ____________________________ to autofill single entry of pro player
    def addOnePro(self):
        sql = 'INSERT INTO Companies (id, name, age) values(?, ?, ?)'
        data = [
                (1, 'Alice', 21),
                (2, 'Bob', 22),
                (3, 'Chris', 23)
            ]
        with self.con:
            self.con.executemany(sql, data)
        return


        #adds all pros to Pros table
    def addPros():

        return


        #does webscraping from ____________________________ to autofill database of disc golf teams 
    def addOneCompany(self):
        sql = 'INSERT INTO ProPlayers (id, name, age) values(?, ?, ?)'
        data = [
                (1, 'Alice', 21),
                (2, 'Bob', 22),
                (3, 'Chris', 23)
            ]
        with self.con:
            self.con.executemany(sql, data)
        return


        #adds all companies to Companies table
    def addCompanies():

        return











#class Disc:
  
#  def getStats():
#    #gets stats for disc for constructor
#       Stats = namedtuple("Stats", ["speed", "glide", "turn", "fade"])
#       DO THIS?@!?#?!@#?!@#?
#       return Stats

#   #Function that uses disc name to scrape all other info about the disc.
#   def getAllInfo(self):


#       return

#  def __init__(self, tab):

#    self.name = name
#    self.stability = stability
#    self.weightRange = weightRange
#    self.discType = discType
#    self.cost = cost
#    self.inStock = inStock
#    self.company = company
#    self.stats = getStats()     #function to set stats




##Professional PDGA players
#class Player:
#    def __init__(self, name, age, team, bag, careerEarnings, tournamentsWon):
#        self.name = name
#        self.age = age
#        self.team = team
#        self.bag = bag
#        self.careerEarnings = careerEarnings
#        self.tournamentsWon = tournamentsWon



###Users logging into the shop
##class User:
##    def __init__(self, name, age):
##        self.name = name
##        self.age = age



#class Team:
#    def __init__(self, teamName, yearFounded, location):
#        self.name = teamName
#        self.yearFounded = yearFounded
#        self.location = location





#---------------------------------------------------------HELPER FUNCTIONS----------------------------------------------------------

def calcStability(turn, fade):
    if turn + fade > 2 :
        return 'overstable'

    if 1 < turn + fade <= 2:
        return 'overstable-stable'

    if 1 >= turn + fade >=0:
        return 'stable'

    if  -2 <= turn + fade <= -1:
        return 'understable-stable'

    if turn + fade < -2:
        return 'understable'




