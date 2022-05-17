import matplotlib.pyplot as plt
import json
import urllib.request

url = "https://api.covidtracking.com/v1/us/daily.json"

def readdata():
  uh = urllib.request.urlopen(url)
  str_data = uh.read()
  return json.loads(str_data)

print(readdata()[1]['positive'])
readData = readdata()

plotdata = [[],[]]
for item in readData:
  plotdata[1].append(item['death'])
  plotdata[0].append(item['positive'])

for list in plotdata:
  for item in list:
    print(item)
    if item == None:
      item = 0
    else:
      item = int(item)

bardata = []
names = ['20200329', '20201003', '20210305']
for item in readData:
  if str(item['date']) in names:
    bardata.append(item['positive'])

print(bardata)

plt.figure(figsize=(11, 4))

plt.subplot(131)
plt.bar(names, bardata[::-1])
plt.ylabel("Positives")
plt.xlabel("Dates")
plt.subplot(122)
plt.plot(plotdata[0], plotdata[1])
plt.xlabel("Positives")
plt.ylabel("Deaths")

plt.show()