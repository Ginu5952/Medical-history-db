
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
           
            if "Key (health_insurance_card_no)=" in detail_message:   
                details = error_message.split("Key (health_insurance_card_no)=")[1].split(")")[0]
                print(RED + BOLD + f"\nFailed key details: {details}" + RESET)
                print(ORANGE + ITALIC + "\n Try Again with non existing health insurance card!" + RESET)
            elif "Failing row contains" in detail_message:
                details = error_message.split("Failing row contains ")[1].strip("()")
                print(RED + BOLD + f"\nFailed row details: {details}" + RESET)   
                print(ORANGE + ITALIC + "\nTry Again with correct format" + RESET) 
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
        elif "invalid input value for enum" in error_message:
            print(RED + BOLD + "\nInvalid marital status choose 'Single', 'Married', 'Divorced', 'Widowed', 'Separated', 'Committed', 'Other'." + RESET)  
        else:
            print(RED + BOLD + f"DataError occurred: {e}" + RESET)
        return False
    
    @staticmethod
    def argparse_argument_error(e):

        print(RED + BOLD + f"Argument error: {e}" + RESET)
        if '--first_name' in str(e):
            print("Error: Missing required argument --first_name")
        elif '--health_insurance_card_no' in str(e):
            print("Error: Missing required argument --health_insurance_card_no")     
        else:
            print(ORANGE + f"ArgumentError: {e}" + RESET)
        sys.exit(1)

    @staticmethod
    def argparse_argument_type_error(e,parser):
        print(RED + BOLD + f"Argument type error: {e}" + RESET)
        if '--first_name' in str(e):
            print("Error: Missing required argument --first_name")
        elif '--health_insurance_card_no' in str(e):
            print("Error: Missing required argument --health_insurance_card_no")     
        else:
            print(f"ArgumentError: {e}")
        sys.exit(1)    