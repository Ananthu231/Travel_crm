from django.shortcuts import render,redirect
from django.views.generic import View
from  work.form import EmpForm
from  work.models import Emp
from work.form import bookform
from work.models import book
from work.form import MoviesForm
from work.models import movies
from work.form import MusicForm , Detialform , CarForm ,StudentsForm , TravelForm , BikeForm
from work.models import Music , Detial , Car ,Students ,Travel ,Bike

# Create your views here.

class BikeView(View):
    def get(self,request):
        form = BikeForm()
        return render(request,"bike.html",{"form":form})
    
    def post(self,request):
        form = BikeForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            return render(request,"bike.html",{"form":form})
        else:
            return render(request,"bike.html",{"form":form})
class Bikelist(View):
    def get(self,request):
        be =Bike.objects.all()
        return render(request,"Bikelist.html",{"be":be})
            
        
    

class TravelView(View):
    def get(self,request):
        form = TravelForm()
        return render(request,"travel.html",{"form":form})
    def post(self,request):
        form = TravelForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            return render(request,"travel.html",{"form":form})
        else:
            return render(request,"travel.html",{"form":form})
        
class travellist(View):
    def get(self,request):
        tr = Travel.objects.all()
        return render(request,"travellist.html",{"tr":tr})
    
class TravelDetails(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("trip")
        tp = Travel.objects.get(id=id)
        return render(request,"traveldetails.html",{"tp":tp})
    
class  Traveldelete(View):
    def get(self,request,*args, **kwargs) :
        id=kwargs.get("trip")
        Travel.objects.get(id=id).delete()
        return redirect('travel-li')



class StudentsView(View):
    def get(self,request):
        form = StudentsForm()
        return render(request,"stud.html",{"form":form})
    def post(self,request):
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            return render(request,"stud.html",{"form":form})
        else:
            
            return render(request,"stud.html",{"form":form})
        

class Studentslist(View):
    def get(self,request):
        gm = Students.objects.all()
        return render(request,"studentslist.html",{"gm":gm})
    

class StudentsDetails(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("ok")
        mg = Students.objects.get(id=id)
        return render(request,"studentsdetails.html",{"mg":mg})








class CarDetails(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("id")
        rl = Car.objects.get(id=id)
        return render(request,"cardetail.html",{"rl":rl})
    

class Carlist(View):
    def get(self,request):
        m = Car.objects.all()
        return render(request,"carlist.html",{"m":m})
    
        
class CarView(View):
    def get(self,request):
        form = CarForm()
        return render(request,"car.html",{"form":form})
    
    def post(self,request):
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            return render(request,"car.html",{"form":form})
        else:
            
            return render(request,"car.html",{"form":form})
        
     
     
     
        

class Detiallist(View):
    def get(self,request):
        s = Detial.objects.all()
        return render(request,"Detiallist.html",{"s":s})

class DetialView(View):
    def get(self,request):
        form = Detialform()
        return render(request,"Detial.html",{"form":form})
    
    def post(self,request):
        form = Detialform(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            return render(request,"Detial.html",{"form":form})
        else:
            
            return render(request,"Detial.html",{"form":form})
        
        
        
        
        
        

class Musiclist(View):
    def get(self,request):
        z=Music.objects.all()
        return render(request,"musiclist.html",{"z":z})


class MusicView(View):
    def get(self,request):
        form = MusicForm()
        return render(request,"music.html",{"form":form})
    
    def post(self,request):
        form = MusicForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            return render(request,"music.html",{"form":form})
        else:
            
            return render(request,"music.html",{"form":form})



class Moviesview(View):
    def get(self,request):
        form = MoviesForm()
        return render(request,"film.html",{"form":form})
    
    def post(self,request):
         
         form = MoviesForm( request.POST)
         if form.is_valid():
             print(form.cleaned_data)
             movies.objects.create(**form.cleaned_data)
             return render(request,"film.html",{"form":form})
         else:
             return render(request,"film.html",{"form":form})



    

        

class BookView(View):
    def get (self,request):
    
        form=bookform()
        return render(request,"book.html",{"form":form})
    
    def post(self,request):
         
         form = bookform( request.POST)
         if form.is_valid():
             print(form.cleaned_data)
             book.objects.create(**form.cleaned_data)
             return render(request,"book.html",{"form":form})
         else:
             return render(request,"book.html",{"form":form})





class Empview(View):
    def get(self,request):
    
        form = EmpForm()
        return render(request,"add.html",{"form":form})
    
    def post(self,request):
        
         form = EmpForm( request.POST)
         if form.is_valid():
             print(form.cleaned_data)
             Emp.objects.create(**form.cleaned_data)
             return render(request,"add.html",{"form":form})
         else:
             return render(request,"add.html",{"form":form})

          

         
         