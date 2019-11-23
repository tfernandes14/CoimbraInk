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
admin.site.register(A5, A5Admin)
admin.site.register(A4, A4Admin)
admin.site.register(A3, A3Admin)
admin.site.register(A2, A2Admin)
admin.site.register(A1, A1Admin)
admin.site.register(A0, A0Admin)
admin.site.register(Tese, TeseAdmin)
