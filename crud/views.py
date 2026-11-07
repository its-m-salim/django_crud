from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *



def home(request):
    return render(request, 'home.html')


def add_task(request):
    if request.method == "POST":
        Tasks.objects.create(
            title = request.POST["title"],
            caption = request.POST["caption"],
            due_date = request.POST["due_date"]
        )
        return redirect('home')

    return render(request, "add_products.html")