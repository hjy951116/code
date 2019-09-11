import csv
with open('./3/frame.csv','rb') as csvfile:
  reader = csv.reader(csvfile)
  column= [row[0] for row in reader]
print(column)