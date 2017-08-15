import requests
url = "http://api.open-notify.org/iss-now.json"

r = requests.get(url)
j = r.json()
n = j['number'] #number of people
print (n)
print (j)
 #type this into shell to run it
