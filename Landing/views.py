from django.shortcuts import render

# Create your views here.
def exp_list(request):
    return render(request, "Landing/exp_list.html", {})
