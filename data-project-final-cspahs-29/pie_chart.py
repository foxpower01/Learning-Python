import matplotlib.pyplot as plt
import utils

def pie_chart(labels, values, title):
  fig, axes = plt.subplots()
  axes.pie(values, labels=labels)
  axes.axis('equal')
  plt.title(title)
  plt.show()
  print([labels, values])

def hoursOfSleep():
  data = utils.getdata("data-project-final-cspahs-29/exercise.csv")
  col = utils.extractcolumn(data, 4)
  uniqs = utils.getuniques(col)
  counts = utils.handleuniquevalues(col, uniqs)
  pie_chart(uniqs, counts, "Hours of Sleep")
