from django.shortcuts import render

def contacts(request):
    return render(request,'contacts.html')
def home_page(request):
    return render(request,'home.html')
def about_page(request):
    return render(request,'about.html')
def news(request):
    return render(request,'news.html')
# Create your views here.
