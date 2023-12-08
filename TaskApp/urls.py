from django.urls import path
from TaskApp import views


urlpatterns = [
    path('', views.login_page, name='login'),
    path('patient_signup', views.patient_signup_page, name='patient_signup'),
    path('doctor_signup', views.doctor_signup_page, name='doctor_signup'),
    path('doctor_home', views.doctor_home_page, name='doctor_home'),
    path('patinet_home', views.patient_home_page, name='patient_home'),

]