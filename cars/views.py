from django.shortcuts import redirect, render

from cars.forms import CarForm
from cars.models import Car


def car_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')

    if search:
        cars = Car.objects.filter(model__icontains=search)

    return render(
        request=request,
        template_name='cars.html',
        context={'cars': cars},
    )


def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')

    else:
        new_car_form = CarForm()
    return render(
        request=request,
        template_name='new_car.html',
        context={'new_car_form': new_car_form},
    )
