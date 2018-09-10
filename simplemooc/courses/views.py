from django.shortcuts import render
from .models import Course

def index(request):
    # Course -> banco de dados | Objects -> manager do bd | all-> metodo do objects
    courses = Course.objects.all()
    template_name = 'courses/index.html'
    # context -> recebe variaveis que serao passadas ao render
    context = {
        'courses':courses
    }
    return render(request,template_name, context)
