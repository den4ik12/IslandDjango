from django.shortcuts import render

from webisland.models import Island


def home(request):
    title = "Главная"
    return render(request, 'index.html', {'title': title})


def listIsland(request):
    title = "Список островов"
    listIslands = Island.objects.all()
    return render(request, 'listIsland.html', {'title': title, 'listIsland': listIslands})
