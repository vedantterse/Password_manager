import hashlib

from cryptography.fernet import Fernet
import random
import string
import os
import nltk
from nltk.corpus import words

nltk.download('words', quiet=True)


def generate_key():
    return Fernet.generate_key()


def load_key():
    if os.path.exists('key.key'):
        with open('key.key', 'rb') as key_file:
            key = key_file.read()
        return key
    else:
        key = generate_key()
        with open('key.key', 'wb') as key_file:
            key_file.write(key)
        return key


def encrypt_data(key, data):
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data


def decrypt_data(key, encrypted_data):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data


def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password


def save_passwords(passwords, key):
    encrypted_data = ''
    for purpose, password in passwords.items():
        encrypted_data += f"{purpose}: {password}\n"

    with open('passwords.txt', 'wb') as file:
        file.write(encrypt_data(key, encrypted_data))


def load_passwords(key):
    passwords = {}
    if os.path.exists('passwords.txt'):
        with open('passwords.txt', 'rb') as file:
            encrypted_data = file.read()
            decrypted_data = decrypt_data(key, encrypted_data)

            for line in decrypted_data.splitlines():
                line = line.strip()
                if line:
                    if ': ' in line:
                        purpose, password = line.split(': ', 1)
                        passwords[purpose] = password
    return passwords


def view_passwords(key):
    passwords = load_passwords(key)
    print("All Passwords:")
    for purpose, password in passwords.items():
        print(f"{purpose}: {password}")


def generate_password(key):
    print('!!This is an automatic password generator!!')
    while True:
        print("Choose an option for password generation:")
        print("1. Custom Password: Include your own words or text in the password.")
        print("2. Random Password: Generate a completely random password.")

        exit_p = False  # Variable to check if "exit" is entered
        while True:
            w = input(
                '\033[32mEnter the value for the corresponding action\033[0m \033[36m(press\033[0m \033[91m exit\033[0m \033[36m for ending '
                'the'
                'program):\033[0m ')
            if w.lower() == 'exit':
                exit_p = True
                break
            if w in ['1', '2']:
                break
            else:
                print('Enter a valid value')

        if exit_p:  # Check if "exit" was entered
            break  # Break out of the outer while loop to end the program
        if w == "1":
            text = input('Enter the text you want: ')
            length_a = random.randint(10, 12)
            length_b = random.randint(13, 16)
            element = ''.join(
                random.choices(string.ascii_letters + string.digits + string.punctuation + string.hexdigits,
                               k=length_a - len(text)))
            element1 = ''.join(
                random.choices(string.ascii_letters + string.digits + string.hexdigits + string.punctuation,
                               k=length_b - len(text)))
            a = text + element
            b = element1 + text
            combined_length = min(len(a), len(b))
            c = a[:combined_length // 2] + b[:combined_length // 2]

            password_choices = {'a': a, 'b': b, 'c': c}
            print("CHOOSE BETWEEN:-")
            print(f"a: {a}")
            print(f"b: {b}")
            print(f"c: {c}")

            inner_loop_flag = True
            while inner_loop_flag:
                choice = input("ENTER the choice of password (a/b/c):- ")

                if choice in password_choices:
                    purpose = input("Enter the purpose of the password: ")

                    existing_passwords = load_passwords(key)

                    if purpose in existing_passwords and existing_passwords[purpose] != password_choices[choice]:
                        # Purpose already exists, ask the user if they want to update it
                        while True:
                            update_existing = input(
                                f"Password for '{purpose}' already exists. Do you want to update it? (yes/no): ")
                            if update_existing.lower() == 'yes':
                                # Update the password in the existing_passwords dictionary
                                existing_passwords[purpose] = password_choices[choice]
                                print(f"Password for '{purpose}' updated successfully.")
                                break
                            elif update_existing.lower() == 'no':
                                print(f"Password for '{purpose}' remains unchanged.")
                                break
                            else:
                                print("Invalid value. Please enter 'yes' or 'no'.")
                    else:
                        existing_passwords[purpose] = password_choices[choice]
                        print(f"PASSWORD SAVED:-  {purpose}: {password_choices[choice]}")

                    # Save the updated passwords to the file
                    save_passwords(existing_passwords, key)

                    inner_loop_flag = False  # Exit the inner loop when a valid choice is made
                else:
                    print('Enter a valid value')

        elif w == "2":
            word = ''.join(random.choice(words.words()))
            remaining_length_a = max(16 - len(word), 0)

            # Ensure that length_a is 16 or less
            length_p = min(random.randint(10, 12), remaining_length_a)

            word1 = ''.join(random.choice(words.words()))

            length_q = random.randint(13, 16)
            element0 = ''.join(
                random.choices(
                    string.ascii_letters.upper() + string.ascii_letters.lower() + string.digits + string.punctuation + string.hexdigits,
                    k=length_p))
            element11 = ''.join(
                random.choices(string.ascii_letters + string.digits + string.hexdigits + string.punctuation,
                               k=length_q))

            p = word + element0
            q = element11 + word1

            # Ensure that the combined length of p and q does not exceed the user-provided length
            combined_length = min(len(p), len(q))

            r = p[:combined_length // 2] + q[:combined_length // 2]
            print("CHOOSE BETWEEN:-")
            print(f"a: {p}")
            print(f"b: {q}")
            print(f"c: {r}")
            password_choices = {'a': p, 'b': q, 'c': r}

            inner_loop_flag = True
            while inner_loop_flag:
                choice = input("ENTER the choice of password (a/b/c):- ")

                if choice in password_choices:
                    purpose = input("Enter the purpose of the password: ")

                    existing_passwords = load_passwords(key)

                    if purpose in existing_passwords and existing_passwords[purpose] != password_choices[choice]:
                        # Purpose already exists, ask the user if they want to update it
                        while True:
                            update_existing = input(
                                f"Password for '{purpose}' already exists. Do you want to update it? (yes/no): ")
                            if update_existing.lower() == 'yes':
                                # Update the password in the existing_passwords dictionary
                                existing_passwords[purpose] = password_choices[choice]
                                print(f"Password for '{purpose}' updated successfully.")
                                break
                            elif update_existing.lower() == 'no':
                                print(f"Password for '{purpose}' remains unchanged.")
                                break
                            else:
                                print("Invalid value. Please enter 'yes' or 'no'.")
                    else:
                        existing_passwords[purpose] = password_choices[choice]
                        print(f"PASSWORD SAVED:-  {purpose}: {password_choices[choice]}")

                    # Save the updated passwords to the file
                    save_passwords(existing_passwords, key)

                    inner_loop_flag = False
                else:
                    print('Enter a valid value')


def adding_passwords(key):
    while True:
        existing_passwords = load_passwords(key)
        exitop = False
        inner_loop_flag = True
        while inner_loop_flag:
            print("ADD your own password")
            password_choices = input("Enter your password: ")
            if password_choices.lower() == "exit":
                exitop = True
                break

            purpose = input("Enter your purpose: ")
            if purpose in existing_passwords:
                # Purpose already exists, ask the user if they want to update it
                while True:
                    update_existing = input(
                        f"Password for '{purpose}' already exists. Do you want to update it? (yes/no): ")
                    if update_existing.lower() == 'yes':
                        # Update the password in the existing_passwords dictionary
                        existing_passwords[purpose] = password_choices
                        print(f"Password for '{purpose}' updated successfully.")
                        break
                    elif update_existing.lower() == 'no':
                        print(f"Password for '{purpose}' remains unchanged.")
                        break
                    else:
                        print("Invalid value. Please enter 'yes' or 'no'.")

            else:
                existing_passwords[purpose] = password_choices
                print(f"NEW PASSWORD SAVED: {purpose}: {password_choices}")

                # Save the updated passwords to the file
            save_passwords(existing_passwords, key)

            inner_loop_flag = False
        if exitop:
         break


print("PASSWORD MANAGER")
print("select fom the given options")
print("1. PASSWORD GENERATION\n2. ADD PASSWORD\n3. VIEW SAVED PASSWORD")
key = load_key()
while True:
    exit_p = False
    while True:
        w = input(
            '\033[36mEnter the value for the corresponding action (press \033[91m exit\033[0m \033[36m for ending the '
            'program):\033[0m ')
        if w.lower() == 'exit':
            exit_p = True
            break
        if w in ['1', '2', '3']:
            break
        else:
            print('Enter a valid value')

    if exit_p:
        break
    if w == '1':
        generate_password(key)

    elif w == '2':
        adding_passwords(key)

    elif w == '3':

        validate = input('Enter a valid password to access passwords: ')
        if validate=="exit":
            continue
        if validate == "1234":  # default password is 1234, change accordingly
            view_passwords(key)
            break
        else:

            print("Please enter a valid password")
