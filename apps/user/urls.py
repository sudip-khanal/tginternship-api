from django.urls import path
from apps.user import views

urlpatterns = [
    path('create_user/',views.create_user,name='create_user'),
    path('get_user/<int:pk>',views.get_user,name='get_user'),
    path('users/', views.users,name='users'),
    path('update_user/<int:pk>',views.update_user,name='update_user'),
    path('delete_user/<int:pk>',views.delete_user,name='delete_user')
]

