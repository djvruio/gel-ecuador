from django.shortcuts import render
from .models import Event, Category, Sponsor, Tema

# Create your views here.

def index(request):
	events = Event.objects.all().order_by('-created')[:10]
	categories = Category.objects.all()
	sponsors = Sponsor.objects.all()
	temas = Tema.objects.all()
	return render(request, 'events/index2.html', {'events':events,
		 'categories':categories, 'sponsors': sponsors, 'temas': temas })