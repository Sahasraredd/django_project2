from django.contrib import admin
from jobs.models import job

# Register your models here.
class jobAdmin(admin.ModelAdmin):
    list_display = ['eno','title','category','location','designation','skills','description','created_at']
admin.site.register(job,jobAdmin)