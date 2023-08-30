print ('''
	          //////////////
	          | SqLi  BuG |/
	          |-----------|/
	          |  checker  |/ 
	          |___________|/
>------------------------------------------------->
Version 1.0.0 (sqli bug checker)
                        C0d3d by SecurityFucker
├─────────────────────────────────────────┤
│                How To Use:              │
│         [1] First Enter Target Url      │
│         [2] Make sure it have parameter │
│         [3] Now u Can Find Out !        │
├─────────────────────────────────────────┤
│ Link: https://github.com/Sm3Rr/sqli        │
└─────────────────────────────────────┘''')
import requests

def check_changes(url):
    original_url = url
    modified_url = url + "'"
    
    original_response = requests.get(original_url)
    modified_response = requests.get(modified_url)
    
    if original_response.text == modified_response.text:
        print(" !SITE DONT HAVE SQLI BUG! ")
    else:
        print(" !SITE HAVE SQLI BUG! ")
        
print("                               ")     
url = input(" < EnTeR ThE SitE UrL ~> ")
check_changes(url)
