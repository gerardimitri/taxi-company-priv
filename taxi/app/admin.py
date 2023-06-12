from django.contrib import admin

from .models import (
    Client,
    Driver,
    Route,
    Trip,
    BackgroundCheck,
    ClientPayment,
    DriverPayment,
    RideChat,
)

# from .models import IntegerBox

# Register your models here.

# --- exmaples ---

# admin.site.register(IntegerBox)

# --- project ---

admin.site.register(Client)
admin.site.register(Driver)
admin.site.register(Route)
admin.site.register(Trip)
admin.site.register(BackgroundCheck)
admin.site.register(ClientPayment)
admin.site.register(DriverPayment)
admin.site.register(RideChat)
