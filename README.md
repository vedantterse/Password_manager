﻿# Password_manager  
Overview
Password Manager is a Python-based command-line utility designed for secure password management. The tool incorporates features such as password generation, adding passwords, and viewing saved passwords. Employing encryption ensures the confidentiality of stored passwords.

# features
### •Password Generation: Create robust and secure passwords using custom or random options.
### •Adding Passwords: Easily add and encrypt passwords for various purposes.
### •View Saved Passwords: Decrypt and view your saved passwords securely.

## Project Structure
•generate_key: Function to generate a Fernet key for encryption.

•load_key: Load an existing Fernet key or create a new one.

•encrypt_data: Encrypt data using Fernet symmetric key encryption.

•decrypt_data: Decrypt encrypted data using the Fernet key.

•hash_password: Hash a password using SHA-256 for secure storage.

•save_passwords: Encrypt and save passwords to a file.

•load_passwords: Load and decrypt saved passwords from a file.

•view_passwords: Display all decrypted passwords.

•generate_password: Automatic password generator with custom and random options.

•adding_passwords: Add and update passwords with associated purposes.

## Setup Instructions
1. **Make sure you have Pip and Python installed on the device**
2. **Clone the Repository:**
    
   ```
   git clone https://github.com/your-username/Password_manager.git
   

   ```
   Note: Replace "your-username" with your actual GitHub username in the repository URL.

   
3.**Install required dependencies:**

   ```
    python -m pip install cryptography nltk

   ```
4.**default password**

  •Default password for Viewing the password it set. Change it accordingly
   
   ![image](https://github.com/vedantterse/Password_manager/assets/69134828/514cfdb2-1b72-4319-9e70-6fb713e35374)

5. **Run the program**
    •you should get the output
    
     ![Screenshot 2023-11-30 010135](https://github.com/vedantterse/Password_manager/assets/69134828/21bdc23a-6c10-4910-b96c-708a86249906)



## Usage

•Choose an action (1 for password generation, 2 for adding passwords, 3 for viewing passwords).

•Follow on-screen instructions for each action.

•Use "exit" at any point to end the program or come back to main menu.


## Security Highlight
Encryption: Passwords are encrypted using Fernet symmetric key encryption, ensuring secure storage.

Feel free to explore and contribute to the project. If you encounter issues, please report them in the Issues section.


