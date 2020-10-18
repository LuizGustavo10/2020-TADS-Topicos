from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Funcionario, Pessoa, Ficha
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome','endereco','telefone', 'email', 'cpf']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class PessoaCreate(CreateView):
    model = Pessoa
    fields = ['nome','endereco','telefone', 'email', 'cpf']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class FichaCreate(CreateView):
    model = Ficha
    fields = ['data','qtd','funcionario', 'pessoa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

####UPDATE#########################################################################
class PessoaUpdate(UpdateView):
    model = Pessoa
    fields = ['nome','endereco','telefone', 'email', 'cpf']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pessoa')

class FuncionarioUpdate(UpdateView):
    model = Funcionario
    fields = ['nome','endereco','telefone', 'email', 'cpf']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcinario')

class FichaUpdate(UpdateView):
    model = Ficha
    fields = ['data','qtd','funcionario', 'pessoa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ficha')

    ### DELETE ###################################################################
class PessoaDelete(DeleteView):
        model = Pessoa
        template_name = 'cadastros/form-excluir.html'
        success_url = reverse_lazy('listar-pessoa')

class FuncionarioDelete(DeleteView):
        model = Funcionario
        template_name = 'cadastros/form-excluir.html'
        success_url = reverse_lazy('listar-funcinario')

class FichaDelete(DeleteView):
        model = Ficha
        template_name = 'cadastros/form-excluir.html'
        success_url = reverse_lazy('listar-ficha')

        ### LISTAR ###################################################################

class PessoaList(LoginRequiredMixin, ListView):
    model = Pessoa
    template_name = 'cadastros/listas/pessoa.html'

class FuncionarioList(LoginRequiredMixin, ListView):
    model = Funcionario
    template_name = 'cadastros/listas/funcionario.html'

class FichaList(LoginRequiredMixin, ListView):
    model = Ficha
    template_name = 'cadastros/listas/ficha.html'

