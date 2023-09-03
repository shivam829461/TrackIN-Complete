from django.contrib import admin
from track.models import Track,Lead


class TrackAdmin(admin.ModelAdmin):
    list_display = ("waybill","pickup","origin","destination","status","EDD","phone","receiver","lastscan")

class ShipAdmin(admin.ModelAdmin):
    list_display= ("type","fname","lname","address1","address2","city","state","pin","country","phone","email","feedback")




admin.site.register(Track, TrackAdmin)
admin.site.register(Lead,ShipAdmin)


# Register your models here.
