from django.urls import path
from . import views

# sign up login url pattren
urlpatterns = [
    path('userSignUp/', views.userSignUp, name='userSignUp'),
    path('user_login/', views.user_login, name='user_login'),
]
