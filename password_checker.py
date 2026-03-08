import re

BLACK   = "\033[30m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
RESET   = "\033[0m"

def strengthbar(score):
    colors = [RED, YELLOW, BLUE, GREEN]
    bar = "["

    for i in range(4):
        if i < score:
            bar += colors[i] + "#" + RESET
        else:
            bar += "-"
    bar += "]"

    print("Password strength:", bar)

def main():

    print(MAGENTA + "Welcome to the land of Python. Are you good at making passwords!" + RESET)
    
    score = 0
     
    while (score != 4):
        score = 4    
        password = input(MAGENTA + "Password: " + RESET)

        if len(password) < 14:
            score -= 1
        if not (re.search(r'[A-Z]', password) and re.search(r'[a-z]', password)):
            score -= 1
        if not re.search(r'\d', password):
            score -= 1
        if not re.search(r'[@$!%*?&]', password):
            score -= 1

        if score == 4:
            print(GREEN + "You've returned a very strong password! Good job!" + RESET)
        elif score == 3:
            print(BLUE + "You've returned a strong password, but there's a way to still be even safer " + RESET)
        elif score == 2:
            print(YELLOW + "You've returned a moderate password. Fix up those vulnerabilities and you're good to go." + RESET)
        elif score == 1:
            print(BLACK + "You've returned a weak password. Come on, you can do better than that!" + RESET)
        else:
            print(RED + "You've returned a very weak password... Are you looking to get hacked?" + RESET)

        strengthbar(score)

        if (score != 4):
            print(RED + "Fix this: " + RESET, end = "")
        
        if len(password) < 14:
            print(RED + "Your password should be 14 characters long!" + RESET)
        elif not (re.search(r'[A-Z]', password) and re.search(r'[a-z]', password)):
            print(RED + "Your password should contain at least one uppercase and one lowercase character each!" + RESET)
        elif not re.search(r'\d', password):
            print(RED + "Your password should contain at least one numerical character (0-9)!" + RESET)
        elif not re.search(r'[@$!%*?&]', password):
            print(RED + "Your password should contain at least one special character (@,$,!,%,*,?,&)" + RESET)
            score -= 1
        


if __name__ == "__main__":
    main()