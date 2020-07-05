from django.contrib import admin
from .models import User, ActivityPeriod
#from import_export.admin import ImportExportModelAdmin

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'uid','real_name','tz',
    )

class ActivityPeriodAdmin(admin.ModelAdmin):
    list_display = (
        'start_time','end_time',
    )

admin.site.register(User,UserAdmin)
admin.site.register(ActivityPeriod,ActivityPeriodAdmin)
