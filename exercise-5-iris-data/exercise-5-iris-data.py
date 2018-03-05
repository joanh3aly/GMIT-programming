'''
Joan Healy - Exercise 5
Parse CSV data
5/3/18
'''


with open('data/iris.data.csv', 'r') as f:
  for line in f:
    row = line.split(',')[0:4]
    row = list(map(float, row))
    print('{:.1f} {:.1f} {:.1f} {:.1f}'.format(row[0],row[1],row[2],row[3]))

