from django import forms

from .models import Car

class CreateNewForm(forms.ModelForm):

	car_name = forms.CharField(label = 'Car Name', max_length = 100)
	car_color = forms.CharField(label = 'Car Color', max_length = 20)

	class Meta:
		model = Car
		fields = ['car_name', 'car_color']

class InsertPositionForm(forms.ModelForm):

	car_name = forms.CharField(label = 'Car Name', max_length = 100)
	car_position = forms.IntegerField(label = 'New Position Number')

	class Meta:
		model = Car
		fields = ['car_name', 'car_position']
	
