from django.contrib import admin
from .models import Parcel,RiderProfile,EmployeeProfile

# Register your models here.


admin.site.register(Parcel)
admin.site.register(RiderProfile)
admin.site.register(EmployeeProfile)
