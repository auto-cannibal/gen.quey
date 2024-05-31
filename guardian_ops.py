import os
from craft import secret_add_flow
from shared import unlock_secret

def list_trustees(trustee_directory):
    print("Please decide from the following list which of the following trustees you are interested in:")
    trustee_directories = os.listdir(trustee_directory)
    for dir in trustee_directories:
        print("- " + dir)
    print("Or add a new trustee (add)")
    choice = input("> ")
    trustee_path = f"{trustee_directory}/{choice}/"
    if choice == "add":
        name = input("Please enter the name of the trustee\n> ").lower()
        surname = input("Please enter the surname of the trustee\n> ").lower()
        new_trustee_path = f"{trustee_directory}/{name}_{surname}"
        try:
            print(f"---\n! Creating new trustee account !\n---")
            os.makedirs(new_trustee_path, exist_ok=True)
            secret_file_name = input("What do we call this secret?\n> ")
            secret_file_path = f"{new_trustee_path}/{secret_file_name}"
            secret_add_flow(secret_file_path)
        except:
            print(f"---\n! Trustee already exists {new_trustee_path} - please choose from the list !\n---")
            list_trustees(trustee_directory)
    elif (os.path.exists(trustee_path)):
        print(f"---\n! Trustee found: {True} !\n---")
        guardian_operations_flow(trustee_path)
    else:
        print(f"---\n! Trustee found: {False} !\n---")
        list_trustees(trustee_directory)

def guardian_operations_flow(trustee_path):
    print("Please decide from the following list which of the following secrets you are interested in:")
    files = os.listdir(trustee_path)
    for file in files:
        if "_questions" not in file:
            print("'" + file + "'")
    print("Or add a new secret (add)")
    choice = input("> ")
    if choice == "add":
        secret_file_name = input("What do we call this secret?\n> ")
        secret_file_path = f"{trustee_path}/{secret_file_name}"
        secret_add_flow(secret_file_path)
    elif (os.path.exists(trustee_path)):
        print(f"---\n! Editing secret file: {choice} !\n---")
        try:
            unlock_secret("{}/{}".format(trustee_path, choice))
        except:
            print("Bad password")
    else:
        print(f"---\n! Secret file not found: {choice} !\n---")
        guardian_operations_flow(trustee_path)