from django.urls import path,include
from . import views

urlpatterns=[
    path('enquiry-form/', views.registration, name="enquiry"),
    path("", views.index, name="index"),
    path('download/', views.download_file)
]