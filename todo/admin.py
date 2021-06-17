from django.contrib import admin
from .models import Todo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):# добавлениие поля для видимости в админке
    readonly_fields = ('date_created',)

admin.site.register(Todo, TodoAdmin)
