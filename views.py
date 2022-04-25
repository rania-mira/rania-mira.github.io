from django.http import HttpResponse
def home(request):
    return HttpResponse('<h1 style='text-align:center'>website django</h1>')