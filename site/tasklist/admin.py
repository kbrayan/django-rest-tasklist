from django.contrib import admin
# from django.contrib.auth import get_user_model
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    search_fields = ['taskname']
    list_display = ('taskname', 'due_date', 'finished')
    list_filter = ('finished',)
    filter_horizontal = ()
    class Meta:
        model = Task


admin.site.register(Task, TaskAdmin)