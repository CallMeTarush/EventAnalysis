import csv
from datetime import datetime

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

dates = {}
days = {}

# Preprocessing
with open('registrations.csv') as csvfile:
    csvReader = csv.DictReader(csvfile)
    for row in csvReader:
        
        day = int(row['timestamp'][8] + row['timestamp'][9])
        year = int(row['timestamp'][11] + row['timestamp'][12] + row['timestamp'][13] + row['timestamp'][14])
        month = row['timestamp'][4] + row['timestamp'][5] + row['timestamp'][6]

        day_of_reg = datetime(2019,2,day).weekday()
        day_of_reg = weekdays[day_of_reg]

        key = str(day) + "th Feb," + day_of_reg
        if(key in dates.keys()):
            dates[key] = dates[key] + 1
        else:
            dates[key] = 1

# Plotting
import plotly.plotly as py
import plotly.graph_objs as go

sorted_keys = dates.keys()
sorted_keys.sort()
sorted_keys = [sorted_keys[len(sorted_keys) - 1]] + sorted_keys[:len(sorted_keys)-1]
sorted_values = []
for i in sorted_keys:
    sorted_values.append(dates[i])

trace = go.Scatter(
    x = sorted_keys,
    y = sorted_values,
    name = 'Riddler Registrations Plot',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4)
)

data = [trace]
py.plot(data, filename='riddlerRegistrationsPlot')


