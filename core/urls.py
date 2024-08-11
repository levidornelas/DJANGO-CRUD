from .views import contato, index, criar_produto, buscar_produto, deletar_produto, atualizar_produto
from django.urls import path


urlpatterns = [
  path('', index, name='index'),
  path('contato/', contato, name='contato'),
  path('produto/', criar_produto, name='produto'),
  path('buscar_produto/', buscar_produto, name='buscar_produto'),
  path('produto/deletar/<int:produto_id>', deletar_produto, name='deletar_produto'),
  path('check_login/', criar_produto, name='check_login'),
  path('atualizar_produto/<int:produto_id>/', atualizar_produto, name='atualizar_produto'),
]