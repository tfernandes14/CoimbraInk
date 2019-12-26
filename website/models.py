from django.db import models


# Create your models here.
class Reprografia(models.Model):
    nome = models.CharField(max_length=50)
    zona = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    webiste = models.CharField(max_length=50, default=-1)
    contacto = models.IntegerField(default=-1)
    email = models.CharField(max_length=50, default=-1)
    rating_medio = models.FloatField(default=0.0)
    horario_abertura_semana_manha = models.FloatField(default=9.30)     # 9.30 ==> 9h30
    horario_fecho_semana_manha = models.FloatField(default=9.30)     # 9.30 ==> 9h30
    horario_abertura_semana_tarde = models.FloatField(default=9.30)     # 9.30 ==> 9h30
    horario_fecho_semana_tarde = models.FloatField(default=9.30)     # 9.30 ==> 9h30
    horario_abertura_fds_manha = models.FloatField(default=9.30)     # 9.30 ==> 9h30
    horario_fecho_fds_manha = models.FloatField(default=9.30)     # 9.30 ==> 9h30
    horario_abertura_fds_tarde = models.FloatField(default=9.30)     # 9.30 ==> 9h30
    horario_fecho_fds_tarde = models.FloatField(default=9.30)     # 9.30 ==> 9h30
    cartao_visita_preco = models.FloatField(default=-1.0)

    def __str__(self):
        return self.nome


class Acinco(models.Model):
    reprografia = models.OneToOneField(
        Reprografia,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    frente_cor_preco = models.FloatField(default=-1.0)
    frente_preto_branco_preco = models.FloatField(default=-1.0)
    frente_verso_cor_preco = models.FloatField(default=-1.0)
    frente_verso_preto_branco_preco = models.FloatField(default=-1.0)
    encadernacao = models.FloatField(default=-1.0)
    digitalizacao = models.FloatField(default=-1.0)
    plastificacao = models.FloatField(default=-1.0)


class Aquatro(models.Model):
    reprografia = models.OneToOneField(
        Reprografia,
        on_delete=models.CASCADE,
        primary_key=True
    )
    frente_cor_preco = models.FloatField(default=-1.0)
    frente_preto_branco_preco = models.FloatField(default=-1.0)
    frente_verso_cor_preco = models.FloatField(default=-1.0)
    frente_verso_preto_branco_preco = models.FloatField(default=-1.0)
    encadernacao = models.FloatField(default=-1.0)
    digitalizacao = models.FloatField(default=-1.0)
    plastificacao = models.FloatField(default=-1.0)


class Atres(models.Model):
    reprografia = models.OneToOneField(
        Reprografia,
        on_delete=models.CASCADE,
        primary_key=True
    )
    frente_cor_preco = models.FloatField(default=-1.0)
    frente_preto_branco_preco = models.FloatField(default=-1.0)
    frente_verso_cor_preco = models.FloatField(default=-1.0)
    frente_verso_preto_branco_preco = models.FloatField(default=-1.0)
    encadernacao = models.FloatField(default=-1.0)
    digitalizacao = models.FloatField(default=-1.0)
    plastificacao = models.FloatField(default=-1.0)


class Adois(models.Model):
    reprografia = models.OneToOneField(
        Reprografia,
        on_delete=models.CASCADE,
        primary_key=True
    )
    frente_cor_preco = models.FloatField(default=-1.0)
    frente_preto_branco_preco = models.FloatField(default=-1.0)
    frente_verso_cor_preco = models.FloatField(default=-1.0)
    frente_verso_preto_branco_preco = models.FloatField(default=-1.0)
    encadernacao = models.FloatField(default=-1.0)
    digitalizacao = models.FloatField(default=-1.0)
    plastificacao = models.FloatField(default=-1.0)


class Aum(models.Model):
    reprografia = models.OneToOneField(
        Reprografia,
        on_delete=models.CASCADE,
        primary_key=True
    )
    frente_cor_preco = models.FloatField(default=-1.0)
    frente_preto_branco_preco = models.FloatField(default=-1.0)
    frente_verso_cor_preco = models.FloatField(default=-1.0)
    frente_verso_preto_branco_preco = models.FloatField(default=-1.0)
    encadernacao = models.FloatField(default=-1.0)
    digitalizacao = models.FloatField(default=-1.0)
    plastificacao = models.FloatField(default=-1.0)


class Azero(models.Model):
    reprografia = models.OneToOneField(
        Reprografia,
        on_delete=models.CASCADE,
        primary_key=True
    )
    frente_cor_preco = models.FloatField(default=-1.0)
    frente_preto_branco_preco = models.FloatField(default=-1.0)
    frente_verso_cor_preco = models.FloatField(default=-1.0)
    frente_verso_preto_branco_preco = models.FloatField(default=-1.0)
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
