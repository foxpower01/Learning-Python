import matplotlib.pyplot as plt
import json
import urllib.request

url = "https://api.covidtracking.com/v1/us/daily.json"

def readdata():
  uh = urllib.request.urlopen(url)
  str_data = uh.read()
  return json.loads(str_data)

print(readdata()[1])

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

plt.show()