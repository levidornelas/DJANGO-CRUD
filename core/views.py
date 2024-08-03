from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages
from .models import Produto
# Create your views here.

def index(request):
  produto = Produto.objects.all()

  context = {
    'produtos': produto
  }
  return render(request, 'index.html', context)

def contato(request):
  form = ContatoForm(request.POST or None)
  if str(request.method) == 'POST':
    if form.is_valid():
      ContatoForm.enviar_email(self=form)
      messages.success(request, 'E-mail enviado com sucesso.')
      form = ContatoForm()
    else:
      messages.error(request, 'Erro ao enviar o e-mail.')

  context = {
      'form': form
    }
  return render(request, 'contato.html', context  )

def criar_produto(request):
  if str(request.user) != 'AnonymousUser':
    form = ProdutoModelForm()  # Inicializa o form
    
    if str(request.method) == 'POST':
      form = ProdutoModelForm(request.POST, request.FILES)
      if form.is_valid():
        form.save()
        messages.success(request, 'Produto salvo com sucesso!')
        form = ProdutoModelForm()  # Reinicializa o form após salvar
        
      else:
        messages.error(request, 'Erro ao cadastrar produto.')
    context = {
      'form': form
    }
    return render(request, 'produto.html', context)
  else:
    return render(request,'check_login.html')

def buscar_produto(request):
  pesquisa = request.GET.get('consulta')

  if pesquisa:
      resultados = Produto.objects.filter(nome__icontains=pesquisa)
  else:
      messages.error(request, 'Forneça um produto.')
      resultados = []  # ou [] se quiser retornar uma lista vazia

  context = {
      'resultados': resultados,
      'pesquisa': pesquisa
  }
  return render(request, 'buscar_produto.html', context)

def deletar_produto(request, produto_id):
  if str(request.user) != 'AnonymousUser':
    produto = get_object_or_404(Produto, id = produto_id)

    if request.method == 'POST':
      produto.delete()
      return redirect('index')
    
    context = {
      'produto': produto
    }
    return render(request, 'confirmar_exclusao.html', context)
  
  else:
    return render(request, 'check_login.html')
  
def atualizar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    if str(request.user) != 'AnonymousUser':
        if request.method == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES, instance=produto)
            if form.is_valid():
                form.save()
                messages.success(request, 'Produto atualizado com sucesso!')
                return redirect('index')
            else:
                messages.error(request, 'Erro ao atualizar produto.')
        else:
            form = ProdutoModelForm(instance=produto)

        context = {
            'form': form,
            'produto': produto
        }
        return render(request, 'atualizar_produto.html', context)
    else:
        return render(request, 'check_login.html')