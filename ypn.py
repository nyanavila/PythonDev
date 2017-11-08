import urllib, json
import pprint
import urllib.parse
import urllib.request
from pprint import pprint as pp
baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = "select * from local.search where query='sushi' and location='nashville, tn'"
yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
result = urllib.request.urlopen(yql_url).read()
data = json.loads(result)
#print(data['query']['results'])
f1 = data['query']
f2= f1['results']
f3=f2['Result']
for i in f3:
    pp(str(i['Title']))


''' d1 = (data['query']['results'])

for i in d1['Result']:
    pp(str("Get your sushi at "+i['Title'] + ", Locate at "+i['Address']+", "+i['City']+", "+i['State']+" Phone #: "+i['Phone']))  '''
rt=[]
def powerTest():
    fc = urllib.request.urlopen("http://www.powerball.com/powerball/winnums-text.txt").readlines()
    for fr in fc:
        rt.append(str(fr))
    pp(rt[0:1])
powerTest()