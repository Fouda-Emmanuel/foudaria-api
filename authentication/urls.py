from django.urls import path
from . import views

urlpatterns =[
    path('signup/', views.UserCreationView.as_view(), name='signup')
]