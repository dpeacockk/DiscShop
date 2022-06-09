#!/usr/bin/python

import os
import requests
from bs4 import BeautifulSoup
import DiscInfo
from tkinter import *
import sqlite3 as sl


con = sl.connect('DiscGolf.db')

#creating tables in DiscGolf database 
#https://towardsdatascience.com/do-you-know-python-has-a-built-in-database-d553989c87bd refer to this
with con:
    con.execute("""
        CREATE TABLE USER (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        );
    """)







