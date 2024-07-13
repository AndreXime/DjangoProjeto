from django.urls import path
from contact import views

urlpatterns = [
    path('',views.Home, name='home'),
    path('login/',views.SignUpIn, name='login'),
    path('dashboard',views.Dashboard, name='dashboard'),
    path('logout',views.UserLogout, name='logout')
]