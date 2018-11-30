import requests
import re   #regular expression

url="url"
#headers = {'content-type': 'application/soap+xml'}
headers = {'content-type': 'text/xml;charset=UTF-8'}

def getCustomerInfo(msisdn):
	soapBody = """SOAP REQUEST"""

	response = requests.post(url, data=soapBody, headers=headers)

	errorCode = int(re.search('row', response.content.decode('utf-8')).group(1))
	if(errorCode != 0):
		#return 'Customer was not found!'
		return False
	else:
		package = re.search('row', response.content.decode('utf-8')).group(1)
		hasPackage = True if len(package) > 0 else False
		return hasPackage

print(getCustomerInfo('msisdn'))