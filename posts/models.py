from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
  nome = models.CharField(max_length = 100)

  def __str__(self) -> str:
    return self.nome

class Post(models.Model):
  titulo = models.CharField(max_length = 50)
  corpo = models.TextField()
  criado = models.DateTimeField(auto_now_add = True)
  editado = models.DateTimeField(auto_now = True)
  category = models.ManyToManyField(Category)

  def __str__(self) -> str:
    return self.titulo
  
  def get_absolute_url(self):
    return reverse('detail', kwargs= {'id': self.pk})

