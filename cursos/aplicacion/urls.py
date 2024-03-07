from django.urls import path, include
from .views import *

urlpatterns = [
    #__________________  Menu Principal
    path('', home, name="home"),

    
    path('entregables/', entregables, name="entregables"),

    # __________________ Otras páginas
    path('acerca/', acerca, name="acerca_de_mi"),

    #___________________ Cursos
    path('cursos/', cursos, name="cursos"),
    path('curso_create/', cursoCreate, name="curso_create"),
    path('curso_update/<id_curso>/', cursoUpdate, name="curso_update"),
    path('curso_delete/<id_curso>/', cursoDelete, name="curso_delete"),

    #___________________ Profesores
    path('profesores/', profesores, name="profesores"),    
    path('prof_create/', profesorCreate, name="prof_create"),
    path('prof_update/<id_profesor>/', profesorUpdate, name="prof_update"),
    path('prof_delete/<id_profesor>/', profesorDelete, name="prof_delete"),

    #___________________ Estudiantes
    path('estudiantes/', EstudianteList.as_view(), name="estudiantes"), 
    path('estu_create/', EstudianteCreate.as_view(), name="estu_create"), 
    path('estu_update/<int:pk>/', EstudianteUpdate.as_view(), name="estu_update"), 
    path('estu_delete/<int:pk>/', EstudianteDelete.as_view(), name="estu_delete"), 

    #____________________ Busqueda
    path('buscar_cursos/', buscarCursos, name="buscar_cursos"),
    path('encontrar_cursos/', encontrarCursos, name="encontrar_cursos"),
]
