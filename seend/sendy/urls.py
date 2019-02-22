from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from sendy import views

urlpatterns = [
    path('parcels/', views.ParcelList.as_view()),
    path('parcels/<int:pk>/', views.OneParcel.as_view()),
    path('parcels/update_status/<int:pk>/', views.UpdateParcelStatus.as_view()),
    path('parcels/update_destination/<int:pk>/', views.UpdateParcelDestination.as_view()),
    path('parcels/<int:pk>/assign_rider', views.AssignRider.as_view()),
    path('parcels/user', views.UserParcels.as_view()),
    path('riders', views.AllRiders.as_view(), name='riders'),
    path("employees", views.Employee.as_view()),
    path("customer", views.Customer.as_view()),
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>/", views.UserDetail.as_view()),
    path("register/user/", views.RegisterUser.as_view()),
    path("register/staff/", views.RegisterStaff.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
