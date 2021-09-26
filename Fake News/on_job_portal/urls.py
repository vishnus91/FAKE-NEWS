
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("/predict", views.predict_job_portal, name = "predict_job_portal")
]




