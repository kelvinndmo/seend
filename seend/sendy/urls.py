from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from sendy import views

urlpatterns = [
    path('parcels/', views.ParcelList.as_view()),
    path('parcels/<int:pk>/', views.OneParcel.as_view()),
    path('riders', views.AllRiders.as_view()),
    path("employees", views.Employee.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
