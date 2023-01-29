from django.shortcuts import render

def index(request):
    return render(request,'polls/polls_list.html')

def home(request):
    return render(request,'home.html')

