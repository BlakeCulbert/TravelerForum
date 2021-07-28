from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

def home(request):
	context = {
		'posts': Posts.objects.all()
	}
	return render(request, 'travelblog/home.html', context)

def about(request):
	return render(request, 'travelblog/about.html', {'title': 'About'})

def continents(request):
	return render(request, 'travelblog/continents.html', {'title': 'Regions'})

def africa(request):
	return render(request, 'travelblog/africacountries.html', {'title': 'Africa'})

def asia(request):
	return render(request, 'travelblog/asiacountries.html', {'title': 'Asia'})

def oceania(request):
	return render(request, 'travelblog/oceaniacountries.html', {'title': 'Oceania'})

def centralamerica(request):
	return render(request, 'travelblog/centralamericacountries.html', {'title': 'Central America'})

def europe(request):
	return render(request, 'travelblog/europecountries.html', {'title': 'Europe '})

def middleeast(request):
	return render(request, 'travelblog/middleeastcountries.html', {'title': 'Middle East'})

def northamerica(request):
	return render(request, 'travelblog/northamericacountries.html', {'title': 'North America'})

def southamerica(request):
	return render(request, 'travelblog/southamericacountries.html', {'title': 'South America'})