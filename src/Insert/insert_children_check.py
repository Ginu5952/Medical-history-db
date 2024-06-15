from src.Connect.connect_db import DatabaseConnection
from src.Command_line.command_line import DataInserter
from utilities.colors import *
from utilities.font_styles import *
from src.Select.display_hospital_details import *
  

def main():

    db_connection = DatabaseConnection()
    db_connection.connect()
    
    pool = db_connection.get_connection()
    inserter = DataInserter(pool)

    if pool is not None:
        print(MAGENTA + ITALIC + "\nSuccessfully connected to Database" + RESET)
        inserter.insert_data_into_children_check_up_details()
       
    else:
        print( RED + BOLD + "\nFailed to establish a database connection" + RESET)
   


if __name__ == '__main__':
    main()
