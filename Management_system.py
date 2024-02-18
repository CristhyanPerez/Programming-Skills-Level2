#Import the libraries
import os
import csv
import pandas as pd

#Declare list
options_menu = ["1", "2", "3", "4", "5", "6", "7"]
available_yes_no = ["y", "yes", "YES", "n", "no", "NO"]

#Given a question and a list of answers, the function will evaluate if the
#answer to the question is within the list
def check_answer(question, list_answers):
    start_check = False
    while start_check == False:
        option_user = input(question)
        if option_user in list_answers:
            start_check = True
        else:
            print("    Wrong option. Let's go again\n")
    return option_user

#Funtion to verify the existence of .csv file. If it doesn't exist, it's created
def file_exists(file):
    file_csv_exists = os.path.isfile(file)
    if not file_csv_exists:
        with open(file, "w") as file:
            file.write('')

#Funtion to transform the csv file into a pandas dataframe
def transform_dataset(file):
    dataframe = pd.read_csv(file, names = ["Name", "Jersey Number", "Position", "Age", "Height(cm)", "Weight(Kg)", "Goals", "Points Speed", "Points Assists", "Passing accuracy", "Defensive Involving"])
    return dataframe

#Function to display the dataframe
def show_data(dataframe):
    print("\n    Full list of players:\n")
    print(dataframe.to_string(index=False))

#Function to add values to csv file
def add_values_csv(file, data_list):
    path_csv_file = os.path.join(os.path.dirname(__file__), file)
    with open(path_csv_file, "a", newline = "") as file_csv:
        write_csv = csv.writer(file_csv, delimiter = ",")
        write_csv.writerow(data_list)

#Function to add new players
def players_new(file, options):
    add_player = True
    count = 1
    while add_player == True:
        list_data_player = []
        print(f"\n    Add Player data #{count}:")
        name_user = input("    Name:                ")
        jersey_user = input("    Jersey Number:       ")
        position_user = input("    Position:            ")
        age_user = input("    Age:                 ")
        height_user = input("    Height(cm):          ")
        weight_user = input("    Weight(Kg):          ")
        goals_user = input("    Goals:               ")
        speed_user = input("    Point Speed:         ")
        assits_user = input("    Point Assits:        ")
        accuracy_user = input("    Passing Accuracy:    ")
        defensive_user = input("    Defensive including: ")
        list_data_player = [name_user, jersey_user, position_user, age_user, height_user, weight_user, goals_user, speed_user, assits_user, accuracy_user, defensive_user]
        question_add_player_01 = check_answer("\n    Are you sure about adding the player with these characteristics? (y/n): ", options)
        if question_add_player_01 in options[0:3]:
            add_values_csv(file, list_data_player)
            print("\n    Player successfully added..!!!!\n")
            question_add_player_02 = check_answer("\n    Do you want to add another player? (y/n): ", options)
            if question_add_player_02 in options[0:3]:
                count = count + 1
                add_player = True
            else:        
                print("\n    OK..!!!!\n")
                add_player = False
        else:        
            print("\n    OK..!!!!\n")
            question_add_player_03 = check_answer("\n    Do you want to exit the 'add players' option? (y/n): ", options)
            if question_add_player_03 in options[0:3]:
                print("\n    OK..!!!!\n")
                add_player = False
            else:
                add_player = True

#Function to add new players
def players_delete(data, file, options):
    list_players = data['Name'].tolist()
    print("\n    Players available in the dataset:\n")
    players_lenght = len(list_players)
    list_numbers = []
    for i in range(1, players_lenght + 1):
        item = str(i)
        list_numbers.append(item)
    count = 0
    for name in list_players:
        print(f"    {list_numbers[count]}|    {name}")
        count = count + 1
    player_delete = check_answer(f"\n    Which player do you want to delete from the dataset(1-{players_lenght}): ", list_numbers)
    question_add_player_01 = check_answer("\n    Are you sure about adding the player with these characteristics? (y/n): ", options)
    if question_add_player_01 in options[0:3]:
        index_player = int(player_delete) - 1
        player = list_players[index_player]
        index_data = data.index[data["Name"] == player]
        #Delete the specific row from the dataframe
        data = data.drop(0) #Delete the headers
        data = data.drop(index_data)
        #Write the update dataframe back to the CSV file
        data.to_csv(file, index=False)
        print("\n    Player successfully deleted..!!!!\n")
    else:        
        print("\n    OK..!!!!\n")

#Function to show the characteristics of a specific player throught the jersey number
def player_characterics(list_options_jersey, df):
    print("\n    Jersey number available to review:", ", ".join(map(str, list_options_jersey)), "\n")
    print()
    question = "    Choose a jersey number: "
    option_jersey = int(check_answer(question, list_options_jersey))
    #Searched in the dataframe, to which index the entered jersey corresponds
    index = df[df["Jersey Number"] == option_jersey].index[0]
    summary = f"""
    ********************************************
            
            Jersey Number: {str(option_jersey)}

    Name:                   {df.loc[index, 'Name']} 
    Position:               {df.loc[index, 'Position']}
    Age:                    {df.loc[index, 'Age']}
    Height(cm):             {df.loc[index, 'Height(cm)']}
    Weight(Kg):             {df.loc[index, 'Weight(Kg)']}
    Goals:                  {df.loc[index, 'Goals']}
    Points Speed:           {df.loc[index, 'Points Speed']}
    Points Assists:         {df.loc[index, 'Points Assists']}
    Passing accuracy:       {df.loc[index, 'Passing accuracy']}
    Defensive Involving:    {df.loc[index, 'Defensive Involving']}

    ********************************************
    """
    print(summary)

#Function to compare two players using the jersey numbers
def player_compare(list_options_jersey, df):
    list_available = []
    list_available = list_options_jersey
    print("\n    Jersey number available to review:", ", ".join(map(str, list_options_jersey)), "\n")
    #We request the first jersey number to compare
    question_1 = "    Choose a jersey number: "
    option_jersey_1 = check_answer(question_1, list_available)
    list_available.remove(option_jersey_1)
    option_jersey_1 = int(option_jersey_1)
    index_1 = df[df["Jersey Number"] == option_jersey_1].index[0]
    print("\n    Remember to choose a different jersey number to be  able to compare.\n")
    #We request the second jersey number to compare
    question_2 = "    Choose a jersey number: "
    option_jersey_2 = check_answer(question_2, list_available)
    option_jersey_2 = int(option_jersey_2)
    index_2 = df[df["Jersey Number"] == option_jersey_2].index[0]
    #Summary to show the comparision
    summary = f"""
    **********************************************************
            
                        {df.loc[index_1, 'Name']}     {df.loc[index_2, 'Name']}   

    Jersey Number:          {str(option_jersey_1)}                  {str(option_jersey_2)}
    Age:                    {df.loc[index_1, 'Age']}                 {df.loc[index_2, 'Age']}
    Height(cm):             {df.loc[index_1, 'Height(cm)']}                {df.loc[index_2, 'Height(cm)']}
    Weight(Kg):             {df.loc[index_1, 'Weight(Kg)']}                 {df.loc[index_2, 'Weight(Kg)']}
    Goals:                  {df.loc[index_1, 'Goals']}                  {df.loc[index_2, 'Goals']}
    Points Speed:           {df.loc[index_1, 'Points Speed']}                  {df.loc[index_2, 'Points Speed']}       
    Points Assists:         {df.loc[index_1, 'Points Assists']}                  {df.loc[index_2, 'Points Assists']} 
    Passing accuracy:       {df.loc[index_1, 'Passing accuracy']}                  {df.loc[index_2, 'Passing accuracy']}      
    Defensive Involving:    {df.loc[index_1, 'Defensive Involving']}                  {df.loc[index_2, 'Defensive Involving']}     

    **********************************************************
    """
    print(summary)

#Function to show the most relevant statistic
def players_statistics(df):
    summary = f"""
    ****************  General Statistics  *******************

        The fastest player:                   
            {df.loc[df['Points Speed'].idxmax(), 'Name']} ({df.loc[df['Points Speed'].idxmax(), 'Points Speed']}) 

        The top goal scorer:                  
            {df.loc[df['Goals'].idxmax(), 'Name']} ({df.loc[df['Goals'].idxmax(), 'Goals']}) 

        The player with the most assists:           
            {df.loc[df['Points Assists'].idxmax(), 'Name']} ({df.loc[df['Points Assists'].idxmax(), 'Points Assists']})

        The player with the highest passing accuracy:         
            {df.loc[df['Passing accuracy'].idxmax(), 'Name']} ({df.loc[df['Passing accuracy'].idxmax(), 'Passing accuracy']})

        the player with the most defensive involvements:      
            {df.loc[df['Defensive Involving'].idxmax(), 'Name']} ({df.loc[df['Defensive Involving'].idxmax(), 'Defensive Involving']})
    
    *********************************************************
    """
    print(summary)

#Menu
def menu_start():
    start = """
    ****************************************************************
    **********  Management System - Manchester United  *************

    Welcome friend to your favourite place. This is a CRUD
    System. The program has the following options:

    1-  Add new players to the system with their respective details
    2-  View the complete list of current players
    3-  Modify player information as needed, such as position, age,
        height, or weight
    4-  Remove players from the system if they are no longer part
        of the team
    5-  Show the characteristics of a specific player
    6-  Compare two players using the jersey numbers
    7-  Show General statistics

    """
    print(start)

#Message to exit the program
def message_custom(sentence):
    print()
    print(sentence)
    print("    Thank you")
    print("    Come back soon\n")

#Main Function
def main():
    reset_main_menu = True
    while reset_main_menu == True:
        file_exists("Manchester_United.csv")
        df_mu = transform_dataset("Manchester_United.csv")
        jersey_numbers = df_mu["Jersey Number"].tolist()
        jersey_available = [str(dato) for dato in jersey_numbers]
        menu_start()
        chosen_option = check_answer("    Chose one of the options (1 - 7): ", options_menu)
        if chosen_option == "1":
            players_new("Manchester_United.csv", available_yes_no)
        elif chosen_option == "2":
            show_data(df_mu)
        elif chosen_option == "3":
            pass
        elif chosen_option == "4":
            players_delete(df_mu, "Manchester_United.csv", available_yes_no)
        elif chosen_option == "5":
            player_characterics(jersey_available, df_mu)
        elif chosen_option == "6":
            player_compare(jersey_available, df_mu)
        elif chosen_option == "7":
            players_statistics(df_mu)
        question_menu = check_answer("\n    Do you want to return to the main menu? (y/n): ", available_yes_no)
        if question_menu in available_yes_no[0:3]:
            print("\n    Let's start again..!!!!\n")
            reset_main_menu = True
        else:        
            message_custom("")
            reset_main_menu = False

#Entry point
if __name__ == "__main__":
    main()