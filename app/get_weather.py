import urllib2, urllib, json


# COMPILE QUERY

baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = "select wind from weather.forecast where woeid=2460286"
yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"

# ISSUE REQUEST

result = urllib2.urlopen(yql_url).read()
data = json.loads(result)
print data['query']['results']



# select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="new haven, ct")
