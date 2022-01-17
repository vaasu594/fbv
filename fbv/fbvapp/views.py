from django.shortcuts import render
from django.http import HttpResponse

def input_page(request):

    return render(request,'input.html')

def Add(request):

    if request.method=='POST':
        try:
            a=int(request.POST['f'])
            b=int(request.POST['s'])
            z=a+b
            return HttpResponse("sum :"+str(z))
        except ValueError:
            return HttpResponse("invalid input")


# Create your views here.
