"""
URL configuration for postgresTodo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views 

app_name= "encuestas"
urlpatterns = [
    path("", views.PollsView.as_view(), name="encuestas"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),   # Debe de ser <pk> para usarlo en la vista genérica
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
]
