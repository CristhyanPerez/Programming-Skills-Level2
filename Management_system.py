#Import the libraries
import os
import csv
import pandas as pd

#Declare list
options_menu = ["1", "2", "3"]
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
            print("Wrong option. Let's go again\n")
    return option_user

#Funtion to verify the existence of .csv file. If it doesn't exist, it's created
def file_exists(file):
    file_csv_exists = os.path.isfile(file)
    if not file_csv_exists:
        with open(file, "w") as file:
            file.write('')

#Funtion to transform the csv file into a pandas dataframe
def transform_dataset(file):
    dataframe = pd.read_csv(file, names = ["Name", "Jersey Number", "Position", "Age", "Height(cm)", "Weight(Kg)", "Goals", "Points Speed", "Points Assists", "Passing accuracy", "Defensive Involving"], sep = "\t")
    return dataframe

#Function to show the characteristics of a specific player throught the jersey number
def player_characterics(list_options_jersey, df):
    #Falta acomodar el print, puesto que ahora habrán más
    print("\nJersey number available to review:", ", ".join(map(str, list_options_jersey)), "\n")
    print()
    question = "Choose a jersey number: "
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
    print("\nJersey number available to review:", ", ".join(map(str, list_options_jersey)), "\n")
    #We request the first jersey number to compare
    question_1 = "Choose a jersey number: "
    option_jersey_1 = check_answer(question_1, list_available)
    print(list_available)
    list_available.remove(option_jersey_1)
    option_jersey_1 = int(option_jersey_1)
    index_1 = df[df["Jersey Number"] == option_jersey_1].index[0]
    print("\nRemember to choose a different jersey number to be  able to compare.\n")
    #We request the second jersey number to compare
    question_2 = "Choose a jersey number: "
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
    ****************  Manchester United  *******************

    Welcome friend to your favourite place
    The program has the following options:

    1- Show the characteristics of a specific player
    2- Compare two players using the jersey numbers
    3- Show General statistics

    """
    print(start)

#Message to exit the program
def message_custom(sentence):
    print()
    print(sentence)
    print("Thank you")
    print("Come back soon\n")

#Main Function
def main():
    reset_main_menu = True
    while reset_main_menu == True:
        file_exists("Manchester_United.csv")
        df_mu = transform_dataset("Manchester_United.csv")
        jersey_numbers = df_mu["Jersey Number"].tolist()
        jersey_available = [str(dato) for dato in jersey_numbers]
        menu_start()
        chosen_option = check_answer("Chose one of the options (1, 2, 3): ", options_menu)
        if chosen_option == "1":
            player_characterics(jersey_available, df_mu)
        elif chosen_option == "2":
            player_compare(jersey_available, df_mu)
        elif chosen_option == "3":
            players_statistics(df_mu)
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
