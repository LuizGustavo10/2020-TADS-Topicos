from django.urls import path
from .views import IndexView, SobreView, CadastrarFichaView, CadastrarFuncionarioView, CadastrarPessoaView

urlpatterns = [
    # path('endereço/', MinhaView.as_view(), name='nome-da-url'),
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('cadastrarPessoa/', CadastrarPessoaView.as_view(), name='cadastrarPessoa'),
    path('cadastrarFuncionario/', CadastrarFuncionarioView.as_view(), name='cadastrarFuncionario'),
    path('ficha/', CadastrarFichaView.as_view(), name='ficha'),
]