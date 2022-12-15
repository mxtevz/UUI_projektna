import csv
import numpy as np
data = open("UUI_projektna\clustered.csv")
csvreader = csv.reader(data)
header = []
header = next(csvreader)

rows = []
for row in csvreader:
   rows.append(row)

rows_np = np.array(rows)

def average_rgb(cluster, array):
   cluster_array = []
   for row in array:
      if(row[-1] == cluster):
         cluster_array.append(row)
   cluster_array = np.array(cluster_array)
   cluster_array = np.delete(cluster_array, 3, axis=1)
   cluster_array = cluster_array.astype(np.float64)
   return cluster_array.mean(axis=0).astype(int)

print(average_rgb("C1", rows))
print(average_rgb("C2", rows))
print(average_rgb("C3", rows))
print(average_rgb("C4", rows))
print(average_rgb("C5", rows))
print(average_rgb("C6", rows))
print(average_rgb("C7", rows))
print(average_rgb("C8", rows))
print(average_rgb("C9", rows))
print(average_rgb("C10", rows))
data.close()