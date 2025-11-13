from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calculator/', views.calculator, name='calculator'),
    path('even_odd/', views.even_odd, name='even_odd'),
    path('factorial/', views.factorial, name='factorial'),
    path('fibonacci/', views.fibonacci, name='fibonacci'),
    path('bmi/', views.bmi, name='bmi'),
    path('prime/', views.prime_checker, name='prime'),
    path('age/', views.age_calculator, name='age'),
    path('simple-interest/', views.simple_interest, name='simple_interest'),
    path('table/', views.table_generator, name='table'),
    path('cube/', views.cube_calculator, name='cube'),
    path('square/', views.square_calculator, name='square'),
    path('about/', views.about, name='about'),
]