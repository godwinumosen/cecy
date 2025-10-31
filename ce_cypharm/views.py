from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy
from .models import MainImageCarousel,CecypharmFirstCategoryImage
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import AppointmentForm
from .models import Appointment 
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin  


def index (request):
    return render (request, 'ce_cypharm/index.html')

def base_view(request):
    return render(request, 'base.html')


#The main HomeView page
class HomeView(ListView): 
    model = MainImageCarousel 
    template_name = 'ce_cypharm/home.html'
    #This model is for the fist category of the home page "What We Offe"
    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)
    #the first  category of the home page "What We Offe"
        context['first_image_categorys'] = CecypharmFirstCategoryImage.objects.all()  
        
        return context  
    
def About (request):
    return render (request, 'ce_cypharm/about.html') 


'''def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'ce_cypharm/success.html')
    else:
        form = AppointmentForm()
    return render(request, 'ce_cypharm/book_appointment.html', {'form': form})'''
    
    

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.cecypharm_author = request.user
            appointment.save()

            # Render HTML template
            html_content = render_to_string('ce_cypharm/email_confirmation.html', {'appointment': appointment})
            
            # Send HTML email to the user
            msg = EmailMultiAlternatives(
                subject='Your Appointment Confirmation',
                body='This is an HTML email. Please enable HTML view.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[appointment.email],
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            # (Optional) Send admin notification in plain text or similar HTML
            send_mail(
                subject='New Appointment Booked',
                message=f"New appointment booked by {appointment.name} on {appointment.date} at {appointment.time}.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['cecypharm@gmail.com'],
            )

            return render(request, 'ce_cypharm/success.html')
    else:
        form = AppointmentForm()
    return render(request, 'ce_cypharm/book_appointment.html', {'form': form})




def appointment_dashboard(request):
    # Order by created_at descending — newest first
    appointments = Appointment.objects.all().order_by('-created_at')
    return render(request, 'ce_cypharm/dashboard.html', {'appointments': appointments})


def messages (request):
    return render (request, 'ce_cypharm/message.html', {})