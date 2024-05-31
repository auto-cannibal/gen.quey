import os
from backend.api import encrypt, getpass

def secret_add_flow(secret_file_name):
    question_0 = input("Add question 0 below\n > ")
    question_1 = input("Add question 1 below\n > ")
    question_2 = input("Add question 2 below\n > ")
    question_to_read = question_0 + ";" + question_1 + ";" + question_2
    with open(secret_file_name + "_questions", "w") as file:
        file.write(question_to_read)
    answer_0 = getpass(f"Add answer below to: '{question_0}'\n> ").lower()
    answer_0_check = getpass(f"Please repeat your answer\n> ").lower()
    if answer_0_check != answer_0:
        print("Answers do not match - process reset\n")
        os.remove(secret_file_name + "_questions")
        return
    answer_1 = getpass(f"Add answer below to: '{question_1}'\n> ").lower()
    answer_1_check = getpass(f"Please repeat your answer\n> ").lower()
    if answer_1_check != answer_1:
        print("Answers do not match - process reset\n")
        os.remove(secret_file_name + "_questions")
        return
    answer_2 = getpass(f"Add answer below to: '{question_2}'\n> ").lower()
    answer_2_check = getpass(f"Please repeat your answer\n> ").lower()
    if answer_2_check != answer_2:
        print("Answers do not match - process reset\n")
        os.remove(secret_file_name + "_questions")
        return
    key = answer_0 + ";" + answer_1 + ";" + answer_2
    secret = input(f"Add your secret\n> ")
    encrypt(key, secret, secret_file_name)