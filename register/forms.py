from .models import profile
from django import forms
from django.forms import ModelForm


class profileform(ModelForm):
	class Meta:
		model=profile
		fields=['First_name','Last_name','Birthdate','Image','Bio']
		widgets={
		'First_name':forms.TextInput(attrs={'class':'form-control mt-2'}),
		'Last_name':forms.TextInput(attrs={'class':'form-control mt-2'}),
		'Birthdate':forms.DateInput(attrs={'class':'form-control mt-2','placeholder':'yy-mm-dd'}),
		'Image':forms.FileInput(attrs={'class':'form-control mt-2'}),
		'Bio':forms.Textarea(attrs={'class':'form-control mt-2'})
		}