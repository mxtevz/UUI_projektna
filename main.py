import csv
import numpy as np
data = open("clustered.csv")
csvreader = csv.reader(data)
header = []
header = next(csvreader)

rows = []
for row in csvreader:
   rows.append(row)

rows_np = np.array(rows)
avg_r = 0
avg_g = 0
avg_b = 0

print(rows_np)
data.close()