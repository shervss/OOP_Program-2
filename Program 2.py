#Program No.2
#Mangulabnan, Shervin Marco DG.
#Display the input in fancy way

import pyfiglet
from colorama import init, Fore

init(autoreset=True)

def print_green(text):
    print(Fore.GREEN + text)

def print_yellow(text):
    print(Fore.YELLOW + text)

# Display prompts in desired colors
print_green("Please enter your name: ")
name = input()

print_yellow("Please enter your dream job: ")
dream_job = input()

print_green(pyfiglet.figlet_format(name))
print_yellow(pyfiglet.figlet_format(dream_job))