from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from sendy import views

urlpatterns = [
    path('parcels/', views.ParcelList.as_view()),
    path('parcels/<int:pk>/', views.OneParcel.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)