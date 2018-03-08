from django.urls import path

from . import views

urlpatterns = [
    path( '', views.index, name = 'index'),
    path( 'bloginput/', views.bloginput, name = 'bloginput'),
    path( 'details/<int:pk>', views.details, name = 'details' ),
]
