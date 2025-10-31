from django.urls import path
from . import views
from .views import HomeView #ArticleDetailView, 

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', HomeView.as_view(), name="home"),
    path('home/', HomeView.as_view(), name='home'),
    #path('article/<int:pk>/', ArticleDetailView.as_view(), name="detail"),
    #path('article2/<int:pk>/', SecondConstructionDetailViewArticleDetailView.as_view(), name="second_detail"),
    #path('about/', AboutView.as_view(), name='about'),
    path('about/', views.About, name='about'),
    #path('contact/', ContactView.as_view(), name='contact'),
    path('message/', views.messages, name='message'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('dashboard/', views.appointment_dashboard, name='appointment_dashboard'),
    
]