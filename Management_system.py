#Import the libraries
import os
import csv
import pandas as pd

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
    dataframe = pd.read_csv(file, names = ["name", "last_name", "program", "city"], sep = "\t")
    return dataframe

#Main Function
def main():
    reset_main_menu = True
    while reset_main_menu == True:
        chosen_option = check_answer("Chose one of the options (1, 2, 3): ", options_menu)
        if chosen_option == "1":
            pass
        elif chosen_option == "2":
            pass
        elif chosen_option == "3":
            pass
        question_menu = check_answer("\nDo you want to return to the main menu? (y/n): ", available_yes_no)
        if question_menu in available_yes_no[0:3]:
            print("\nLet's start again..!!!!\n")
            reset_main_menu = True
        else:        
            pass
            reset_main_menu = False

#Entry point
if __name__ == "__main__":
    main()
