
from utilities.colors import *
from utilities.font_styles import *
import sys


class ErrorHandler:

    @staticmethod
    def operational_error(e):
        print(RED + BOLD + f"OperationalError occurred: {e}" + RESET)
        return False

    @staticmethod
    def integrity_error(e):
    
        error_message = str(e)
        if "DETAIL:" in error_message:
            detail_message = error_message.split("DETAIL: ")[1].strip()
            print('\n')
            print(RED + BOLD + f"{detail_message}" + RESET)
        return False

    @staticmethod
    def exception_error(e):
        
        print(RED + BOLD + f"Unexpected error occurred: {e}" + RESET)
        return False

    @staticmethod
    def data_error(e):
        
        error_message = str(e)
        
        if "invalid input syntax for type boolean" in error_message:
            print(RED + BOLD + "\nInvalid value for boolean field. Should be 'yes' or 'no'." + RESET)
        elif "invalid input syntax for type date" in error_message:
            print(RED + BOLD + "\nInvalid date format. Should be YYYY-MM-DD format." + RESET)   
        else:
            print(RED + BOLD + f"DataError occurred: {e}" + RESET)
        return False
    
    @staticmethod
    def argparse_argument_error(e,parser):

        print(RED + BOLD + f"Argument error: {e}" + RESET)
        print(ORANGE + ITALIC + "\nPlease refer to the usage instructions below and ensure you enter the fields correctly.\n" + RESET)
        parser.print_help()
        sys.exit(1)

    @staticmethod
    def argparse_argument_type_error(e,parser):
        print(RED + BOLD + f"Argument type error: {e}" + RESET)
        print(ORANGE + ITALIC + "\nPlease refer to the usage instructions below and ensure you enter the fields correctly.\n" + RESET)
        parser.print_help()
        sys.exit(1)    