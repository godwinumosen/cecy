from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy
#from .models import ServicesPagePicture,RealEstatePicture,FacilityManagementPicture,ConstructionPicture
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin  


def index (request):
    return render (request, 'ce_cypharm/index.html')

def base_view(request):
    return render(request, 'base.html')
