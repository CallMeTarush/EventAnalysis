import csv
from datetime import datetime

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

track_attempts = {}
correct_track_attempts = {}

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

        if(row['track']):
            track = row['track']
        else:
            continue

        day = int(row['timestamp'][8] + row['timestamp'][9])
        year = int(row['timestamp'][11] + row['timestamp'][12] + row['timestamp'][13] + row['timestamp'][14])
        month = row['timestamp'][4] + row['timestamp'][5] + row['timestamp'][6]

        key = track

        if(key in track_attempts.keys()):
            track_attempts[key] = track_attempts[key] + 1
        else:
            track_attempts[key] = 1

        if(correct):
            if(key in correct_track_attempts.keys()):
                correct_track_attempts[key] = correct_track_attempts[key] + 1
            else:
                correct_track_attempts[key] = 1

# Plotting
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Bar(
        x=track_attempts.keys(),
        y=track_attempts.values(),
        name="Number of Attempts"
    ),
    go.Bar(
        x=correct_track_attempts.keys(),
        y=correct_track_attempts.values(),
        name="Correct Attempts"
    )
]

py.plot(data, filename='riddlerAttemptsPerCategory')