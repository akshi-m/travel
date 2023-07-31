from django.contrib import admin
from .models.locations import Locations
from .models.feedback import Feedback
from .models.traveldesk import Traveldesk


# Register your models here.
class AdminUser(admin.ModelAdmin):
    list_display = ['username', 'email', 'contact', 'image', 'password']


@admin.register(Locations)
class AdminLocation(admin.ModelAdmin):
    list_display = ('place', 'timing', 'description', 'image',
                    'category', 'created', 'modified')


@admin.register(Feedback)
class AdminFeedback(admin.ModelAdmin):
    list_display = ('name', 'email', 'review', 'image',
                    'date_created', 'date_modified')


@admin.register(Traveldesk)
class AdminTraveldesk(admin.ModelAdmin):
    list_display = ('name', 'email', 'expected_date', 'phone',
                    'message', 'number_of_person', 'date_created', 'date_modified')
