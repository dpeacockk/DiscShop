#!/usr/bin/python3
import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By


class DiscGolfDatabase:
    num_discs = 0

     #does webscraping from https://alldiscs.com/ to auto fill single entry of disc
    def addDiscs(self):
         options = webdriver.ChromeOptions()
         options.add_argument('--ignore-certificate-errors')
         options.add_argument('--incognito')
         options.add_argument('--headless')
         driver = webdriver.Chrome("chromedriver", chrome_options=options)
         
         url = 'https://alldiscs.com/'
         driver.get(url)
         
         #setting up dataframe with columns
         page = driver.page_source
         soup = BeautifulSoup(page, 'lxml')
         table = soup.find('table', {'id':'table_1'})
         headers = []

         for i in table.find_all('th')[0:7]:
                   title = i.text.strip()
                   headers.append(title)
         df = pd.DataFrame(columns = headers)
         # print(headers)
         #clicking Next button and extracting data till its all in the DB
         for i in range(0,75):
             time.sleep(1.5)
             
             page = driver.page_source #requests.get(url)     #gets HTML from website
             soup = BeautifulSoup(page, 'lxml')
             table = soup.find('table', {'id':'table_1'})
         
             for row in table.find_all('tr')[2:]:
                     data = row.find_all('td')[0:7]
                     row_data = [td.text.strip() for td in data]
                     length = len(df)
                     df.loc[length] = row_data
                     # print(row_data)   
             elm = driver.find_element_by_id('table_1_next')
             # if 'inactive' or 'disabled' in elm.get_attribute('class'):
             #      break;
             elm.click()
             
         df.to_pickle("./DiscDatabase.pkl")
         driver.close()
         return


    #does webscraping from https://www.pdga.com/united-states-tour-ranking to autofill single entry of pro player
    def addPros(self):
        #MPO database
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')
        driver = webdriver.Chrome("chromedriver", chrome_options=options)
         
        url = 'https://www.pdga.com/united-states-tour-ranking'
        driver.get(url)
        
        #setting up data frame with headers
        headers = ['Name', 'Career Earnings', 'Location', 'Career Wins', 'US Tour Rank', 'Current Rating', 'PDGA Number']
        
        df_MPO = pd.DataFrame(columns = headers)
        df_FPO = pd.DataFrame(columns = headers)
        
        #get MPO data from table
        page = driver.page_source 
        soup = BeautifulSoup(page, 'lxml')
        table = driver.find_element_by_class_name('world-MPO') 
        body = table.find_element_by_tag_name('tbody')
        cells = body.find_elements_by_tag_name('td')
        
        names = []
        pdga_nums = []
        for cell in cells:
            if(len(cell.text) > 7):
                n = cell.text
                names.append(n.partition("\n")[0])
                pdga_nums.append(n.partition("\n")[-1])
        #print(names)
        #print(pdga_nums)
        #rows = body.find_elements_by_tag_name("tr")
        
        #Gathers data for top 25 pros -------(MPO)--------
        for i in range(0,25):
            time.sleep(1.25)
            
            #use links within table to open up pro player web page
            driver.find_element_by_partial_link_text(names[i][0:8]).click()
            time.sleep(1)
            
            #add data to databases
            name = names[i]
            pdga_num = pdga_nums[i]
            location = a
            curr_rating =a 
            carr_earn = a
            carr_wins = a
            tour_rank = a
            
            #adding all saved data to the dataframe
            row_data = [name, carr_earn, location, carr_wins, tour_rank, curr_rating, pdga_num]
            length = len(df)
            df.loc[length] = row_data
            
            driver.back() #goes back to top 25 page
            
        print(df_MPO)   
        #df_MPO.to_pickle("./MPODatabase.pkl")
        
        
        #---------------FPO table-------------
        table = soup.find('table', {'class':'world-FPO'}) 
        for i in range(0,25):
            time.sleep(1.5)
            
            elm = driver.find_elements_by_xpath('//*[@id="block-system-main"]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[' + str(i) + ']/td[2]/div/a')
            elm.click()
            
            #add data to databases
            temp_str = driver.find_elements_by_xpath('//*[@id="block-system-main"]/div/div/div/div/div/div[1]/div/h1')
            
            name = temp_str.rsplit(' ', 1)[0]
            pdga_num = temp_str.split()[-1]
            location = driver.get_element_by_xpath('//*[@id="block-system-main"]/div/div/div/div/div/div[7]/div/ul/li[1]/a').text
            curr_rating = driver.get_element_by_xpath('//*[@id="block-system-main"]/div/div/div/div/div/div[7]/div/ul/li[6]/text()').text
            carr_earn = driver.get_element_by_xpath('//*[@id="block-system-main"]/div/div/div/div/div/div[7]/div/ul/li[9]/text()').text
            carr_wins = driver.get_element_by_xpath('//*[@id="block-system-main"]/div/div/div/div/div/div[7]/div/ul/li[8]/a').text
            tour_rank = driver.get_element_by_xpath('//*[@id="block-system-main"]/div/div/div/div/div/div[7]/div/ul/li[10]/a').text
            
            #adding all saved data to the dataframe
            row_data = [name, carr_earn, location, carr_wins, tour_rank, curr_rating, pdga_num]
            length = len(df)
            df.loc[length] = row_data
            
            driver.back() #goes back to top 25 page
            
            
        #df_FPO.to_pickle("./FPODatabase.pkl")
        
        driver.close()
        return


    #does webscraping from ____________________________ to autofill database of disc golf teams 
    #adds all companies to Companies table
    def addCompanies(self):

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


def calcType(speed):
    if 0 < speed <= 3:
        return 'Putt and Approach'
    if 3 < speed <= 5:
        return 'Mid Range'
    if 5 < speed <= 8:
        return 'Fairway Driver'
    if speed > 8:
        return 'Distance Driver'
