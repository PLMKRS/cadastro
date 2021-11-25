from django.urls import path
from .views import ListaPessoaView, PessoaCreateView, PessoaUpdateView, PessoaDeleteView, contatos
from . import views

urlpatterns = [
    path('', ListaPessoaView. as_view(), name='pessoa.index'),
    path('novo/', PessoaCreateView.as_view(), name='pessoa.novo'),
    path('<int:pk_pessoa>/editar', PessoaUpdateView.as_view(), name='pessoa.editar'),
    path('<int:pk_pessoa>/remover', PessoaDeleteView.as_view(), name='pessoa.remover'),
    path('<int:pk_pessoa>/contatos', views.contatos, name='pessoa.contatos')
]
