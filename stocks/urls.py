'''
Implements interface to satisfy the request.
And choose the specific function serviced the request.
'''
from django.contrib import admin
from django.urls import path
from stocks import views

urlpatterns = [
    # stocks/
    path('calc', views.calc_weights, name='calc'),
    path('list', views.list, name='list'),
    path('companyList', views.company_list, name='list'),
]