from TimeInMeasurement import TimeMeasurement

class Calculate:
    def __init__(self, timeSeries, pressureSeries):
        self._timeSeries = timeSeries
        self._pressureSeries = pressureSeries
      
    
    _tempWeight = 7
    _pressureWeight = 5
    _humidityWeight = 2
    _weatherDescWeight = 10
    _cloudWeight = 4
    _windSpeed = 8
    _windDirection = 9
    _rain = 6
    
    _tempIdeal = 75
    
    
    
    #def evalTimeSet - this should evaluate each of the elements here and
    #then provide one main score from the element value and weight
    
    def evalTimeSet(self):
        tempScore = self._tempWeight * self.evalTemp()
        #print("tempScore:" + str(tempScore))
        weatherDescrip = self._weatherDescWeight * self.evalWeatherDescrip()
        self.evalPressure()
    
    def evalTemp(self):
        temp = float(self._timeSeries.timemeasurements[0]._currentstatus) - self._tempIdeal
        distanceAbs = abs(temp)
        if (distanceAbs < 10):
            return 10
        elif (distanceAbs < 15):
            return 9
        elif (distanceAbs < 20):
            return 8
        elif (distanceAbs < 25):
            return 5
        else:
            return 1
        
    def evalWeatherDescrip(self):
        descrip = self._timeSeries.timemeasurements[3]._currentstatus
        if (descrip == 'Rain'):
            return 2
        elif (descrip == 'Clear'):
            return 8
        elif (descrip == 'Clouds'):
            return 10
    
    #our pressure is in hpa
    def evalPressure(self):
        print(len(self._pressureSeries.pressures))
        
        if (len(self._pressureSeries.pressures) == 0):
            return
            
        #print(self._pressureSeries.pressures[0].currentstatus)
        print(self._pressureSeries.pressures[0]._currentstatus + ": " + self._pressureSeries.pressures[0]._timeframe)
        print(self._pressureSeries.pressures[1]._currentstatus + ": " + self._pressureSeries.pressures[1]._timeframe)
        print(self._pressureSeries.pressures[2]._currentstatus + ": " + self._pressureSeries.pressures[2]._timeframe)

            
    #high hpa is above 1013?
    #also need to adjust for sea level?
    
    """
    ---This honestly probably means we should somehow know the pressure of the times before???
    High Pressure (30.50 +/Clear Skies) - Fish bite Medium to Slow in deeper water or near cover while fishing slowly.
    Medium Pressure (29.70 – 30.40/Fair Weather) - Normal Fishing using different gear or baits to meet the needs of the fish.
    Low Pressure (29.60 and under/Cloudy/Rainy Weather) - Fishing Slows. Go at them slow in deeper water or near cover.
    Rising Pressure/Improving Weather – The fish are slightly active. Go at them slow in deeper water or near cover.
    Stable Pressure/Fair Weather - Normal Fishing. This is the perfect to try different gear or baits.
    Falling Pressure/Degrading Weather - Best Fishing. The fish are likely to take anything they can get!!
    """
    
    
    def evalHumidity(self):
        print("this does absolutely nothing to fish, only enjoyment.. and at that minimal... I will leave it out")
    
    
    def evalClouds(self):
        cloudCount = int(self._timeSeries.timemeasurements[4]._currentstatus)
        
        #could possibly be part of the pressure consideration?... just recreate the pressure class but CloudCount
        
        
        
    #def evalWindSpeed
    #def evalWindDirection
    #def evalRain
    #def evalOverall
        