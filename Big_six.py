#Import libraries
import pandas as pd
import random

#Declare list
bix_six = ["Manchester United", "Liverpool", "Arsenal", "Chelsea", "Manchester City", "Tottenham Hotspur"]  #List of teams
headers_teams = ["Team", "Played", "Won", "Drawn", "Lost", "GF", "GA", "GD", "Points"]  #Column header of the first dataframe
header_games = ["Team_01", "Goals_01", "Team_02", "Goals_02"]   #Column header of the second dataframe

#Declare the data of the first dataframe
data_teams = [
    ["Manchester United", 0, 0, 0, 0, 0, 0, 0, 0],
    ["Liverpool", 0, 0, 0, 0, 0, 0, 0, 0],
    ["Arsenal", 0, 0, 0, 0, 0, 0, 0, 0],
    ["Chelsea", 0, 0, 0, 0, 0, 0, 0, 0],
    ["Manchester City", 0, 0, 0, 0, 0, 0, 0, 0],
    ["Tottenham Hotspur", 0, 0, 0, 0, 0, 0, 0, 0]
]

#Function to create the dataframes to use
def create_df():
    df_01 = pd.DataFrame(data_teams, columns=headers_teams) #Create the first dataFrame
    df_02 = pd.DataFrame(columns=header_games) #Create the second dataFrame
    return df_01, df_02

df_points, df_games = create_df()

#Function to traverse the list. This function allows you to face different teams without repeating
def big_six_random(six_teams, df_01, df_02):
    lenght_teams = len(bix_six)
    for i in range(lenght_teams):
        for j in range(lenght_teams):
            if j > i :
                team_01 = six_teams[i]
                team_02 = six_teams[j]
                #funcion que se tiene que repetir tres veces
                goals_team_01 = random.randint(0,5)
                goals_team_02 = random.randint(0,5)
                print(team_01, team_02, goals_team_01, goals_team_02)

big_six_random(bix_six, df_points, df_games)