import os
from guardian_main import guardian_main_flow
from trustee import trustee_main_flow

def init(current_path):
    _type = input("Are you the guardian, or a trustee (guardian/trustee)?\n> ")
    if _type == "guardian":
        attempts=0
        guardian_main_flow(current_path, attempts)
    elif _type == "trustee":
        trustee_main_flow(current_path)
    else:
        init(current_path)

if __name__=="__main__":
    current_path = os.getcwd()
    init(current_path)