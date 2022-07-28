from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    
    path('',views.index,name='homepage'),
    path('about/',views.about,name="about"),
    path('contactus/',views.contactus,name="contactpage"),
    path('feedback/',views.feedback,name="feedbackpage"),
    path('anotherpage/',views.another,name="another"),
]
