import requests
import json
import os
import time
bold = "\u001b[1m"
Black = "\u001b[30m"
Red = "\u001b[31m"
Green = "\u001b[32m"
Yellow = "\u001b[33m"
Blue =  "\u001b[34m"
Magenta = "\u001b[35m"
Cyan = "\u001b[36m"
clear = "\u001b[0m"
print(Yellow, bold, "s2pyStats",Blue,"v0.1 beta",clear)
def clearconsole():
    os.system("clear")
def getMessages(user,url,headers):
    loading = "true"
    print(Green,bold,"Loading, Please wait...",clear)
    try:
     response = requests.get(url, headers=headers)
     data = response.text
     parse_json = json.loads(data)
     active_case = parse_json['count']
     print(Yellow,bold,f"The user you had searched: {user} has", active_case, "messages",clear)
     time.sleep(2)
     print("Would you like to continue with s2pyStats?")
     commander = str(input("\n> "))
     loading = "false"
    except:
     clearconsole()
     print(bold,Yellow,"s2pyStats:",bold,Red,"Error getting data, try connecting to the internet", clear)
     print("Would you like to continue with s2pyStats?")
     commander = str(input("\n> "))
     if commander == "no":
        print("Thanks for using!")
        os.system('exit')
def getFollowers(user,url,headers):
    loading = "true"
    print(Green,bold,"Loading, Please wait...",clear)
    try:
     response = requests.get(url, headers=headers)
     data = response
     parse_json = json.loads(data)
     active_case = parse_json['followers']
     print(Yellow,bold,f"The user you had searched: {user} has", active_case, "followers",clear)
     time.sleep(2)
     print("Would you like to continue with s2pyStats?")
     commander = str(input("\n> "))
     loading = "false"
    except:
     clearconsole()
     print(bold,Yellow,"s2pyStats:",bold,Red,"Error getting data, try again", clear)
     print("Would you like to continue with s2pyStats?")
     commander = str(input("\n> "))
     if commander == "no":
        print("Thanks for using!")
        os.system('exit')
def s2pyStats():
    while True:
        clearconsole()
        print(bold,Green,"Enter a data name that you want!", clear)
        requester = str(input("\n> "))
        if requester == "messages":
            #Tests
            print("Enter a user to get started!")
            user = str(input("\n> "))
            url = f"https://api.scratch.mit.edu/users/{user}/messages/count"
            headers = {'User-Agent': 'Api get', 'From': 'qipylato@lyricspad.net'}
            getMessages(user,url,headers)
        elif requester == "followers":
         print("Enter a user to get started!")
         user = str(input("\n> "))
         url = f"https://scratchdb.lefty.one/v3/user/info/{user}/"
         headers = {'User-Agent': 'Api get', 'From': 'qipylato@lyricspad.net'}
         getFollowers(user,url,headers)