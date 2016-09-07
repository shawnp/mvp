from django.shortcuts import render



def home(request):
    context = {}
    template = "home.html"
    return render(request, template, context)

def page(request):
    context = {}
    template = "page.html"
    return render(request, template, context)
