from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from . import fake_news_on_article

PREDICTOR = fake_news_on_article.Fake_News_On_Article()

FILE_LOCATION = './database.json'
DATABASE = None

def read_data():
    try:
        with open(FILE_LOCATION) as f:
            DATABASE = json.load(f)
            return DATABASE
    except:
        return {
            "logged_in": "",
            "users": {}
        }


try:
    DATABASE = read_data()
except:
    print ("there is an error reading database file...")

# Create your views here.

def is_check_logged_in():
    DATABASE = read_data()
    if DATABASE != None:
        if DATABASE["logged_in"] != "":
            user_logged = DATABASE["logged_in"]
            return True
    return False


# Create your views here.

def home(request):
    if is_check_logged_in():
        return render(request, "on_article.html")
    return redirect("/home")

def predict(request):
    news = request.GET["news"]
    l=len(news)
    if l>1:
        status = PREDICTOR.predict(news)
    else:
        status = "Please Enter The Article"

    data = {
        "result": status
    }
    return HttpResponse(status)






