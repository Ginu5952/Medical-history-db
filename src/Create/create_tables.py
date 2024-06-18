from psycopg import OperationalError
from src.Error_handling.error_handling import ErrorHandler
from utilities.colors import *
from utilities.font_styles import *


# Create type    

def create_type(pool):

    # Query to check if the type exists
    check_query = """
        SELECT EXISTS (
            SELECT 1 
            FROM pg_type 
            WHERE typname = 'family_member_marital_status'
        );
    """
    
    # Query to create the type if it does not exist
    create_query = """
        CREATE TYPE family_member_marital_status AS ENUM (
            'Single', 'Married', 'Divorced', 'Widowed', 'Separated', 'Committed', 'Other'
        );
    """
    
    try:
        with pool.connection() as conn:
            with conn.cursor() as cursor:
                # Check if the type exists
                cursor.execute(check_query)
                exists = cursor.fetchone()[0]
                
                if not exists:
                    # Create the type if it does not exist
                    cursor.execute(create_query)
                    conn.commit()
                    print(ORANGE + ITALIC + "\nEnum type created successfully" + RESET)
               
    except OperationalError as e:
        return ErrorHandler.operational_error(e)
    except Exception as e:
       return ErrorHandler.exception_error(e)

          

# Create tables

def create_tables(pool) -> bool:

    # queries
    queries = {
        "family_health_insurance_card_details": """
            CREATE TABLE IF NOT EXISTS family_health_insurance_card_details(
                health_insurance_card_no VARCHAR(50) PRIMARY KEY,
                expiry_date_of_card DATE,

                CHECK (expiry_date_of_card > CURRENT_DATE)
            );
        """,
        "hospital_details": """
            CREATE TABLE IF NOT EXISTS hospital_details(
                hospital_id SERIAL PRIMARY KEY,
                hospital_name VARCHAR(50) NOT NULL,
                location VARCHAR(50),
                address VARCHAR(50),
                contact_number VARCHAR(15) UNIQUE,
                website VARCHAR(100) UNIQUE,
                registration_fees MONEY,
                UNIQUE(hospital_name,location, address)
            );
        """,
        "doctor_details": """
            CREATE TABLE IF NOT EXISTS doctor_details ( 
                doctor_id SERIAL PRIMARY KEY,
                hospital_id INT NOT NULL,
                department VARCHAR(50) NOT NULL, 
                doctor_name VARCHAR(20) NOT NULL, 
                gender CHAR(1) CHECK (gender IN ('M', 'F')), 
                availability_days TEXT[],
                consultation_hours JSONB,
                contact_no VARCHAR(15) UNIQUE,
                UNIQUE (doctor_id, hospital_id, department),
                FOREIGN KEY (hospital_id) REFERENCES hospital_details(hospital_id)
                
            );
        """,
        "family_member_details": """
            CREATE TABLE IF NOT EXISTS family_member_details(
                member_id SERIAL PRIMARY KEY,
                health_insurance_card_no VARCHAR(50) NOT NULL,
                first_name VARCHAR(20) NOT NULL,
                last_name VARCHAR(20),
                age INT,
                relation VARCHAR(15),
                gender VARCHAR(10) CHECK (gender IN ('M', 'F')),
                marital_status family_member_marital_status,
                profession VARCHAR(20),
                contact_no VARCHAR(15) UNIQUE,
                UNIQUE(health_insurance_card_no, first_name, relation),
           
                FOREIGN KEY (health_insurance_card_no) REFERENCES family_health_insurance_card_details (health_insurance_card_no)
            );
        """,
        "children_check_up_details": """
            CREATE TABLE IF NOT EXISTS children_check_up_details (
                check_up_id SERIAL PRIMARY KEY,
                health_insurance_card_no  VARCHAR(50),
                parents_name VARCHAR(50) NOT NULL,
                number_of_children INT,
                children_name_and_age JSONB,
                vaccination_details JSONB,
                date_of_vaccination JSONB,
                vaccination_name TEXT[],
                UNIQUE(health_insurance_card_no,parents_name),
                FOREIGN KEY (health_insurance_card_no) REFERENCES family_health_insurance_card_details (health_insurance_card_no)
            );
        """,
        "family_yearly_check_up_details": """
            CREATE TABLE IF NOT EXISTS family_yearly_check_up_details(
               yearly_check_up_id SERIAL PRIMARY KEY,
               health_insurance_card_no VARCHAR(50) NOT NULL,
               yearly_check_up_done BOOLEAN,
               date_of_check_up DATE,
               
               CHECK(yearly_check_up_done IN (TRUE, FALSE)),
               CHECK(date_of_check_up <= CURRENT_DATE),
               UNIQUE(health_insurance_card_no, date_of_check_up),
               FOREIGN KEY (health_insurance_card_no) REFERENCES family_health_insurance_card_details (health_insurance_card_no)
            );
        """,
        "family_medical_details": """
            CREATE TABLE IF NOT EXISTS family_medical_details(
                visit_id SERIAL PRIMARY KEY,
                health_insurance_card_no VARCHAR(50) NOT NULL,
                doctor_id INT NOT NULL,
                hospital_id INT NOT NULL,
                department VARCHAR(50) NOT NULL,
                date_of_visit TIMESTAMPTZ NOT NULL,
                symptoms TEXT[],
                diagnosis TEXT[],
                medication TEXT[],

                CHECK(date_of_visit <= CURRENT_DATE),
                FOREIGN KEY (health_insurance_card_no) REFERENCES family_health_insurance_card_details (health_insurance_card_no),
                FOREIGN KEY (doctor_id, hospital_id, department) REFERENCES doctor_details (doctor_id, hospital_id, department)
            );
        """
    }

    try:
        
        with pool.connection() as conn:
            with conn.cursor() as cursor:
             
                for table_name, query in queries.items():
                    
                    check_query = ("""
                        SELECT EXISTS (
                            SELECT 1 
                            FROM information_schema.tables 
                            WHERE table_name = %s
                        );
                    """)
                    cursor.execute(check_query, (table_name,))
                    exists = cursor.fetchone()[0]
                    
                    if not exists:
                        print(GREEN + ITALIC + "\nCreating table..." + RESET)
                        cursor.execute(query)
                        print(GREEN + f"Table '{table_name}' created successfully." + RESET)
                  
            conn.commit()
        return True 
    except OperationalError as e:
       conn.rollback()
       return ErrorHandler.operational_error(e)
    except Exception as e:
        conn.rollback()
        return ErrorHandler.exception_error(e)
        
    
        