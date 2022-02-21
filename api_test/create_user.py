import json
import requests


data = open("api_test/data.json", "r").read()

response = requests.post("https://reqres.in/api/users", data=json.loads(data))

print(response)
print(response.json())
print(response.headers.get("Content-Type"))

assert response.json()['job']=="automation", "job must be automation"