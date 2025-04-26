# Simple Bruteforce Tool for DVWA (DAMN VULNERABLE WEB APPLICATION)

A simple Python script that performs a brute force attack using **username.txt** and **password.txt** files, leveraging the **Requests** library to attempt login attempts.

## Features

- Performs brute force login attempts using a list of usernames and passwords.
- Supports customization of the login URL and form fields.
- Simple and easy to use.

## Technologies

- Python 3.x
- Requests (for making HTTP requests)

## Setup and Usage

1. Make sure you have Python 3.x installed on your system.
2. Install the required library:

```bash
pip install requests
```
3. Prepare your username.txt and password.txt files. Each file should contain a list of usernames and passwords, one per line.
4. Update the script with the login URL and the relevant form field names (e.g., username, password, etc.).
5. Run the script:
```
python bruteforce.py
```
The script will attempt to log in using each combination of username and password from the provided files.

Note: Make sure you have permission to perform a brute force attack on the target system. Unauthorized access is illegal.
