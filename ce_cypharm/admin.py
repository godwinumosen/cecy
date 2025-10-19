from django.contrib import admin
# Register your models here.
from . import models
from .models import MainImageCarousel,CecypharmFirstCategoryImage


#This model is for the fist carousel image
class MainImageCarouselAdmin (admin.ModelAdmin):
    prepopulated_fields = {'cecypharm_slug': ('cecypharm_title',)}
    list_display = ['cecypharm_title','cecypharm_description','cecypharm_publish_date']
admin.site.register(MainImageCarousel, MainImageCarouselAdmin)

#This model is for the fist image what we offer 
class CecypharmFirstCategoryImageAdmin (admin.ModelAdmin):
    prepopulated_fields = {'first_category_cecypharm_slug': ('first_category_cecypharm_title',)}
    list_display = ['first_category_cecypharm_title','first_category_cecypharm_description','first_category_cecypharm_publish_date']
admin.site.register(CecypharmFirstCategoryImage, CecypharmFirstCategoryImageAdmin)