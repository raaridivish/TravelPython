from django.http import HttpResponse
from django.shortcuts import render
from . models import Place, Team   #inmakes_travelproject

# Create your views here.
def demo(request):
    obj_place = Place.objects.all()
    obj_team = Team.objects.all()
    return render(request, "index.html", {'result':obj_place, 'teamdata':obj_team})

    # return HttpResponse("Hello world")
#     name="india"
#     return render(request, "home.html", {'obj':name})
#
# def addition(request):
#     a=int(request.GET['val1'])
#     b=int(request.GET['val2'])
#     c=a+b
#     return render(request, "sum.html", {'sum':c})
