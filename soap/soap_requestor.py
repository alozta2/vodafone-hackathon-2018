from soap import account_service

def testAccountService():
	msisdnTrue = 'msisdnTrue'
	msisdnFalse = 'msisdnFalse'
	print('Msisdn ' + msisdnTrue + ' has any package: ' + str(account_service.getCustomerInfo(msisdnTrue)))
	print('Msisdn ' + msisdnFalse + ' has any package: ' + str(account_service.getCustomerInfo(msisdnFalse)))

if __name__ == "__main__":
	testAccountService()