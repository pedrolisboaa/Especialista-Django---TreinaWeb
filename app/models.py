from django.db import models

# Create your models here.

class Endereco(models.Model):
    ESTADOS = (
        ('AC', 'Acre'), 
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranão'),
        ('MG', 'Minas Gerais'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernanbuco'),
        ('PI', 'Piauí'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SE', 'Sergipe'),
        ('SP', 'São Paulo'),
        ('TO', 'Tocantins'))
    
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    cidade = models.CharField(max_length=100)
    estados = models.CharField(choices=ESTADOS, max_length=2)
    
    def __str__(self):
        return f'Rua {self.rua} - nº {self.numero}, {self.cidade}/{self.estados}'
 
    
class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False, default='')
    email = models.EmailField(null=False, blank=False)
    profissao = models.CharField(max_length=100, null=False, blank=False)
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.nome


class Dependente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=50)
    titular = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False, blank=False)
    
    def __str__(self):
        return self.nome


class Atendente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    clientes = models.ManyToManyField(to=Cliente, related_name='atendente_cliente')
    
    def __str__(self):
        return self.nome

