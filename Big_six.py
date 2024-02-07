#Import libraries
import pandas as pd
import random

#Declare list
bix_six = ["Manchester United", "Liverpool", "Arsenal", "Chelsea", "Manchester City", "Tottenham Hotspur"]  #List of teams
headers_teams = ["Team", "Played", "Won", "Drawn", "Lost", "GF", "GA", "GD", "Points"]  #Column header of the first dataframe
header_games = ["Team_01", "Goals_01", "Team_02", "Goals_02"]   #Column header of the second dataframe
available_yes_no = ["y", "yes", "YES", "n", "no", "NO"]
options_menu = ["1", "2"]

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

#Given a question and a list of answers, the function will evaluate if the
#answer to the question is within the list
def check_answer(question, list_answers):
    start_check = False
    while start_check == False:
        option_user = input(question)
        if option_user in list_answers:
            start_check = True
        else:
            print("Wrong option. Let's go again\n")
    return option_user

#Function to assign values specific in the main dataframe
def assign_first_dataframe(first_team, second_team, goals_01, goals_02, first_df):
    index_01 = first_df.index[first_df["Team"] == first_team]
    index_02 = first_df.index[first_df["Team"] == second_team]
    if goals_01 > goals_02:
        first_df.loc[index_01, "Points"] += 3
        first_df.loc[index_01, "Won"] += 1
        first_df.loc[index_02, "Lost"] += 1
    if goals_02 > goals_01:
        first_df.loc[index_02, "Points"] += 3
        first_df.loc[index_02, "Won"] += 1
        first_df.loc[index_01, "Lost"] += 1
    else:
        first_df.loc[index_01, "Points"] += 1
        first_df.loc[index_02, "Points"] += 1
        first_df.loc[index_01, "Drawn"] += 1
        first_df.loc[index_02, "Drawn"] += 1
    first_df.loc[index_01, "GF"] += goals_01
    first_df.loc[index_01, "GA"] += goals_02
    first_df.loc[index_02, "GF"] += goals_02
    first_df.loc[index_02, "GA"] += goals_01
    first_df.loc[index_01, "Played"] += 1
    first_df.loc[index_02, "Played"] += 1


#Function to evaluate the 3 games between two teams
def games_played(number_games, first_team, second_team, first_df, second_df):
    for i in range(number_games):
        goals_team_01 = random.randint(0,5)
        goals_team_02 = random.randint(0,5)
        list_row = [first_team, goals_team_01, second_team, goals_team_02]
        #Assign a row to the games dataframe
        second_df.loc[len(second_df)]= list_row
        #Function to assign values to the first dataframe
        assign_first_dataframe(first_team, second_team, goals_team_01, goals_team_02, first_df)


#Function to traverse the list. This function allows you to face different teams without repeating
def big_six_random(six_teams, df_01, df_02):
    lenght_teams = len(bix_six)
    for i in range(lenght_teams):
        for j in range(lenght_teams):
            if j > i :
                team_01 = six_teams[i]
                team_02 = six_teams[j]
                games_played(3, team_01, team_02, df_01, df_02)
    #Add goal difference
    for i in range(lenght_teams):
        df_01.loc[i, "GD"] = df_01.loc[i, "GF"] - df_01.loc[i, "GA"]
    #Sort by points from highest to lowest
    df_01.sort_values(by='Points', ascending=False, inplace=True)

#Message to exit the program
def message_custom(sentence):
    print()
    print(sentence)
    print("Thank you")
    print("Come back soon\n")

#Initial menu
menu_start = """

"""

#Main Function
def main():
    reset_main_menu = True
    while reset_main_menu == True:

        print(menu_start)
        chosen_option = check_answer("Chose one of the options (1, 2): ", options_menu)
        if chosen_option == "1":
            print("opcion_1")
        elif chosen_option == "2":
            print("opcion_2")
        question_menu = check_answer("\nDo you want to return to the main menu? (y/n): ", available_yes_no)
        if question_menu in available_yes_no[0:3]:
            print("\nLet's start again..!!!!\n")
            reset_main_menu = True
        else:        
            message_custom("")
            reset_main_menu = False

#Entry point
if __name__ == "__main__":
    main()

#Hace falta una funcion para acceder a los partidos entre dos equipos en particular
    
#Hay que probarlo con un dataframe más pequeño de 3 equipos para poder ver el funcionamiento