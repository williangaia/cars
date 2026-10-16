from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView

from cars.forms import CarModelForm
from cars.models import Car


class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars


class NewCarView(View):
    def get(self, request):
        new_car_form = CarModelForm()
        return render(
            request=request,
            template_name='new_car.html',
            context={'new_car_form': new_car_form},
        )

    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return render(
            request=request,
            template_name='new_car.html',
            context={'new_car_form': new_car_form},
        )
