from django.contrib import admin
from .models import Activity, Record


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


class RecordAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'date',
                    'get_activities', 'description')
    list_filter = ('title', 'date', 'activities')
    search_fields = ('title', 'activities__name', 'description')
    date_hierarchy = 'date'
    ordering = ('date', )

    def get_activities(self, record_object):
        return ','.join([activity.name for activity in record_object.activities.all()])


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Record, RecordAdmin)
