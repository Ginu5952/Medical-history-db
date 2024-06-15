from src.Connect.connect_db import *
from utilities.os import clear_screen
from src.Create.create_tables import *
from src.Insert.insert_tables import *
from utilities.colors import *
from utilities.font_styles import *
from src.Command_line.command_line import DataInserter
from src.helper.helper import *



def main():     

    try:
        db_connection = DatabaseConnection()
        db_connection.connect()  
      
        pool = db_connection.get_connection()
        inserter = DataInserter(pool)

        if pool is not None:
            print(PURPLE + BOLD + "\nSuccessfully connected to Database" + RESET)
            create_type(pool)

            if create_tables(pool):
                print('\n')
                inserter.insert_data_into_health_card()
            else:
                sys.exit()   


        else:
            print(RED + BOLD + "Failed to establish a database connection" + RESET)
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if pool is not None:
            pool.close()
             

if __name__ == '__main__':
    main()