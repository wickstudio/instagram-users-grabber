import colorama
from colorama import Fore, Style
import pyfiglet
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import os
import sys

colorama.init(autoreset=True)

def print_title():
    ascii_title = pyfiglet.figlet_format("WICK STUDIO", font="slant")
    print(f"{Fore.CYAN}{ascii_title}{Style.RESET_ALL}")

def check_username_availability(username):
    base_url = f"https://www.instagram.com/{username}/"

    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1080")

    try:
        with webdriver.Chrome(options=options) as driver:
            driver.get(base_url)
            page_source = driver.page_source
            return "Sorry, this page isn't available." not in page_source
    except WebDriverException as e:
        print(f"{Fore.RED}Error checking username {username}: {e}{Style.RESET_ALL}")
        return False

def write_username_to_file(file_path, username):
    folder_path = "usernames"
    os.makedirs(folder_path, exist_ok=True)
    full_path = os.path.join(folder_path, file_path)
    
    with open(full_path, "a") as file:
        file.write(username + "\n")

def sort_usernames(usernames):
    available_usernames = []
    unavailable_usernames = []

    for username in usernames:
        if check_username_availability(username):
            available_usernames.append(username)
            write_username_to_file("available_usernames.txt", username)
        else:
            unavailable_usernames.append(username)
            write_username_to_file("unavailable_usernames.txt", username)

    return available_usernames, unavailable_usernames

def read_usernames_from_file(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]

def user_menu():
    print_title()
    print(f"{Fore.MAGENTA}Welcome to Wick Tool:{Style.RESET_ALL}")
    print(f"{Fore.BLUE}1. Check Usernames in file.txt{Style.RESET_ALL}")
    print(f"{Fore.BLUE}2. Exit{Style.RESET_ALL}")
    choice = input(f"{Fore.YELLOW}Enter your choice (1 or 2): {Style.RESET_ALL}")

    if choice == '1':
        check_usernames()
    elif choice == '2':
        sys.exit(0)
    else:
        print(f"{Fore.RED}Invalid choice. Exiting.{Style.RESET_ALL}")

def check_usernames():
    usernames_to_check = read_usernames_from_file("file.txt")
    available, unavailable = sort_usernames(usernames_to_check)
    print(f"{Fore.GREEN}Checked {len(usernames_to_check)} usernames.{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Available Usernames: {len(available)}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Unavailable Usernames: {len(unavailable)}{Style.RESET_ALL}")

if __name__ == "__main__":
    user_menu()
