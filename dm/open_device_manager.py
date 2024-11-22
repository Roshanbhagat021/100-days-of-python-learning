# import os

# def open_device_manager():
#     # Open Device Manager on Windows
#     os.system("devmgmt.msc")

# if __name__ == "__main__":
#     open_device_manager()
import webbrowser
import time

def open_website():
    # Path to Chrome browser (replace with your Chrome executable path if needed)
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    
    # Website to open
    url = "https://students.masaischool.com/signin"
    
    # Open the website using Chrome
    webbrowser.get(chrome_path).open(url)
    
if __name__ == "__main__":
    # Add a slight delay to ensure other startup processes settle
    time.sleep(5)
    open_website()
