from django.shortcuts import render

def home(request):
    context ={}
    return render(request,'home.html',context)


def about(request):
    context ={}
    return render(request,'about.html',context)


def contact(request):
    context ={}
    return render(request,'contact.html',context)