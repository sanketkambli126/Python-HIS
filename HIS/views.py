from django.shortcuts import render
from django.http import JsonResponse
from HIS import models
from HIS.models import Customer,Role

# Create your views here.

def Create(request):
    return render(request,'Policy.html',{})


def RegisterUser(request):
    return render(request,'CustomerRegisteration.html',{})

def GetRoles(request):
    roles = Role.objects.all()
    obj_Roles = [] 
    for x in roles:
       role={}
       role['id']=x.role_id
       role['name']=x.name
       obj_Roles.append(role)
    dict = {}
    dict["data"]=obj_Roles
    

    return JsonResponse(dict,safe=True)

def CheckEmail(request):
    #email =request.get()
    dict={}
    # dict['IsValid']=Isvalid
    #dict['resp']=request
    Isvalid = len(Customer.objects.filter(emails=''))==0
    return JsonResponse(dict,safe=True)