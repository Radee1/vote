from django.shortcuts import render


def index(request):
    return render(request, 'polls/polls_list.html')


def home(request):
    return render(request, 'home.html')


def handler404(request, exception):
    # Error Handler 404- Page not found
    return render(request, 'notfound.html', status=404)
