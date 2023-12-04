"""
URL configuration for employee project.

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
from work.views import Empview
from work.views import BookView
from work.views import Moviesview
from work.views import MusicView,Musiclist,DetialView,Detiallist,CarView,Carlist,CarDetails,StudentsView,Studentslist,StudentsDetails,TravelView,travellist,TravelDetails,Traveldelete
from work.views import BikeView,Bikelist
urlpatterns = [
    path('admin/', admin.site.urls),
    path('model/',Empview.as_view()),
    path('book/',BookView.as_view()),
    path('films/',Moviesview.as_view()),
    path('songs/',MusicView.as_view()),
    path('song/all',Musiclist.as_view()),
    path('detial/',DetialView.as_view()),
    path('detials/all',Detiallist.as_view()),
    path('cars/',CarView.as_view()),
    path('car/all',Carlist.as_view()),
    path('car/<int:id>',CarDetails.as_view()),
    path('stud/',StudentsView.as_view()),
    path('stud/all',Studentslist.as_view()),
    path('stud/<int:ok>',StudentsDetails.as_view(),name="students"),
    path('travel/',TravelView.as_view()),
    path('travel/all',travellist.as_view(),name="travel-li"),
    path('travel/<int:trip>',TravelDetails.as_view(),name="travel"),
    path('travel/<int:trip>/remove',Traveldelete.as_view(),name="travel-del")
    
    
]
