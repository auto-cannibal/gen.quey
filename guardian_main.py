import os
from guardian_ops import list_trustees
from backend.api import kdf, getpass

def guardian_main_flow(current_path, attempts):
    rekt = ".normie"
    with open(rekt, "rb") as file:
        content = file.read()
    if len(content) > 0:
        attempted_password = getpass("Please enter your password\n> ")
        encoded = kdf(attempted_password, b"0x69")
        with open(rekt, "rb") as file:
            _match = file.read()
        if encoded == _match:
            print("---\n! Successful login !\n---")
            list_trustees(os.path.join(current_path, "trustees"))
        else:
            attempts += 1
            if attempts < 3:
                guardian_main_flow(current_path, attempts)
            else:
                print("...")
    else:
        new_password = input("Please type your password in now\n> ")
        test_new_password = input("Please type your password in again\n> ")
        if new_password != test_new_password:
            print("Passwords did not match...")
            guardian_main_flow(current_path, attempts)
        else:
            encoded = kdf(new_password, b"0x69")
            with open(rekt, "wb") as file:
                file.write(encoded)
            guardian_main_flow(current_path, attempts)