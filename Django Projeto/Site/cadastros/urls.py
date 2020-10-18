from django.urls import path
from .views import FuncionarioCreate, PessoaCreate, FuncionarioUpdate, PessoaUpdate, FichaCreate, FichaUpdate
from .views import PessoaDelete, FuncionarioDelete, FichaDelete
from .views import PessoaList, FuncionarioList, FichaList

urlpatterns = [
    path('cadastrar/funcionario/', FuncionarioCreate.as_view(), name="cadastrar-funcionario"),
    path('cadastrar/pessoa/', PessoaCreate.as_view(), name="cadastrar-pessoa"),
    path('cadastrar/ficha/', FichaCreate.as_view(), name="cadastrar-ficha"),

    path('editar/funcionario/<int:pk>/', FuncionarioUpdate.as_view(), name="editar-funcionario"),
    path('editar/pessoa/<int:pk>/', PessoaUpdate.as_view(), name="editar-pessoa"),
    path('editar/ficha/<int:pk>/', FichaUpdate.as_view(), name="editar-ficha"),

    path('excluir/funcionario/<int:pk>/', FuncionarioDelete.as_view(), name="excluir-funcionario"),
    path('excluir/pessoa/<int:pk>/', PessoaDelete.as_view(), name="excluir-pessoa"),
    path('excluir/ficha/<int:pk>/', FichaDelete.as_view(), name="excluir-ficha"),

    path('listar/pessoa/', PessoaList.as_view(), name="listar-pessoa"),
    path('listar/funcionario/', FuncionarioList.as_view(), name="listar-funcionario"),
    path('listar/ficha/', FichaList.as_view(), name="listar-ficha"),

    
    
]