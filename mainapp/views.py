from django.shortcuts import render
from django.http import HttpResponse

def home(Request):
    return render(Request, "index.html")

def index(Request):
    return render(Request, "index-2.html")
def homedemo(Request):
    return render(Request, "index-3.html")
def about(Request):
    return render(Request, "about.html")
def workspaces(Request):
    return render(Request, "workspaces.html")
def events(Request):
    return render(Request, "events.html")
def eventsbooking(Request):
    return render(Request, "events-booking.html")
def eventsdetails(Request):
    return render(Request, "events-details.html")
def services(Request):
    return render(Request, "services.html")
def servicesdetails(Request):
    return render(Request, "services-details.html")
def features(Request):
    return render(Request, "features.html")
def team(Request):
    return render(Request, "team.html")
def pricing(Request):
    return render(Request, "pricing.html")
def gallery(Request):
    return render(Request, "gallery.html")
def faq(Request):
    return render(Request, "faq.html")
def login(Request):
    return render(Request, "login.html")
def register(Request):
    return render(Request, "register.html")
def privacypolicy(Request):
    return render(Request, "privacy-policy.html")
def termsofservice(Request):
    return render(Request, "terms-of-service.html")
def error404(Request):
    return render(Request, "error-404.html")
def comingsoon(Request):
    return render(Request, "coming-soon.html")
def blog(Request):
    return render(Request, "blog.html")
# def blogrightsidebar(Request):
#     return render(Request, "blog-right-sidebar.html")
def blogrightsidebar(Request):
    return render(Request, "blog-right-sidebar.html")
def blogdetails(Request):
    return render(Request, "blog-details.html")
def contact(Request):
    return render(Request, "contact.html")

 


