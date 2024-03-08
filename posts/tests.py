from django.test import TestCase
from .models import Category, Post
from http import HTTPStatus
# Create your tests here.

class PostModelTest(TestCase):
  def test_post_model_existe(self):
    posts = Post.objects.count()

    self.assertEqual(posts, 0)
  
  def test_string_rep_object(self):
    post = Post.objects.create(
          titulo="Teste titulo",
          corpo= "Teste corpo"
    )
    self.assertEqual(str(post), post.titulo)

class HomepageTest(TestCase):
  def setUp(self) -> None:
    post = Post.objects.create(
      titulo = "Post 1",
      corpo = "Enim diam vulputate ut pharetra. Facilisis mauris sit amet massa vitae tortor condimentum. Pretium viverra suspendisse potenti nullam ac. Amet est placerat in egestas. Mauris augue neque gravida in fermentum et sollicitudin. Amet facilisis magna etiam tempor orci eu lobortis.",
    )
    category = Category.objects.create(nome='comida')
    post.category.add(category)
  
  def test_homepage_retorna_response_template_correto(self):
    
    response = self.client.get('/')
    self.assertTemplateUsed(response, 'posts/index.html')
    self.assertEqual(response.status_code, HTTPStatus.OK)

  def test_homepage_retorna_lista(self):
    response = self.client.get('/')

    self.assertContains(response, "Post 1")

  def test_homepage_retorna_categoria(self):
    response = self.client.get('/')

    self.assertContains(response, "comida")

class DetailpageTest(TestCase):
    def setUp(self) -> None:
      self.post = Post.objects.create(
        titulo = "Detalhes post teste",
        corpo = " labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum"
      )
    
    def test_pagedetalhe_retorna_response_correta(self):
      response = self.client.get(self.post.get_absolute_url())
      
      self.assertEqual(response.status_code, HTTPStatus.OK)
      self.assertTemplateUsed(response, 'posts/detail.html')
    
    def test_detailpage_retorna_conteudo_correto(self):
      response = self.client.get(self.post.get_absolute_url())

      self.assertContains(response, self.post.titulo)
      self.assertContains(response, self.post.corpo)

