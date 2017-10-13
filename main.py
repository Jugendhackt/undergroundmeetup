from numpy import genfromtxt

data = genfromtxt('data.csv', delimiter=',')
print(data.shape)
print(data)
