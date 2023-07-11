from django.contrib import admin
from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path("",home),# if someone giving blank data
    path("home/",home), # if user types home manually it should go to home
    path("add-employees/",add_employees),
    path("delete-employees/<int:Employee_ID>",delete_employees),
    path("update-employees/<int:Employee_ID>",update_employees),
    path("do-update-employees/<int:Employee_ID>",do_update_employees)
    
]

