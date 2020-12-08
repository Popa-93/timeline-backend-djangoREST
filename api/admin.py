from django.contrib import admin
from .models import Activity, Record


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'name',)
    list_filter = ('user', 'name',)
    search_fields = ('name',)


class RecordAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'activity', 'description')
    list_filter = ('title', 'date', 'activity')
    search_fields = ('title', 'activity', 'description')
    date_hierarchy = 'date'
    ordering = ('date', )


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Record, RecordAdmin)
