from django.urls import path
from .views import fornecedores, IndexView, produto, produtos, representante, fornecedor, representantes, \
    UpadteProdutoView, DeleteProdutoView, UpadteRepresentanteView, \
    DeleteRepresentanteView, UpadteFornecedorView, DeleteFornecedorView


app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('produto/', produto, name='produto'),
    path('fornecedores/', fornecedores, name='fornecedores'),
    path('produtos-list/', produtos, name='produtos'),
    path('representantes/', representante, name='representantes'),
    path('fornecedor/', fornecedor, name='fornecedor'),
    path('representante/', representantes, name='representante'),
    path('<uuid:pk>/atualizar/', UpadteProdutoView.as_view(), name='atualizar-produto'),
    path('<uuid:pk>/delete/', DeleteProdutoView.as_view(), name='delete-produto'),
    path('<int:pk>/atualizar/', UpadteRepresentanteView.as_view(), name='atualizar-representante'),
    path('<int:pk>/delete/', DeleteRepresentanteView.as_view(), name='excluir-representante'),
    path('<int:pk>/editar/', UpadteFornecedorView.as_view(), name='editar-fornecedor'),
    path('<int:pk>/apagar/', DeleteFornecedorView.as_view(), name='apagar-fornecedor'),


]


