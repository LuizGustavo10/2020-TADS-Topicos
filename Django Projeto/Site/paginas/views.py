from django.views.generic import TemplateView

class IndexView(TemplateView):
    # template_name = "paginas/index.html"
    template_name = "paginas/modelo.html"
    
class CadastrarPessoaView(TemplateView):
    template_name = 'paginas/cadastrarPessoa.html'

    
class CadastrarFuncionarioView(TemplateView):
    template_name = 'paginas/cadastrarFuncionario.html'

class CadastrarFichaView(TemplateView):
    template_name = 'paginas/ficha.html'

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'

