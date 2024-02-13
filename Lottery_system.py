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
    question_01 = "\nDo you want to buy 1 or 2 tickets?: "
    number = check_answer(question_01, options_answers)
    number = int(number)
    return number

#Function to choose the tickets
def tickets(number_tickets, tickets_list):
    list_numbers = []
    tickets_user_list = []
    print("\nTicket numbers available for sale:\n")
    j = 1
    for i in tickets_list:
        print(f" {j}- {i}")
        k = str(j)
        list_numbers.append(k)
        j = j + 1
    print()
    count = 1
    while count <= number_tickets:
        question_02 = f"Choose ticket #{count} (1-20): "
        ticket_i = check_answer(question_02, list_numbers)
        list_numbers.remove(ticket_i)
        ticket_user = tickets_list[int(ticket_i) - 1]
        tickets_user_list.append(ticket_user)
        print(f"The purchase ticket is: {tickets_user_list[count-1]}\n")
        count = count + 1
    return tickets_user_list

#Function to choose the number of tickets to buy
def buy_ticket(options_answers):
    question_01 = "Choose one of the options(1-2): "
    number = check_answer(question_01, options_answers)
    number = int(number)
    return number

#Function to declare the success of the lottery ticket payment
def successful_payment(tickets_amount, menu_01, menu_02, menu_03, options):
    print(menu_01)
    option_01 = buy_ticket(options)
    if option_01 == 1:
        if tickets_amount == 1:
            print(menu_03)
            option_02 = buy_ticket(options)
            print(f"\nYou have bought {tickets_amount} lottery ticket")
            if option_02 == 1:
                print("Cost: $1.00")
                print("Return: $4.00")
            else:
                print("Cost: $1.00")
                print("Return: $0.00")
        else:
            print(menu_02)
            option_03 = buy_ticket(options)
            print(f"\nYou have bought {tickets_amount} lottery ticket")
            if option_03 == 1:
                print("Cost: $2.00")
                print("Return: $3.00")
            else:
                print("Cost: $2.00")
                print("Return: $0.00")

#Function to define if the lottery was won
def lottery_play(list_options, ticket_random):
    print(f"\nThe winning ticket is: {ticket_random}\n")
    i = 1
    count = 0
    for ticket in list_options:
        print(f"Ticket #{i}: {ticket}")
        if ticket == ticket_random:
            count = count + 1
            number_win = i
        i = i + 1
    if count == 0:
        print("\nNo ticket matches the winner.\n")
    else:
        print(f"\nTicket #{number_win} matches the winning ticket")
        print("\n**************  Congratulations - You won the lottery  ****************\n")

#Message to exit the program
def message_custom(sentence):
    print(sentence)
    print("Thank you")
    print("Come back soon\n")

#Initial menu
menu_start = """
*************************    Lottery System    *************************

Welcome to your favourite lottery game.

Notes:
* You can buy a minimum of 1 and a maximum of two tickets.
* Each ticket costs $1.00.
* Payment methods are cash or bank card.
* This system only accepts $1.00 and $5.00 bills.
* You cannot choose the same ticket twice, in case you decide to buy
  two tickets.
"""

#Cash-card menu
second_menu = """
As mentioned at the beginning. 
You have the following payment options:

1. Cash
2. Credit card
"""

#Cash payment options #01
third_menu = """ 
You have the following cash payment options:

1. A $5.00 bill
2. Two $1.00 bills
"""

#Cash payment options #02
fourth_menu = """ 
You have the following cash payment options:

1. A $5.00 bill
2. A $1.00 bill
"""

#Main Function
def main():
    reset_main_menu = True
    while reset_main_menu == True:
        print(menu_start)
        ticket_system = winning_ticket()
        number_tickets_purchased = number_tickets(options_numbers)
        list_tickets = tickets(number_tickets_purchased, options_tickets)
        successful_payment(number_tickets_purchased, second_menu, third_menu, fourth_menu, options_numbers)
        print("\n*************************  Successful Payment  *************************\n")
        print("\n*************************       Playing        *************************\n")
        lottery_play(list_tickets, ticket_system)
        print("\n************************************************************************\n")
        question_menu = check_answer("\nDo you want to return to the main menu? (y/n): ", options_yes_no)
        if question_menu in options_yes_no[0:3]:
            print("\nLet's start again..!!!!\n")
            reset_main_menu = True
        else:        
            message_custom("")
            reset_main_menu = False

#Entry point
if __name__ == "__main__":
    main()