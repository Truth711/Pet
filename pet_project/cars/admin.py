from django.contrib import admin
from cars.models import Brand, Car, Favorites

admin.site.register(Brand)
admin.site.register(Car)
admin.site.register(Favorites)
