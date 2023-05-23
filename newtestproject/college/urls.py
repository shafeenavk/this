from . import views
from django.urls import path


app_name = 'college'

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name='login'),
    path("register/", views.register, name='register'),
    path('dropdown/',views.dropdown,name='dropdown'),
    path("submit/", views.submit, name='submit'),

]