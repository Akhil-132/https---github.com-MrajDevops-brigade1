from django.contrib import admin
from .models import enquire_now,overview,configuration,gallery,amenities,walkthrough,know_your_locality,locality_map,Logo
# Register your models here.
admin.site.register(enquire_now)
admin.site.register(overview)
admin.site.register(configuration)
admin.site.register(gallery)
admin.site.register(amenities)
admin.site.register(walkthrough)
admin.site.register(know_your_locality)
admin.site.register(locality_map)
admin.site.register(Logo)