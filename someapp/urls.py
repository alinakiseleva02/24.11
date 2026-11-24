from django.urls import path
from . import views

urlpatterns = [
    path('services', views.ServicesView.as_view()),
    path('new_request', views.NewRequestView.as_view()),
    path('request-form', views.RequestFormView.as_view()),
    path('doctors', views.DoctorsView.as_view()),
    path('requests', views.RequestsView.as_view()),
]
