import requests
from bs4 import BeautifulSoup
from teams import *
import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-F46GKKA;'
                          'Database=Baseball_data;'
                          'Trusted_Connection=yes;')

def web_scrape():
    i = 0 # keeps track of how many times the loop gets executed to determine url
    cursor = conn.cursor()

    for j in range (30):# will loop through all 30 mlb teams
        x = 1 + i # to keep track of iterations of the loop for the url to change teams
        x = str(x) #must be a string for the URL
        print(x) # to see progress of loop
        url = 'https://www.espn.com/mlb/player/batvspitch/_/id/35201/teamId/' + x
        #print(url)
        #print("URL ^")
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')     
        data = soup.find('td', attrs = {'class': 'Table__TD'})        
        data = data.findNext('td')
        data_print = data.get_text()
        #print(data_print)
        if data_print in teams: #if player hasn't faced any pitchers on the team, the loop will break.
            print("BROKE")
            i = i+1
            continue 
 #----------------------------------------------------------------------
 #The players name is currently saved in data_print. 
 #Next block of code is to add the player to the db if not already there         
 #----------------------------------------------------------------------
        #Opponents_Name = data_print
        Opponents_Name = 'dummy2'
        x = cursor.execute("SELECT * FROM dbo.Opponents$ WHERE Opponents_Name = ?",Opponents_Name)
        x = cursor.fetchall()
        print(Opponents_Name)
        
        x = len(x)
        if x == 0:
            print("Not in DB")
            Max_ID = cursor.execute("SELECT * FROM dbo.Opponents$")
            Max_ID = cursor.fetchall()
            Max_ID = len(Max_ID)
            print(Max_ID)
            Opponents_ID = int(Max_ID) + 1
            print(Opponents_ID)
            print("MAX ID")
            cursor.execute("INSERT INTO dbo.Opponents$(Opponents_ID, Opponents_Name) VALUES (?,?)", (Opponents_ID, Opponents_Name))    
            conn.commit()
        else:
            print("IN DB ALREADY")
        my_list= []
        for x in range(12):
            data = data.findNext('td')
            data_print = data.get_text()
            print("*")
            print(data_print)
            my_list.append(data_print)

            if data_print == 'Totals':
                break
        print(my_list)
        break
            #print(data_print)
          
        i = i +1 #outside of loop. Determines URL path
web_scrape()