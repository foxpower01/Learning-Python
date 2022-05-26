import matplotlib.pyplot as plt
import utils

def simple_bar_chart(xaxis, yaxis, label):
  fig, axes = plt.subplots()
  axes.bar(xaxis, yaxis, label=label, color="#06145F")
  axes.ticklabel_format(style='plain', useOffset=False, axis='y')
  axes.legend()
  plt.show()


def hoursOfGames():
  data = utils.getdata("data-project-final-cspahs-29/exercise.csv")
  col = utils.extractcolumn(data, 10)
  uniqs = utils.getuniques(col)
  counts = utils.handleuniquevalues(col, uniqs)
  labels = []
  for uniq in uniqs:
    if uniq == 'I do not play video or computer games or use a computer for something that is not school work':
      labels.append("0 Hours")
    elif uniq == '5 or more hours per day':
      labels.append('5+ hours per day')
    else:
      labels.append(uniq)
  simple_bar_chart(labels, counts, "Hours of Video Games Per Day")

