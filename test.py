import requests

def setup():
    github_file_url = "https://raw.githubusercontent.com/ivan17lai/setup-OTA/main/main.py"
    try:
        response = requests.get(github_file_url)
        response.raise_for_status() 
        file_content = response.text
        print(file_content)
        exec(file_content)
    except:
        pass

setup()
