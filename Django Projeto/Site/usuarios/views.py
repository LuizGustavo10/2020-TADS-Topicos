from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import UsuarioForm
from django.urls import reverse_lazy


# Create your views here.
class UsuarioCreate(CreateView):

    template_name= "cadastros/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')
    # model = User
    # fields = ['username','email','password']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Registro de Novo Usuário"
        return context