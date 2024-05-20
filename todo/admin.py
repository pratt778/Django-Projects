from django.contrib import admin
from .models import todolist
# Register your models here.
class todoshow(admin.ModelAdmin):
    list_display=('todoname','tododesc','user')

admin.site.register(todolist)