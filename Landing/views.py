from django.shortcuts import render
from .models import *


# Create your views here.
def exp_list(request):
    exp_list = Exp.objects.all()

    sc_list = School.objects.all()

    return render(request, "Landing/exp_list.html",
                  {'exp_list':exp_list,
                   'sc_list': sc_list,})


