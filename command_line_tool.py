#!/usr/bin/env python
import optparse
 

def request_body_builder(accountId, name, email, fromTo):

	import json
	import urllib2
	from datetime import datetime

	req = urllib2.Request('https://api.evrythng.com/analytics/executions')
	req.add_header('Content-Type', 'application/json')
	req.add_header('Accept', 'application/json')
	req.add_header('Authorization', MASTER_API_KEY)

	from_to = fromTo.split();

	dates = [x.split('-') for x in fromTo.split()]

	#to_timestamp = lambda y,m,d: datetime(y,m,d).strftime('%s')
	#timestamps = {}
	#timestamps ['from'] = to_timestamp(int(dates[0][0],10),int(dates[0][1],10),int(dates[0][2],10))
	#timestamps ['to'] = to_timestamp(int(dates[1][0],10),int(dates[1][1],10),int(dates[1][2],10))
	#For future purposes
	
	request_body = {
    "report": "Coke:Actions",
    "description": name,
    "requestor": "dshulgin",
    "arguments": {
        "account": accountId,
        "digest": "day",
        "outputType": "email",
        "outputLocation": email,
        "from": from_to[0],
        "to": from_to[1]
    },
    "plan": "now"
	}

	response = urllib2.urlopen(req, json.dumps(request_body)).read()
	return response


        
def main():
	p = optparse.OptionParser()
	p.add_option('--accountId', '-a', default="")
	p.add_option('--name', '-n', default="name")
	p.add_option('--email', '-e', default="dmitry.shulgin@evrythng.com")
	p.add_option('--fromTo', '-t', default="1470614400000 1471219200000")
	options, arguments = p.parse_args()
	print  request_body_builder(options.accountId,options.name,options.email,options.fromTo)





         
if __name__ == '__main__':
   	main()
