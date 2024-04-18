
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 16:10:30 2022

@author: hp
"""

import pandas as pd
"""Qui metto funzioni che non uso"""

#Calcolo l'altezza media delle pressioni per valutare altezza pressing.
#Da non usare
def Pressure_height(df,team):
    height=0
    Pressure=df[(df['type_name']=='Pressure') & (df['team_name']==team)]
    for i in range(len(Pressure)):
        height+=int(Pressure['location'].iloc[i][0])
    height_mean=height/len(Pressure)
    return height_mean



#calcolo i contrasti effettuati nell'ultimo terzo di campo.
#e la loro percentuale sul totale.
#Da non usare
def thirdPitch_tackles(df,team):
    duel=df[(df['type_name']=='Duel') & (df['team_name']==team)]
    total_duel=len(duel)
    third_duel=0
    for i in range(len(duel)):
        if duel['location'].iloc[i][0]>=80:
            third_duel+=1
    third_duel_perc=(third_duel/total_duel)*100
    return third_duel,third_duel_perc
            
            
#calcolo le pressioni effettuatenell'ultimo terzo di campo.
#e la loro percentuale sul totale.
#Da non usare
def thirdPitch_pressures(df,team):
    pressure=df[(df['type_name']=='Pressure') & (df['team_name']==team)]
    total_pressure=len(pressure)
    third_pressure=0
    for i in range(len(pressure)):
        if pressure['location'].iloc[i][0]>=80:
            third_pressure+=1
    third_pressure_perc=(third_pressure/total_pressure)*100
    return third_pressure,third_pressure_perc   


#IL PPDA nel modo eseguito da opta come riportato sulla pagina di StatsBomb.
#Quindi utilizzo come azioni difensive i Tackle, riusciti e no, gli intercetti, e i falli fatti dai 40m in su.
#Stessa cosa per i passaggi dai 40 metri in su.
def PPDA_opta(df,d_team_name,o_team_name):
    Offensive_pass_number=0
    Number_of_defensive_actions=0
    df_o=df[(df['team_name']==o_team_name)]
    df_d=df[(df['team_name']==d_team_name)]
    for c in range(len(df_o)):
        if df_o['type_name'].iloc[c]=='Pass' and 120-df_o['location'].iloc[c][0]>=40 and pd.isna(df_o['pass_outcome_name'].iloc[c])==True :

            Offensive_pass_number+=1
    for i in range(len(df_d)):            
        if df_d['type_name'].iloc[i]=='Duel' and df_d['location'].iloc[i][0]>=40:  

            Number_of_defensive_actions+=1
        if df_d['type_name'].iloc[i]=='Interception' and df_d['location'].iloc[i][0]>=40 :
            Number_of_defensive_actions+=1
        if df_d['type_name'].iloc[i]=='Foul Committed' and df_d['location'].iloc[i][0]>=40  :
            Number_of_defensive_actions+=1



    PPDA=Offensive_pass_number/Number_of_defensive_actions
    return PPDA,Offensive_pass_number,Number_of_defensive_actions




"""Calcolo Percentuale dei titi totali concessi, divisi in open paly e set pieces.
  Calcolo anche conversione dei totali non considerndo però i Rigori e gli autogol."""
def Gol_conversion_conceded_onShot(npgol,nps,setpgol,sps,total_conceded_gol_nopenalty,total_shots_no_penalty):

    #Calcolo i Goal su tiro
    
    #Nonpenalty gol su tiro in open play
    npgol_onshot=npgol/nps
    
    #SetPiece gol su tiro in Set Piece
    setpgol_onshot=setpgol/sps 
    
    #Gol totali escluso i rigori su tiri totali esclusi quelli dei rigori
    total_gol_nopenalty_onshot=total_conceded_gol_nopenalty/total_shots_no_penalty
    
    return npgol_onshot,setpgol_onshot,total_gol_nopenalty_onshot





"""Percentuale conversione dei tiri in porta concessi, divisi in open paly e set pieces.
     E anche i totali non considerndo però i Rigori e gli autogol."""
    
def Gol_conversion_conceded_onTarghetShot(npgol,shot_ot_np,setpgol,shot_ot_sp,total_conceded_gol_nopenalty,Total_ot_shots_nopenalty):
    
    #Nonpenalty gol su tiro in porta in open play
    npgol_onTarghetshot=npgol/shot_ot_np
    
    #SetPiece gol su tiro in porta in Set Piece
    setpgol_onTarghetshot=setpgol/shot_ot_sp 
    
    #Gol totali escluso i rigori su tiri totali in porta esclusi quelli dei rigori
    total_gol_nopenalty_onTarghetshot=total_conceded_gol_nopenalty/Total_ot_shots_nopenalty    
    return npgol_onTarghetshot,setpgol_onTarghetshot,total_gol_nopenalty_onTarghetshot



  
#Calcolo il PAPI
def PAPI(df,d_team_name,o_team_name):
    Offensive_pass_number=0
    Number_of_interceptions=0
    for i in range(len(df)):
        if df['type_name'].iloc[i]=='Pass' and df['team_name'].iloc[i]==o_team_name:
            Offensive_pass_number+=1
        if df['type_name'].iloc[i]=='Interception' and df['team_name'].iloc[i]==d_team_name:
            Number_of_interceptions+=1
    PAPI=Offensive_pass_number/Number_of_interceptions
    return PAPI

#Calcolo il PAPT
def PAPT(df,d_team_name,o_team_name):
    Offensive_pass_number=0
    Number_of_Tackle=0
    for i in range(len(df)):
        if df['type_name'].iloc[i]=='Pass' and df['team_name'].iloc[i]==o_team_name:
            Offensive_pass_number+=1
        if df['type_name'].iloc[i]=='Duel' and df['team_name'].iloc[i]==d_team_name:
            Number_of_Tackle+=1
    PAPT=Offensive_pass_number/Number_of_Tackle
    return PAPT  

#calcolo la PPAPPA 
def PPAPPA(df,d_team_name,o_team_name):
    Offensive_pass_number=0
    Number_of_Pressure=0
    for i in range(len(df)):
        if df['type_name'].iloc[i]=='Pass' and df['team_name'].iloc[i]==o_team_name:
            Offensive_pass_number+=1
        if df['type_name'].iloc[i]=='Pressure' and df['team_name'].iloc[i]==d_team_name:
            Number_of_Pressure+=1
    PPAPPA=Offensive_pass_number/Number_of_Pressure
    return PPAPPA 



"""2)STATISTICHE PER SINGOLI GIOCATORI"""


"""FUNZIONE PER Le divisioni con 0 a denominatore."""
def division(y, x):
    return 0 if x == 0 else y / x

def percentage(y, x):
    return 0 if x == 0 else (y / x)*100


"""Defensive Stats For Team"""
#Calcolo il PPDA come fa Statsbomb, nel modo che mi hanno speiegato per e-mail.
def PPDA(df,d_team_name,o_team_name):
    ppda_list=[0 for i in range(len(d_team_name[1:]))]
    d_team_name=d_team_name[-1]
    o_team_name=o_team_name[-1]
    columns=list(df.columns)
    Offensive_pass_number=0
    Number_of_defensive_actions=0
    fc=0
    df_o=df[(df['team_name']==o_team_name)]
    df_d=df[(df['team_name']==d_team_name)]
    for c in range(len(df_o)):
        if df_o['type_name'].iloc[c]=='Pass' and pd.isnull(df_o['pass_outcome_name'].iloc[c])==True and df_o['location'].iloc[c][0]<72:            
            Offensive_pass_number+=1
                
    for i in range(len(df_d)):            
        if df_d['duel_type_name'].iloc[i]=='Tackle' and df_d['location'].iloc[i][0]>=48:  
            Number_of_defensive_actions+=1
            
        if df_d['type_name'].iloc[i]=='Interception' and df_d['location'].iloc[i][0]>=48:
            Number_of_defensive_actions+=1
            
        if 'foul_committed_type_name' in columns:
            if 'foul_committed_offensive' in columns:
                if df_d['type_name'].iloc[i]=='Foul Committed' and df_d['foul_committed_offensive'].iloc[i]!=True and pd.isnull(df_d['foul_committed_type_name'].iloc[i])==True and df_d['location'].iloc[i][0]>=48:
                    fc+=1
                    Number_of_defensive_actions+=1
            else:
                if df_d['type_name'].iloc[i]=='Foul Committed' and pd.isnull(df_d['foul_committed_type_name'].iloc[i])==True and df_d['location'].iloc[i][0]>=48: 
                    Number_of_defensive_actions+=1
        else:    
            if 'foul_committed_offensive' in columns:
                if df_d['type_name'].iloc[i]=='Foul Committed' and df_d['location'].iloc[i][0]>=48 and df_d['foul_committed_offensive'].iloc[i]!=True:
                    Number_of_defensive_actions+=1
            else:       
                if df_d['type_name'].iloc[i]=='Foul Committed' and df_d['location'].iloc[i][0]>=48:
                    Number_of_defensive_actions+=1

        if df_d['type_name'].iloc[i]=='Dribbled Past' and df_d['location'].iloc[i][0]>=48:
            Number_of_defensive_actions+=1

        if df_d['type_name'].iloc[i]=='Block' and df_d['location'].iloc[i][0]>=48 :
            Number_of_defensive_actions+=1
            
    PPDA=Offensive_pass_number/Number_of_defensive_actions
    ppda_list.append(PPDA)
    return ppda_list



"""Calcolo altezza media interventi difensivi, escludo le pressioni e metto solo tackle e non duelli aerei"""
def Average_Defensive_Distance(df,home_list):
    add_list=[0 for i in range(len(home_list[1:]))]
    team=home_list[-1]
    columns=list(df.columns)
    height=0
    df=df[df['team_name']==team]
    n=0
    
    for i in range(len(df)):
        if df['duel_type_name'].iloc[i]=='Tackle':
            height+=int(df['location'].iloc[i][0])        
            n+=1
        if df['type_name'].iloc[i]=='Dribbled Past':
            height+=int(df['location'].iloc[i][0])        
            n+=1       
        if df['type_name'].iloc[i]=='Interception':
            height+=int(df['location'].iloc[i][0])        
            n+=1    
        if df['type_name'].iloc[i]=='Block':
            height+=int(df['location'].iloc[i][0])        
            n+=1    
        if 'foul_committed_type_name' in columns:
            if 'foul_committed_offensive' in columns:

                if df['type_name'].iloc[i]=='Foul Committed' and df['foul_committed_offensive'].iloc[i]!=True and pd.isnull(df['foul_committed_type_name'].iloc[i])==True:
                        height+=int(df['location'].iloc[i][0])        
                        n+=1         
            else:
                if df['type_name'].iloc[i]=='Foul Committed'  and pd.isnull(df['foul_committed_type_name'].iloc[i])==True:
                        height+=int(df['location'].iloc[i][0])        
                        n+=1         
                
        else:
            if 'foul_committed_offensive' in columns:

                if df['type_name'].iloc[i]=='Foul Committed' and df['foul_committed_offensive'].iloc[i]!=True:
                        height+=int(df['location'].iloc[i][0])        
                        n+=1     
            else:
                if df['type_name'].iloc[i]=='Foul Committed':
                        height+=int(df['location'].iloc[i][0])        
                        n+=1               
        #Faccio il numero totale di interventi meno il numero di falli fatti in possesso della palla
    ADD=height/n
    add_list.append(ADD)
    return add_list



"""Calcolo le azioni difensive fatte in area e fuori area""" 
def Defensive_Actions_in_out_Area(df,home_list):
    inside_list=[0 for i in range(len(home_list[1:]))]
    outside_list=[0 for i in range(len(home_list[1:]))]
    total_list=[0 for i in range(len(home_list[1:]))]
    inside_perc_list=[0 for i in range(len(home_list[1:]))]
    outside_perc_list=[0 for i in range(len(home_list[1:]))]

    defensiveteam=home_list[-1]

    inside=0
    outside=0
    defensive_team=df[df['team_name']==defensiveteam]
    
    columns=list(df.columns)
        
    for i in range(len(defensive_team)):

        if defensive_team['duel_type_name'].iloc[i]=='Tackle':
            if defensive_team['location'].iloc[i][0]<=18 and 18<=defensive_team['location'].iloc[i][1]<=62:
                inside+=1
            else:
                outside+=1
        if defensive_team['type_name'].iloc[i]=='Dribbled Past':
            if defensive_team['location'].iloc[i][0]<=18 and 18<=defensive_team['location'].iloc[i][1]<=62:
                inside+=1
            else:
                outside+=1
        if defensive_team['type_name'].iloc[i]=='Interception':
            if defensive_team['location'].iloc[i][0]<=18 and 18<=defensive_team['location'].iloc[i][1]<=62:
                inside+=1
            else:
                outside+=1
        if defensive_team['type_name'].iloc[i]=='Block':
            if defensive_team['location'].iloc[i][0]<=18 and 18<=defensive_team['location'].iloc[i][1]<=62:
                inside+=1
            else:
                outside+=1
                
        if 'foul_committed_type_name' in columns:
            if 'foul_committed_offensive' in columns:
           
                if defensive_team['type_name'].iloc[i]=='Foul Committed' and pd.isnull(defensive_team['foul_committed_type_name'].iloc[i])==True and df['foul_committed_offensive'].iloc[i]!=True:
                    if defensive_team['location'].iloc[i][0]<=18 and 18<=defensive_team['location'].iloc[i][1]<=62:
                        inside+=1
                    else:
                        outside+=1 
            else:
                if defensive_team['type_name'].iloc[i]=='Foul Committed' and pd.isnull(defensive_team['foul_committed_type_name'].iloc[i])==True:
                    if defensive_team['location'].iloc[i][0]<=18 and 18<=defensive_team['location'].iloc[i][1]<=62:
                        inside+=1
                    else:
                        outside+=1 
                
        else:
            if 'foul_committed_offensive' in columns:

                if defensive_team['type_name'].iloc[i]=='Foul Committed' and df['foul_committed_offensive'].iloc[i]!=True:
                    if defensive_team['location'].iloc[i][0]<=18 and 18<=defensive_team['location'].iloc[i][1]<=62:
                        inside+=1
                    else:
                        outside+=1
            else:
                if defensive_team['type_name'].iloc[i]=='Foul Committed':
                    if defensive_team['location'].iloc[i][0]<=18 and 18<=defensive_team['location'].iloc[i][1]<=62:
                        inside+=1
                    else:
                        outside+=1 
                        
    total=inside+outside
    
    inside_perc=percentage(inside,total)
    outside_perc=percentage(outside,total)
    
    inside_list.append(inside)
    outside_list.append(outside)
    total_list.append(total)
    inside_perc_list.append(inside_perc)
    outside_perc_list.append(outside_perc)

    return inside_list,outside_list,total_list,inside_perc_list,outside_perc_list
 
"""calcolo i passaggi, che non sono cross, permessi agli avversari entro 20 metri dalla porta."""
def Deep_Pass_Completions(df,home_list,o_team):
    dpc_list=[0 for i in range(len(home_list[1:]))]
    Pass=0
    Pass_no_cross=df[(df['type_name']=='Pass')  & (df['pass_cross']!=True) & (df['team_name']==o_team)] 
    for i in range(len(Pass_no_cross)):
        if Pass_no_cross['location'].iloc[i][0]>=100:
                Pass+=1
                
    dpc_list.append(Pass)
    return dpc_list




"""calcolo i cross permessi agli avversari entro 20 metri dalla porta."""
def Deep_Cross_Completions(df,home_list,o_team):
    dcc_list=[0 for i in range(len(home_list[1:]))]
    Cross=0
    cross=df[(df['type_name']=='Pass') & (df['pass_cross']==True) & (df['team_name']==o_team)] 
    for i in range(len(cross)):
        if cross['location'].iloc[i][0]>=100:
                Cross+=1
                
    dcc_list.append(Cross)
    return dcc_list





"""Defensive Macro Stats"""


"""Calcolo il numero di pressioni e contropressioni effettuate per valutare pressing e gegenpressing.
Calcolo la percentuale di pressioni effettuate nella metà campo avversaria,conisderando pressioni e contropress"""

def Pressure_and_Counterpressures_for_player(df,lista):
    p_list=[]#Lista numero pressioni
    cp_list=[]#Lista numero contropressioni
    ph_list=[]#Lista altezza pressioni
    ch_list=[]#Lista altezza contropressioni
    mph_list=[]#Lista altezza media pressioni
    mcph_list=[]#Lista altezza media contropressioni
    op_list=[]#Lista pressioni offensive    
    op_perc_list=[]#Lista percentuale sul totale pressioni offensive  
    
    for p in lista:
        Pressures=0
        Counterpressures=0
        pressure_height=0
        counterpressure_height=0

        press=df[df['player_name']==p]
        for i in range(len(press)):
            if press['type_name'].iloc[i]=='Pressure' and press['counterpress'].iloc[i]!=True:
                
                Pressures+=1
                pressure_height+=press['location'].iloc[i][0]
            elif press['type_name'].iloc[i]=='Pressure' and press['counterpress'].iloc[i]==True:
                
                Counterpressures+=1
                counterpressure_height+=press['location'].iloc[i][0]
                
        p_list.append(Pressures)
        cp_list.append(Counterpressures)
        ph_list.append(pressure_height)
        ch_list.append(counterpressure_height)
                
        #Calculation of mean pressure height
        mean_pressure_height=division(pressure_height,Pressures)

        mph_list.append(mean_pressure_height)
        
        #Calculation of mean counterpressure height
        mean_counterpressure_height=division(counterpressure_height,Counterpressures)

        mcph_list.append(mean_counterpressure_height)
        
        #Calcolo la percentuale di pressioni nella metà campo avversaria
        Pressure=df[(df['type_name']=='Pressure') & (df['player_name']==p) & (df['counterpress']!=True)]
        Total_Pressure=len(Pressure)
        offensive_half_pressure=0
        for b in range(len(Pressure)):
            if Pressure['location'].iloc[b][0]>60:
                offensive_half_pressure+=1
        op_list.append(offensive_half_pressure)
        
        #Calculation of offensive pressure percentage on the total ammount of pressure
        offensive_half_pressure_perc=percentage(offensive_half_pressure,Total_Pressure)
        
        op_perc_list.append(offensive_half_pressure_perc)
    
    """I Calculate Pressure and Conterpressue for Team"""  
    p_list.append(sum(p_list))
    cp_list.append(sum(cp_list))
    ph_list.append(sum(ph_list))
    ch_list.append(sum(ch_list))
    mph_list.append(ph_list[-1]/p_list[-1])
    mcph_list.append(ch_list[-1]/cp_list[-1])
    op_list.append(sum(op_list))
    op_perc_list.append((op_list[-1]/p_list[-1])*100) 

    return p_list,mph_list,cp_list,mcph_list,op_list,op_perc_list



""" Calcolo il numero di palloni recuperati in tutto il campo e l'altezza media dei recuperi, per giocatore"""

def Ball_Recovery_for_player(df,lista):
    columns=list(df.columns)
    b_r_list=[]
    h_list=[]
    m_r_h_list=[]
    for p in lista:
        df_p=df[(df['player_name']==p) & (df['type_name']=='Ball Recovery') ]
        height=0
        B_r=0
        
        if 'ball_recovery_recovery_failure' in columns:
            for i in range(len(df_p)):
                if df_p['type_name'].iloc[i]=='Ball Recovery' and df_p['ball_recovery_recovery_failure'].iloc[i]!=True:
                    B_r+=1
                    height+=df_p['location'].iloc[i][0]

        else:
            for i in range(len(df_p)):
                if df_p['type_name'].iloc[i]=='Ball Recovery':
                    B_r+=len(df_p)
                    height+=df_p['location'].iloc[i][0]

            
        #Calcualation of mean recovery height
        mean_recovery_height=division(height,B_r)
        
        b_r_list.append(B_r)   
        h_list.append(height)   
        m_r_h_list.append(mean_recovery_height)   

    """I Calculate Ball recovery for Team"""  
    b_r_list.append(sum(b_r_list))
    h_list.append(sum(h_list))
    m_r_h_list.append(division(h_list[-1],b_r_list[-1]))        
    
    return b_r_list,m_r_h_list


""" Calcolo il numero di palloni recuperati nella metà campo avversaria."""        
def High_Ball_Recovery_for_player(df,lista):
    columns=list(df.columns)
    h_b_r_lista=[]
    for p in lista:

        df_p=df[(df['player_name']==p) & (df['type_name']=='Ball Recovery') ]
        H_B_r=0
        
        if 'ball_recovery_recovery_failure' in columns:
            for i in range(len(df_p)):
                if df_p['type_name'].iloc[i]=='Ball Recovery' and df_p['ball_recovery_recovery_failure'].iloc[i]!=True and df_p['location'].iloc[i][0]>=60:
                    H_B_r+=1
        else:
            for i in range(len(df_p)):
                if df_p['type_name'].iloc[i]=='Ball Recovery' and df_p['location'].iloc[i][0]>=60:
                    H_B_r+=1
                    
        h_b_r_lista.append(H_B_r)

    """I Calculate High Ball recovery for Team"""  
    
    h_b_r_lista.append(sum(h_b_r_lista))        
    return h_b_r_lista







"""CALCOLO AZIONI DIFENSIVE SQUADRA"""

"""Calcolo numero contrasti fatti e la percentuale dei vinti"""

def Tackles_for_player(df,lista):
    t_n_list=[]
    w_t_list=[]
    t_w_p_list=[]
    for p in lista:
        Duel=df[(df['type_name']=='Duel') & (df['player_name']==p)]
        tackles=Duel[Duel['duel_type_name']=='Tackle']
        tackles_n=0
        won_tackles_n=0
        for i in range(len(tackles)):
            tackles_n+=1
            if tackles['duel_outcome_name'].iloc[i]=='Success In Play' or tackles['duel_outcome_name'].iloc[i]=='Success Out' or tackles['duel_outcome_name'].iloc[i]=='Won' or tackles['duel_outcome_name'].iloc[i]=='Success':
                won_tackles_n+=1
                
        t_n_list.append(tackles_n)
        w_t_list.append(won_tackles_n)
         
        #Calculation of percentage of tackles won on total ammount of tackle
        tackles_won_perc=percentage(won_tackles_n,tackles_n)
            
        t_w_p_list.append(tackles_won_perc)
        
    """I Calculate Tackles for Team"""  
    t_n_list.append(sum(t_n_list))
    w_t_list.append(sum(w_t_list))
    t_w_p_list.append(percentage(w_t_list[-1],t_n_list[-1]))   
       
    return t_n_list,w_t_list,t_w_p_list



"""Calcolo i contrasti fatti nella 3/4 difensiva, centrale e offensiva."""
def Tackles_zones_for_player(df,lista):
    #Creo le liste dove mettere i tackle fatti per le varie zone di campo per ogni player
    d_tq_t_list=[]
    md_tq_t_list=[]
    mo_tq_t_list=[]
    o_tq_t_list=[]
    
    #Creo le liste dove mettere i tackle vinti per le varie zone di campo per ogni player
    s_d_tq_t_list=[]
    s_md_tq_t_list=[]
    s_mo_tq_t_list=[]
    s_o_tq_t_list=[]

    #Creo le liste dove mettere le percentuali dei tackle completati per le varie zone di campo per ogni player
    p_d_tq_t_list=[]
    p_md_tq_t_list=[]
    p_mo_tq_t_list=[]
    p_o_tq_t_list=[]
    
    for p in lista:
        tackles=df[(df['duel_type_name']=='Tackle') & (df['player_name']==p) ] 
        #Calcolo contrasti tentati nelle varie one del campo
        d_tq_t=0#contrasti nei primi 30 metri di campo lontani dalla propria porta.
        md_tq_t=0#contrasti fatti tra i 30 e i 60 metri di campo lontani dalla propria porta.
        mo_tq_t=0#contrasti fatti tra i 60 e i 90 metri di campo lontani dalla propria porta.
        o_tq_t=0#contrasti fatti tra i 90 e i 120 metri di campo lontani dalla propria porta.
        
        #Calcolo contrasti completati nelle varie one del campo
        s_d_tq_t=0#contrasti nei primi 30 metri di campo lontani dalla propria porta.
        s_md_tq_t=0#contrasti fatti tra i 30 e i 60 metri di campo lontani dalla propria porta.
        s_mo_tq_t=0#contrasti fatti tra i 60 e i 90 metri di campo lontani dalla propria porta.
        s_o_tq_t=0#contrasti fatti tra i 90 e i 120 metri di campo lontani dalla propria porta.
        
        for i in range(len(tackles)):
            if tackles['location'].iloc[i][0]<=30:
                d_tq_t+=1
                if tackles['duel_outcome_name'].iloc[i]=='Success In Play' or tackles['duel_outcome_name'].iloc[i]=='Success Out' or tackles['duel_outcome_name'].iloc[i]=='Won' or tackles['duel_outcome_name'].iloc[i]=='Success':
                    s_d_tq_t+=1
            if 30<tackles['location'].iloc[i][0]<=60:
                md_tq_t+=1
                if tackles['duel_outcome_name'].iloc[i]=='Success In Play' or tackles['duel_outcome_name'].iloc[i]=='Success Out' or tackles['duel_outcome_name'].iloc[i]=='Won' or tackles['duel_outcome_name'].iloc[i]=='Success':
                    s_md_tq_t+=1                
            if 60<tackles['location'].iloc[i][0]<=90:
                mo_tq_t+=1
                if tackles['duel_outcome_name'].iloc[i]=='Success In Play' or tackles['duel_outcome_name'].iloc[i]=='Success Out' or tackles['duel_outcome_name'].iloc[i]=='Won' or tackles['duel_outcome_name'].iloc[i]=='Success':
                    s_mo_tq_t+=1     
            if 90<tackles['location'].iloc[i][0]<=120:
                o_tq_t+=1
                if tackles['duel_outcome_name'].iloc[i]=='Success In Play' or tackles['duel_outcome_name'].iloc[i]=='Success Out' or tackles['duel_outcome_name'].iloc[i]=='Won' or tackles['duel_outcome_name'].iloc[i]=='Success':
                    s_o_tq_t+=1  
                    
        #aggiungo alla lista i valori per i vari giocatori dei passaggi fatti.
        d_tq_t_list.append(d_tq_t)
        md_tq_t_list.append(md_tq_t)
        mo_tq_t_list.append(mo_tq_t)
        o_tq_t_list.append(o_tq_t)

        #aggiungo alla lista i valori per i vari giocatori il numero di passaggi riusciti.       
        s_d_tq_t_list.append(s_d_tq_t)
        s_md_tq_t_list.append(s_md_tq_t)
        s_mo_tq_t_list.append(s_mo_tq_t)
        s_o_tq_t_list.append(s_o_tq_t)          
        
        #Calcolo percentuali passaggi completati per ogni zona del campo interessata per ogni giocatore.
        p_d_tq_t=percentage(s_d_tq_t,d_tq_t)

        p_md_tq_t=percentage(s_md_tq_t,md_tq_t)

        p_mo_tq_t=percentage(s_mo_tq_t,mo_tq_t)

        p_o_tq_t=percentage(s_o_tq_t,o_tq_t)

        #aggiungo alla lista i valori per i vari giocatori della percentuale dei passaggi riusciti.      
        p_d_tq_t_list.append(p_d_tq_t)
        p_md_tq_t_list.append(p_md_tq_t)
        p_mo_tq_t_list.append(p_mo_tq_t)
        p_o_tq_t_list.append(p_o_tq_t)  
        
        
    """I Calculate Tackles zone for Team"""  
    #Number of total passes in the different pitch zones
    d_tq_t_list.append(sum(d_tq_t_list))
    md_tq_t_list.append(sum(md_tq_t_list))
    mo_tq_t_list.append(sum(mo_tq_t_list))
    o_tq_t_list.append(sum(o_tq_t_list))

    #Number of total succesfull passes in the different pitch zones
    s_d_tq_t_list.append(sum(s_d_tq_t_list))
    s_md_tq_t_list.append(sum(s_md_tq_t_list))
    s_mo_tq_t_list.append(sum(s_mo_tq_t_list))
    s_o_tq_t_list.append(sum(s_o_tq_t_list))

    #Percentage of succesfull passes on total amount of passes done.    
    p_d_tq_t=percentage(s_d_tq_t_list[-1],d_tq_t_list[-1])

    p_md_tq_t=percentage(s_md_tq_t_list[-1],md_tq_t_list[-1])

    p_mo_tq_t=percentage(s_mo_tq_t_list[-1],mo_tq_t_list[-1])

    p_o_tq_t=percentage(s_o_tq_t_list[-1],o_tq_t_list[-1])        
    
    p_d_tq_t_list.append(p_d_tq_t)
    p_md_tq_t_list.append(p_md_tq_t)
    p_mo_tq_t_list.append(p_mo_tq_t)
    p_o_tq_t_list.append(p_o_tq_t)   
    
    return d_tq_t_list,s_d_tq_t_list,p_d_tq_t_list,md_tq_t_list,s_md_tq_t_list,p_md_tq_t_list,mo_tq_t_list,s_mo_tq_t_list,p_mo_tq_t_list,o_tq_t_list,s_o_tq_t_list,p_o_tq_t_list




"""Calcolo i duelli aerei fatti, vinti e persi e la percentuale di quelli vinti."""
def Aerel_duels_for_player(df,lista):
    columns=list(df.columns)
    a_l_lista=[]
    a_w_lista=[]
    t_a_d_lista=[]
    a_w_p_lista=[]
    
    for p in lista:
        #Calcolo i duelli persi 
        aerial_lost=df[(df['player_name']==p) & (df['duel_type_name']=='Aerial Lost') ]
        a_l=len(aerial_lost)
        a_l_lista.append(a_l)
        #Calcolo i duelli vinti
        if 'shot_aerial_won' in columns:
            shot_aerial_won=df[(df['player_name']==p) &  (df['shot_aerial_won']==True) ]
            s_a_w=len(shot_aerial_won)
        else:
            s_a_w=0
        
        if 'shot_aerial_won' in columns:
            pass_aerial_won=df[(df['player_name']==p) &  (df['pass_aerial_won']==True) ]
            p_a_w=len(pass_aerial_won)

        else:
            p_a_w=0


        if 'clearance_aerial_won' in columns:
            clearance_aerial_won=df[(df['player_name']==p) &  (df['clearance_aerial_won']==True) ]
            c_a_w=len(clearance_aerial_won)
        
        else:
            c_a_w=0

        if 'miscontrol_aerial_won' in columns:
            miscontrol_aerial_won=df[(df['player_name']==p) &  (df['miscontrol_aerial_won']==True) ]
            m_a_w=len(miscontrol_aerial_won)
        
        else:
            m_a_w=0
            
        a_w = s_a_w + p_a_w + c_a_w + m_a_w
        a_w_lista.append(a_w)
        #Calcolo i duelli totali fatti
        t_a_d=a_l+a_w
        t_a_d_lista.append(t_a_d)
        
        #Calcolo la percentuale sul totale dei duelli aerei vinti
        a_w_p=percentage(a_w,t_a_d)
            
        a_w_p_lista.append(a_w_p)

    """I Calculate Aereal Duel for Team"""  
    a_l_lista.append(sum(a_l_lista))
    a_w_lista.append(sum(a_w_lista))
    t_a_d_lista.append(sum(t_a_d_lista))
    
    a_w_p_lista.append(percentage(a_w_lista[-1],t_a_d_lista[-1]))        
    
    return a_l_lista,a_w_lista,t_a_d_lista,a_w_p_lista


"""Calcolo i Dribbling affrontati, dove sei stato superato e quelli fermati"""
def Faced_Dribbling_for_player(df,lista):
    dribbling_subiti=[]
    dribbling_fermati=[]
    tackled_dribbling_perc=[]
    
    #Cerco i dribbling dove un giocatore è stato saltato
    for p in lista:
        player_dribble_past=df[(df['type_name']=='Dribbled Past') & (df['player_name']==p)]
        d_p=len(player_dribble_past)
        dribbling_subiti.append(d_p)
    
    #Cerco i dribbling contrastati
    for p in lista:
        d_f=0
        duel_player=df[(df['type_name']=='Duel') & (df['player_name']==p)]
        #trovo l'indice
        ind=list(duel_player.index)
        #ora cerco se l'evento prima del duello è un dribbling, se lo è sarà da contare come dribbling fermato.
        for i in ind:
            if df['type_name'].loc[i-1]=='Dribble':
                d_f+=1
                
            else:
                continue
            
        dribbling_fermati.append(d_f)
    
    #Dribbling affrontati
    dribling_affrontati=[a+b for a,b in zip(dribbling_subiti,dribbling_fermati)]           
    
    #Calcolo i tackle/Dribbled%
    tackle_dribble_perc=[percentage(a,b) for a,b in zip(dribbling_fermati,dribling_affrontati)]
    
    """I Calculate Dribbling for Team"""  
    dribling_affrontati.append(sum(dribling_affrontati))
    dribbling_subiti.append(sum(dribbling_subiti))
    dribbling_fermati.append(sum(dribbling_fermati))
    
    #Percentage of dribbling stopped
    tackle_dribble_perc_team=percentage(dribbling_fermati[-1],dribling_affrontati[-1]) #Percentage of Stopped Dribble 

    tackle_dribble_perc.append(tackle_dribble_perc_team)  
    
    return  dribling_affrontati, dribbling_subiti, dribbling_fermati, tackle_dribble_perc
            
        


"""Calcolo i dribbling subiti e fermati da un player"""    
def Dribbling_for_player(df,lista):
    d_list=[]
    s_d_list=[]
    st_d_list=[]
    t_d_list=[]
    
    for p in lista:
        dribble=df[(df['type_name']=='Dribble') & (df['player_name']==p)] #DF of the Dribble happened
        Dribble=len(dribble) #Number of Dribble happened
        d_list.append(Dribble)
        
        #Succesfull dribbling
        success_dribble=dribble[dribble['dribble_outcome_name']=='Complete'] #DF of Successfull Dribble
        Success_dribble=len(success_dribble) #Number of Succesfull Dribble
        s_d_list.append(Success_dribble)
        
        #Stopped dribbling
        stopped_dribble=dribble[dribble['dribble_outcome_name']=='Incomplete'] #DF of Stopped Dribble
        Stopped_dribble=len(stopped_dribble) #Number of stopped dribble
        st_d_list.append(Stopped_dribble)
        
        #Percentage of dribbling stopped
        Dribble_tackled=percentage(Stopped_dribble,Dribble) #Percentage of Stopped Dribble 
        t_d_list.append(Dribble_tackled)
        
    """I Calculate Dribbling for Team"""  
    d_list.append(sum(d_list))
    s_d_list.append(sum(s_d_list))
    st_d_list.append(sum(st_d_list))
    
    #Percentage of dribbling stopped
    Dribble_tackled=percentage(st_d_list[-1],d_list[-1]) #Percentage of Stopped Dribble 

    t_d_list.append(Dribble_tackled)     
      
    return d_list,s_d_list,st_d_list,t_d_list



"""Calcolo i tiri e i passaggi bloccati."""
def Blocks_for_player(df,lista,o_team):
    p_b_list=[]
    s_b_list=[]
    for p in lista:
        shot_block=0
        pass_block=0
        for i in range(len(df)):
            if df['type_name'].iloc[i]=='Block' and df['player_name'].iloc[i]==p:
                if df['type_name'].iloc[i-1]=='Shot' and df['team_name'].iloc[i-1]==o_team:
                    shot_block+=1
                elif df['type_name'].iloc[i-1]=='Pass' and df['team_name'].iloc[i-1]==o_team:
                    pass_block+=1
                    
        p_b_list.append(pass_block)
        s_b_list.append(shot_block)       
        
    """I Calculate Blocks for Team"""  
    p_b_list.append(sum(p_b_list))
    s_b_list.append(sum(s_b_list))
    return s_b_list,p_b_list



"""Calcolo gli intercetti fatti"""
def Interceptions_for_player(df,lista):
    int_lista=[]
    s_i_lista=[]
    p_s_i_list=[]
    
    for p in lista:
        interceptions=df[(df['type_name']=='Interception') & (df['player_name']==p)] #DF of Interceptions
        intercepts=len(interceptions) #Number of Interceptions Happened
        int_lista.append(intercepts)
        
        
        succesfull_interceptions=interceptions[(interceptions['interception_outcome_name']!='Lost') & (interceptions['interception_outcome_name']!='Lost In Play')] #DF of Interceptions
        Succesfull_interceptions=len(succesfull_interceptions) #Number of Successfull Interceptions
        s_i_lista.append(Succesfull_interceptions)


        p_s_i_list.append(percentage(Succesfull_interceptions, intercepts))
    """I Calculate Interceptions for Team"""  
    int_lista.append(sum(int_lista))   
    s_i_lista.append(sum(s_i_lista))   
    
    p_s_i_list.append(percentage(s_i_lista[-1], int_lista[-1]))
    
    return int_lista,s_i_lista,p_s_i_list


def clearance(df,lista):
    clearance_list=[]
    for p in lista:
        clearance=df[(df['type_name']=='Clearance') & (df['player_name']==p)]
        clearance=len(clearance) #Numero di errori che portano ad un tiro o ad una palla recuperata o ecc.
        clearance_list.append(clearance)

    """I Calculate Clearances for Team"""  
    clearance_list.append(sum(clearance_list)) 

    return clearance_list

"""Calcolo i falli commessi"""

def Fouls_Committed_for_player(df,lista):
    columns=list(df.columns)
    fouls_list=[]
    for p in lista:
        df=df[df['player_name']==p]
        fouls=0
        if 'foul_committed_type_name' in columns:
            for i in range(len(df)):
                if df['type_name'].iloc[i]=='Foul Committed':  
                    if pd.isnull(df['foul_committed_type_name'].iloc[i])==True:
                        fouls+=1
        else:
            for i in range(len(df)):
                if df['type_name'].iloc[i]=='Foul Committed':
                    fouls+=1
        fouls_list.append(fouls)    
        
    """I Calculate Fouls committed for Team"""  
    fouls_list.append(sum(fouls_list))   
     
    return fouls_list



    

""""Calcolo gli Errori che hanno portato ad un tiro o ad un evento di un portiere o a una palla recuperata.
In generale gli errori sono un controllo sbagliato o una spazzata fatta male."""

def Error_for_player(df,lista):
    error_list=[]
    for p in lista:
        error=df[(df['type_name']=='Error') & (df['player_name']==p)]
        Error=len(error) #Numero di errori che portano ad un tiro o ad una palla recuperata o ecc.
        error_list.append(Error)

    """I Calculate Interceptions for Team"""  
    error_list.append(sum(error_list)) 
    return error_list


    