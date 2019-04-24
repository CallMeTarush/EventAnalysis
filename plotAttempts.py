import csv
from datetime import datetime

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

dates = {}
days = {}
correct_dates = {}

# Preprocessing
with open('attempts.csv') as csvfile:
    csvReader = csv.DictReader(csvfile)
    c = 0
    for row in csvReader:
        
        c = c+1
        hour = int(row['timestamp'][16] + row['timestamp'][17])
        if(c==1):
            if( int(row['timestamp'][19]) >= 3 ):
                hour = hour + 1
        
        if(row['correct'] == 'false' ):
            correct = False
        else:
            correct = True

        day = int(row['timestamp'][8] + row['timestamp'][9])
        year = int(row['timestamp'][11] + row['timestamp'][12] + row['timestamp'][13] + row['timestamp'][14])
        month = row['timestamp'][4] + row['timestamp'][5] + row['timestamp'][6]

        day_of_reg = datetime(2019,2,day).weekday()
        day_of_reg = weekdays[day_of_reg]
        
        # Re-evaluating my life for writing this
        if(day == 23):
            key = str(day) + "rd " + str(hour).zfill(2) + "00"
        else:
            key = str(day) + "th " + str(hour).zfill(2) + "00"

        if(key in dates.keys()):
            dates[key] = dates[key] + 1
        else:
            dates[key] = 1
        
        if(correct):
            if(key in correct_dates.keys()):
                correct_dates[key] = correct_dates[key] + 1
            else:
                correct_dates[key] = 1
            
# Plotting
import plotly.plotly as py
import plotly.graph_objs as go

sorted_keys = dates.keys()
sorted_keys.sort()
sorted_values = []
for i in sorted_keys:
    sorted_values.append(dates[i])

trace0 = go.Scatter(
    x = sorted_keys,
    y = sorted_values,
    name = 'Riddler Attempts',
    line = dict(
        color = ('rgb(78, 66, 255)'),
        width = 4)
)

sorted_keys = correct_dates.keys()
sorted_keys.sort()
sorted_values = []
for i in sorted_keys:
    sorted_values.append(correct_dates[i])

trace1 = go.Scatter(
    x = sorted_keys,
    y = sorted_values,
    name = 'Riddler Correct Attempts',
    line = dict(
        color = ('rgb(65, 255, 106)'),
        width = 4)
)

data = [trace0, trace1]
py.plot(data, filename='riddlerAttemptsPlot')
