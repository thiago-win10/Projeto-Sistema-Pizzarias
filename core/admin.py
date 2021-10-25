from django.contrib import admin
from .models import Produto, Fornecedor, RepresentanteComercial


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'empresa', 'categoria', 'medida', 'preco', 'estoque', 'situacao_produto',)

    def nome(self, instance):
        return f'{instance.nome.get_full_name()}'

    list_filter = ('nome',)



@admin.register(RepresentanteComercial)
class RepresentanteComercialAdmin(admin.ModelAdmin):
    list_display = ('nomecontato', 'empresa', 'endereco', 'bairro', 'cep', 'cidade', 'estado', 'cpf',)

    def nomecontato(self, instance):
        return f'{instance.nomecontato.get_full_name()}'

    search_fields = ('nomecontato', 'empresa',)


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'cnpj', 'telefone', 'email',)

    def empresa(self, instance):
        return f'{instance.empresa.get_full_name()}'

    search_fields = ('empresa',)

