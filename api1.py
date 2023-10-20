import requests

#x = requests.get('http://google.com')
x = requests.get("http://20.198.72.70:9009/api/sync")

print(x.status_code)
print(x.json())
