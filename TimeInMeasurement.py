class TimeMeasurement:
    def __init__(self, i_d, name, description, evaluationtype, latitude, longitude, state, location, conditiondatetime, timeframe, currentstatus,
                 lastupdate, locationid, timegroupid):
        self._id = i_d
        self._name = name
        self._description = description
        self._evaluationtype = evaluationtype
        self._latitude = latitude
        self._longitude = longitude
        self._state = state
        self._location = location
        self._conditiondatetime = conditiondatetime
        self._timeframe = timeframe
        self._currentstatus = currentstatus
        self._lastupdate = lastupdate
        self._locationid = locationid
        self._timegroupid = timegroupid
        
class TimeSeries:
    def __init__(self):
        self.timemeasurements = []
        
    def addTimeMeasure(self, timemeasurement):
        self.timemeasurements.append(timemeasurement)
        
class Pressure:
    def __init__(self):
        self.pressures = []
        
    def addPressure(self, pressureMeasure):
        self.pressures.append(pressureMeasure)
   