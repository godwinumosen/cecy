from django.contrib import admin
# Register your models here.
from . import models
from .models import MainImageCarousel



class MainImageCarouselAdmin (admin.ModelAdmin):
    prepopulated_fields = {'cecypharm_slug': ('cecypharm_title',)}
    list_display = ['cecypharm_title','cecypharm_description','cecypharm_publish_date']
admin.site.register(MainImageCarousel, MainImageCarouselAdmin)