from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from accounts.views import login_view, logout_view, register_view
from cars.views import CarsView, NewCarView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(route='cars/', view=CarsView.as_view(), name='cars_list'),
    path(route='new_car/', view=NewCarView.as_view(), name='new_car'),
    path(route='register', view=register_view, name='register'),
    path(route='login/', view=login_view, name='login'),
    path(route='logout', view=logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
