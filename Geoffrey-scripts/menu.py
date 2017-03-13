# IMPORTS
#---------------------------------------------------------------------------
import sys
import os.path
from data_handler import *
import pandas as pd

# PREAMBLE
#---------------------------------------------------------------------------
options = ['1', '2','3', '4']

# MENU FUNCTIONS
#---------------------------------------------------------------------------
# def import_raw():
#
#
# def import_processed():

def menu_choice():

    # Menu options printed to screen
    print("GROUP B7 DATA PROCESSING & ANALYSIS SOFTWARE\n")
    print(45*'-')
    print(15*' '+"MAIN MENU")
    print(45*'-'+'\n')
    print("(1) Import data '.csv' & '.tsa.csv'")
    print("(2) Plot data'")
    print("(3) Create animation")
    print("(4) Perform statistical analysis\n")

    while True:

        choice = input('What would you like to do?: ')
        if choice in options:
            break

        elif choice not in options:
            raise ValueError("Choice is not recognised! Try again.")

    return choice

def menu(menu_choice):
        if menu_choice == '1':
            global df
            filename = file_name_query()
            df = DataFrame(filename)
        elif menu_choice == '2':
            pass
        elif menu_choice == '3':
            pass
        elif menu_choice == '4':
            pass

def file_name_query():
    file = input('Filename of datafile: ')

    if file[-4:] == '.csv':
        file = file

    elif file[-4:] != '.csv':
        file = (file + '.csv')

    return file

while True:
    menu(menu_choice())
    print(df.df)



#
#---------------------------------------------------------------------------


