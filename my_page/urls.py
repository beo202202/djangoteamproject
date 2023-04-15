from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.my_page, name='my-page'),
    path('profile-modify/',views.update, name='profile-modify'),
]
