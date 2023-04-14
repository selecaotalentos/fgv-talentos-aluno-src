# code responsible for creating logins
import requests

# registration url
url = "https://www.authpro.com/api2/create/"

def add_login(user:str, email:str, name:str, manager_user:str, api_key:str):
    # formats request
    data = {
        '_login': user,
        '_email': email,
        'name': name,
        'user': manager_user,
        'api_key':api_key }
    # makes request
    r = requests.post(url, data)
    if r.json()["result"] == "OK":
        print("Added user: ", user)
        return r.json()["password"]
    else:
        print("Error: ", user, r.text)
