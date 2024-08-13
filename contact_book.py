#!/usr/bin/env python3
#Emma Ryan

#Contact Book

#instructions:
'''
Build a contact book with this data for each record: full name, birthday, address, phone. 

I can either enter a new record or I can search previous records. 

I have the ability to enter unlimited people with this data: full name, birthday, address, phone. 

I can search by each category: full name, birthday, address, phone. 

I can do this until I type “quit” that gets me out of the program, but the program gives me the option to quit by warning me that I am about to exit y/n.

'''

import sys #clean exit
#i know i couldve figured out how to do this with a giant array, but i wanted to keep organized and labeled so i like this better with just a bunch of separate lists
name = ["N/A"] #name list
birthday = ["N/A"] #birthday list
address = ["N/A"] #address list
phone = ["N/A"] #phone list


def start_menu(): #function for the "start menu" with 3 options always
    start_menu_options = input("MAKE A NEW RECORD(1), SEARCH PREVIOUS RECORDS(2), or QUIT PROGRAM(quit): ")

    if start_menu_options == "1":
        new_entry() #goes to new record function
        
    elif start_menu_options == "2":
        search() #goes to search function
        
    elif start_menu_options.lower() == "quit": #quitting
        while True:
            end_program = str(input("Are you sure you want to quit?(Y/N): "))
            end_program = end_program.upper()
            if end_program == "Y" or end_program == "YES":
                print("Goodbye!")
                sys.exit()
            elif end_program == "N" or end_program == "NO":
                break
            else:
                print("Not a valid input.")
                continue
        start_menu()
        
    else:
        print("Not a valid input.")
        start_menu()

            
#(1)
def new_entry():
    print("To Create a New Entry, Please Answer the Following:")
    
    new_name = input("   Enter FULL NAME(LAST, FIRST): ")
    new_name = new_name.upper() #makes it uppercase so search later isnt case sensitive
    name.append(new_name) #adds it to the end of related list
    
    new_birthday = input("   Enter BIRTHDAY(MM/DD/YYYY): ")
    new_birthday = new_birthday.upper() #repeat for the other categories
    birthday.append(new_birthday)
    
    new_address = input("   Enter ADDRESS(123 N MAIN ST, CITY, STATE): ")
    new_address = new_address.upper()
    address.append(new_address)
    
    new_phone = input("   Enter PHONE NUMBER(000-000-0000): ")
    new_phone = new_phone.upper()
    phone.append(new_phone)
    
    print("Entry Recorded")
    start_menu() #after entry is done, go back to menu


#(2)
def search():
    search_category = input("Search by FULL NAME(1), BIRTHDAY(2), ADDRESS(3), or PHONE NUMBER(4): ")
    
    try: #try block for incase the search isnt in list
        if search_category == "1":
            search_input = input("   Enter FULL NAME(LAST, FIRST) to search: ")
            search_input = search_input.upper() #not case sensitive
            search_number = name.count(search_input) #this makes a variable equal to the number of results in the list
            search_result = name.index(search_input) #this makes a variable equal to the location in the list of this search
            
        elif search_category == "2":
            search_input = input("   Enter BIRTHDAY(MM/DD/YYYY) to search: ")
            search_input = search_input.upper()
            search_number = birthday.count(search_input) 
            search_result = birthday.index(search_input)
            
        elif search_category == "3":
            search_input = input("   Enter ADDRESS(123 N MAIN ST, CITY, STATE) to search: ")
            search_input = search_input.upper()
            search_number = address.count(search_input)
            search_result = address.index(search_input)
            
        elif search_category == "4":
            search_input = input("   Enter PHONE NUMBER(000-000-0000) to search: ")
            search_input = search_input.upper()
            search_number = phone.count(search_input)
            search_result = phone.index(search_input)
            
        else:
            print("Not a valid input.")
            search()
    except ValueError: #this is the error i wouldve gotten if it wasnt in list, so this way, it will just print this and not crash
        print("No results found")
        start_menu() #if not in list, go back to menu
    else:
        print_results(search_number, search_result) #go to print_results function, with the count and index variables related



def print_results(search_number, search_result): 
    print(search_number,"Search Result(s) Found")
    
    if search_number == 0: #if search_number == 0, dont print any results, go straight to menu
        start_menu()
        
    elif search_number == 1: #print search results (if one result only)
        print("   FULL NAME:",name[search_result])
        print("   BIRTHDAY:",birthday[search_result])
        print("   ADDRESS:",address[search_result])
        print("   PHONE NUMBER:",phone[search_result])
        start_menu()
        
    else: #(in case there are multiple entries with same name (two emma ryans or something), it wont print any of them,
        #becuase i dont want to only print the first one found, incase thats not the one they are looking for, so they need to change up their search instead
        
        print("Try Searching by Different Category to Narrow Down Results.")
        search()

        
#beginning
print("-Welcome to the Contact Book-")
start_menu() #go to start_menu function
