# Part. 1

#=======================================

# Import module

#  csv -- fileIO operation

import csv

#=======================================


# Part. 2

#=======================================

# Read cwb weather data

cwb_filename = '106061139.csv'

data = []

header = []

with open(cwb_filename) as csvfile:

   mycsv = csv.DictReader(csvfile)

   header = mycsv.fieldnames

   for row in mycsv:

      data.append(row)

#=======================================


# Part. 3

#=======================================

# Analyze data depend on your group and store it to target_data like:

# Retrive all data points which station id is "C0X260" as a list.

# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))


# Retrive ten data points from the beginning.

for v in data[:]:
    if v['WDSD']=='-99.000' or v['WDSD']=='-999.000':
        data.remove(v)
        
ids=['C0A880','C0F9A0','C0G640','C0R190','C0X260']
target_data=[]
for i in range(len(ids)):
    list1=[v for v in data if v['station_id'] == ids[i]]
    if len(list1)==0 or len(list1)==1:
        list1=[ids[i],'None']
    else:
        Max=max(list1, key=lambda x: x['WDSD'])
        Min=min(list1, key=lambda x: x['WDSD'])
        list1=[ids[i],abs(float(Max['WDSD'])-float(Min['WDSD']))]
    target_data.append(list1)

#=======================================


# Part. 4

#=======================================

# Print result

print(target_data)

#========================================
