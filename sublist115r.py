import requests 
import sys
import pyfiglet
flag = pyfiglet.figlet_format("SUBLIST115R", font = "big")
print(flag)
print("Create By @khaledziadi")
print("Domain :[",sys.argv[1],"]")
sud_list = open("Wordlist/wordlist.txt").read()
subs = sud_list.splitlines()
for sub in subs :
        subdomain = f"http://{sub}.{sys.argv[1]}"
        
        try:
                requests.get(subdomain)
        except requests.ConnectionError:
                pass        
        else :
                print("Valid Domain:",subdomain)
            
