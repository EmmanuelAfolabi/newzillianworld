from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.register(Subscriber)

@admin.register(Upload)
class UploadAdmin(ImportExportModelAdmin):
    list_display = ('title', 'availability')

@admin.register(Testimonials)
class TestimonialsAdmin(ImportExportModelAdmin):
    list_display = ('name', 'message')

@admin.register(Feedbacks)
class FeedbacksAdmin(ImportExportModelAdmin):
    list_display = ('name', 'subject')