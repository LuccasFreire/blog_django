from django.test import TestCase
from .models import Category, Post
from http import HTTPStatus
from django.urls import reverse
from model_bakery import baker
# Create your tests here.

class PostModelTest(TestCase):
  def test_post_model_existe(self):
    posts = Post.objects.count()

    self.assertEqual(posts, 0)
  
  def test_string_rep_object(self):
    post = baker.make(Post)

    self.assertEqual(str(post), post.titulo)
    self.assertTrue(isinstance(post, Post))
    
class HomepageTest(TestCase):
  def setUp(self) -> None:
    self.post1 = baker.make(Post)
    category = Category.objects.create(nome='comida')
    self.post1.category.add(category)
  
  def test_homepage_retorna_response_template_correto(self):
    
    response = self.client.get('/')
    self.assertTemplateUsed(response, 'posts/index.html')
    self.assertEqual(response.status_code, HTTPStatus.OK)

  def test_homepage_retorna_lista(self):
    response = self.client.get('/')

    self.assertContains(response, self.post1.titulo)

  def test_homepage_retorna_categoria(self):
    response = self.client.get(reverse('home'))

    self.assertContains(response, 'comida')

class DetailpageTest(TestCase):
    def setUp(self) -> None:
      self.post = baker.make(Post)
    
    def test_pagedetalhe_retorna_response_correta(self):
      response = self.client.get(self.post.get_absolute_url())
      
      self.assertEqual(response.status_code, HTTPStatus.OK)
      self.assertTemplateUsed(response, 'posts/detail.html')
    
    def test_detailpage_retorna_conteudo_correto(self):
      response = self.client.get(self.post.get_absolute_url())

      self.assertContains(response, self.post.titulo)
      self.assertContains(response, self.post.corpo)

