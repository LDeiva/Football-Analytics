# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:11:54 2023

@author: USR02709
"""


"""FBref"""

"""Scarico le statistiche di squadra"""
from bs4 import BeautifulSoup 
import requests
import contextlib
import pandas as pd

req = requests.get("https://fbref.com/en/comps/18/Serie-B-Stats")


req.status_code

req.text

soup=BeautifulSoup(req.text,"html.parser")
soup.prettify
soup.title

"""Faccio prima quella con xg e xga per squadra e con classifica"""
i_d='all_results2023-2024181'
div=soup.find('div', attrs={'id':i_d})
table_body = div.find('tbody')
rows = table_body.find_all('tr')

table_columns = div.find('thead')
column = table_columns.find('tr')

testo=div.get_text()


data=[]
for count,row in zip(range(len(rows)),rows):

    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    team_name = row.findAll('th')[0].contents
    data.append(cols) # Get rid of empty values
    # [ele for ele in cols if ele] serve a togliere i valori empty, se si vuole inserire dentro  data.append(cols)
    t_n=team_name[0].text
    data[count].insert(0,t_n)
        
    colonne=[]
    for col in column:
        if col.text!=' ':
            colonne.append(col.text)
      
result=pd.DataFrame(columns=colonne,data=data)
result.to_excel(rf'C:\Users\hp\OneDrive\Football Analytics\Calcio\Dati e Progetti\Dati\fbref\Serie B 2023_2024\Team Stats\Giornata 20\Own\Classifica_con_stats.xlsx',index=False)



"""Ora faccio le altre table"""
ids=['all_stats_squads_standard','all_stats_squads_keeper',"all_stats_squads_keeper_adv",'all_stats_squads_shooting',
     'all_stats_squads_passing','all_stats_squads_passing_types','all_stats_squads_gca','all_stats_squads_defense',
     'all_stats_squads_possession','all_stats_squads_playing_time','all_stats_squads_misc']

for i_d in ids:
    #i_d='switcher_stats_squads_shooting'
    div=soup.find('div', attrs={'id':i_d})
    table_body = div.find('tbody')
    rows = table_body.find_all('tr')
    
    table_columns = div.find('thead')
    column = table_columns.find_all('tr')
    
    testo=div.get_text()
    
    
    data=[]
    for count,row in zip(range(len(rows)),rows):
    
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        team_name = row.findAll('th')[0].contents
        data.append(cols) # Get rid of empty values
        # [ele for ele in cols if ele] serve a togliere i valori empty, se si vuole inserire dentro  data.append(cols)
        t_n=team_name[0].text
        data[count].insert(0,t_n)
        
        

    colonne=[]

    cols = column[1].find_all('th', attrs={"aria-label": True})


    cols = [ele['aria-label'] for ele in cols]
    colonne.append([ele for ele in cols if ele]) # Get rid of empty values
    #first_column = col.findAll('th')[2].contents
    
    
    
    
    #Creo dataframe
    df=pd.DataFrame(data=data,columns=cols)
    name=i_d[10:]
    df.to_excel(rf'C:\Users\hp\OneDrive\Football Analytics\Calcio\Dati e Progetti\Dati\fbref\Serie B 2023_2024\Team Stats\Giornata 20\Own\{name}.xlsx',index=False)

"""Faccio stats against"""



ids=['div_stats_squads_standard_against','div_stats_squads_keeper_against',"div_stats_squads_keeper_adv_against",'div_stats_squads_shooting_against',
     'div_stats_squads_passing_against','div_stats_squads_passing_types_against','div_stats_squads_gca_against','div_stats_squads_defense_against',
     'div_stats_squads_possession_against','div_stats_squads_playing_time_against','div_stats_squads_misc_against']

for i_d in ids:
    div=soup.find('div', attrs={'id':i_d})
    table=div.find('table')
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    
    table_columns = table.find('thead')
    column = table_columns.find_all('tr')
    
    testo=div.get_text()
    
    
    data=[]
    for count,row in zip(range(len(rows)),rows):
    
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        team_name = row.find_all('th',)[0].contents
        data.append(cols) # Get rid of empty values
        # [ele for ele in cols if ele] serve a togliere i valori empty, se si vuole inserire dentro  data.append(cols)
        t_n=team_name[0].text
        data[count].insert(0,t_n)
            
            
    #Trovo le colonne
    colonne=[]

    cols = column[1].find_all('th', attrs={"aria-label": True})


    cols = [ele['aria-label'] for ele in cols]
    colonne.append([ele for ele in cols if ele]) # Get rid of empty values
    #first_column = col.findAll('th')[2].contents


    #Creo dataframe
    df=pd.DataFrame(data=data,columns=cols)
    name=i_d[10:]
    df.to_excel(rf'C:\Users\hp\OneDrive\Football Analytics\Calcio\Dati e Progetti\Dati\fbref\Serie B 2023_2024\Team Stats\Giornata 20\Against\{name}.xlsx',index=False)

"""Scarico le statistiche per i singoli giocatori"""
from bs4 import BeautifulSoup 
import requests
import contextlib
import pandas as pd
import os
       
link=['https://fbref.com/it/squadre/72c031e3/Statistiche-Ascoli','https://fbref.com/it/squadre/01baa639/Statistiche-Bari',
       'https://fbref.com/it/squadre/4ef57aeb/Statistiche-Brescia','https://fbref.com/it/squadre/f4d63608/Statistiche-Calcio-Lecco-1912',
      'https://fbref.com/it/squadre/b964e6bb/Statistiche-Catanzaro','https://fbref.com/it/squadre/1a8d4355/Statistiche-Cittadella',
      'https://fbref.com/it/squadre/28c9c3cd/Statistiche-Como','https://fbref.com/it/squadre/34963d0d/Statistiche-Cosenza',
      'https://fbref.com/en/squads/9aad3a77/Cremonese-Stats','https://fbref.com/en/squads/c41460da/FeralpiSalo-Stats',
      'https://fbref.com/it/squadre/71a3700b/Statistiche-Modena','https://fbref.com/it/squadre/ee058a17/Statistiche-Palermo',
      'https://fbref.com/it/squadre/eab4234c/Statistiche-Parma','https://fbref.com/en/squads/4cceedfc/Pisa-Stats',
      'https://fbref.com/en/squads/19008e93/Reggiana-Stats','https://fbref.com/en/squads/8ff9e3b3/Sampdoria-Stats',
      'https://fbref.com/en/squads/68449f6d/Spezia-Stats','https://fbref.com/en/squads/13dabbde/Sudtirol-Stats',
      'https://fbref.com/en/squads/d8be8b3e/Ternana-Stats','https://fbref.com/en/squads/af5d5982/Venezia-Stats']

for lk in link:
    #lk='https://fbref.com/it/squadre/eab4234c/Statistiche-Parma#all_matchlogs'
    req = requests.get(lk)
    
    
    req.status_code
    
    
    
    req.text
    
    
    
    
    soup=BeautifulSoup(req.text,"html.parser")
    soup.prettify
    
    title=soup.title.text
    
    title=title[:20].strip()
    print(title)
    
    
    ids=['all_stats_standard','all_stats_keeper',"all_stats_keeper_adv",'all_stats_shooting',
         'all_stats_passing','all_stats_passing_types','all_stats_gca','all_stats_defense',
         'all_stats_possession','all_stats_playing_time','all_stats_misc']


    os.mkdir(rf'C:\Users\hp\OneDrive\Football Analytics\Calcio\Dati e Progetti\Dati\fbref\Serie B 2023_2024\Player Stats\Giornata 20\{title}')
    
    for i_d in ids:
        #i_d='all_matchlogs'
        div=soup.find('div', attrs={'id':i_d})
        table_body = div.find('tbody')
        rows = table_body.find_all('tr')
        
        table_columns = div.find('thead')
        column = table_columns.find_all('tr')
        
        testo=div.get_text()

        data=[]
        for count,row in zip(range(len(rows)),rows):
        
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            team_name = row.findAll('th')[0].contents
            data.append(cols) # Get rid of empty values
            t_n=team_name[0].text
            data[count].insert(0,t_n)
        # [ele for ele in cols if ele]
        
        
        
        
        #Totale di squadra e avverssario  
        tot_team=div.find('tfoot')
        r=tot_team.find_all('tr')   
    
        for riga in r:
            
           description=row.find_all('th')
           riga.findAll('th')[0].contents
           
           desc=riga.findAll('th')[0].contents
           values=riga.find_all('td')
           tot = [val.text.strip() for val in values]
           tot.insert(0,desc[0])
           data.append(tot) 
     
           

        colonne=[]
        for col in column:
            
            cols = col.find_all('th')
        
            cols = [ele.text.strip() for ele in cols]
            colonne.append(cols) 
            #[ele for ele in cols if ele] serve a togliere i valori empty, se si vuole inserire dentro  data.append(cols)
            #first_column = col.findAll('th')[2].contents
        
        
        colonne=[]
    
        cols = column[1].find_all('th', attrs={
            "aria-label": True})
    
    
        cols = [ele['aria-label'] for ele in cols]
        colonne.append(ele for ele in cols if ele) # Get rid of empty values
        
        
        #Creo dataframe
        df=pd.DataFrame(data=data,columns=cols)
        name=i_d[10:]

        df.to_excel(rf'C:\Users\hp\OneDrive\Football Analytics\Calcio\Dati e Progetti\Dati\fbref\Serie B 2023_2024\Player Stats\Giornata 20\{title}\{name}.xlsx',index=False)



"""Scrapping singole partite"""
from bs4 import BeautifulSoup 
import requests
import contextlib
import pandas as pd
import os
       

links=['https://fbref.com/it/squadre/eab4234c/Statistiche-Parma#all_matchlogs','https://fbref.com/it/squadre/af5d5982/Statistiche-Venezia',
       'https://fbref.com/it/squadre/28c9c3cd/Statistiche-Como','https://fbref.com/it/squadre/b964e6bb/Statistiche-Catanzaro',
       'https://fbref.com/it/squadre/9aad3a77/Statistiche-Cremonese','https://fbref.com/it/squadre/1a8d4355/Statistiche-Cittadella',
       'https://fbref.com/it/squadre/71a3700b/Statistiche-Modena','https://fbref.com/it/squadre/ee058a17/Statistiche-Palermo',
       'https://fbref.com/it/squadre/8ff9e3b3/Statistiche-Sampdoria','https://fbref.com/it/squadre/01baa639/Statistiche-Bari',
       'https://fbref.com/it/squadre/4ef57aeb/Statistiche-Brescia','https://fbref.com/it/squadre/34963d0d/Statistiche-Cosenza',
       'https://fbref.com/it/squadre/4cceedfc/Statistiche-Pisa','https://fbref.com/it/squadre/13dabbde/Statistiche-Sudtirol',
       'https://fbref.com/it/squadre/19008e93/Statistiche-Reggiana','https://fbref.com/it/squadre/68449f6d/Statistiche-Spezia',
       'https://fbref.com/it/squadre/f4d63608/Statistiche-Calcio-Lecco-1912','https://fbref.com/it/squadre/d8be8b3e/Statistiche-Ternana',
       'https://fbref.com/it/squadre/72c031e3/Statistiche-Ascoli','https://fbref.com/it/squadre/c41460da/Statistiche-FeralpiSalo']


#link='https://fbref.com/it/squadre/eab4234c/Statistiche-Parma#all_matchlogs'
for link in links:
    req = requests.get(link)
    
    
    req.status_code
    
    
    
    req.text
    
    
    
    
    soup=BeautifulSoup(req.text,"html.parser")
    soup.prettify
    
    title=soup.title.text
    
    title=title[:20].strip()
    print(title)
    
    i_d='all_matchlogs'
    div=soup.find('div', attrs={'id':i_d})
    table_body = div.find('tbody')
    rows = table_body.find_all('tr')
    
    table_columns = div.find('thead')
    column = table_columns.find_all('tr')
    
    testo=div.get_text()
    
    data=[]
    for count,row in zip(range(len(rows)),rows):
    
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        team_name = row.findAll('th')[0].contents
        data.append(cols) # Get rid of empty values
        t_n=team_name[0].text
        data[count].insert(0,t_n)
    # [ele for ele in cols if ele]
            
    
       
    
    colonne=[]
    for col in column:
        
        cols = col.find_all('th')
    
        cols = [ele.text.strip() for ele in cols]
        colonne.append(cols) 
        #[ele for ele in cols if ele] serve a togliere i valori empty, se si vuole inserire dentro  data.append(cols)
        #first_column = col.findAll('th')[2].contents
    
    
    
    #Creo dataframe
    df=pd.DataFrame(data=data,columns=cols)
    name=i_d[10:]
    #os.mkdir(rf'C:\Users\Davide\OneDrive\Football Analytics\Calcio\Dati e Progetti\Dati\fbref\Serie B 2023_2024\Match Stats\Giornata 16\{title}')
    
    df.to_excel(rf'C:\Users\hp\OneDrive\Football Analytics\Calcio\Dati e Progetti\Dati\fbref\Serie B 2023_2024\Match Stats\{name}_{title}.xlsx',index=False)

