import pandas as pd
import sqlite3
import re
import requests
from bs4 import BeautifulSoup
from teams import *
import pyodbc 

def web_scrape():
    i = 0
    
    for j in range (30):
        x = 1 + i
        x = str(x)
        print("LOOK HERE")
        print(x)
        url = 'https://www.espn.com/mlb/player/batvspitch/_/id/35201/teamId/' + x
        print(url)
        print("URL ^")
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        
        data = soup.find('td', attrs = {'class': 'Table__TD'})
        
        data = data.findNext('td')
        data_print = data.get_text()
        #print(type(data_print))
        print(data_print)
        if data_print in teams:
            print("BROKE")
            i = i+1
            continue
        
        
        # =============================================================================
        # for x in range(10):
        #     #data2 = data.findNext('td').get_text()
        #     data2 = data.findNext('td')
        #     print(data2)
        # =============================================================================
     
    
    
        
        
        o = 1
        it = 0 
        conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-F46GKKA;'
                          'Database=Baseball_data;'
                          'Trusted_Connection=yes;')
        cursor = conn.cursor()
        for x in range(200):
            it = it + 1
            p= 0 + o
            data = data.findNext('td')
            H = data.get_text()
            
            if H == 'Totals':
                break
            
            print(H)
            cursor.execute("INSERT INTO dbo.STATS$(H) VALUES (?)", (H))    
            #Values = [H, AVG]
            #cursor.execute(SQLCommand,Values)
            conn.commit() 
            print('committed')
            
            o = o+1
        i = i +1
web_scrape()