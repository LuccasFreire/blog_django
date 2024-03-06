from django.test import TestCase
from .models import Post
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
    Post.objects.create(
      titulo = "Post 1",
      corpo = "Enim diam vulputate ut pharetra. Facilisis mauris sit amet massa vitae tortor condimentum. Pretium viverra suspendisse potenti nullam ac. Amet est placerat in egestas. Mauris augue neque gravida in fermentum et sollicitudin. Amet facilisis magna etiam tempor orci eu lobortis."
    )
    Post.objects.create(
      titulo = "Post 2",
      corpo = "Enim diam vulputate ut pharetra. Facilisis mauris sit amet massa vitae tortor condimentum. Pretium viverra."
    )
  
  def test_homepage_retorna_response_template_correto(self):
    
    response = self.client.get('/')
    self.assertTemplateUsed(response, 'posts/index.html')
    self.assertEqual(response.status_code, HTTPStatus.OK)

  def test_homepage_retorna_lista(self):
    response = self.client.get('/')

    self.assertContains(response, "Post 1")
    self.assertContains(response, "Post 2")