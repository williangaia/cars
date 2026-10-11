from django import forms

from cars.models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        #fields = '__all__'
        fields = [
            'model',
            'brand',
            'factory_year',
            'model_year',
            'plate',
            'value',
            'photo',
        ]
