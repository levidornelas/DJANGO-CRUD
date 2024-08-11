from django.db import models
from stdimage import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser
# Create your models here.

#Criando as Classes necessárias para o projeto:
class Base(models.Model): #Servirá como base para o restante das tabelas, e não criará mais uma no banco.
  criado = models.DateField('Data de criação', auto_now_add= True)
  modificado = models.DateField('Data da Atualização', auto_now= True)
  ativo = models.BooleanField('Ativo?', default=True)

  class Meta:
    abstract = True #Faz com que essa classe seja instanciada como abstrata, ou seja: Não criará uma tabela no banco de dados, mas sim servirá como base para que outros models a herdem.

class Produto(Base):
  nome = models.CharField('Nome', max_length=45)
  preco = models.DecimalField('Preco', max_digits=8, decimal_places=2)
  estoque = models.IntegerField('Estoque')
  imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124,124)})
  slug = models.SlugField('Slug', max_length= 100, blank=True, editable=False)

  def __str__(self) -> str:
    return self.nome

def produto_pre_save(signal, instance, sender, **kwargs):
  instance.slug = slugify(instance.nome)

signals.pre_save.connect(produto_pre_save, Produto)