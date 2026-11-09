from django.shortcuts import render, redirect
from .models import*
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

def home_page(request):
    return render(request, 'home.html')


def create(request):

    if request.method == "POST":
        if request.POST["caption"] is None or request.POST["caption"].strip() == "":
            caption = None
        else:
            caption = request.POST["caption"] 
        Book.objects.create(
            title = request.POST["title"],
            author = request.POST["author"],
            genre = request.POST["genre"],
            year = request.POST["year"],
            caption = caption

        )
        return redirect("home")
    
    return render(request, 'add_book.html')


def read(request):
    books = Book.objects.all()
    count = Book.objects.count()
    return render(request, 'all_books.html', {"books": books})





def about_book(request, id):
    book = Book.objects.get(pk = id)
    return render(request, 'about_book.html', {"book":book})




def update(request, id):

    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        
        book.title = request.POST["title"]
        book.author = request.POST["author"]
        book.genre = request.POST["genre"]
        book.year = request.POST["year"]

        caption = request.POST["caption"].strip()
        book.caption = caption if caption else None
        book.save()

        return redirect("home")
    
    return render(request, 'update_book.html', {"book": book})



def delete(request, id):

    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.delete()
        return redirect("home")

    return render(request, 'delete.html', {"book": book})
