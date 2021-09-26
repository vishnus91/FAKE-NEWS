from os import read
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json


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

def logout_func():
    DATABASE = read_data()
    print ("before")
    print (DATABASE)
    DATABASE["logged_in"] = ""
    print ("after")
    print (DATABASE)
    try:
        json_object = json.dumps(DATABASE, indent = 4)
        with open(FILE_LOCATION, "w") as outfile:
            outfile.write(json_object)
        return True
    except:
        return False



def is_check_logged_in():
    DATABASE = read_data()
    if DATABASE != None:
        if DATABASE["logged_in"] != "":
            user_logged = DATABASE["logged_in"]
            return True
    return False

def write_data(DATABASE):
    try:
        json_object = json.dumps(DATABASE, indent = 4)
        with open(FILE_LOCATION, "w") as outfile:
            outfile.write(json_object)
        print ("written data")
        print ("-"*30)
        print (DATABASE)
        print ("-"*30)
        return True
    except:
        return False
    


def home(request):
    if is_check_logged_in():
        return render(request, "home.html")
    return redirect("/")

def login(request):
    if is_check_logged_in():
        return redirect("/home")
    return render(request, "log.html")
def register(request):
    if is_check_logged_in():
        return redirect("/home")
    return render(request, "register.html")

def verify_login(request):
    uname = request.GET.get("uname")
    upassword = request.GET.get("upassword")
    print (uname, upassword)
    DATABASE = read_data()
    status = {
        "message": "user ID not found"
    }
    if uname in DATABASE["users"]:
        status = {
            "message": "password is invalid"
        }
        if upassword == DATABASE["users"][uname]["password"]:
            status = {
                "message": "error logging in"
            }
            DATABASE["logged_in"] = uname
            if write_data(DATABASE):
                status = {
                    "message": "successfully logged in",
                    "name": DATABASE["users"][uname]["name"]
                }
    print (status)
    return JsonResponse(status)

def add_new_user(request):
    DATABASE = read_data()
    uname = request.GET.get("uname")
    uemail = request.GET.get("uemail")
    upassword = request.GET.get("upassword")
    status = {
        "message": "user ID already exists"
    }
    if uemail not in DATABASE["users"]:
        DATABASE["users"].update({
            uemail: {
                "name": uname,
                "password": upassword
            }
        })
        status = {
            "message": "error while adding new user"
        }
        if write_data(DATABASE):
            status = {
                "message": "successfully registered"
            }
    return JsonResponse(status)

def logout(request):
    print ("logout function called")
    status = {
            "message": "error while logging out"
        }
    try:
        if logout_func():
            status = {
                "message": "successfully logged out"
            }
    except:
        pass
    return JsonResponse(status)


from django.shortcuts import redirect

def fontawesome(request):
       return redirect("https://kit.fontawesome.com/a076d05399.js")
def back(request):
    if is_check_logged_in():
        return render(request, "home.html")
    return redirect("/")