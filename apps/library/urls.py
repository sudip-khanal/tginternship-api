from django.urls import path
from apps.library import views
urlpatterns = [

    path('create_library/',views.create_library,name='create_library'),
    path('get_library/<int:pk>',views.get_library,name='get_library'),
    path('libraries/', views.libraries,name='libraries'),
    path('update_library/<int:pk>',views.update_library,name='update_library'),
    path('delete_library/<int:pk>',views.delete_library,name='delete_library')

    
]

   
