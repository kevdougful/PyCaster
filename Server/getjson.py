from urllib import request
import json

# get the api key
def _get_apikey():
    return open('./api.key').read()

def forecast(location):
    # build up url
    url = 'http://api.wunderground.com/api/'
    url += _get_apikey() + '/forecast/q/' + location + '.json'
    # send http request
    forecast_req = request.urlopen(url)
    # read response
    forecast_res = forecast_req.read()
    # return parsed json
    return json.loads(forecast_res.decode())