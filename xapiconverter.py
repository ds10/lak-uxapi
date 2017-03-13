import os
import json
import requests
import base64
import dateutil.parser
import datetime
import pytz

class xapiconverter:

    ok = False

    modvlemap = []



    def postStatement(self,statement,xapiusername,xapipassword):

        url = 'https://jiscv2.learninglocker.net/v1/data/xAPI/statements'
        print xapiusername
        print xapipassword
        base64string = base64.encodestring('%s:%s' % (xapiusername, xapipassword)).replace('\n', '')
        headers = {'content-type': 'application/json', 'Authorization': 'Basic ' + base64string,
                   'X-Experience-API-Version': '1.0.0'}
        print 'sending to LRW'
        response = requests.post(url, statement, headers=headers)
        print response.status_code
        print response.text
        print statement
        print 'done'

    def getModVlEMap(self,uddusername,uddpassword):

        baseURL = 'https://jiscv2.learninglocker.net/api/jisc/v1.2.5'
        url = baseURL + '/modulevlemap'
        base64string = base64.encodestring('%s:%s' % (uddusername, uddpassword)).replace('\n', '')
        headers = {'content-type': 'application/json', 'Authorization': 'Basic ' + base64string}
        response = requests.get(url, headers=headers)

        self.modvlemap = json.loads(response.text)
        return 1

    def readandconvert(self,lasttimedone,type,filelocation,homepage,xapiusername,xapipassword):

        newest = lasttimedone

        now = datetime.datetime.now()
        ok =False
        f = open(filelocation, 'r')
        rowcount = 0
        headerarr = []
        actitems = []

        self.getModVlEMap(xapiusername,xapipassword)

        templatefilename = 'templates/'+type+'.json'

        template = open(templatefilename,'r').read()

        for row in f:
            row = row.replace('\n',"")
            row = row.replace('"','')
            if rowcount==0:
                headerarr = row.split('\t')
            else:
                arr = row.split('\t')
                count = 0
                obj ={}
                for item in arr:
                    obj[headerarr[count]]=item
                    count = count +1
                statement = template
                statement = statement.replace('**HOMEPAGE**', homepage)

                for key, value in obj.iteritems():
                        if key == 'ACTIVITY_ATTENDED':
                            if value=='1':
                                statement = statement.replace('**COMPLETITION**', 'true')
                            else:
                                statement = statement.replace('**COMPLETITION**', 'false')
                        statement = statement.replace('**' + key + '**', value)
                        statement = statement.replace('**' + key + '**', value)


                xapi = json.loads(statement)
                if 'timestamp' in xapi:
                    xapiTSString = xapi['timestamp'] +'+00:00'
                    xapiTS = dateutil.parser.parse(xapiTSString)
                else:
                    xapiTS = pytz.utc.localize(datetime.datetime.fromtimestamp(os.path.getmtime(filelocation)))

                if xapiTS.tzinfo is None:
                    xapiTS = pytz.utc.localize(xapiTS)
                if newest.tzinfo is None:
                    newest = pytz.utc.localize(newest)
                if lasttimedone.tzinfo is None:
                    lasttimedone = pytz.utc.localize(lasttimedone)

                if xapiTS < pytz.utc.localize(now):

                    if xapiTS> newest:
                        newest=xapiTS

                    print lasttimedone
                    if xapiTS > lasttimedone:
                        tsString = xapiTS.strftime("%Y-%m-%dT%H:%M:%S.000Z")
                        xapi['timestamp'] = tsString
                        statement = json.dumps(xapi)
                        print statement
                        self.postStatement(statement,xapiusername,xapipassword)
                    else:
                        print 'already done'

            rowcount = rowcount + 1

        return newest.strftime("%Y-%m-%dT%H:%M:%S.000Z")







