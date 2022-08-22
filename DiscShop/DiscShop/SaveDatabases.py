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
    img_directory_MPO = './MPO-Images'
    img_directory_FPO = './FPO-Images'
    img_list_MPO = []
    img_list_FPO = []
    #MOVING MPO IMAGES FIRST
    for filename in os.listdir(img_directory_MPO):
        img_list_MPO.append(iio.imread('MPO-Images/' + filename))
    df_MPO = df_MPO.sort_values('Name')
    df_MPO['images'] = img_list_MPO
    #NOW MOVING FPO IMAGES
    for filename in os.listdir(img_directory_FPO):
        img_list_FPO.append(iio.imread('FPO-Images/' + filename))
    df_FPO = df_FPO.sort_values('Name')
    df_FPO['images'] = img_list_FPO
    print("Done moving pro images")
    #don t forget to rePickle the data frame
    #don t forget to rePickle the data frame
    #don t forget to rePickle the data frame
    #don t forget to rePickle the data frame
    #df_MPO.to_pickle("./MPODatabase.pkl")
    #df_FPO.to_pickle("./FPODatabase.pkl")
    return


def moveCompanyImages():
    df = pd.read_pickle("./Companies.pkl")
    #print(df)
    img_directory = './company-Images'
    img_list = []
    for filename in os.listdir(img_directory):
        img_list.append(iio.imread('company-Images/' + filename))
    df = df.sort_values('Name')
    df['images'] = img_list
    print(df)
    #don t forget to rePickle the data frame
    #don t forget to rePickle the data frame
    #don t forget to rePickle the data frame
    #don t forget to rePickle the data frame
    #df.to_pickle("./Companies.pkl")
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