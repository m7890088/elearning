from django.urls import path
from kindergarten import views

app_name= "kindergarten"

urlpatterns = [
    path('class/', views.ClassView.as_view() , name='classes'),
    path('login/', views.LoginView.as_view() , name='login'),

]
