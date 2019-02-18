from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from sendy import views

urlpatterns = [
	path('riders', views.AllRiders.as_view()),
	]

urlpatterns = format_suffix_patterns(urlpatterns)
