import urllib, json
import pprint
import urllib.parse
import urllib.request
from pprint import pprint as pp
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

rt=[]
p=''
pbdate={}
date=[]
ddata=[]
def powerTest():
    fc = urllib.request.urlopen("http://www.powerball.com/powerball/winnums-text.txt").readlines()
    ''' for i in fc:
        rt.append(str(i[:44])) '''
    for ht in fc:
        ddata.append(ht[0:37])
        #pp(ht[2:36])
        #date.append(str(ht[2:10]))
    s = str(ddata[1])
    for j in ddata:
        pbdate[str(j[0:10])] = j[15:999]
    pb
    pp(pbdate.keys())    
    #pp(s[15:999])


powerTest()