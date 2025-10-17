from django.urls import path
from . import views
#from .views import HomeView, ArticleDetailView, SecondConstructionDetailViewArticleDetailView,VideoImageDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    #path('', HomeView.as_view(), name="home"),
    #path('home/', HomeView.as_view(), name='home'),
    #path('article/<int:pk>/', ArticleDetailView.as_view(), name="detail"),
    #path('article2/<int:pk>/', SecondConstructionDetailViewArticleDetailView.as_view(), name="second_detail"),
    #path('about/', AboutView.as_view(), name='about'),
    #path('contact/', ContactView.as_view(), name='contact'),
    #path('message/', views.message, name='message'),
    
]