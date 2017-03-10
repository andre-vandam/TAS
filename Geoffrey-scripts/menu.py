# IMPORTS
#---------------------------------------------------------------------------
import sys
import os.path
import data_handler as dh
import pandas as pd

# PREAMBLE
#---------------------------------------------------------------------------
options = ['1', '2']

# MENU FUNCTIONS
#---------------------------------------------------------------------------
# def import_raw():
#
#
# def import_processed():

def menu_choice():

    print("GROUP B7 DATA PROCESSING & ANALYSIS SOFTWARE\n")
    print(45*'-')
    print(15*' '+"MAIN MENU")
    print(45*'-'+'\n')
    print("(1) Import & process raw data '.csv'")
    print("(2) Load processed data '.tsa.csv'\n")

    while True:

        choice = input('What would you like to do?: ')

        if choice in options:
            break

        elif choice not in options:
            raise ValueError("Choice is not recognised! Try again.")

    return choice

def menu(choice):
        menu(choice)

while True:
    menu(menu_choice())


#
#---------------------------------------------------------------------------


