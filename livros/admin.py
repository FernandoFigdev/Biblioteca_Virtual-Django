from django.contrib import admin
from .models import Livro

class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'isbn', 'ativo')
    list_filter = ('ativo',)

admin.site.register(Livro, LivroAdmin)
