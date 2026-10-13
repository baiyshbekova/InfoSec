import requests

with open("log.txt", "r") as file:
    test_data = file.read()

response = requests.post(
    "http://127.0.0.1:8000/logs",
    json={"data": test_data},
    timeout=5
)

print(response.status_code)
print(response.text)
