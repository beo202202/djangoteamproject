from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.my_page, name='my-page'),
    path('profile_modify/', views.update, name='profile-modify'),
]
