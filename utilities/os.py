import os

def clear_screen():
    # Check if the operating system is Windows or Unix-like
    if os.name == 'posix':  # posix is for Linux, macOS, and Unix
        _ = os.system('clear')  # Clear command for Unix-like systems
    elif os.name == 'nt':  # 'nt' is for Windows
        _ = os.system('cls')