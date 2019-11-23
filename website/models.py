from django.db import models


# Create your models here.
class Reprografia(models.Model):
    nome = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    rating_medio = models.FloatField(default=0.0)
    horario_abertura_semana_manha = models.FloatField()     # 9.30 ==> 9h30
    horario_fecho_semana_manha = models.FloatField()     # 9.30 ==> 9h30
    horario_abertura_semana_tarde = models.FloatField()     # 9.30 ==> 9h30
    horario_fecho_semana_tarde = models.FloatField()     # 9.30 ==> 9h30
    horario_abertura_fds_manha = models.FloatField()     # 9.30 ==> 9h30
    horario_fecho_fds_manha = models.FloatField()     # 9.30 ==> 9h30
    horario_abertura_fds_tarde = models.FloatField()     # 9.30 ==> 9h30
    horario_fecho_fds_tarde = models.FloatField()     # 9.30 ==> 9h30
    cartao_visita_preco = models.FloatField(default=-1.0)


class A5(models.Model):
    reprografia = models.OneToOneField(
        Reprografia,
        on_delete=models.CASCADE,
        primary_key=True
    )
    cor_preco = models.FloatField(default=-1.0)
    preto_branco_preco = models.FloatField(default=-1.0)
    encadernacao = models.FloatField(default=-1.0)
    digitalizacao = models.FloatField(default=-1.0)
    plastificacao = models.FloatField(default=-1.0)


class A4(models.Model):
    reprografia = models.OneToOneField(
        Reprografia,
        on_delete=models.CASCADE,
        primary_key=True
    )
    cor_preco = models.FloatField(default=-1.0)
    preto_branco_preco = models.FloatField(default=-1.0)
    encadernacao = models.FloatField(default=-1.0)
    digitalizacao = models.FloatField(default=-1.0)
    plastificacao = models.FloatField(default=-1.0)


class A3(models.Model):
    reprografia = models.OneToOneField(
        Reprografia,
        on_delete=models.CASCADE,
        primary_key=True
    )
    cor_preco = models.FloatField(default=-1.0)
    preto_branco_preco = models.FloatField(default=-1.0)
    encadernacao = models.FloatField(default=-1.0)
    digitalizacao = models.FloatField(default=-1.0)
    plastificacao = models.FloatField(default=-1.0)


class A2(models.Model):
    reprografia = models.OneToOneField(
        Reprografia,
        on_delete=models.CASCADE,
        primary_key=True
    )
    cor_preco = models.FloatField(default=-1.0)
    preto_branco_preco = models.FloatField(default=-1.0)
    encadernacao = models.FloatField(default=-1.0)
    digitalizacao = models.FloatField(default=-1.0)
    plastificacao = models.FloatField(default=-1.0)


class A1(models.Model):
    reprografia = models.OneToOneField(
        Reprografia,
        on_delete=models.CASCADE,
        primary_key=True
    )
    cor_preco = models.FloatField(default=-1.0)
    preto_branco_preco = models.FloatField(default=-1.0)
    encadernacao = models.FloatField(default=-1.0)
    digitalizacao = models.FloatField(default=-1.0)
    plastificacao = models.FloatField(default=-1.0)


class A0(models.Model):
    reprografia = models.OneToOneField(
        Reprografia,
        on_delete=models.CASCADE,
        primary_key=True
    )
    cor_preco = models.FloatField(default=-1.0)
    preto_branco_preco = models.FloatField(default=-1.0)
    encadernacao = models.FloatField(default=-1.0)
    digitalizacao = models.FloatField(default=-1.0)
    plastificacao = models.FloatField(default=-1.0)


class Tese(models.Model):
    reprografia = models.OneToOneField(
        Reprografia,
        on_delete=models.CASCADE,
        primary_key=True
    )
    preco = models.FloatField()
