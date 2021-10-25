from django.db import models
import uuid


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Fornecedor(Base):
    empresa = models.CharField('Nome da Empresa', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=18)
    telefone = models.CharField('Telefone', max_length=12, help_text='Digite o numero do Telefone')
    email = models.EmailField('E-mail', max_length=100, help_text='Digite seu email')

    class Meta:
        verbose_name_plural = 'Fornecedores'
        unique_together = ('empresa', 'cnpj', 'telefone', 'email',)

    def __str__(self):
        return self.empresa


class Produto(Base):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True, editable=False)
    nome = models.CharField('Nome do Produto', max_length=100, help_text='nome do produto')
    categoria = models.CharField('Categoria', max_length=200, help_text='Ex: frios, massas')
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2, help_text='R$')
    medida = models.CharField('Medida', max_length=2, help_text='Ex: kg, Un')
    estoque = models.IntegerField('Estoque Atual', null=True, blank=True, default=None)
    empresa = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        return str(self.empresa)

    @property
    def situacao_produto(self):
        if self.estoque > 0 and self.estoque <= 20:
            return "Situação/Ruim"
        elif self.estoque > 20 and self.estoque <= 40:
            return 'Situação/Regular'
        elif self.estoque > 40 and self.estoque <= 50:
            return 'Situação/Bom'
        elif self.estoque > 50:
            return 'Situação/Excelente'

    @property
    def validade_produto(self):
        if self.nome > 'queijo':
            return 'Produto vencido'
        else:
            f'Produto a Vencer na data: {self.nome}'


class RepresentanteComercial(Base):
    empresa = models.OneToOneField(Fornecedor, on_delete=models.CASCADE)
    nomecontato = models.CharField('Nome do Representante', max_length=100)
    endereco = models.CharField('Endereço', max_length=100)
    bairro = models.CharField('Bairro', max_length=100)
    cep = models.CharField('CEP', max_length=10)
    cidade = models.CharField('Cidade', max_length=20)
    estado = models.CharField('Estado', max_length=2)
    cpf = models.CharField('CPF', max_length=20)

    class Meta:
        verbose_name_plural = 'Representantes Comerciais'
        unique_together = ('nomecontato', 'endereco', 'cpf',)

    def __str__(self):
        return self.nomecontato


