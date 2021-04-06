from django.http import HttpResponse


def pro1(request):
    return HttpResponse('<h1>Hello Python</h1>')
    