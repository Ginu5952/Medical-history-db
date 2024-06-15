
import psycopg
from psycopg import OperationalError
from psycopg_pool import ConnectionPool

from utilities.colors import *
from utilities.font_styles import *


class DatabaseConnection:

    def __init__(self):
        self.pool = None

    def connect(self):
        try:
            self.pool = ConnectionPool(
                conninfo="dbname=family_medical_info user=postgres password=postgres host=localhost options='-c search_path=family'",
                min_size=1,
                max_size=10
            )
            print(PURPLE + ITALIC + "\nConnection pool created successfully" + RESET)
        except OperationalError as e:
            print(f"An error occurred: {e}")

    def get_connection(self):
        if not self.pool:
            self.connect()
        return self.pool
     
    


