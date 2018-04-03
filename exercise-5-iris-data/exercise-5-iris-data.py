'''
Joan Healy - Exercise 5
Parse CSV data
5/3/18
'''

# Open csv file, loop through rows
with open('data/iris.data.csv', 'r') as f:
  for line in f:
    # split first 4 columns into separate lists at ',' 
    row = line.split(',')[0:4]
    # convert every item in row from a string to a float using map(), then convert back into a list. The map function works perfectly yet throws an erron in Python 3 as it has been deprecated.
    row = list(map(float, row))
    # print rows in the specific order outlined in the brief
    print('{:.1f} {:.1f} {:.1f} {:.1f}'.format(row[2],row[3],row[0],row[1]))

