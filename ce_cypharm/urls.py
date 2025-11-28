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
    path('contact/', views.contact, name='contact'),
    path('message/', views.message, name='message'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('faq/', views.faq, name='faq'),
    path('terms/', views.terms, name='terms'),
    path('download-terms/', views.download_terms, name='download_terms'),
    path('dashboard/', views.appointment_dashboard, name='appointment_dashboard'),
    path('our_team/', views.our_team, name='our_team'),
    path('blog/', views.blog, name='blog'),
    path('products/', views.products, name='products'),
    path('services/', views.services, name='services'),
    path('product2/', views.product2, name='product2'),
    
    
]