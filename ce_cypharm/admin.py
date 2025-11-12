from django.contrib import admin
# Register your models here.
from . import models
from .models import MainImageCarousel,CecypharmFirstCategoryImage,CecypharmSecondCategoryImage,BlogPost #Appointment


'''class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'time')
    list_filter = ('date',)
admin.site.register(Appointment, AppointmentAdmin)'''
    
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


#This model is for the second image what we offer 
class CecypharmSecondCategoryImageAdmin (admin.ModelAdmin):
    prepopulated_fields = {'second_category_cecypharm_slug': ('second_category_cecypharm_title',)}
    list_display = ['second_category_cecypharm_title','second_category_cecypharm_description','second_category_cecypharm_publish_date']
admin.site.register(CecypharmSecondCategoryImage, CecypharmSecondCategoryImageAdmin)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    search_fields = ('title', 'author')
    list_filter = ('date_posted',)