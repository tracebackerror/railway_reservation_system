from django.contrib import admin
from .models import *


class BookingAdmin(admin.ModelAdmin):
    readonly_fields = ["booked_by", "created_at", "updated_at"]
    list_display = ["name","pnr","source","destination","status","booked_by"]


admin.site.register(Booking,BookingAdmin)
