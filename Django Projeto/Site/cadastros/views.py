from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Funcionario, Pessoa, Ficha
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404

# Create your views here.
class FuncionarioCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Funcionario
    fields = ['nome','endereco','telefone', 'email', 'cpf']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = " Cadastro de Funcionário"
        return context


class PessoaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Pessoa
    fields = ['nome','endereco','telefone', 'email', 'cpf']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = " Cadastro de Pessoa"
        return context

class FichaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Ficha
    fields = ['data','qtd','funcionario', 'pessoa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = " Cadastro de Ficha"
        return context


    def form_valid(self, form):
        #objeto não criado
        form.instance.usuario = self.request.user
        url= super().form_valid(form)
        #objeto criado
        #self.object.pessoa = "teste: "+ self.object.pessoa
        #self.object.save()  
        return url

####UPDATE#########################################################################
class PessoaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Pessoa
    fields = ['nome','endereco','telefone', 'email', 'cpf']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pessoa')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = " Edição de Pessoa"
        return context


class FuncionarioUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Funcionario
    fields = ['nome','endereco','telefone', 'email', 'cpf']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcinario')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = " Cadastro de Funcionário"
        return context


class FichaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Ficha
    fields = ['data','qtd','funcionario', 'pessoa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ficha')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = " Cadastro de Ficha"
        return context


    # #aula 22-----------o usuario tal só ve os cadastros dele----------------------------------------
    def get_object(self, queryset=None):
        # get_object_or_404(Classe, atr="isso", atr2=val2 )
        #self.object = Ficha.objects.get(pk=self.kwargs['pk'], usuario=self.request.user)
        self.object = get_object_or_404(Ficha, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

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
        #aula22
        def get_object(self, queryset=None):
        # get_object_or_404(Classe, atr="isso", atr2=val2 )
        #self.object = Ficha.objects.get(pk=self.kwargs['pk'], usuario=self.request.user)
            self.object = get_object_or_404(Ficha, pk=self.kwargs['pk'], usuario=self.request.user)
            return self.object


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

    #aula 21-------------------o usuario tal só ve os cadastros dele-------------------------------
    def get_queryset(self):
    #     ##padrao self.object_list = ficha.objects.all()
    #     #registros por usuario
        self.object_list = Ficha.objects.filter(usuario=self.request.user)
        return self.object_list

