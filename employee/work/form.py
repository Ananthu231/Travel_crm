from django import forms
from work.models import movies
from work.models import Music 
from work.models import Detial
from work.models import Car
from work.models import Students
from work.models import Travel
from work.models import Bike

class BikeForm(forms.ModelForm):
    class Meta:
        model=Bike
        fields='__all__'

class TravelForm(forms.ModelForm):
    class Meta:
        model=Travel
        fields ='__all__'



class StudentsForm(forms.ModelForm):
    class Meta:
        model=Students
        fields='__all__'



class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields ='__all__'
    
class EmpForm(forms.Form):
    name=forms.CharField()
    place=forms.CharField()
    salary=forms.CharField()
    contact=forms.CharField()
    
class bookform(forms.Form):
    tittle=forms.CharField()
    author=forms.CharField()
    publication_year=forms.CharField()
    genre=forms.CharField()
    
class MoviesForm(forms.ModelForm):
    
    class Meta:
        model= movies
        fields ='__all__'


class MusicForm(forms.ModelForm):
    
    class Meta:
            model = Music
            fields ='__all__'
            
class Detialform(forms.ModelForm):
    class Meta:
            model = Detial
            fields ='__all__'
            