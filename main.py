import json
import pymysql
import urllib
import boto3
from decimal import *
from datetime import datetime
from ScoreCalculator import Calculate
from TimeInMeasurement import TimeMeasurement
from TimeInMeasurement import TimeSeries
from TimeInMeasurement import Pressure

with open('config.json') as f:
  config = json.load(f)

conn = pymysql.connect(host='test1.ce8cn9mhhgds.us-east-1.rds.amazonaws.com', user='Wallen', passwd='MyRDSdb1', db='whattodo')
myCursor = conn.cursor()


locationsArr = ['Galveston','Conroe','Freeport','Corpus Christi']

for loc in locationsArr:

  myCursor.execute("""SELECT * FROM WeatherCondition WHERE Location = (%s)""", (loc))
  tplConditions = myCursor.fetchall()
  
  endDex = len(tplConditions) - 24

  j = 8 #increments us through each time series, in a single time series there are 8 elements to consider
  i = 0 #meant to increment through each record
  #this jumps to the next entire time series
  while i < len(tplConditions):
    timSeries = TimeSeries()
    pressureSeries = Pressure()
    
    #Allows to access a specific element in timeseries... like 1 for pressure.. not used now
    innerCounter = 0
    
    #this loop adds each element in a given time series
    while i < j:
      tim = TimeMeasurement(tplConditions[i][0], tplConditions[i][1], tplConditions[i][2],
                            tplConditions[i][3], tplConditions[i][4], tplConditions[i][5],
                            tplConditions[i][6], tplConditions[i][7], tplConditions[i][8],
                            tplConditions[i][9], tplConditions[i][10], tplConditions[i][11],
                            tplConditions[i][12], tplConditions[i][13])
  
      timSeries.addTimeMeasure(tim)
      i = i + 1
  
    p = j+1 #used to access the next pressure reading, and the next two after that
    innerCounter = 0
    while (p < (j + 24)):
      if (j > endDex): #still won't really work because needs to end at the end for each location
        break
  
      pressuretim = TimeMeasurement(tplConditions[p][0], tplConditions[p][1], tplConditions[p][2],
                            tplConditions[p][3], tplConditions[p][4], tplConditions[p][5],
                            tplConditions[p][6], tplConditions[p][7], tplConditions[p][8],
                            tplConditions[p][9], tplConditions[p][10], tplConditions[p][11],
                            tplConditions[p][12], tplConditions[p][13])
      
      innerCounter = innerCounter + 1
  
      pressureSeries.addPressure(pressuretim)
      p = p + 8
  
    calculator = Calculate(timSeries, pressureSeries)
    calculator.evalTimeSet()
  
    j = j + 8
  


