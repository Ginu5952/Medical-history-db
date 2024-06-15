from psycopg import OperationalError, IntegrityError,DataError
from utilities.colors import *
from utilities.font_styles import *
import json

from src.Error_handling.error_handling import ErrorHandler

class DataOperations:

    @staticmethod
    def insert_health_card(pool, health_insurance_card_no, expiry_date_of_card):

        query = """
                INSERT INTO family_health_insurance_card_details(health_insurance_card_no, expiry_date_of_card)
                VALUES(%s, %s)

        """

        try:
            
            with pool.connection() as conn:
                with conn.cursor() as cursor:   

                    print(GREEN + ITALIC + "\nInserting data..." + RESET)
                    cursor.execute(query, (health_insurance_card_no, expiry_date_of_card))
                    conn.commit() 
                    print(GREEN + ITALIC + f"\nHealth insurance card {health_insurance_card_no} details added successfully...." + RESET)    
                    return True   
        except IntegrityError as e:
            print(RED + ITALIC + "\nFailed to insert data!" + RESET)
            return ErrorHandler.integrity_error(e)
        except OperationalError as e:
            return ErrorHandler.operational_error(e)
        except DataError as e:
            print(RED + ITALIC + "\nFailed to insert data!" + RESET)
            return ErrorHandler.data_error(e)
        except Exception as e:
            return ErrorHandler.exception_error(e)


    @staticmethod
    def insert_family_member(pool,health_insurance_card_no, first_name, last_name, age, relation, gender, marital_status, profession, contact_no) -> bool:
        
        check_query = """
            SELECT COUNT(*)
            FROM family_member_details
            WHERE health_insurance_card_no = %s
        """
        
        query = """
                INSERT INTO family_member_details(health_insurance_card_no, first_name, last_name, age, relation, gender, marital_status, profession, contact_no)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)

        """

        try:
            
            with pool.connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(check_query, (health_insurance_card_no,))
                    count = cursor.fetchone()[0]

                    if count > 0:
                        print(RED + "\nData already exists for health insurance card number:", health_insurance_card_no + RESET)    
                        return False   
                    
                    
                    print(GREEN + ITALIC + "\nInserting data..." + RESET)
                    cursor.execute(query, (health_insurance_card_no, first_name, last_name, age, relation, gender, marital_status, profession, contact_no))
                    conn.commit() 
                    print(GREEN + ITALIC + f"\nFamily member {first_name} {last_name} added successfully..." + RESET)    
                    return True
        except IntegrityError as e:
            print(RED + ITALIC + "\nFailed to insert data!" + RESET)
            return ErrorHandler.integrity_error(e)  
        except OperationalError as e: 
            return ErrorHandler.operational_error(e)
        except Exception as e:
        
            return ErrorHandler.exception_error(e)
        
    
    @staticmethod
    def insert_doctor_details(pool,hospital_id,department,doctor_name, gender, availability_days, consultation_hours, contact_no):

        query = """
                INSERT INTO doctor_details(hospital_id,department,doctor_name,gender, availability_days, consultation_hours, contact_no)
                VALUES(%s, %s, %s, %s, %s, %s::jsonb, %s)

        """

        try:
            
            with pool.connection() as conn:
                with conn.cursor() as cursor:   

                    print(GREEN + ITALIC + "\nInserting data..." + RESET)
                    cursor.execute(query, (hospital_id,department,doctor_name, gender, availability_days, json.dumps(consultation_hours), contact_no))
                    conn.commit() 
                    print(GREEN + ITALIC + f"\nDoctor {doctor_name} details added successfully...." + RESET)    
                    return True   
        except IntegrityError as e:
            print(RED + ITALIC + "\nFailed to insert data!" + RESET)
            return ErrorHandler.integrity_error(e)
        except OperationalError as e:
            return ErrorHandler.operational_error(e)
        except DataError as e:
            print(RED + ITALIC + "\nFailed to insert data!" + RESET)
            return ErrorHandler.data_error(e)
        except Exception as e:
            return ErrorHandler.exception_error(e)
        
    @staticmethod
    def insert_hospital_details(pool,hospital_name, location, address, contact_number, website,registration_fees):

        query = """
                INSERT INTO hospital_details(hospital_name, location, address, contact_number, website, registration_fees)
                VALUES(%s, %s, %s, %s, %s, %s)

        """

        try:
            
            with pool.connection() as conn:
                with conn.cursor() as cursor:   

                    print(GREEN + ITALIC + "\nInserting data..." + RESET)
                    cursor.execute(query, (hospital_name,location, address, contact_number, website, registration_fees))
                    conn.commit() 
                    print(GREEN + ITALIC + f"\n{hospital_name} details added successfully...." + RESET)    
                    return True   
        except IntegrityError as e:
            print(RED + ITALIC + "\nFailed to insert data!" + RESET)
            return ErrorHandler.integrity_error(e)
        except OperationalError as e:
    
            return ErrorHandler.operational_error(e)
        except Exception as e:
        
            return ErrorHandler.exception_error(e)

        
        
    @staticmethod
    def insert_yearly_check_details(pool,health_insurance_card_no, yearly_check_up_done, date_of_check_up):

        query = """
                INSERT INTO family_yearly_check_up_details(health_insurance_card_no, yearly_check_up_done, date_of_check_up)
                VALUES(%s, %s, %s)

        """

        try:
            
            with pool.connection() as conn:
                with conn.cursor() as cursor:   

                    print(GREEN + ITALIC + "\nInserting data..." + RESET)
                    cursor.execute(query, (health_insurance_card_no, yearly_check_up_done, date_of_check_up))
                    conn.commit() 
                    print(GREEN + ITALIC + f"\nYearly check up details of card number {health_insurance_card_no} added successfully...." + RESET)    
                    return True   
        except IntegrityError as e:
            print(RED + ITALIC + "\nFailed to insert data!" + RESET)
            return ErrorHandler.integrity_error(e)
        except OperationalError as e:
            return ErrorHandler.operational_error(e)
        except DataError as e:
            print(RED + ITALIC + "\nFailed to insert data!" + RESET)
            return ErrorHandler.data_error(e)
        except Exception as e:
            return ErrorHandler.exception_error(e)

    @staticmethod    
    def insert_children_checkup_details(pool,health_insurance_card_no, parents_name, number_of_children, children_name_and_age, vaccination_details, date_of_vaccination, vaccination_name):
       
        query = """
                INSERT INTO children_check_up_details(health_insurance_card_no, parents_name, number_of_children, children_name_and_age, vaccination_details, date_of_vaccination, vaccination_name)
                VALUES(%s, %s, %s, %s::jsonb, %s::jsonb, %s::jsonb, %s)

        """

        try:
            
            with pool.connection() as conn:
                with conn.cursor() as cursor:   

                    print(GREEN + ITALIC + "\nInserting data..." + RESET)
                    cursor.execute(query, (
                    health_insurance_card_no,
                    parents_name,
                    number_of_children,
                    json.dumps(children_name_and_age),  
                    json.dumps(vaccination_details),  
                    json.dumps(date_of_vaccination),  # Convert to JSON string
                    vaccination_name
                ))
                    conn.commit() 
                    print(GREEN + ITALIC + "\nChildren check up details added successfully...." + RESET)    
                    return True   
        except IntegrityError as e:
            print(RED + ITALIC + "\nFailed to insert data!" + RESET)
            return ErrorHandler.integrity_error(e)
        except OperationalError as e:
            return ErrorHandler.operational_error(e)
        except DataError as e:
            print(RED + ITALIC + "\nFailed to insert data!" + RESET)
            return ErrorHandler.data_error(e)
        except Exception as e:
            return ErrorHandler.exception_error(e)   
        

   
    @staticmethod
    def insert_medical_details(pool,health_insurance_card_no, doctor_id=None, hospital_id=None,department=None, date_of_visit =None, symptoms=None, diagnosis=None, medication=None) -> bool:
        


        query = """
                INSERT INTO family_medical_details(health_insurance_card_no, doctor_id, hospital_id, department, date_of_visit, symptoms, diagnosis, medication)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s)

        """

        try:
            
            with pool.connection() as conn:
                with conn.cursor() as cursor:   

                    print(GREEN + ITALIC + "\nInserting data..." + RESET)
                    cursor.execute(query, (health_insurance_card_no,doctor_id, hospital_id, department, date_of_visit, symptoms, diagnosis, medication))
                    conn.commit() 
                    print(GREEN + ITALIC + f"\nMedical details of card no {health_insurance_card_no} added successfully...." + RESET)    
                    return True   
        except IntegrityError as e:
            print(RED + ITALIC + "\nFailed to insert data!" + RESET)
            return ErrorHandler.integrity_error(e)
        except OperationalError as e:
    
            return ErrorHandler.operational_error(e)
        except Exception as e:
        
            return ErrorHandler.exception_error(e)

   
