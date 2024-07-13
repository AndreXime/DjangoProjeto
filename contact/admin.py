from django.contrib import admin
from contact import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class UserInLine(admin.StackedInline):
    model = models.Client
    can_delete = False

# Define a new User admin
class NewUserAdmin(UserAdmin):
    inlines = [UserInLine]

admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)

@admin.register(models.Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display =  'nome_da_equipe',
    