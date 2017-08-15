import requests
url = "http://api.open-notify.org/iss-now.json"

r = requests.get(url)
j = r.json()

 #type this into shell to run it 
f = open ['dtLatLong.txt', 'w']
f.write ("Timestamp \t Longitude \t Latitude")
for i in range (1,10):
    f.write (j['iss_position'](['timestamp'] + "\t" + ['longitude'] + "\t" + ['latitude']))
    time.sleep(10)
f.close()   
