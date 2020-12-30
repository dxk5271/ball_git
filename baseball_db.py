import pandas as pd
import sqlite3
import re
import requests
from bs4 import BeautifulSoup
from teams import *
import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-F46GKKA;'
                      'Database=Baseball_data;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()


my_list = []
my_list = pd.Series(my_list)
i = 0
columns_names = ['AB','Hits','2B','3B','HR','RBI','BB','K', 'AVG','OBP','SLG','OPS','SlG','OPS']
df = pd.DataFrame(columns = columns_names)
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
 

    ab = []
    single = []
    double = []
    triple = []
    homer = []
    rbi = []
    bb =[]
    k = []
    avg = []
    obp = []
    slg = []
    ops = []
    
d
    
    
    o = 1
    it = 0 
    
    for x in range(200):
        it = it + 1
        p= 0 + o
        data = data.findNext('td')
        data_print= data.get_text()
        if data_print == 'Totals':
            break
        
        print(data_print)
        
        
        o = o+1
    i = i +1
    #df.append(my_list)