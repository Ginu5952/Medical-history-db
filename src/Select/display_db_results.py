from utilities.os import clear_screen
from utilities.colors import *
from utilities.font_styles import *
from psycopg import OperationalError, IntegrityError
from src.Error_handling.error_handling import ErrorHandler
from prettytable import PrettyTable
from colorama import Fore, Style

class FamilyMedicalHistory:

    def __init__(self, pool):
        self.pool = pool

    @staticmethod
    def family_member_and_health_card_details(self):
      
        clear_screen()
        print(ORANGE + ITALIC + "\nSuccessfully Inserted All Data" + RESET)  
        print(BLUE + ITALIC + "\nFamily Member's health insurance card expiry date\n" + RESET)
        
        select_query = """
            SELECT family_member_details.*, family_health_insurance_card_details.expiry_date_of_card
            FROM family_member_details
            LEFT JOIN family_health_insurance_card_details ON family_member_details.health_insurance_card_no = family_health_insurance_card_details.health_insurance_card_no;
        """

        try:
            with self.pool.connection() as conn:
                with conn.cursor() as cursor:
                   
                    cursor.execute(select_query)
                    members = cursor.fetchall()

                    table = PrettyTable()
                    
                    table.field_names = [Fore.YELLOW + "Member ID" + Fore.RESET, Fore.YELLOW + "Name" + Fore.RESET, Fore.YELLOW + "Age" + Fore.RESET, Fore.YELLOW + "Relation" + Fore.RESET, Fore.YELLOW + "Expiry Date of Card" + Fore.RESET]

              
                    for member in members:
                        
                        formatted_row = [
                            f"{Fore.CYAN}{member[0]}{Fore.RESET}",  
                            f"{Fore.GREEN}{member[2]} {member[3]}{Fore.RESET}",  
                            f"{Fore.RED}{member[4]}{Fore.RESET}", 
                            f"{Fore.MAGENTA}{member[5]}{Fore.RESET}",  
                            f"{Fore.CYAN}{member[10]}{Fore.RESET}"  
                        ]
                        table.add_row(formatted_row)

                    table.align[Fore.YELLOW + "Member ID" + Fore.RESET] = "center"
                    table.align[Fore.YELLOW + "Age" + Fore.RESET] = "center"
                    table.align[Fore.YELLOW + "Relation" + Fore.RESET] = "left"
                    table.max_width[Fore.YELLOW + "Name" + Fore.RESET] = 30
                    table.padding_width = 2
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

    @staticmethod    
    def family_medical_visits(self):

        print(ORANGE + ITALIC + "\nFathers's Medical Visit Details\n" + RESET)  

        select_query = """
           SELECT
                family_member_details.first_name,
                family_member_details.last_name,
                hospital_details.hospital_name,
                family_medical_details.symptoms,
                family_medical_details.date_of_visit,
                family_medical_details.department,
                doctor_details.doctor_name
            FROM
                family_medical_details
                JOIN family_member_details ON family_medical_details.health_insurance_card_no = family_member_details.health_insurance_card_no
                JOIN doctor_details ON family_medical_details.doctor_id = doctor_details.doctor_id
                                    AND family_medical_details.hospital_id = doctor_details.hospital_id
                                    AND family_medical_details.department = doctor_details.department
                JOIN hospital_details ON family_medical_details.hospital_id = hospital_details.hospital_id
            WHERE
                family_medical_details.health_insurance_card_no = 'HIC123';
        """

        try:
            with self.pool.connection() as conn:
                with conn.cursor() as cursor:
                   
                    cursor.execute(select_query)
                    visits = cursor.fetchall()

                    table = PrettyTable()
                    
                    table.field_names = [
                    Fore.YELLOW + "Name" + Fore.RESET,
                    Fore.YELLOW + "Hospital Name" + Fore.RESET,
                    Fore.YELLOW + "Symptoms" + Fore.RESET,
                    Fore.YELLOW + "Date of Visit" + Fore.RESET,
                    Fore.YELLOW + "Department" + Fore.RESET,
                    Fore.YELLOW + "Doctor Name" + Fore.RESET
                ]

                    for visit in visits:
                        formatted_row = [
                            f"{Fore.CYAN}{visit[0]} {visit[1]}{Fore.RESET}",  
                            f"{Fore.GREEN}{visit[2]}{Fore.RESET}",  
                            f"{Fore.RED}{visit[3]}{Fore.RESET}",  
                            f"{Fore.MAGENTA}{visit[4]}{Fore.RESET}",  
                            f"{Fore.MAGENTA}{visit[5]}{Fore.RESET}",  
                            f"{Fore.CYAN}{visit[6]}{Fore.RESET}"  
                        ]
                        table.add_row(formatted_row)

                   
                    table.align[Fore.YELLOW + "Name" + Fore.RESET] = "left"
                    table.align[Fore.YELLOW + "Symptoms" + Fore.RESET] = "left"
                    table.align[Fore.YELLOW + "Date of Visit" + Fore.RESET] = "center"
                    table.align[Fore.YELLOW + "Department" + Fore.RESET] = "center"
                    table.align[Fore.YELLOW + "Doctor Name" + Fore.RESET] = "left"
                    table.padding_width = 2
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
        
    @staticmethod
    def family_yearly_check_up_details(self):

        print(ORANGE + ITALIC + "\nFamily Yearly Check-Up Details\n" + RESET)

        select_query = """
            SELECT
                family_member_details.first_name,
                family_member_details.last_name,
                family_member_details.age,
                family_yearly_check_up_details.yearly_check_up_done,
                family_yearly_check_up_details.date_of_check_up
            FROM
                family_member_details
            LEFT JOIN family_yearly_check_up_details 
            ON family_member_details.health_insurance_card_no = family_yearly_check_up_details.health_insurance_card_no;
        """

        try:
            with self.pool.connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(select_query)
                    checkups = cursor.fetchall()

                    table = PrettyTable()

                    table.field_names = [
                        Fore.YELLOW + "Name" + Fore.RESET,
                        Fore.YELLOW + "Age" + Fore.RESET,
                        Fore.YELLOW + "Yearly Check-Up Done" + Fore.RESET,
                        Fore.YELLOW + "Date of Check-Up" + Fore.RESET
                    ]

                    for checkup in checkups:
                        formatted_row = [
                            f"{Fore.CYAN}{checkup[0]} {checkup[1]}{Fore.RESET}",  
                            f"{Fore.GREEN}{checkup[2]}{Fore.RESET}",  
                            f"{Fore.RED}{checkup[3]}{Fore.RESET}",  
                            f"{Fore.MAGENTA}{checkup[4]}{Fore.RESET}"   
                        ]
                        table.add_row(formatted_row)

                    table.align[Fore.YELLOW + "Name" + Fore.RESET] = "center"
                    table.align[Fore.YELLOW + "Age" + Fore.RESET] = "center"
                    table.align[Fore.YELLOW + "Yearly Check-Up Done" + Fore.RESET] = "center"
                    table.align[Fore.YELLOW + "Date of Check-Up" + Fore.RESET] = "center"
                    table.padding_width = 2
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
        

    @staticmethod
    def children_check_up_details(self):

        print(ORANGE + ITALIC + "\nChildren's Check-Up Details\n" + RESET)

        select_query = """
            SELECT
                family_member_details.first_name,
                children_check_up_details.parents_name,
                children_check_up_details.number_of_children,
                children_check_up_details.children_name_and_age,
                children_check_up_details.vaccination_details,
                children_check_up_details.date_of_vaccination,
                children_check_up_details.vaccination_name
            FROM
                family_member_details
            INNER JOIN children_check_up_details 
            ON family_member_details.health_insurance_card_no = children_check_up_details.health_insurance_card_no;
        """

        try:
            with self.pool.connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(select_query)
                    checkups = cursor.fetchall()

                    table = PrettyTable()

                    table.field_names = [
                        Fore.YELLOW + "Father Name" + Fore.RESET,
                        Fore.YELLOW + "Mother Name" + Fore.RESET,
                        Fore.YELLOW + "Number of Children" + Fore.RESET,
                        Fore.YELLOW + "Children Details" + Fore.RESET,
                        Fore.YELLOW + "Vaccination Details" + Fore.RESET,
                        Fore.YELLOW + "Date of Vaccination" + Fore.RESET,
                        Fore.YELLOW + "Vaccination Name" + Fore.RESET
                    ]

                    for checkup in checkups:
                        formatted_row = [
                            f"{Fore.GREEN}{checkup[0]}{Fore.RESET}",  
                            f"{Fore.GREEN}{checkup[1]}{Fore.RESET}",  
                            f"{Fore.RED}{checkup[2]}{Fore.RESET}",  
                            f"{Fore.CYAN}{checkup[3]}{Fore.RESET}",  
                            f"{Fore.MAGENTA}{checkup[4]}{Fore.RESET}",  
                            f"{Fore.YELLOW}{checkup[5]}{Fore.RESET}",  
                            f"{Fore.CYAN}{checkup[6]}{Fore.RESET}"  
                        ]
                        table.add_row(formatted_row)

                    # Customize table appearance
                    table.align[Fore.YELLOW + "Father Name" + Fore.RESET] = "left"
                    table.align[Fore.YELLOW + "Mother Name" + Fore.RESET] = "left"
                    table.align[Fore.YELLOW + "Children Details" + Fore.RESET] = "left"
                    table.align[Fore.YELLOW + "Vaccination Details" + Fore.RESET] = "left"
                    table.align[Fore.YELLOW + "Date of Vaccination" + Fore.RESET] = "center"
                    table.align[Fore.YELLOW + "Vaccination Name" + Fore.RESET] = "left"

                    table.max_width[Fore.YELLOW + "Father Name" + Fore.RESET] = 15
                    table.max_width[Fore.YELLOW + "Mother Name" + Fore.RESET] = 20
                    table.max_width[Fore.YELLOW + "Number of Children" + Fore.RESET] = 5
                    table.max_width[Fore.YELLOW + "Children Details" + Fore.RESET] = 25
                    table.max_width[Fore.YELLOW + "Vaccination Details" + Fore.RESET] = 25
                    table.max_width[Fore.YELLOW + "Date of Vaccination" + Fore.RESET] = 25
                    table.max_width[Fore.YELLOW + "Vaccination Name" + Fore.RESET] = 20


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
        
                
    @staticmethod
    def total_sum_hospital_registration_fees(self):

        print(ORANGE + ITALIC + "\nHospital registration fees total" + RESET)

        select_query = """
        SELECT
            family_medical_details.visit_id,
            family_medical_details.hospital_id,
            family_member_details.first_name,
            hospital_details.hospital_name,
            hospital_details.registration_fees
        FROM 
            family_medical_details
            LEFT JOIN family_member_details ON family_medical_details.health_insurance_card_no = family_member_details.health_insurance_card_no
            LEFT JOIN hospital_details ON family_medical_details.hospital_id = hospital_details.hospital_id;
        """

        total_fees_query = """
                SELECT
                    SUM(hospital_details.registration_fees) AS total_registration_fees
                FROM 
                    family_medical_details
                    LEFT JOIN family_member_details ON family_medical_details.health_insurance_card_no = family_member_details.health_insurance_card_no
                    LEFT JOIN hospital_details ON family_medical_details.hospital_id = hospital_details.hospital_id;
            """  

        try:
            with self.pool.connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(select_query)
                    checkups = cursor.fetchall()

                    cursor.execute(total_fees_query)
                    total_fees = cursor.fetchone()[0]

                    table = PrettyTable()

                    table.field_names = [
                        Fore.YELLOW + "Visit ID" + Fore.RESET,
                        Fore.YELLOW + "Hospital ID" + Fore.RESET,
                        Fore.YELLOW + "First Name" + Fore.RESET,
                        Fore.YELLOW + "Hospital Name" + Fore.RESET,
                        Fore.YELLOW + "Registration Fees" + Fore.RESET,
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

                    
                    table.align[Fore.YELLOW + "Visit ID" + Fore.RESET] = "left"
                    table.align[Fore.YELLOW + "Hospital ID" + Fore.RESET] = "left"
                    table.align[Fore.YELLOW + "First Name" + Fore.RESET] = "left"
                    table.align[Fore.YELLOW + "Hospital Name" + Fore.RESET] = "left"
                    table.align[Fore.YELLOW + "Registration Fees" + Fore.RESET] = "center"

                    table.padding_width = 1
                    table.border = True
                    table.header = True
                    table.horizontal_char = f"{Fore.MAGENTA}-"
                    table.junction_char = f"{Fore.CYAN}+"

                    print(table)

                    # Print total registration fees
                    print(Fore.YELLOW + Style.BRIGHT + f"\nTotal Registration Fees: {Fore.GREEN}{total_fees}{Fore.RESET}\n" + Style.RESET_ALL)

                    return True
        except IntegrityError as e:
            return ErrorHandler.integrity_error(e)
        except OperationalError as e:
            return ErrorHandler.operational_error(e)
        except Exception as e:
            return ErrorHandler.exception_error(e)
        

        