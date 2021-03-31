import requests

response = requests.get("https://track.aftership.com/api/couriers")
response_json = response.json()
print(response_json)

