from django.contrib import admin
from .models import *


# Register your models here.
class ReprografiaAdmin(admin.ModelAdmin):
    # O que mostra na aba de Reprografia
    list_display = ('nome', 'latitude', 'longitude')


class A5Admin(admin.ModelAdmin):
    # O que mostra na aba de Reprografia
    list_display = ('reprografia',)


class A4Admin(admin.ModelAdmin):
    # O que mostra na aba de Reprografia
    list_display = ('reprografia',)


class A3Admin(admin.ModelAdmin):
    # O que mostra na aba de Reprografia
    list_display = ('reprografia',)


class A2Admin(admin.ModelAdmin):
    # O que mostra na aba de Reprografia
    list_display = ('reprografia',)


class A1Admin(admin.ModelAdmin):
    # O que mostra na aba de Reprografia
    list_display = ('reprografia',)


class A0Admin(admin.ModelAdmin):
    # O que mostra na aba de Reprografia
    list_display = ('reprografia',)


class TeseAdmin(admin.ModelAdmin):
    # O que mostra na aba de Reprografia
    list_display = ('reprografia',)


admin.site.register(Reprografia, ReprografiaAdmin)
admin.site.register(Acinco, A5Admin)
admin.site.register(Aquatro, A4Admin)
admin.site.register(Atres, A3Admin)
admin.site.register(Adois, A2Admin)
admin.site.register(Aum, A1Admin)
admin.site.register(Azero, A0Admin)
admin.site.register(Tese, TeseAdmin)
