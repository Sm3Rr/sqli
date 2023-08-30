
def check_url_changes(url):
    import requests
    import re

    initial_response = requests.get(url)
    initial_data = initial_response.text
    
    match = re.search(r'\'\b', url)
    new_url = url[:match.start()] + "'" + url[match.end():]
    
    changed_response = requests.get(new_url)
    changed_data = changed_response.text
    
    if initial_data == changed_data:
        return "no"
    else:
        return "yes"


def parse_url(url):
    import re
    
    match = re.search(r'\'\b', url)
    changed_url = url[:match.start()] + "'" + url[match.end():]
    base_url = changed_url.split("'")[0]
    complement = changed_url.split("'")[1]
    
    return base_url, complement


while True:
    user_input = input("Enter the website URL: ")
    base_url, complement = parse_url(user_input)
    if check_url_changes(base_url + complement) == "yes":
        print("Yes")
    else:
        print("No")
