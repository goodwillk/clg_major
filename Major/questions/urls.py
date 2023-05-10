from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('problems/',views.problems,name='problems'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('learn/dsa',views.learn_dsa,name='learn_dsa'),
    path('learn/oops',views.learn_oops,name='learn_oops'),
    path('learn/dbms',views.learn_dbms,name='learn_dbms'),
    path('learn/networking',views.learn_networking,name='learn_networking'),
]