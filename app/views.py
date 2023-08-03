from django.shortcuts import render

# Create your views here.
def msd(request):
    return render(request, 'msd.html')

def kohli(request):
    return render(request, 'kohli.html')