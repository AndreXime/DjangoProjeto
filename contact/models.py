from django.db import models
from django.contrib.auth.models import User

class Equipe(models.Model):
    nome_da_equipe = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome_da_equipe
    
class Client(models.Model):
    #Informações pessoais
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone =  models.CharField(max_length=50,blank=True)
    imagem = models.ImageField(blank=True, upload_to='pictures/%Y/%m/%d')

    #Administração
    equipe = models.ForeignKey(Equipe, on_delete=models.SET_NULL, blank=True, null=True)
    cargo = models.CharField(max_length=50,blank=True)

    def __str__(self) -> str:
        return f'{self.cargo} - {self.name}'
