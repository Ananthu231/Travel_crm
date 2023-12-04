from django.db import models

# Create your models here.

class Bike(models.Model):
    company=models.CharField(max_length=25)
    model=models.CharField(max_length=25)
    name=models.CharField(max_length=25)
    cc=models.CharField(max_length=25)
    colour=models.CharField(max_length=25)

class Travel(models.Model):
    state=models.CharField(max_length=30)
    district= models.CharField(max_length=30)
    visit=models.CharField(max_length=30)
    experience= models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.state} {self.district}  {self.visit}  {self.experience}"
    

class Students(models.Model):
    name=models.CharField(max_length=20)
    age=models.CharField(max_length=20)
    course=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    palce=models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.name}  {self.age}  {self.course}   {self.gender}   {self.palce}"
         
class Car(models.Model):
    car_name=models.CharField(max_length=20)
    colour=models.CharField(max_length=20)
    model=models.CharField(max_length=20)
    
    def __str__(self):
        return self.car_name
    
    
    


class Detial(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=False,null=True)
    course=models.CharField(max_length=30)

class Employee(models.Model):
    uname=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    place=models.CharField(max_length=30)
    email= models.EmailField(null=True)
    
    def __str__(self):
        return self.uname
    
class student(models.Model):
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=20)
    subject=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=30)
    email= models.EmailField(null=True)
    
    def __str__(self):
        return self.name
    
    def __str__(self):
        return self.gender
    
    def __str__(self): 
        return self.place
    
class Emp(models.Model):
    
        name=models.CharField(max_length=30)
        place=models.CharField(max_length=20)
        salary=models.PositiveIntegerField()
        contact=models.CharField(max_length=20)
        
class book(models.Model):
    tittle=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    publication_year=models.PositiveIntegerField()
    genre=models.CharField(max_length=20)
    
class movies(models.Model):
    M_name=models.CharField(max_length=20)
    director=models.CharField(max_length=20)
    year=models.CharField(max_length=20)
    genre=models.CharField(max_length=20)
        
class Music(models.Model):
    song_name=models.CharField(max_length=20)
    director=models.CharField(max_length=20)
    year=models.CharField(max_length=20)
    genre=models.CharField(max_length=20)

 