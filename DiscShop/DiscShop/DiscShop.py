#!/usr/bin/python

import os
import requests
from bs4 import BeautifulSoup
#from tkinter import *
import pygame
import button
from DiscInfo import DiscGolfDatabase
import pandas as pd


#Loading in the databases
disc_db = pd.read_pickle("./DiscDatabase.pkl")
MPO_db = pd.read_pickle("./MPODatabase.pkl")
FPO_db = pd.read_pickle("./FPODatabase.pkl")
companies_db = pd.read_pickle("./Companies.pkl")

#initializing pygame
pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
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
quit_button = button.Button(0, 0, quit_img, .0125)
back_button = button.Button(500, 200, back_img, .1)
pros_button = button.Button(500, 300, pros_img, 1)
discs_button = button.Button(500, 400, shop_img, 1)
companies_button = button.Button(500, 500, companies_img, 1)
 
#Application loop
run = True

while run:
    screen.blit(background, (0, 0))
    #Quit
    if quit_button.draw(screen):
        run = False
        
    #Main Menu
    if back_button.draw(screen):
        menu_state = "main"
        
    #Professional Players menu
    if pros_button.draw(screen):
        menu_state = "pros"
    
    #Companies Menu
    if companies_button.draw(screen):
        menu_state = "companies"
    
    #Discs Menu
    if discs_button.draw(screen):
        menu_state = "discs"
    
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()


pygame.quit()
