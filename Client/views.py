from django.shortcuts import render

def Home(request):
    context = {}
    return render(request, "base.html", context)