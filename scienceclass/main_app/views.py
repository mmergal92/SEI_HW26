from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import scienceclass

# Create your views here.
class ClassList(ListView):
    model = scienceclass

class ClassCreate(CreateView):
    model = scienceclass
    fields = '__all__'
    success_url = '/class/'

class ClassUpdate(UpdateView):
    model = scienceclass
    fields = ['labs', 'price', 'description']

class ClassDelete(DeleteView):
    model = scienceclass
    success_url = '/class/'

def home(request):
    return HttpResponse('Hello class')

def about(request):
    return render(request, 'about.html')

# def class_index(request):
#     return render(request, 'class/index.html')