from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def item(request):
    return render(request, 'item.html')

def detail(request):
    return render(request, 'detail.html')

def order(request):
    return render(request, 'order.html')
