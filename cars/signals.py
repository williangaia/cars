from django.db.models import Sum
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver

from cars.models import Car, CarInventory
from openai_api.client import get_car_ai_bio


def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(total_value=Sum('value'))['total_value']

    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value,
    )


@receiver(signal=pre_save, sender=Car)
def car_pre_save(sender, instance, raw=False, **kwargs):
    if raw:
        return

    if not instance.bio:
        instance.bio = get_car_ai_bio(
            brand=instance.brand,
            model=instance.model,
            year=instance.model_year,
        )


@receiver(signal=post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()


@receiver(signal=post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()
