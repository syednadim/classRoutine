from django.contrib import admin
from .models import *

admin.site.register(ClassRoom)
admin.site.register(Subject)
admin.site.register(Teacher)


@admin.register(ClassRoutine)
class ClassRoutineAdmin(admin.ModelAdmin):
    list_display = ('ClassRoom','subject','teacher','start','end')
    list_filter = ('ClassRoom','subject')