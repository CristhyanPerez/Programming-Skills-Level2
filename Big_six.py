#Import libraries
import pandas as pd
import random

#Declare list
big_six = ["Manchester United", "Liverpool", "Arsenal", "Chelsea", "Manchester City", "Tottenham Hotspur"]  #List of teams
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
    lenght_teams = len(big_six)
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

#Function to choose two teams from a list. Without repeating
def choose_2_teams(menu, list_teams):
    list_options_01 = []
    list_options_02 = list_teams
    list_options_03 = []
    number_options = len(list_options_02)
    for j in range(2):
        print(menu)
        for i in range(1, number_options + 1):
            print(f"{i}- { list_options_02[i-1]}")
            option = str(i)
            list_options_01.append(option)
        question = f"\nChoose a team (1 - {number_options}): "
        team_choose_01 = check_answer(question, list_options_01)
        index = int(team_choose_01) - 1
        team_number_01 = list_teams[index]
        list_options_03.append(team_number_01)
        list_options_02.remove(team_number_01)
        number_options = len(list_options_02)
    list_options_02 = []
    return list_options_03

#Function that will be used to give 2 chosen teams, order them from
#lowest to highest according to their index and return the two ordered teams
def teams_and_values(list_six_teams, two_teams):
    index_01 = list_six_teams.index(two_teams[0])
    index_02 = list_six_teams.index(two_teams[1])
    if index_01 < index_02:
        value_01 = index_01
        value_02 = index_02
    else:
        value_01 = index_02
        value_02 = index_01
    team_1_match = list_six_teams[value_01]
    team_2_match = list_six_teams[value_02]
    return team_1_match, team_2_match

#Summary of matches between two teams
def summary_option_2(data, team_01, team_02):
    list_01 = data['Goals_01'].tolist()
    list_02 = data['Goals_02'].tolist()
    print("\nSummary of matchs:\n")
    for i in range(1, 4):
        print(f"Match 0{i}  |   {team_01} ({list_01[i-1]})   -   {team_02} ({list_02[i-1]})") 

#Message to exit the program
def message_custom(sentence):
    print(sentence)
    print("Thank you")
    print("Come back soon\n")

#Initial menu
menu_start = """
*************************    Premier League    *************************

Welcome to your favourite Premier League Blog.

Options:
1. See position table
2. Scoreboard of a duel between two teams
"""

second_menu = """
Teams available:
"""

#Main Function
def main():
    reset_main_menu = True
    df_points, df_games = create_df()
    big_six_00 = ["Manchester United", "Liverpool", "Arsenal", "Chelsea", "Manchester City", "Tottenham Hotspur"]
    big_six_random(big_six_00, df_points, df_games)
    while reset_main_menu == True:
        print(menu_start)
        chosen_option = check_answer("Chose one of the options (1, 2): ", options_menu)
        if chosen_option == "1":
            print()
            print(df_points.to_string(index=False))
        elif chosen_option == "2":
            big_six_01 = ["Manchester United", "Liverpool", "Arsenal", "Chelsea", "Manchester City", "Tottenham Hotspur"]
            list_2_teams = choose_2_teams(second_menu, big_six_01)
            big_six_02 = ["Manchester United", "Liverpool", "Arsenal", "Chelsea", "Manchester City", "Tottenham Hotspur"]
            team_01, team_02 = teams_and_values(big_six_02, list_2_teams)
            df_filtered_1 = df_games.loc[(df_games["Team_01"] == team_01)]
            df_filtered_2 = df_filtered_1.loc[(df_filtered_1["Team_02"] == team_02)]
            summary_option_2(df_filtered_2, team_01, team_02)
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