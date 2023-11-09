from django.shortcuts import render

def Homepage(request):
    return render(request, 'animals/homepage.html')
