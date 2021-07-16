from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def customer_page(request):
    return render(request, 'customer_page.html')

def courier_page(request):
    return render(request, 'courier_page.html')