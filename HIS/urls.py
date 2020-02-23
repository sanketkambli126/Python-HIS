
from django.contrib import admin
from django.urls import path,include
from HIS import views

urlpatterns = [
    path('', views.Create),
    path('CustomerRegistration',views.RegisterUser),
    path('GetRoles',views.GetRoles),
    path('CheckEmail',views.CheckEmail)
    # path('', include('HIS.urls')),
]
