from django.shortcuts import render

def index(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'pages/about.html')

def catalogy(request):
    return render(request, 'pages/catalogy.html')

def resource(request):
    return render(request, 'pages/resource.html')

def contact(request):
    return render(request, 'pages/contact.html')