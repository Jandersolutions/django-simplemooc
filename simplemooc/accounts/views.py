from django.conf import settings
from django.conf.global_settings import LOGIN_URL
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import EditAccountForm


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

#decorator que so permite chamar a função abaixo no caso do usuario estar logado
@login_required
def dashboard(request):
    template_name = 'accounts/dashboard.html'
    form = EditAccountForm()
    context = {}
    context['form'] = form
    return render(request,template_name,context)

@login_required
def edit(request):
    template_name = 'accounts/edit.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            context['success'] = True
    else:
        form = EditAccountForm(instance=request.user)
    context['form'] = form
    return render(request, template_name, context)


