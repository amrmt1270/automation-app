import requests

url = 'https://api.aoikujira.com/time/get.php'
result = requests.get(url)

print(result.text)