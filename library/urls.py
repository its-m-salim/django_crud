from django.urls import path, include
from .views import*


urlpatterns = [
    path('', home_page, name="home"),
    path('create/', create, name="create"),
    path('read/', read, name="read"),
    path('read/<int:id>/', about_book, name="read_id"),
    path('update/<int:id>/', update, name="update"),
    path('delete/<int:id>/', delete, name="delete")
]