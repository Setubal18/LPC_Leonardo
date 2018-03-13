from django.contrib import admin


from .models import *
# Register your models here.
admin.site.register(Pessoa)
admin.site.register(PessoaFisica)
admin.site.register(PessoaJuridica)
admin.site.register(Evento)
admin.site.register(Autor)