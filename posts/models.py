from django.db import models

# Create your models here.

class Post(models.Model):
  titulo = models.CharField(max_length = 50)
  corpo = models.TextField()
  criado = models.DateTimeField(auto_now_add = True)
  editado = models.DateTimeField(auto_now = True)

  def __str__(self) -> str:
    return self.titulo