from django.contrib import admin
from .models import Activity, Record, Timeline


class RecordAdmin(admin.ModelAdmin):
    list_display = ('timelineID', 'title', 'date', 'activityID', 'description')
    list_filter = ('title', 'date', 'activityID')
    search_fields = ('title', 'activityID', 'description')
    date_hierarchy = 'date'
    ordering = ('date', )


class RecordInline(admin.StackedInline):
    model = Record
    extra = 0


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'name',)
    list_filter = ('user', 'name',)
    search_fields = ('name',)
    inlines = [RecordInline]


class TimelineAdmin(admin.ModelAdmin):
    list_display = ('user', 'title',)
    inlines = [RecordInline]


admin.site.register(Timeline, TimelineAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Record, RecordAdmin)
