import matplotlib.pyplot as plt
import utils

def simple_bar_chart(xaxis, yaxis, label):
  fig, axes = plt.subplots()
  axes.bar(xaxis, yaxis, label=label, color="#06145F")
  axes.ticklabel_format(style='plain', useOffset=False, axis='y')
  axes.legend()
  plt.show()


def days_of_pe():
  data = utils.getdata("data-project-final-cspahs-29/exercise.csv")
  col = utils.extractcolumn(data, 7)
  uniqs = utils.getuniques(col)
  counts = utils.handleuniquevalues(col, uniqs)
  simple_bar_chart(uniqs, counts, "Days of PE")

