from django.shortcuts import render
import requests

# Create your views here.
def get_geographic_info(request):
	ip = request.META.get('HTTP_X_FORWARDED_FOR',"") or request.META.get('REMOTE_ADDR')
	url ='http://api.ipstack.com/'+str(ip)+'?access_key=b5683afa5cc7e1c9b64e5b42c9f5b6a5'

	#key = 'b5683afa5cc7e1c9b64e5b42c9f5b6a5'
	response = requests.get(url)
	data = response.json()
	return render(request,'info.html',{'data':data})