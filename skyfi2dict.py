#/usr/bin/python
import urllib2
import json
import urlparse
import config

url = "http://" + config.skyfiIpaddress + ":2000/ac.cgi?pass=" + config.skyfiPassword

print "please wait connecting to your Skyfi system"
urldata = urllib2.Request(url)

try:
	resp = urllib2.urlopen(urldata)
except urllib2.HTTPError as e:
	if e.code == 404:
		print 'http 400 response - something wrong'
	else:
		urllib2.urlopen(urldata)
		print '1st else'
except urllib2.URLError as e:
		print 'Not an HTTP-specific error (e.g. connection refused)'
else:
	# 200
	# need away to check that returned data isn't blank
	strs = resp.read() #reads the HTML body response from the urllib2.urlopen
	data = dict(urlparse.parse_qsl(strs)) # takes the HTML body that converts a query string key1=values&key2=value etc into a dictionary
	for key, value in data.iteritems():
		print "The key value is: " + key + " and the value is" , value
	print "The current temperature is: " + data["roomtemp"] + " degrees"
	print 'http 200 response - all good'
