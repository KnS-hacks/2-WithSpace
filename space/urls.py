from django.urls import path
from . import views

urlpatterns = [
   path('', views.main, name='main'),
   path('register', views.register_space, name='register_space'),
   # path('space/<str:id>', views.space, name='space'),
]