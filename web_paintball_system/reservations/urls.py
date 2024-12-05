from django.urls import path
from . import views


urlpatterns = [
    # path('cos/', views.field_list, name='field_list'),
    # path('reserve/<int:field_id>/', views.create_reservation, name='create_reservation'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('open_field/', views.open_field, name='open_field'),
    path('requirements/', views.requirements, name='requirements'),
    path('contact/', views.contact, name='contact'),
]
