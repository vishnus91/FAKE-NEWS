
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.login, name = "login"),
    path("login", views.login, name = "login"),
    path("verify_login", views.verify_login, name = "verify_login"),
    path("logout", views.logout, name = "logout"),
    path("register", views.register, name = 'register'),
    path("home", views.home, name="home"),
    path("add_new_user", views.add_new_user, name="newUser"),
    path("on_article", include("on_article.urls")),
    path("on_job_portal", include("on_job_portal.urls")),
    path("on_social_media", include("on_social_media.urls")),
    path("back",views.back,name="back"),
    path("fontawesome",views.fontawesome,name="fontawesome")
]






