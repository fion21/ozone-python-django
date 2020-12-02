from django.shortcuts import render

def home (request):
	import json
	import requests

	api_request =requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=96AD20D0-6896-49A1-8FE5-D1B5E2D53EE7")


	try:
		api = json.loads(api_request.content)

	except Exceptoin as e:
		api = "Error..."

	return render(request, 'home.html', {'api' : api})

	





def about (request):
	return render(request, 'about.html', {})
