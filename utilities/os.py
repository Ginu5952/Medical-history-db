import os

def clear_screen():
    try:
        if os.name == 'posix':
            os.system('clear')
        elif os.name == 'nt':
            os.system('cls')
    except Exception as e:
        print(f"Error clearing the screen: {e}")