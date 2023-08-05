import pyfiglet
from colorama import init, Fore, Style
import requests
import codecs
import re

# Initialize colorama
init()

# Function to print ASCII art
def print_ascii_art(text):
    result = pyfiglet.figlet_format(text)
    print(result)

# Function to check if a subdomain is valid
def is_valid_subdomain(subdomain):
    # Using regex to check if the subdomain contains only valid characters (alphanumeric and hyphen)
    return re.match(r'^[a-zA-Z0-9\-]+$', subdomain) is not None

# Function for scanning subdomains
def domain_scanner(domain_name, subdomain_list, directory_list):
    print('----URLs after scanning----')

    for subdomain in subdomain_list:
        if subdomain and is_valid_subdomain(subdomain):
            url = f"https://{subdomain}.{domain_name}"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print(f'[+] {Fore.GREEN}{url} - Live (Status Code: {response.status_code}){Style.RESET_ALL}')
                else:
                    print(f'[-] {Fore.RED}{url} - Not Live (Status Code: {response.status_code}){Style.RESET_ALL}')
            except requests.ConnectionError:
                print(f'[-] {Fore.RED}{url} - Connection Error{Style.RESET_ALL}')

        for directory in directory_list:
            url = f"https://{subdomain}.{domain_name}/{directory}"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print(f'[+] {Fore.GREEN}{url} - Live (Status Code: {response.status_code}){Style.RESET_ALL}')
                else:
                    print(f'[-] {Fore.RED}{url} - Not Live (Status Code: {response.status_code}){Style.RESET_ALL}')
            except requests.ConnectionError:
                print(f'[-] {Fore.RED}{url} - Connection Error{Style.RESET_ALL}')

# Main function
if __name__ == '__main__':
    # Print ASCII art for the program name
    print_ascii_art("Seer")
    print("Made By R4GN4R0K")

    # Input option for directory scanning
    switch_to_directory_mode = input("Do you want to switch to directory mode? (y/n): ")

    if switch_to_directory_mode.lower() == 'y':
        # Input the domain name
        dom_name = input("Enter the Domain Name: ")

        # Input the word list filename for subdomains
        subdomain_word_list_file = input("Enter the Subdomain Word List Filename: ")

        # Attempt to open the subdomain word list file with 'utf-8' encoding
        try:
            with codecs.open(subdomain_word_list_file, 'r', encoding='utf-8') as file:
                # Reading the file and splitting it into lines
                subdomain_word_list = file.read().splitlines()
        except UnicodeDecodeError:
            # If 'utf-8' encoding fails, try 'latin-1' encoding
            with codecs.open(subdomain_word_list_file, 'r', encoding='latin-1') as file:
                # Reading the file and splitting it into lines
                subdomain_word_list = file.read().splitlines()

        # Input the word list filename for directories
        directory_word_list_file = input("Enter the Directory Word List Filename: ")

        # Opening the directory word list file
        with codecs.open(directory_word_list_file, 'r', encoding='utf-8') as file:
            # Reading the file and splitting it into lines
            directory_word_list = file.read().splitlines()

        # Calling the function for scanning the subdomains and directories
        domain_scanner(dom_name, subdomain_word_list, directory_word_list)
    else:
        # Input the domain name
        dom_name = input("Enter the Domain Name: ")

        # Input the word list filename for subdomains
        subdomain_word_list_file = input("Enter the Subdomain Word List Filename: ")

        # Attempt to open the subdomain word list file with 'utf-8' encoding
        try:
            with codecs.open(subdomain_word_list_file, 'r', encoding='utf-8') as file:
                # Reading the file and splitting it into lines
                subdomain_word_list = file.read().splitlines()
        except UnicodeDecodeError:
            # If 'utf-8' encoding fails, try 'latin-1' encoding
            with codecs.open(subdomain_word_list_file, 'r', encoding='latin-1') as file:
                # Reading the file and splitting it into lines
                subdomain_word_list = file.read().splitlines()

        # Calling the function for scanning the subdomains
        domain_scanner(dom_name, subdomain_word_list, []) 

