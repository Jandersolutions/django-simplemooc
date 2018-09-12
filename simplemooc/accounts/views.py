from django.conf import settings
from django.conf.global_settings import LOGIN_URL
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = UserCreationForm()
    context = {
        'form' : form
    }
    return render(request,template_name,context)


