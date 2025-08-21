from django.urls import path
from . import views

urlpatterns = [
    # Main pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('products/cakes/', views.cakes, name='cakes'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),

    # Authentication
    path('login/', views.login, name='login'),
    path('logout/', views.logout_user, name='logout_user'),
]