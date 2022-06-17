#!/usr/bin/python

import os
import requests
from bs4 import BeautifulSoup
from tkinter import *
from DiscInfo import DiscGolfDatabase
import pandas as pd



# db = DiscGolfDatabase()
# db.addDiscs()
disc_db = pd.read_pickle("./DiscDatabase.pkl")
print(disc_db)
#pros_db = pd.read_pickle("./ProsDatabase.pkl")
#companies_db = pd.read_pickle("./CompaniesDatabase.pkl")





