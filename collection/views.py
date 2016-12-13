from django.shortcuts import render
from collection.models import Thing
# Create your views here.
# def index(request):
# 	#defining a variable
# 	number = 9
# 	thing = "Thing name"
# 	#this is our new def def view
# 	return render(request, 'index.html', {'number':number,})

# def index(request):
# 	number = 6
# 	# Dont forget the quotes because its a string,
# 	# Not an interger
# 	thing = "Thing name"
# 	return render(request, 'index.html',{
# 		'number':number,
# 		#Donot forget to pass it in tand the last comma
# 		'thing':thing,


def index(request):
	things = Thing.objects.all()
	return render(request, "index.html", {
		'things':things,
	})

def thing_detail(request, slug):
	#grab the object...
	thing = Thing.objects.get(slug=slug)


	# and pass to the template 
	return render(request, 'things/thing_detail.html', {
	'thing': thing,
	})