from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('cars_list')
    else:
        user_form = UserCreationForm()
    return render(
        request=request,
        template_name='register.html',
        context={'user_form': user_form},
    )
