from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    """
    Agrupa os cargos em classificações maiores.
    Ex: 'Técnico Administrativo', 'Magistério Superior'
    """
    id_categoria = models.AutoField(primary_key=True)
    nome_categoria = models.CharField(max_length=255, null=False, blank=False)
    
    def __str__(self):
        return self.nome_categoria

class Cargo(models.Model):
    """
    O cargo ou a função específica.
    Ex: 'Analista de TI', 'Professor Adjunto'
    """
    id_cargo = models.AutoField(primary_key=True)
    nome_cargo = models.CharField(max_length=255, null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='cargos')
    
    def __str__(self):
        return self.nome_cargo

class Departamento(models.Model):
    """
    A unidade organizacional onde o servidor está alocado.
    """
    id_depto = models.AutoField(primary_key=True)
    nome_depto = models.CharField(max_length=255, null=False, blank=False)
    sigla_depto = models.CharField(max_length=10, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, blank=False)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, blank=False)
    
    def __str__(self):
        return f'{self.sigla_depto} - {self.nome_depto}'
    
class Servidor(AbstractUser):
    """
    Perfil do Servidor, estendendo o modelo AbstractUser.
    O 'id' e o 'username' são herdados.
    """
    siape = models.CharField(max_length=11, null=False, blank=False)
    nome_servidor = models.CharField(max_length=255, null=False, blank=False)
    carga_horaria = models.CharField(max_length=50, null=False, blank=False)

    REQUIRED_FIELDS = ["siape", "nome_servidor", "carga_horaria"]
      
    def __str__(self):
        return self.nome_servidor

class Vinculo(models.Model):
    """
    A entidade associativa ternária. Representa o "contrato" de um servidor
    em um cargo e departamento por um período.
    """
    id_vinculo = models.AutoField(primary_key=True)
    servidor = models.ForeignKey(Servidor, on_delete=models.PROTECT, related_name='vinculos')
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT, related_name='vinculos')
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, related_name='vinculos')
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    
    class Meta:
        unique_together = ('servidor', 'data_inicio')
    
    def __str__(self):
        return f'{self.servidor.nome_servidor} - {self.cargo.nome_cargo}'

TIPOS_PONTOS = [
    ('1', 'Entrada'),
    ('2', 'Saída'),
]

class Ponto(models.Model):
    """
    Registro de ponto eletrônico de um servidor.
    """
    id_ponto = models.AutoField(primary_key=True)
    servidor = models.ForeignKey(Servidor, on_delete=models.PROTECT, related_name='pontos')
    tipo_ponto = models.CharField(max_length=1, choices=TIPOS_PONTOS, default='1')
    data_hora = models.DateTimeField(auto_now_add=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, blank=False)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=False, blank=False)
    
    def __str__(self):
        return f'{self.servidor.nome_servidor} - {self.get_tipo_ponto()}'