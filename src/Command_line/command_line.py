
import argparse
from src.Insert.insert_tables import *
from src.helper.helper import confirm_data_entry_completed
import sys
from datetime import datetime
from src.Error_handling.error_handling import ErrorHandler
import json
from src.Select.display_hospital_details import *
from src.Select.display_db_results import *
from src.Select.display_hospital_address import *

operations = DataOperations()

class DataInserter:

    def __init__(self, pool):
        self.pool = pool

    # Health Insurance card
    def insert_data_into_health_card(self):

        parser = argparse.ArgumentParser(description='Insert a record into health_insurance_card_details.')
        parser.add_argument('--health_insurance_card_no', required=True, help='Health Insurance Card Number')
        parser.add_argument('--expiry_date_of_card', required=True, help='Expiry date of card')

        try:
            args = parser.parse_args()
        except argparse.ArgumentError as e: 
            ErrorHandler.argparse_argument_error(e,parser)   
        except argparse.ArgumentTypeError as e:
            ErrorHandler.argparse_argument_type_error(e,parser)
        except Exception as e:
            print(f"Unexpected error: {e}")
            sys.exit(1)          

        if not operations.insert_health_card(
            self.pool,
            args.health_insurance_card_no,
            args.expiry_date_of_card

        ):
            sys.exit()

        done_entry = input(PURPLE + BOLD + "\nCompleted your data entry? Type yes or no: " + RESET)
        confirm_data_entry_completed(done_entry,tablename = "Family member details")     


    # Family member details
    def insert_data_to_family_member_details(self):
        
        parser = argparse.ArgumentParser(description='Insert a record into family_member_details.')
        parser.add_argument('--health_insurance_card_no', required=True, help='Health Insurance Card Number')
        parser.add_argument('--first_name', required=True, help='First Name')
        parser.add_argument('--last_name', help='Last Name (optional)')
        parser.add_argument('--age', type=int, help='Age (optional)')
        parser.add_argument('--relation', help='Relation (optional)')
        parser.add_argument('--gender', choices=['M', 'F'], help='Gender (optional)')
        parser.add_argument('--marital_status', help='Marital Status (optional)')
        parser.add_argument('--profession', help='Profession (optional)')
        parser.add_argument('--contact_no', help='Contact Number (optional)'),
       
        try:
            args = parser.parse_args()
        except argparse.ArgumentError as e: 
            ErrorHandler.argparse_argument_error(e) 
        except SystemExit as e:
        
            if e.code != 0:
                print(RED + BOLD + "Argument parsing failed due to an error." + RESET)
                print(ORANGE + ITALIC + "\nPlease fill the required fields.\n" + RESET)
                
            raise      
        except argparse.ArgumentTypeError as e:
            ErrorHandler.argparse_argument_type_error(e)
        except Exception as e:
            print(f"Unexpected error: {e}")
            parser.print_help()
            sys.exit(1)    
        


        if not operations.insert_family_member(
            self.pool,
            args.health_insurance_card_no,
            args.first_name,
            args.last_name,
            args.age,
            args.relation,
            args.gender,
            args.marital_status,
            args.profession,
            args.contact_no
        ):
            sys.exit()  
       
        done_entry = input(PURPLE + BOLD + "\nCompleted your data entry? Type yes or no: " + RESET)
        confirm_data_entry_completed(done_entry,tablename = "Hospital details")     

    # Hospital Details
    def insert_data_into_hospital_details(self):

        parser = argparse.ArgumentParser(description='Insert a record into hospital_details.')
        parser.add_argument('--hospital_name', required=True, help='ID of hospital')
        parser.add_argument('--location',  help='Location of hospital (optional)')
        parser.add_argument('--address',  help='Address of hospital (optional)')
        parser.add_argument('--contact_number',help='Contact number of doctor (optional)')
        parser.add_argument('--website', help='Website of hospital (optional)')
        parser.add_argument('--registration_fees',help='Registration fee of hospital (optional)')
        
        try:
            args = parser.parse_args()   
        except argparse.ArgumentError as e: 
            ErrorHandler.argparse_argument_error(e,parser)  
        except SystemExit as e:
        
            if e.code != 0:
                print(RED + BOLD + "Argument parsing failed due to an error." + RESET)
                print(ORANGE + ITALIC + "\nPlease fill the required fields.\n" + RESET)
            raise        
        except argparse.ArgumentTypeError as e:
            ErrorHandler.argparse_argument_type_error(e,parser)
        except Exception as e:
            print(f"Unexpected error: {e}")
            sys.exit(1)      


        if not operations.insert_hospital_details(
            self.pool,
            args.hospital_name,
            args.location,
            args.address,
            args.contact_number,
            args.website,
            args.registration_fees

        ):
        
            sys.exit()     

        Display_hospital_id_and_hospital_name(self.pool) 
        done_entry = input(PURPLE + BOLD + "\nCompleted your data entry? Type yes or no: " + RESET).lower()
        confirm_data_entry_completed(done_entry,tablename = "Doctor details")  
       

    # Doctor Details
    def insert_data_into_doctor_details(self): 

        parser = argparse.ArgumentParser(description='Insert a record into consulted_doctor_details.')
        parser.add_argument('--hospital_id', type=int,required=True, help='ID of hospital')
        parser.add_argument('--department', required=True, help='Department of doctor')
        parser.add_argument('--doctor_name', required=True, help='Doctor name')
        parser.add_argument('--gender',help='Gender of doctor (optional)')
        parser.add_argument('--availability_days', nargs='+', help='Available days (optional),array')
        parser.add_argument('--consultation_hours', type=json.loads,help='Consultation hours (optional),JSON array')
        parser.add_argument('--contact_no', help='Contact number of doctor (optional)')

        try:
            args = parser.parse_args()   
        except argparse.ArgumentError as e: 
            ErrorHandler.argparse_argument_error(e,parser)  
        except SystemExit as e:
        
            if e.code != 0:
                print(RED + BOLD + "Argument parsing failed due to an error." + RESET)
                print(ORANGE + ITALIC + "\nPlease refer to the usage instructions below and ensure you enter the fields correctly.\n" + RESET)
                parser.print_help()
            raise        
        except argparse.ArgumentTypeError as e:
            ErrorHandler.argparse_argument_type_error(e,parser)
        except Exception as e:
            print(f"Unexpected error: {e}")
            sys.exit(1)      


        if not operations.insert_doctor_details(
            self.pool,
            args.hospital_id,
            args.department,
            args.doctor_name,
            args.gender,
            args.availability_days,
            args.consultation_hours,
            args.contact_no

        ):
        
            sys.exit()     
        Display_doctor_hospital_id(self.pool)
        done_entry = input(PURPLE + BOLD + "\nCompleted your data entry? Type yes or no: " + RESET).lower()
        confirm_data_entry_completed(done_entry,tablename = "Yearly check up details")   


    # Family medical history
    def insert_data_into_family_medical_details(self):


        parser = argparse.ArgumentParser(description='Insert a record into family_medical_details.')
        parser.add_argument('--health_insurance_card_no', required=True, help='Health Insurance Card Number')
        parser.add_argument('--doctor_id',type=int, required=True,help='ID of doctor')
        parser.add_argument('--hospital_id',type=int,required=True,help='ID of hospital')
        parser.add_argument('--department',help='Department of consult (optional)')
        parser.add_argument('--date_of_visit', required=True, help='Date of visit (format: YYYY-MM-DD HH:MM)')
        parser.add_argument('--symptoms', nargs='+', help='Symptoms (optional), array')
        parser.add_argument('--diagnosis', nargs='+', help='Diagnosis (optional), array')
        parser.add_argument('--medication', nargs='+', help='Medication (optional), array')

        try:
            args = parser.parse_args()
        except argparse.ArgumentError as e: 
            ErrorHandler.argparse_argument_error(e,parser) 
        except SystemExit as e:
        
            if e.code != 0:
                print(RED + BOLD + "Argument parsing failed due to an error." + RESET)
                print(ORANGE + ITALIC + "\nPlease fill the required fields.\n" + RESET)
            raise         
        except argparse.ArgumentTypeError as e:
            ErrorHandler.argparse_argument_type_error(e,parser)
        except Exception as e:
            print(f"Unexpected error: {e}")
            sys.exit(1)      

        
        try:
            date_of_visit = datetime.strptime(args.date_of_visit, '%Y-%m-%d %H:%M')
        except ValueError:
            print("Error: Incorrect date format. Should be 'YYYY-MM-DD HH:MM'")
            print(LIGHT_BLUE + ITALIC + "\n Try again with correct format." + RESET)
            sys.exit()
        

        if not operations.insert_medical_details(
            self.pool,
            args.health_insurance_card_no,
            args.doctor_id,
            args.hospital_id,
            args.department,
            date_of_visit,
            args.symptoms,
            args.diagnosis,
            args.medication

        ):
        
            sys.exit() 

        done_entry = input(PURPLE + BOLD + "\nCompleted your data entry? Type yes or no: " + RESET).lower()

        if done_entry == 'yes':
             
            FamilyMedicalHistory.family_member_and_health_card_details(self)
            FamilyMedicalHistory.family_medical_visits(self)
            FamilyMedicalHistory.family_yearly_check_up_details(self)
            FamilyMedicalHistory.children_check_up_details(self)
            FamilyMedicalHistory.total_sum_hospital_registration_fees(self)
            HospitalDetails.hospital_address(self)
        else:
            print(GREEN + ITALIC + '\nKindly continue entering your data....\n' + RESET)     
    
 

    # Yearly check up details
    def insert_data_into_yearly_check_details(self) :
        
        parser = argparse.ArgumentParser(description='Insert a record into family_yearly_checkup_details.')
        parser.add_argument('--health_insurance_card_no', required=True, help='Health Insurance Card Number')
        parser.add_argument('--yearly_check_up_done', help='Yerly check up done (optional)')
        parser.add_argument('--date_of_check_up', help='Date of check up (optional) (format: YYYY-MM-DD')

       

        try:
            args = parser.parse_args()   
        except argparse.ArgumentError as e: 
            ErrorHandler.argparse_argument_error(e,parser)   
        except SystemExit as e:
        
            if e.code != 0:
                print(RED + BOLD + "Argument parsing failed due to an error." + RESET)
                print(ORANGE + ITALIC + "\nPlease fill the required fields.\n" + RESET)
            raise       
        except argparse.ArgumentTypeError as e:
            ErrorHandler.argparse_argument_type_error(e,parser)
        except Exception as e:
            print(f"Unexpected error: {e}")
            sys.exit(1)   
   

        if not operations.insert_yearly_check_details(
            self.pool,
            args.health_insurance_card_no,
            args.yearly_check_up_done,
            args.date_of_check_up
        ):
        
            sys.exit()     
    
        done_entry = input(PURPLE + BOLD + "\nCompleted your data entry? Type yes or no: " + RESET)
        confirm_data_entry_completed(done_entry,tablename = "Children checkup details")   


    # Children check up details
    def insert_data_into_children_check_up_details(self):

        parser = argparse.ArgumentParser(description='Insert a record into children_checkup_details.')
        parser.add_argument('--health_insurance_card_no', required=True, help='Health Insurance Card Number')
        parser.add_argument('--parents_name', required=True, help='Name of parent (optional)')
        parser.add_argument('--number_of_children',type=int, help='Number of children (optional)')
        parser.add_argument('--children_name_and_age', type=json.loads, help='Name and age of children (optional),JSON array')
        parser.add_argument('--vaccination_details', type=json.loads, help='Vaccination completed (optional),JSON array')
        parser.add_argument('--date_of_vaccination',type=json.loads, help='Date of vaccination (optional),JSON array')
        parser.add_argument('--vaccination_name', nargs='+', help='Vaccination name (optional),array')
       
        try:
            args = parser.parse_args()   
        except argparse.ArgumentError as e: 
            ErrorHandler.argparse_argument_error(e,parser)
        except SystemExit as e:
        
            if e.code != 0:
                print(RED + BOLD + "Argument parsing failed due to an error." + RESET)
                print(ORANGE + ITALIC + "\nPlease fill the required fields.\n" + RESET)
                parser.print_help()
            raise          
        except argparse.ArgumentTypeError as e:
            ErrorHandler.argparse_argument_type_error(e,parser)
        except Exception as e:
            print(f"Unexpected error: {e}")
            sys.exit(1)      

        #date_of_vaccination = args.date_of_vaccination if args.date_of_vaccination else None

       # if args.date_of_vaccination:
          #  try:
              #  for vaccination_date in date_of_vaccination:
                 #   date_vaccination_str = vaccination_date.get("date", "")
                  #  if date_vaccination_str:
                  #      date_vaccination_obj = datetime.strptime(date_vaccination_str, "%Y-%m-%d").date()
                   #     if date_vaccination_obj > date.today():
                  #          print("\033[91m\033[3m\nDate of vaccination cannot be in the future.\033[0m")
                   #         return False
                  #  else:
                  #      print("\033[91m\033[3m\nInvalid date format for date_of_vaccination.\033[0m")
                  #      return False
           # except json.JSONDecodeError:
              #  print("\nInvalid JSON format for date_of_vaccination.")
              #  return False

        if not operations.insert_children_checkup_details(
            self.pool,
            args.health_insurance_card_no,
            args.parents_name,
            args.number_of_children,
            args.children_name_and_age,
            args.vaccination_details,
            args.date_of_vaccination,
            args.vaccination_name
        ):
        
            sys.exit()  

        
        done_entry = input(PURPLE + BOLD + "\nCompleted your data entry? Type yes or no: " + RESET).lower()
        confirm_data_entry_completed(done_entry,tablename = "Family medical details")   

       
   


