import os
import tkinter as tk
from tkinter import filedialog
import requests
import mimetypes
import keyboard
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to get the best server
def get_best_server():
    """Get the best server for uploading."""
    response = requests.get("https://api.gofile.io/getServer")
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'ok':
            return data['data']['server']
    return None

# Function to get the MIME type of the file
def get_mime_type(file_path):
    """Get the MIME type of the file."""
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type

# Function to upload file
# Function to upload file
def upload_file(server, file_path):
    """Upload file to the specified server."""
    if file_path:
        url = f'https://{server}.gofile.io/uploadFile'
        files = {'file': open(file_path, 'rb')}
        response = requests.post(url, files=files)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'ok':
                download_link = data['data']['downloadPage']
                file_name = os.path.basename(file_path)
                print(Fore.GREEN + f"{download_link} - [{file_name}]")
            else:
                file_name = os.path.basename(file_path)
                print(Fore.RED + f"Failed to upload - [{file_name}]")
        else:
            print(Fore.RED + f"Failed to upload file. Status code: {response.status_code}")
            print(Fore.RED + "Response:", response.text)  # Corrected indentation
    else:
        print(Fore.RED + "No file selected")


# Create tkinter window
root = tk.Tk()
root.withdraw() # Hide the main window

# Function to start uploading
def start_uploading():
    file_paths = filedialog.askopenfilenames()
    for file_path in file_paths:
        upload_file(best_server, file_path)

# Get the best server
best_server = get_best_server()

# Main menu
print(Fore.LIGHTBLUE_EX + r"""
 __   ___    _       _                 _           
 \ \ / / |  | |     | |               | |          
  \ V /| |  | |_ __ | | ___   __ _  __| | ___ _ __ 
   > < | |  | | '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
  / . \| |__| | |_) | | (_) | (_| | (_| |  __/ |   
 /_/ \_\\____/| .__/|_|\___/ \__,_|\__,_|\___|_|   
              | |                                  
              |_|                                   
""")

print(Fore.LIGHTCYAN_EX + "made by Low\n")

options = ["Start uploading", "Leave the tool"]
selected_option = 0

def print_menu():
    clear_screen()
    print(Fore.LIGHTBLUE_EX + r"""
 __   ___    _       _                 _           
 \ \ / / |  | |     | |               | |          
  \ V /| |  | |_ __ | | ___   __ _  __| | ___ _ __ 
   > < | |  | | '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
  / . \| |__| | |_) | | (_) | (_| | (_| |  __/ |   
 /_/ \_\\____/| .__/|_|\___/ \__,_|\__,_|\___|_|   
              | |                                  
              |_|       
""")
    print(Fore.LIGHTCYAN_EX + "made by Low\n")
    print("Menu:")
    for i, option in enumerate(options):
        if i == selected_option:
            print(">", option)
        else:
            print(" ", option)

print_menu()

while True:
    if keyboard.is_pressed('down') and selected_option < len(options) - 1:
        selected_option += 1
        print_menu()
    elif keyboard.is_pressed('up') and selected_option > 0:
        selected_option -= 1
        print_menu()
    elif keyboard.is_pressed('enter'):
        if selected_option == 0:
            start_uploading()
        elif selected_option == 1:
            print("Leaving the tool. Goodbye!")
            break
