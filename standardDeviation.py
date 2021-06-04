import csv
import plotly_express as px
import pandas as pd
import math 

with open("randomnum",newline="") as f:
    reader=csv.reader(f)
    fileData = list(reader)

fileData.pop(0)

totalnum = 0
totalEntries = len(fileData)
for marks in fileData:
    totalnum=totalnum+float(marks[1])

mean = totalnum/totalEntries  

print(mean)

df = pd.read_csv("randomnum")

fig = px.scatter(df,x="Student Number",y="Marks")
fig.update_layout(shapes=[dict(type="line",y0=mean,y1=mean,x0=0,x1=totalEntries)])
#fig.show()
#print(fileData)
squaredList = []
for number in fileData:
    a=int(number[1])-mean
    a = a**2
    squaredList.append(a)



sum = 0
for i in squaredList:
    sum = sum+i

result = sum/totalEntries

std_dev = math.sqrt(result)

print(std_dev)