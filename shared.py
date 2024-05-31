from backend.api import decrypt, getpass

def unlock_secret(secret_path):
    with open(secret_path + "_questions", "r") as file:
        questions = file.read()
    question = questions.split(";")
    answer_0 = getpass(f"Add answer below to: '{question[0]}'\n> ").lower()
    answer_1 = getpass(f"Add answer below to: '{question[1]}'\n> ").lower()
    answer_2 = getpass(f"Add answer below to: '{question[2]}'\n> ").lower()
    key = answer_0 + ";" + answer_1 + ";" + answer_2
    decrypt(key, secret_path)