from django.urls import path
from user import views

app_name = "accountapp"

urlpatterns = [
    path("sign-up/", views.sign_up_view, name="sign-up"),
    path("sign-in/", views.sign_in_view, name="sign-in"),
    path("logout/", views.logout, name="logout"),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name="activate"),
]
