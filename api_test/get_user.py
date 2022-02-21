import requests

response = requests.get("https://reqres.in/api/users?page=2")

code = response.status_code
text = response.text
content = response.content
json_response = response.json()
headers = response.headers

assert code==200, "Status Code != 200"

#print(text)
#print(content)
#print(headers)
#print(response.cookies)