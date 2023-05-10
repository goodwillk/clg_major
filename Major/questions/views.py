from django.shortcuts import render
from .models import Problem,Tag
def home(request):
    return render(request,'index.html')

def problems(request):
    problem=Problem.objects.all()
    context={
        'problems':problem,
    }
    return render(request,'questions/questions.html',context)

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def learn_dsa(request):
    return render(request,'study_material/dsa/dsa.html')
def learn_oops(request):
    return render(request,'study_material/oops/oops.html')
def learn_dbms(request):
    return render(request,'study_material/dbms/dbms.html')
def learn_networking(request):
    return render(request,'study_material/networking/networking.html')