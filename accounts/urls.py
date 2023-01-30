from django.urls import path
from . import views

app_name = "accounts"

urlpatterns=[
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.create_user, name='register'),
    path('payment_page/', views.payment_page, name='payment_page'),
    path('newsletter/', views.newsletter, name='newsletter'),
]