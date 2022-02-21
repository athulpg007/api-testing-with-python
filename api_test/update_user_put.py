import requests
import json

payload = {
    "name" : "athul",
}

response = requests.patch("https://reqres.in/api/users/2", data=payload)

print(response.json())
