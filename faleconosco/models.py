from django.core.validators import FileExtensionValidator, MaxLengthValidator
from django.db import models


class Contato(models.Model):
    nome = models.CharField(max_length=240)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    documento = models.FileField(
        upload_to='documentos/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
    )
    mensagem = models.TextField(validators=[MaxLengthValidator(1000)])
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return f'{self.nome} - {self.email}'