import os
from shared import unlock_secret

def trustee_main_flow(current_path):
    name = input("Please enter your first name\n> ").lower()
    surname = input("Please enter your surname\n> ").lower()
    trustee_path = f"trustees/{name}_{surname}/"
    if (os.path.exists(trustee_path)):
        trustee_files = os.listdir(trustee_path)
        secret_choice = print("Please choose a secret from your account: ")
        for file in trustee_files:
            if "_questions" not in file:
                print("'" + file + "'")
        secret_choice = input("> ")
        if (os.path.exists(trustee_path + secret_choice)):
            try:
                unlock_secret(trustee_path + secret_choice)
            except:
                print("Bad password")
        else:
            print("Secret not found")
            trustee_main_flow(current_path)
    else:
        print(f"---\n! No account found !\n---")