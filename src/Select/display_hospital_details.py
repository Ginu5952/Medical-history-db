from src.Error_handling.error_handling import ErrorHandler
from psycopg import OperationalError, IntegrityError
from utilities.colors import *
from utilities.font_styles import *

def Display_hospital_id_and_hospital_name(pool): 

        select_query = """
            SELECT hospital_id, hospital_name FROM hospital_details
        """

        try:
            with pool.connection() as conn:
                with conn.cursor() as cursor:
                   
                    cursor.execute(select_query)
                    hospitals = cursor.fetchall()

                    print(YELLOW + ITALIC + "\n Please find ID's of Hospital from here\n" + RESET)
                    for hospital in hospitals:
                        print(ORANGE + ITALIC + f"ID: {hospital[0]} : {hospital[1]}" + RESET)
                    
                    return True
        except IntegrityError as e:
            return ErrorHandler.integrity_error(e)
        except OperationalError as e:
            return ErrorHandler.operational_error(e)
        except Exception as e:
            return ErrorHandler.exception_error(e)
        

def Display_doctor_hospital_id(pool):
     
        select_query = """
            SELECT doctor_details.doctor_id, doctor_details.hospital_id, doctor_details.department, doctor_details.doctor_name,hospital_details.hospital_name 
            FROM doctor_details
            LEFT JOIN hospital_details ON doctor_details.hospital_id = hospital_details.hospital_id
        """

        try:
            with pool.connection() as conn:
                with conn.cursor() as cursor:
                   
                    cursor.execute(select_query)
                    doctor = cursor.fetchall()

                    print(YELLOW + ITALIC + "\n Please find ID's of Doctor from here\n" + RESET)
                    for item in doctor:
                        print(ORANGE + ITALIC + f"Doctor id: {item[0]}  Hospital id : {item[1]} Department: {item[2]} Doctor name: {item[3]} Hospital name: {item[4]}" + RESET)
                    
                    return True
        except IntegrityError as e:
            return ErrorHandler.integrity_error(e)
        except OperationalError as e:
            return ErrorHandler.operational_error(e)
        except Exception as e:
            return ErrorHandler.exception_error(e)
        
             