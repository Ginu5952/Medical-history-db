
from utilities.colors import *
from utilities.font_styles import *
from psycopg import OperationalError, IntegrityError
from src.Error_handling.error_handling import ErrorHandler
from prettytable import PrettyTable
from colorama import Fore, Style

class HospitalDetails:

    def __init__(self, pool):
        self.pool = pool

    @staticmethod
    def hospital_address(self):

       
        print(BLUE + ITALIC + "\nHospital Address And Contact Details\n" + RESET)
        
        select_query = """
            SELECT
                family_medical_details.visit_id,
                family_medical_details.hospital_id,
                family_member_details.first_name,
                hospital_details.hospital_name,
                hospital_details.address,
                hospital_details.contact_number
            FROM 
                family_medical_details
                LEFT JOIN family_member_details ON family_medical_details.health_insurance_card_no = family_member_details.health_insurance_card_no
                LEFT JOIN hospital_details ON family_medical_details.hospital_id = hospital_details.hospital_id
        """

        try:
            with self.pool.connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(select_query)
                    members = cursor.fetchall()

                    table = PrettyTable()

                    table.field_names = [
                        Fore.YELLOW + "Visit ID" + Fore.RESET,
                        Fore.YELLOW + "Hospital ID" + Fore.RESET,
                        Fore.YELLOW + "First Name" + Fore.RESET,
                        Fore.YELLOW + "Hospital Name" + Fore.RESET,
                        Fore.YELLOW + "Address" + Fore.RESET,
                        Fore.YELLOW + "Contact Number" + Fore.RESET
                    ]

                    for member in members:
                        formatted_row = [
                            f"{Fore.GREEN}{member[0]}{Fore.RESET}",  
                            f"{Fore.GREEN}{member[1]}{Fore.RESET}",  
                            f"{Fore.RED}{member[2]}{Fore.RESET}",  
                            f"{Fore.CYAN}{member[3]}{Fore.RESET}",  
                            f"{Fore.MAGENTA}{member[4]}{Fore.RESET}", 
                            f"{Fore.BLUE}{member[5]}{Fore.RESET}"  
                        ]
                        table.add_row(formatted_row)

                  
                    table.align[Fore.YELLOW + "Visit ID" + Fore.RESET] = "left"
                    table.align[Fore.YELLOW + "Hospital ID" + Fore.RESET] = "left"
                    table.align[Fore.YELLOW + "First Name" + Fore.RESET] = "left"
                    table.align[Fore.YELLOW + "Hospital Name" + Fore.RESET] = "left"
                    table.align[Fore.YELLOW + "Address" + Fore.RESET] = "left"
                    table.align[Fore.YELLOW + "Contact Number" + Fore.RESET] = "left"

                    table.padding_width = 1
                    table.border = True
                    table.header = True
                    table.horizontal_char = f"{Fore.MAGENTA}-"
                    table.junction_char = f"{Fore.CYAN}+"

                    print(table)

                    return True

        except IntegrityError as e:
            return ErrorHandler.integrity_error(e)
        except OperationalError as e:
            return ErrorHandler.operational_error(e)
        except Exception as e:
            return ErrorHandler.exception_error(e)
        
    @staticmethod
    def doctor_consultation_day_time_details(self):

        print(BLUE + ITALIC + "\n Doctor's consultation days and time\n" + RESET)

        select_query = """
            SELECT
                doctor_details.doctor_name,
                doctor_details.availability_days,
                doctor_details.consultation_hours,
                doctor_details.contact_no,
                hospital_details.hospital_name     
            FROM 
                doctor_details
                RIGHT JOIN hospital_details ON doctor_details.hospital_id = hospital_details.hospital_id;
              
        """

        try:
            with self.pool.connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(select_query)
                    checkups = cursor.fetchall()

                    table = PrettyTable()

                    table.field_names = [
                        Fore.YELLOW + "Doctor Name" + Fore.RESET,
                        Fore.YELLOW + "Consultation Days" + Fore.RESET,
                        Fore.YELLOW + "Consultation Time" + Fore.RESET,
                        Fore.YELLOW + "Contact Number" + Fore.RESET,
                        Fore.YELLOW + "Hospital Name" + Fore.RESET,
                    ]

                    for checkup in checkups:
                        formatted_row = [
                            f"{Fore.GREEN}{checkup[0]}{Fore.RESET}",  
                            f"{Fore.GREEN}{checkup[1]}{Fore.RESET}",  
                            f"{Fore.RED}{checkup[2]}{Fore.RESET}",  
                            f"{Fore.CYAN}{checkup[3]}{Fore.RESET}",  
                            f"{Fore.MAGENTA}{checkup[4]}{Fore.RESET}",  
                          
                        ]
                        table.add_row(formatted_row)

                    # Customize table appearance
                    table.align[Fore.YELLOW + "Doctor Name" + Fore.RESET] = "left"
                    table.align[Fore.YELLOW + "Consultation Days" + Fore.RESET] = "left"
                    table.align[Fore.YELLOW + "Consultation Time" + Fore.RESET] = "left"
                    table.align[Fore.YELLOW + "Contact Number" + Fore.RESET] = "left"
                    table.align[Fore.YELLOW + "Hospital Name" + Fore.RESET] = "left"

                    table.max_width[Fore.YELLOW + "Doctor Name" + Fore.RESET] = 15
                    table.max_width[Fore.YELLOW + "Consultation Days" + Fore.RESET] = 25
                    table.max_width[Fore.YELLOW + "Consultation Time" + Fore.RESET] = 25
                    table.max_width[Fore.YELLOW + "Contact Number" + Fore.RESET] = 25
                    table.max_width[Fore.YELLOW + "Hospital Name" + Fore.RESET] = 25


                    table.padding_width = 1
                    table.border = True
                    table.header = True
                    table.horizontal_char = f"{Fore.MAGENTA}-"
                    table.junction_char = f"{Fore.CYAN}+"

                    print(table)

                  
        except IntegrityError as e:
            return ErrorHandler.integrity_error(e)
        except OperationalError as e:
            return ErrorHandler.operational_error(e)
        except Exception as e:
            return ErrorHandler.exception_error(e)



