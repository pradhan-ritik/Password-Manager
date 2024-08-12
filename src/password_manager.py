from constants import *
from generate_password import *
from login import *
from os.path import exists
from shutil import rmtree

def run():
    if invalid_config_folder():
        if exists(DATA_FOLDER):
            rmtree(DATA_FOLDER)
            print("Sorry, .PASSWORD file in .data folder in this directory was deleted. This unfortunately means that I will have to delete it. This will restart the program to the state it started as when you downloaded this program.")

        setup_user()

    if login():
        logged_in = True
        print("You are successfully logged in.")
    
    else:
        print("You failed to login.")
        return
    


if __name__ == "__main__":
    run()