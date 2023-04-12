from django.urls import path
from . import views


urlpatterns = [

    path('', views.home),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<codigo>', views.edicion_curso),
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<codigo>', views.eliminar_curso)
]