
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name = "on_article"),
    path("/predict", views.predict, name = "predict")
]




