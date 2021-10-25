from django import forms
from .models import Produto, Fornecedor, RepresentanteComercial


class ProdutoModelForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'


class RepresentanteComercialModelForm(forms.ModelForm):
    class Meta:
        model = RepresentanteComercial
        fields = '__all__'


class FornecedorModelForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'