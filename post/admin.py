from django.contrib import admin
from . models import OfferType, PropertyType, ConstructionType, Heating, Post

admin.site.register(OfferType)
admin.site.register(PropertyType)
admin.site.register(ConstructionType)
admin.site.register(Heating)
admin.site.register(Post)