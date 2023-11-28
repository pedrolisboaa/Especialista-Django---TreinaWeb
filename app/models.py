from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False, default='')
    email = models.EmailField(null=False, blank=False)
    profissao = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.nome