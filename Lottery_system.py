#Import libraries
import random

#Declare tuples
options_tickets = ("5678B", "9876C", "2345D", "6789E", "3456F", "8765G", "4321H", "7890J", "5432K", "2109L", "8765M", "1357N", "2468P", "6543Q", "7891R", "3579S", "9821T", "4682U", "5763V", "1234A")
options_yes_no = ("y", "yes", "YES", "n", "no", "NO")
options_numbers = ("1", "2")

#Function to generate the winning lottery ticket
def winning_ticket():
    ticket_win = ""
    for i in range(5):
        if i == 4:
            digit_win = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        else:
            digit_win = str(random.randint(0,9))
        ticket_win = ticket_win + digit_win
    return ticket_win

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

#Function to choose the number of tickets to buy
def number_tickets(options_answers):
    question_01 = "Do you want to buy 1 or 2 tickets?: "
    number = check_answer(question_01, options_answers)
    number = int(number)
    return number

#Function to choose the tickets
def tickets(number_tickets, tickets_list):
    list_numbers = []
    tickets_user_list = []
    print("Ticket numbers available for sale:\n")
    j = 1
    for i in tickets_list:
        print(f"{j}- {i}")
        k = str(j)
        list_numbers.append(k)
        j = j + 1
    count = 1
    while count <= number_tickets:
        question_02 = f"Choose ticket #{count} (1-20): "
        ticket_i = check_answer(question_02, list_numbers)
        list_numbers.remove(ticket_i)
        ticket_user = tickets_list[int(ticket_i) - 1]
        tickets_user_list.append(ticket_user)
        count = count + 1
    return tickets_user_list

