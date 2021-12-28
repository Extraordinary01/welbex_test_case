from django.contrib import admin
from .models import Table

class TableAdmin(admin.ModelAdmin):
    list_display = ("date", "name", "amount", "distance")

admin.site.register(Table, TableAdmin)