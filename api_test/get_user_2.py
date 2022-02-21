import requests

p = {"page":2}
response = requests.get("https://reqres.in/api/users", params=p)

print(response.url)
json_response = response.json()
print(json_response['total_pages'])

print(json_response['data'][0]['email'])

assert json_response['total_pages'] ==2, "Page count did not match"
assert (json_response['data'][0]['email']).endswith("reqres.in"), "Email domain is not matching"
