from django.shortcuts import render
from .forms import ProdutoModelForm, FornecedorModelForm, RepresentanteComercialModelForm
from django.contrib import messages
from .models import Produto, Fornecedor, RepresentanteComercial
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class UpadteProdutoView(UpdateView):
    model = Produto
    template_name = 'produto_atualizar.html'
    fields = ['nome','preco', 'estoque']
    success_url = reverse_lazy('core:produtos')


class DeleteProdutoView(DeleteView):
    model = Produto
    template_name = 'produto_del.html'
    success_url = reverse_lazy('core:produtos')


class UpadteRepresentanteView(UpdateView):
    model = RepresentanteComercial
    template_name = 'representante_atualizar.html'
    fields = ['empresa', 'nomecontato', 'endereco', 'bairro', 'cep', 'cidade', 'estado', 'cpf']
    success_url = reverse_lazy('core:representantes')


class DeleteRepresentanteView(DeleteView):
    model = RepresentanteComercial
    template_name = 'representante_deletar.html'
    success_url = reverse_lazy('core:representantes')


class UpadteFornecedorView(UpdateView):
    model = Fornecedor
    template_name = 'fornecedor_atualizar.html'
    fields = ['empresa', 'cnpj', 'telefone', 'email']
    success_url = reverse_lazy('core:fornecedores')


class DeleteFornecedorView(DeleteView):
    model = Fornecedor
    template_name = 'fornecedor_deletar.html'
    success_url = reverse_lazy('core:fornecedores')


def produtos(request):

    context = {
        'produtos': Produto.objects.all()

    }
    return render(request, 'produtos.html', context)


def fornecedores(request):
    context = {
        'fornecedores': Fornecedor.objects.all()
    }
    return render(request, 'fornecedores.html', context)


def representante(request):
    context = {
        'representantes': RepresentanteComercial.objects.all()
    }
    return render(request, 'representantes.html', context)


def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request, 'Produto salvo com Sucesso.')
            form = ProdutoModelForm()
        else:
            messages.error(request, 'Erro ao salvar Produto.')
    else:
        form = ProdutoModelForm()
    context = {
        'form': form
    }
    return render(request, 'produto.html', context)


def fornecedor(request):
    if str(request.method) == 'POST':
        form = FornecedorModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request, 'Fornecedor salvo com Sucesso.')
            form = FornecedorModelForm()
        else:
            messages.error(request, 'Erro ao salvar Fornecedor.')
    else:
        form = FornecedorModelForm()
    context = {
        'form': form
    }
    return render(request, 'fornecedor.html', context)


def representantes(request):
    if str(request.method) == 'POST':
        form = RepresentanteComercialModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request, 'Representante salvo com Sucesso.')
            form = FornecedorModelForm()
        else:
            messages.error(request, 'Erro ao salvar Representante.')
    else:
        form = RepresentanteComercialModelForm()
    context = {
        'form': form
    }
    return render(request, 'representante.html', context)
