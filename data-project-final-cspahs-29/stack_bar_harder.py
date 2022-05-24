import matplotlib.pyplot as plt
import utils

def stacked_bar_chart(xaxis, yaxis1, yaxis2, label):
  plt.bar(xaxis, yaxis1, color='r', label=label)
  plt.bar(xaxis, yaxis2, bottom=yaxis1, color='b')
  plt.show()

# def getGenderActive(data):
#   values = [0,0]
#   for line in data:
#     if line[1] == 'Male':
#       values[0] += int(split(line[3])[0])
#     else:
#       values[1] += int(split(line[3])[0])
#   return values

def your_function_to_execute():
  data = utils.getdata("data-project-final-cspahs-29/exercise.csv")
  col_grade = utils.extractcolumn(data, 2)
  grade_uniqs = utils.getuniques(col_grade)
  i = 0
  values = []
  for grade in grade_uniqs:
    for line in data:
      if line[2] == grade:
        
    i += 1
  # stacked_bar_chart(....)
  pass
