#!/usr/bin/python
from DiscInfo import DiscGolfDatabase
import pandas as pd
import os
import imageio as iio

#db = DiscGolfDatabase()
#db.addDiscs()
#db.addPros()
#db.addCompanies()

def moveProImages():
    df_FPO = pd.read_pickle("./FPODatabase.pkl")
    df_MPO = pd.read_pickle("./MPODatabase.pkl")
    return

def moveCompanyImages():
    df = pd.read_pickle("./Companies.pkl")
    #print(df)
    img_directory = './company-Images'
    img_list = []
    for filename in os.listdir(img_directory):
        print(filename)
        img_list.append(iio.imread('company-Images/' + filename))
        
    df = df.sort_values('Name')
    df['images'] = img_list
    print(df)
    return 

def moveDiscImages():
    df = pd.read_pickle("./DiscDatabase.pkl")
    return

def moveAllImages():
    moveDiscImages()
    moveCompanyImages()
    moveProImages()
    return

moveAllImages()