from library import Library

def Credentials():
    with open("test.txt") as f:
        data = f.readlines()
        credentials = data[0].split(',')
    return credentials


def authentication():
    credentials = Credentials()
    while(1):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if (credentials[0] ==  username) and (credentials[1] ==  password):
                print("authentication successful!\n")
                # LibrarianMenu()
                return

        else:
            print("Credentials are incorrect\n")
            choice = input("Do you want to enter again(y/n)?")
            if(choice == 'y'):
                     continue;   
            else:
                return
   

if __name__ == "__main__":
    # Library()
    loginchoice = input("Admin or User").lower()
    str1 = "admin"
    str2 = "user"
    if (loginchoice == str1):
         authentication()
    elif(loginchoice == str2):
         print("good")
        # UserMenu()
    else:
         print("Invalid choice entered")
