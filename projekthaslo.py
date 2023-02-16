import random
import string
import sys
import json
import clipboard

SAVED_PASSWORDS = "hasla.json"

def save_password(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_password(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_password(SAVED_PASSWORDS)

    if command == 'generate':
        key = input('Enter a key: ')
        try: 
            length = int(input("Enter your password length: "))
            letters = string.ascii_lowercase
            odpowiedz1 = input("Do you want to have uppercase letters in your password? Type Yes or No\n")
            if odpowiedz1 == "yes" or odpowiedz1 == "Yes":
                letters += string.ascii_uppercase
            elif odpowiedz1 == "no" or odpowiedz1 == "No":
                pass
            else:
                print("This is not a correct answer. Please type yes or no.")
            odpowiedz2 = input("Do you want to have special characters in your password? Type Yes or No\n")
            if odpowiedz2 == "yes" or odpowiedz2 == "Yes":
                letters += string.punctuation
            elif odpowiedz2 == "no" or odpowiedz2 == "No":
                pass
            else:
                print("This is not a correct answer. Please type yes or no.")
            odpowiedz3 = input("Do you want to have digits in your password? Type Yes or No\n")
            if odpowiedz3 == "yes" or odpowiedz3 == "Yes":
                letters += string.digits
            elif odpowiedz3 == "no" or odpowiedz3 == "No":
                pass
            else:
                print("This is not a correct answer. Please type yes or no.")
            password = "".join(random.choice(letters) for i in range(length))
            print(f"Your password is: {password} .")
            data[key] = password
            save_password(SAVED_PASSWORDS, data)
            print('Data saved')
        except ValueError:
            print("This is not a digit. Please type a number next time.")
    elif command == 'load':
        key = input('Enter a key: ')
        if key in data:
            clipboard.copy(data[key])
            print('Data copied to clipboard')
        else:
            print('Key does not exist.')
    elif command == 'list':
        print(data)
    elif command == 'delete':
        key = input('Enter a key to delete: ')
        if key in data:
            data.pop(key)
            save_password(SAVED_PASSWORDS, data)
            print(f'Key {key} deleted.')
        else:
            print(f'Key {key} does not exist in json file.')
    else:
        print('Unknown command')
else:
    print('Type exactly one command')