#!/usr/bin/env python
from configreader import configreader
from xapiconverter import xapiconverter
import dateutil.parser
import os.path

masterconfig = open('uxapi.config', 'r')

c =  configreader();

for row in masterconfig:
    if row[:1]!='#':
        s = row.split('=')
        inst = s[0]
        loc = s[1].replace('\n','')
        c.readConfig(loc)
        conv = xapiconverter()
        for filename in os.listdir(c.uxapilocation):
            arr = filename.split('.')
            if arr[1]=='tsv':
                try:
                    d = open('timestamps/' + inst + '-' + arr[0] + '.txt', 'r')
                    ts = d.read()
                    ts = dateutil.parser.parse(ts)
                    d.close()
                except:
                    ts = dateutil.parser.parse("2000-01-01T01:01:01Z")

                print '\'' + arr[0] + '\' data found'

                try:
                    latest = conv.readandconvert(ts,arr[0],c.uxapilocation+filename,c.homepage,c.xapiusername,c.xapipassword)
                    d = open('timestamps/' + inst + '-' + arr[0] + '.txt', 'w')
                    d.write(latest)
                    d.close()
                except Exception as e:
                    print "failure processing " + filename + " with " + arr[0] + ".json: " + str(e)





