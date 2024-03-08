from django.db import models
from datetime import date
class Livros(models.Model):
    id_livro = models.AutoField(primary_key=True)
    nome = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 30)
    co_autor = models.CharField(max_length = 30, blank=True)
    data_cadastro = models.DateField(default=date.today)
    emprestado = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Livro'
    def __str__(self) :
        return self.id_livro

class Emprestimo(models.Model):
    id_emprestimo = models.AutoField(primary_key=True)
    id_livro = models.ForeignKey(Livros, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField()
    data_devolucao = models.DateTimeField()
    tempo_duracao = models.DateField()