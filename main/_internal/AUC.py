import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp

def str_to_func(function):
  def func(x):
    return eval(function)
  return func

def trapezoidal_rule(f, a, b, n):
  func = str_to_func(f)
  h = (b - a) / n
  x = np.linspace(a, b, n + 1)
  y = func(x)
  result = (h/2)*(y[0] + 2*np.sum(y[1:-1]) + y[-1])
  graphCreator(x,y)
  return result

def graphCreator(x, y):
  a=[]
  a.append(0)
  for i in range(len(x)):
    a.append(x[i])
  a.append(max(x)+1)
  b=[]
  b.append(0)
  for i in range(len(y)):
    b.append(y[i])
  b.append(max(y)+1)
  plt.plot(a, b)
  plt.fill_between(x, y, color='lightblue', alpha=0.5)
  plt.show()

