from django.shortcuts import render_to_response

def home(request):
	'''a view to display the homepage'''
	return render_to_response('index.html')

def search(request):
	pass
