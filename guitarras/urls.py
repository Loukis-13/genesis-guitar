from django.urls import path

from . import views


app_name = 'guitarras'
urlpatterns = [
    path('', views.GuitarraListaView.as_view(), name='index'),
    path('guitarras', views.GuitarraListaView.as_view(), name='guitarras'),
    path('guitarras/criar', views.GuitarraView.as_view(), name='criar'),
    path('guitarras/salvar', views.salvar, name='salvar'),
    path('guitarras/editar/<int:pk>', views.editar, name='editar'),
    path('guitarras/excluir/<int:pk>', views.excluir, name='excluir'),
]