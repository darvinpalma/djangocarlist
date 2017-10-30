from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import CreateNewForm
from .models import Car

# Create your views here.
def homeview(request):

	#get method for home.html (adding new cars and viewing list)
	if request.method == 'GET':
		form = CreateNewForm()
		color_values = Car.objects.values('car_color').order_by().distinct()
		context = {'form' : form, 'all_cars' : Car.objects.all().order_by('car_position'), 'color_values' : color_values}	
		return render(request, 'carlistapp/home.html', context)


	#post method for home.html(a new car is added)
	if request.method == 'POST':
		form = CreateNewForm(request.POST)

		if form.is_valid():
			new_car = form.save(commit = False)
			new_car.car_name = request.POST['car_name']
			new_car.car_color = request.POST['car_color']
			new_car.car_position = Car.objects.all().count() + 1
			new_car.save()
		else:
			return HttpResponse('Form is invalid')

		form = CreateNewForm()
		context = {'form' : form, 'all_cars' : Car.objects.all().order_by('car_position')}	

		return render(request, 'carlistapp/home.html', context)


def editposition(request):

	if request.method == 'GET':
		form = CreateNewForm()
		color_values = Car.objects.values('car_color').order_by().distinct()
		context = {'form' : form, 'all_cars' : Car.objects.all().order_by('car_position'), 'color_values' : color_values}
		return render(request, 'carlistapp/home.html', context)

	if request.method == 'POST':
		cur_position = request.POST.get('current_position')
		n_position = request.POST.get('new_position')
		current_position = int(cur_position)
		new_position = int(n_position)
		form = CreateNewForm()

		if(current_position == new_position):
			return redirect('/home/')
		
		elif (new_position > Car.objects.count()):
			return HttpResponse('New position is invalid')
		
		else:
			car_for_positioning = get_object_or_404(Car, car_position = current_position)
			if (current_position > new_position):
				car_query_set = Car.objects.filter(car_position__lt=current_position, car_position__gte=new_position)
				
				if (current_position - new_position < 1000):
					for car in car_query_set:
						car.car_position = car.car_position + 1
						car.save()
				else:	
					for car in car_query_set.iterator():
						car.car_position = car.car_position + 1
						car.save()
			
			if (current_position < new_position):
				car_query_set = Car.objects.filter(car_position__lte=new_position, car_position__gt=current_position)
				if (new_position - current_position < 1000):
					for car in car_query_set:
						car.car_position = car.car_position - 1
						car.save()
				else:
					for car in car_query_set.iterator:
						car.car_position = car.car_position - 1
						car.save()

			car_for_positioning.car_position = new_position
			car_for_positioning.save()
			color_values = Car.objects.values('car_color').order_by().distinct()
			context = {'form' : form, 'all_cars' : Car.objects.all().order_by('car_position'), 'color_values' : color_values}
			return render(request, 'carlistapp/home.html', context)

def choosecolor(request):
	
	if request.method == 'GET':
		form = CreateNewForm()
		color_values = Car.objects.values('car_color').order_by().distinct()
		context = {'form' : form, 'all_cars' : Car.objects.all().order_by('car_position'), 'color_values' : color_values}
		return render(request, 'carlistapp/home.html', context)

	if request.method == 'POST':
		form = CreateNewForm()
		chosen_color = request.POST.get('colorselect')
		car_query_set = Car.objects.filter(car_color=chosen_color)
		color_values = Car.objects.values('car_color').order_by().distinct()
		context = {'form' : form, 'all_cars' : car_query_set.order_by('car_position'), 'color_values' : color_values}
		return render(request, 'carlistapp/home.html', context)