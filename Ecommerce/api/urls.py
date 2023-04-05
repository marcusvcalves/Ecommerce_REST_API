from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('listar-produtos/', views.listarProdutos, name="listar-produtos"),
    path('detalhes-produto/<str:pk>', views.detalhesProduto, name="detalhes-produto"),
    path('adicionar-produto/', views.adicionarProduto, name="adicionar-produto"),
    path('editar-produto/<str:pk>', views.editarProduto, name="editar-produto"),
    path('excluir-produto/<str:pk>', views.excluirProduto, name="excluir-produto"),

]