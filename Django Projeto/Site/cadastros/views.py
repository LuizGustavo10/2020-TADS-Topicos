from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Funcionario, Pessoa, Ficha
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

# Create your views here.
class FuncionarioCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Funcionario
    fields = ['nome','endereco','telefone', 'email', 'cpf']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class PessoaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Pessoa
    fields = ['nome','endereco','telefone', 'email', 'cpf']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class FichaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Ficha
    fields = ['data','qtd','funcionario', 'pessoa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        #objeto não criado
        form.instance.usuario = self.request.user
        url= super().form_valid(form)
        #objeto criado
        return url

####UPDATE#########################################################################
class PessoaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Pessoa
    fields = ['nome','endereco','telefone', 'email', 'cpf']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pessoa')

class FuncionarioUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Funcionario
    fields = ['nome','endereco','telefone', 'email', 'cpf']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcinario')

class FichaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Ficha
    fields = ['data','qtd','funcionario', 'pessoa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ficha')

    ### DELETE ###################################################################
class PessoaDelete(LoginRequiredMixin, DeleteView):
        login_url = reverse_lazy('login')
        model = Pessoa
        template_name = 'cadastros/form-excluir.html'
        success_url = reverse_lazy('listar-pessoa')

class FuncionarioDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
        login_url = reverse_lazy('login')
        group_required = u"Administrador"
        model = Funcionario
        template_name = 'cadastros/form-excluir.html'
        success_url = reverse_lazy('listar-funcinario')

class FichaDelete(LoginRequiredMixin, DeleteView):
        login_url = reverse_lazy('login')
        model = Ficha
        template_name = 'cadastros/form-excluir.html'
        success_url = reverse_lazy('listar-ficha')

        ### LISTAR ###################################################################

class PessoaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Pessoa
    template_name = 'cadastros/listas/pessoa.html'

class FuncionarioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Funcionario
    template_name = 'cadastros/listas/funcionario.html'

class FichaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Ficha
    template_name = 'cadastros/listas/ficha.html'

