import usaepay
from usaepay import run_call


def get(data={}):
	"""Calls /transactions
	Gets a list of transactions

	If trankey is included:
	Retrieve a specific transaction.
			return_origin (str) optional
			return_bin (str) optional
			return_fraud (str) optional
			trankey (str) optional
			limit (str) optional
			offset (str) optional
			fuzzy (str) optional
			filters (str) optional

	Returns:
		Dictionary Transaction

	Returns:
		Dictionary TransactionList
	"""
	params={}
	if 'return_origin' in data:
		params['return_origin']=data['return_origin']
	if 'return_bin' in data:
		params['return_bin']=data['return_bin']
	if 'return_fraud' in data:
		params['return_fraud']=data['return_fraud']

	path='/transactions'
	if 'trankey' in data:
		path = path + '/' + data['trankey']
	if 'limit' in data:
		params['limit']=data['limit']
	if 'offset' in data:
		params['offset']=data['offset']
	if 'fuzzy' in data:
		params['fuzzy']=data['fuzzy']
	if 'filters' in data:
		params['filters']=data['filters']

	return run_call('get','json',path,data,params)

def post(data={}):
	"""Calls /transactions
	Run a transaction

	Args:
		data (dict) TransactionRequest

	Returns:
		Dictionary TransactionResponse
	"""
	params={}
	path='/transactions'
	return run_call('post','json',path,data,params)
