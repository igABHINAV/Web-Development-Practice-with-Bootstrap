from django.http import HttpResponse
from django.shortcuts import render,HttpResponse
from home.models import contact,fb
from django.contrib import messages
# Create your views here.
def index(req):
    return render(req,"template1.html")

def about(req):
    return render(req,"aboutus.html")

def contactus(req):
    if req.method == "POST":
        fname=req.POST.get('fname')
        lname=req.POST.get('lname')
        emaill=req.POST.get('emaill')
        gender=req.POST.get('gender')
        contactno=req.POST.get('contactno')
        contactus=contact(fname=fname,lname=lname, emaill=emaill,gender=gender,contactno=contactno )
        contactus.save()
        messages.success(req,' contact details updated ...')
    return render(req,"contactus.html")

def feedback(req):
    if req.method == "POST":
        emaill=req.POST.get('emaill')
        feedbacki=req.POST.get('feedbacki')
        feedback=fb(emaill=emaill,feedbacki=feedbacki)
        feedback.save()
    return render(req,"feedback.html") 
    messages.success(req,' contact details updated ...')    

def another(req):
    return render(req,"templatepage2.html")              