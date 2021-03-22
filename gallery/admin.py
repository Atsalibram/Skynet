from django.contrib import admin
from .models import Image,Category,Location

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal=('location',)

# Register your models here.
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Location)