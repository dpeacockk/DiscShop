#!/usr/bin/python

import os
import requests
from bs4 import BeautifulSoup
import pygame
import button
from DiscInfo import DiscGolfDatabase
import pandas as pd
import webbrowser       #import web-browser for opening links in Disc Shop


#Loading in the databases
disc_db = pd.read_pickle("./DiscDatabase.pkl")
MPO_db = pd.read_pickle("./MPODatabase.pkl")
FPO_db = pd.read_pickle("./FPODatabase.pkl")
companies_db = pd.read_pickle("./Companies.pkl")

#initializing pygame
pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 675
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#menu variables
menu_state = "main"
font = pygame.font.SysFont('calibri', 30)

#Loading images
background = pygame.image.load("./images/menubackground.jpg").convert_alpha()
prodigy_logo = pygame.image.load("./images/prodigy.jpg").convert_alpha()
lat64_logo = pygame.image.load("./images/latitude64.png").convert_alpha()
innova_logo = pygame.image.load("./images/innova.jpg").convert_alpha()
discraft_logo = pygame.image.load("./images/discraft.jpg").convert_alpha()
dynamic_logo = pygame.image.load("./images/dynamicdiscs.png").convert_alpha()
kasta_logo = pygame.image.load("./images/kastaplast.png").convert_alpha()
discmania_logo = pygame.image.load("./images/discmania.jpg").convert_alpha()

title_img = pygame.image.load("./images/title.png").convert_alpha()
companies_img = pygame.image.load("./images/button_companies.png").convert_alpha()
shop_img = pygame.image.load("./images/button_shop.png").convert_alpha()
pros_img = pygame.image.load("./images/button_professional-players.png").convert_alpha()
quit_img = pygame.image.load("./images/rcLxML7Ri.png").convert_alpha()
back_img = pygame.image.load("./images/PngItem_198377.png").convert_alpha()
 
#Creating button instances
quit_button = button.Button(10, 10, quit_img, .01)
back_button = button.Button(10, 10, back_img, .1)
pros_button = button.Button(400, 400, pros_img, 1)
discs_button = button.Button(400, 300, shop_img, 1)
companies_button = button.Button(400, 500, companies_img, 1)
 
#Application loop
run = True
while run:
    white = (253, 244, 220)
    screen.blit(background, (0, 0))
    
    #Main Menu
    if menu_state == "main":
        screen.blit(title_img, (150,100))
        
        #Quit
        if quit_button.draw(screen):
            run = False
        #Professional Players menu
        if pros_button.draw(screen):
            menu_state = "pros"
        
        #Companies Menu
        if companies_button.draw(screen):
            menu_state = "companies"
        
        #Discs Menu
        if discs_button.draw(screen):
            menu_state = "discs"
            
            
    #Not main menu screen  
    else:
        screen.fill(white)
        if back_button.draw(screen):
            pygame.time.wait(200)
            menu_state = "main"
   
    
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()


pygame.quit()
