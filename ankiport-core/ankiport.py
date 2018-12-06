import quizlet_helper

def main():
    print("Welcome to Ankiport!")
    print("Authorizing...")
    if quizlet_helper.creds_file_exists() == False:
        print("creds.txt file not found in this directory!!\nPlease make sure your credentals file is named creds.txt.")
        return
    print("Credentials verified!")
    usr_name = input("To get started, please enter the username whose sets you'd like to browse: ")
    set_name = input("Thank you! Now, please enter the name of the set that you'd like to port: ")
    print("Great! Porting set now....")
    if quizlet_helper.port(usr_name, set_name) != False:
        print("Set ported!")
    else:
        print("Failure!")


main()
