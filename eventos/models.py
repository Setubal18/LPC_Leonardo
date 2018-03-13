from django.db import models


class EventoCientifico(models.Model):
    issn = models.CharField('issn', max_length=5)



class Artigo(models.Model):
    evento = models.ForeignKey(EventoCientifico,on_delete=models.CASCADE ,blank=False)


class Pessoa(models.Model):
    nome_pessoa = models.CharField('Nome', max_length=50)
    email = models.CharField('E-mail', max_length=50)

    def __str__(self):
        return self.nome_pessoa


class Autor(Pessoa):
    curriculo = models.TextField(blank=True)
    artigos = models.ManyToManyField(Artigo)


class PessoaJuridica(Pessoa):
    cnpj = models.CharField('CNPJ', max_length=15)
    razaoSocial = models.CharField('Razao Social', max_length=30)


class PessoaFisica(Pessoa):
    cpf = models.CharField('CPF', max_length=14)


class Evento(models.Model):
    nome = models.CharField('Nome', max_length=50)
    eventoPrincipal = models.CharField('Evento Principal ', max_length=50)
    sigla = models.CharField('Sigla', max_length=10)
    timeInicio = models.DateTimeField(blank=True, null=False)
    keywords = models.TextField(blank=True)
    realizador = models.ForeignKey(Pessoa, related_name='evento',on_delete=models.CASCADE , blank=False)
    cidade = models.CharField('Cidade', max_length=30)
    uf = models.CharField('UF', max_length=2)
    cep = models.CharField('CEP', max_length=5)



    def __str__(self):
        return self.nome

