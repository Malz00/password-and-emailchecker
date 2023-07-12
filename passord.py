import requests

url = ('https://haveibeenpwned.com//range/' + 'password123')

Res = requests.get(url)

print(Res)

