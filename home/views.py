from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

# Create your views here.

def home(request):

    return redirect(reverse('home:home_en'))

def home_en(request):

    return render(request, 'home/home_en.html')

def home_de(request):

   return render(request, 'home/home_de.html')
