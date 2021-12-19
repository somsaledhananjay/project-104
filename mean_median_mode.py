import csv

with open('SOCR-HeightWEIGHT.csv', newline='') as fileObject:
    reader = csv.reader(fileObject)
    file_data = list(reader)

#To remove headers from CSV
file_data.pop(0)

total_weight = 0    
total_number = len(file_data)

for weight in file_data:
    total_weight += float(weight[1])

mean = total_weight / total_number
print("Mean (Average) is -> "+str(mean))

