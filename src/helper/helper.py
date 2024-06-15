
from src.Command_line.command_line import *
from utilities.colors import *
from utilities.font_styles import *

import sys


def confirm_data_entry_completed(finished,tablename):

   
    if finished == 'yes':
        print('\n')
        print(ORANGE + ITALIC + f"Run the command to insert {tablename} (Copy from README.md)\n" + RESET)
        sys.exit()
    elif finished == 'no':
        print(GREEN + ITALIC + '\nKindly continue entering your data....\n' + RESET)    
    else:
        print(ORANGE + ITALIC + "\nInvalid comment Type yes or no" + RESET)
        print(ORANGE + ITALIC + "Try again!" + RESET) 
       


