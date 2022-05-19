# open the data file and reads the data creating
# a table to be returned 
def getdata(file_path):
  file = open(file_path)
  data = []
  for line in file:
    data.append(line.strip().split(","))
  return data

# return the column of values from the data table
def extractcolumn(data, colNum):
  values = []
  for line in data:
    values.append(line[colNum])
  return values

# return the one of every unique value in column
def getuniques(column):
  uniqs = []
  for item in column[1:]:
    if not item in uniqs and item != '':
      uniqs.append(item)
  return uniqs

# returns how many times value is in column
# used by the handleuniquevalues function below
def getcountofunique(column, value):
  count = 0
  for item in column[1:]:
    if item == value:
      count += 1
  return count

# This traverses the uniqs list and return a list of how
# many of each unique value in uniqs exists in the column
def handleuniquevalues(column, uniqs):
  counts = []
  for possible in uniqs:
      counts.append(getcountofunique(column,possible))
  return counts