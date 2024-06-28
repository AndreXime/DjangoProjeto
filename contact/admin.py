from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display =  'id','firstName','phone','createDate',
    ordering = 'id',
    search_fields = 'id','firstName','lastName'