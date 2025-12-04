from django.urls import path

from . import views

urlpatterns = [
    path('', views.contato_view, name='contato'),
    path('api/contatos/', views.ContatoListAPIView.as_view(), name='contatos_api'),
]
