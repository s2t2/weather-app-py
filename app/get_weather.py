import urllib.parse
import urllib.request
import json
from IPython import embed

#
# COMPILE QUERY
#

baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='new haven, ct')"
yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"

#
# ISSUE REQUEST
#

response = urllib.request.urlopen(yql_url).read()

#
# PARSE RESPONSE
#

raw_response = json.loads(response)
results = raw_response["query"]["results"]["channel"]
weather = results["item"]

# FYI: results["units"] #> {'distance': 'mi', 'pressure': 'in', 'speed': 'mph', 'temperature': 'F'}
print(results["title"]) #> Yahoo! Weather - New Haven, CT, US
print(results["lastBuildDate"]) #> Sat, 22 Jul 2017 07:22 PM EDT
print(results["location"]) #> {'city': 'New Haven', 'country': 'United States', 'region': ' CT'}
print(results["atmosphere"]) #> {'humidity': '61', 'pressure': '1003.0', 'rising': '0', 'visibility': '16.1'}
print(results["wind"]) #> {'chill': '82', 'direction': '190', 'speed': '7'}
print(results["astronomy"]) #> {'sunrise': '5:37 am', 'sunset': '8:19 pm'}



print(weather['title']) #> 'Conditions for New Haven, CT, US at 06:00 PM EDT'
print(weather['pubDate']) #> Sat, 22 Jul 2017 06:00 PM EDT
print(weather['condition']) #> {'code': '26', 'date': 'Sat, 22 Jul 2017 06:00 PM EDT', 'temp': '82', 'text': 'Cloudy'}
#print(weather['forecast']) #> a list of seven days like: {'code': '28', 'date': '22 Jul 2017', 'day': 'Sat', 'high': '85', 'low': '70', 'text': 'Mostly Cloudy'}
