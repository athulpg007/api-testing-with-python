import requests

response = requests.get("https://the-internet.herokuapp.com/basic-auth", auth=('asda', 'pass'))

print(response.status_code)