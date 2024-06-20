from django.urls import path
from apps.book import views

urlpatterns = [
    path('create_book/',views.create_book,name='create_book'),
    path('get_book/<int:pk>',views.get_book,name='get_book'),
    path('books/', views.books,name='books'),
    path('update_book/<int:pk>',views.update_book,name='update_book'),
    path('delete_book/<int:pk>',views.delete_book,name='delete_book')
]

