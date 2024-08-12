from constants import *
from getpass import getpass
from os.path import exists, join
from os import environ
from shutil import rmtree
import base64

def _data_folder_slash(filepath: str) -> str:
    return os.path.join(DATA_FOLDER, filepath)

def _input_password() -> tuple[str, bool]:
    master_password = getpass("Set a Master Password(Used to unlock the program at startup): ")
    confirm_password = getpass("Type it again to confirm it as your Master Password: ")
    return master_password, (master_password != "") and (master_password == confirm_password)


def setup_user() -> None:
    os.mkdir(DATA_FOLDER)
    with open(_data_folder_slash("WARNING"), "w") as fh:
        fh.write(WARNING_TEXT_DOT_DATA)

    while True:
        master_password, success = _input_password()
        if not success:
            print("Failed. Password inputted was wrong")
            continue

        break

    with open(_data_folder_slash(".PASSWORD"), "w") as fh:
        fh.write(base64.b64encode(master_password.encode()).decode())

    # just create it for later use
    with open(_data_folder_slash(".PASSWORDS"), "w") as fh:
        pass
    
    print("You are done setting up. I suggest you make a backup of the .data folder just in case.")

def is_master_password(password: str) -> bool:
    res = False
    with open(_data_folder_slash(".PASSWORD"), "r") as fh:
        res = base64.b64encode(password.encode()).decode() == fh.read()

    return res

# return true if operation was successful. Else false
def invalid_config_folder() -> bool:
    if not exists(_data_folder_slash(".PASSWORD")):
        return True

    return False

def login() -> bool:
    password = getpass("Use your password to log in: ")
    if is_master_password(password):
        return True

    return False