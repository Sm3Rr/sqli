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
        
        
url = input(" < EnTeR ThE SitE UrL ~> ")
check_changes(url)
