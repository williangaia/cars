from django.apps import AppConfig


class CarsConfig(AppConfig):
    name = 'cars'

    def ready(self):
        import cars.signals
