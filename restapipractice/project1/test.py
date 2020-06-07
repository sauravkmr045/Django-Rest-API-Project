import requests
import json
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT ='api/'
URL = BASE_URL+ENDPOINT

def get_data(id= None):
	data ={}
	if id is not None:
		data = {
		'id':id
		}
	resp =requests.get(URL, data= json.dumps(data))
	print(resp.status_code)

	print(resp.json())

#get_data()
#print(URL)

#-------------------------------------------------------------------------------------------------------

def create_entry():
	data ={
		'ename' : 'Roopesh',
		'esal' : 6000,
		'eno' :1400,
		'eaddr': 'Jharkhand'
	}
	resp =requests.post(URL, data= json.dumps(data))
	print(resp.status_code)

	print(resp.json())

create_entry()

#----------------------------------------------------------------------------------------------------------------


def update_entry(id):
	data ={
		'ename' : 'Naveen',
		'id' : id,
		'esal' : 8000,
		'eno' :600,
		'eaddr': 'Gurgaon'
	}
	resp =requests.put(URL, data= json.dumps(data))
	print(resp.status_code)

	print(resp.json())

#update_entry(7)

#---------------------------------------------------------------------------------------------------------


def delete_entry(id):
	data ={
			'id' : id,
		
	}
	resp =requests.delete(URL, data= json.dumps(data))
	print(resp.status_code)

	print(resp.json())

#delete_entry(7)