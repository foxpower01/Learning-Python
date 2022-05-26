import matplotlib.pyplot as plt
import utils

def stacked_bar_chart(xaxis, yaxis1, yaxis2, label1, label2, title):
  plt.bar(xaxis, yaxis1, color='r')
  plt.bar(xaxis, yaxis2, bottom=yaxis1, color='b')
  plt.legend([label1, label2])
  plt.title(title)
  plt.show()

def daysActiveBySex():
  data = utils.getdata("data-project-final-cspahs-29/exercise.csv")
  col_grade = utils.extractcolumn(data, 2)
  grade_uniqs = utils.getuniques(col_grade)
  i = 0
  Mvalues = [0,0,0,0,0]
  Fvalues = [0,0,0,0,0]
  for grade in grade_uniqs:
    for line in data:
      if line[2] == grade and line[3]:
        if line[1] == 'Male':
          Mvalues[i] += int(line[3].split()[0])
        elif line[1] == 'Female':
          Fvalues[i] += int(line[3].split()[0])
    i += 1
  stacked_bar_chart(grade_uniqs, Mvalues, Fvalues, 'Male', 'Female', 'Days Active')
  pass
