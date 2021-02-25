import requests
import db_connector

try:
    #Step 1 - adding a new user to the DB
    res = requests.post('http://127.0.0.1:5000/users/3', json={"user_name": "Itzik"})

    #Step 2 - Check if the user was inserted
    check_insert = requests.get('http://127.0.0.1:5000/users/3')

    #Setp 3 - print DB
    db_connector.get_all_info()

    print(res.json())
    print(check_insert.json())
except:
    print("test failed")