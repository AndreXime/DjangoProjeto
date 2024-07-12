from django.contrib import admin
from contact import models

@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display =  'id','name','cargo'

@admin.register(models.Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display =  'nome_da_equipe',
    