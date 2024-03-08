from .import views
from django.urls import path
urlpatterns = [
  path('', views.index, name="home"),
  path('post/<int:id>', views.post_detail, name="detail")

]