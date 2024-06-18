
from utilities.colors import *
from utilities.font_styles import *
import sys
from enum import Enum


class ErrorType(Enum):

    HEALTH_INSURANCE_CARD_EXISTS = "Key (health_insurance_card_no)="
    CONTACT_NUMBER_EXISTS = "Key (contact_number)="
    FAILING_ROW = "Failing row contains"
    GENERAL_DETAIL = "DETAIL:"

class ErrorHandler:

    @staticmethod
    def operational_error(e):
        print(RED + BOLD + f"OperationalError occurred: {e}" + RESET)
        return False

    @staticmethod
    def integrity_error(e):
    
        error_message = str(e)

        if ErrorType.GENERAL_DETAIL.value in error_message:

            detail_message = error_message.split(ErrorType.GENERAL_DETAIL.value)[1].strip()

            if ErrorType.HEALTH_INSURANCE_CARD_EXISTS.value in detail_message:

                details = detail_message.split(ErrorType.HEALTH_INSURANCE_CARD_EXISTS.value)[1].split(")")[0].strip()
                print(RED + BOLD + f"\nFailed key details: {details} already exists" + RESET)
                print(ORANGE + ITALIC + "\nTry Again with a non-existing health insurance card!" + RESET)

            elif ErrorType.FAILING_ROW.value in detail_message:

                details = detail_message.split(ErrorType.FAILING_ROW.value)[1].strip("()")
                print(RED + BOLD + f"\nFailed row details: {details} already exists" + RESET)
                print(ORANGE + ITALIC + "\nTry Again with the correct format" + RESET)

            elif ErrorType.CONTACT_NUMBER_EXISTS.value in detail_message:

                details = detail_message.split(ErrorType.CONTACT_NUMBER_EXISTS.value)[1].split(")")[0].strip()
                print(RED + BOLD + f"\nContact number {details} already exists" + RESET)
                print(ORANGE + ITALIC + "\nTry Again with another contact number" + RESET)

            else:
                print(RED + BOLD + f"\n{detail_message}" + RESET)
                print(ORANGE + ITALIC + "\nTry Again with non-existing data" + RESET) 

        return False

    @staticmethod
    def exception_error(e):
        
        print(RED + BOLD + f"Unexpected error occurred: {e}" + RESET)
        return False

    @staticmethod
    def data_error(e):
        
        error_message = str(e)
        
        if "invalid input syntax for type boolean" in error_message:
            print(RED + BOLD + f"\nInvalid value for boolean field. Should be 'yes' or 'no'." + RESET)
        elif "invalid input syntax for type date" in error_message:
            print(RED + BOLD + f"\nInvalid date format. Should be YYYY-MM-DD format." + RESET)  
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