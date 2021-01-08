import requests
from bs4 import BeautifulSoup
from teams import *
import pyodbc 

def web_scrape():
    i = 0 # keeps track of how many times the loop gets executed to determine url
    
    for j in range (30):# will loop through all 30 mlb teams
        x = 1 + i # to keep track of iterations of the loop for the url to change teams
        x = str(x) #must be a string for the URL
        print(x) # to see progress of loop
        url = 'https://www.espn.com/mlb/player/batvspitch/_/id/35201/teamId/' + x
        print(url)
        print("URL ^")
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')     
        data = soup.find('td', attrs = {'class': 'Table__TD'})        
        data = data.findNext('td')
        data_print = data.get_text()
        print(data_print)
        if data_print in teams: #if player hasn't faced any pitchers on the team, the loop will break.
            print("BROKE")
            i = i+1
            continue  
          
        o = 1
        loopy = 0 
        #conn = pyodbc.connect('Driver={SQL Server};'
                          #'Server=DESKTOP-F46GKKA;'
                          #'Database=Baseball_data;'
                          #'Trusted_Connection=yes;')
        #cursor = conn.cursor()
        for x in range(200):
            loopy = loopy + 1
            data = data.findNext('td')
            data_print = data.get_text()
            #if loopy == 1: #oppoenets name
               # first step is to determine if the player is already in the database.
               #Opponents_Name = data_print
               #cursor.execute("SELECT * FROM dbo.Opponents$ WHERE Opponents_NAME = ?",Opponents_Name)
               #x = cursor.fetchone()
               #if len(x) > 0 
                
                
            
            if data_print == 'Totals':
                break
            
            print(data_print)
            #cursor.execute("INSERT INTO dbo.STATS$(H) VALUES (?)", (H))    
            #Values = [H, AVG]
            #cursor.execute(SQLCommand,Values)
            #conn.commit() 
            print('committed')
            
            o = o+1
        i = i +1
web_scrape()