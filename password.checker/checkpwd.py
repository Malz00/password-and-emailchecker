import urllib.request

url = 'https://api.pwnedpassword.com/range/'+ 'CBFDA'

res = urllib.request.urlopen(url)

print(res.read())


