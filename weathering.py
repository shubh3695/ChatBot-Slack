from weather import Weather

'''

@author ssaxena36

'''

class Weathering(object):
    def __init__(self):
        pass

    def getWeather(self, city):
        weather = Weather()
        try:
            location = weather.lookup_by_location(city)
            res = ""
            forecast = location.forecast()
            for forecasts in forecast:
                res += 'Date: ' + forecasts.date() + '\nCondition: ' + forecasts.text() + '\nHigh Temperature (F): ' + \
                    forecasts.high() + '\nLow Temperature (F): ' + forecasts.low() + '\n\n'
            return res
        except:
            return "Some Error Occured."