from django.contrib import admin
from api.models import Servidor, Departamento, Cargo, Vinculo, Ponto, Categoria

@admin.register(Servidor)
class ServidoresAdmin(admin.ModelAdmin):
    list_display = ("siape", "nome_servidor", "username", "carga_horaria")
    list_display_links = ("nome_servidor", "username", "carga_horaria")
    list_per_page = 20
    search_fields = ("siape", "nome_servidor", "username")

@admin.register(Departamento)
class DepartamentosAdmin(admin.ModelAdmin):
    list_display = ("id_depto", "nome_depto", "sigla_depto", "latitude", "longitude")
    list_display_links = ("nome_depto", "sigla_depto")
    list_per_page = 20
    search_fields = ("id_depto", "nome_depto", "sigla_depto")

@admin.register(Cargo)
class CargosAdmin(admin.ModelAdmin):
    list_display = ("id_cargo", "nome_cargo", "categoria")
    list_display_links = ("nome_cargo",)
    list_per_page = 20
    search_fields = ("id_cago", "nome_cargo")

@admin.register(Categoria)
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ("id_categoria", "nome_categoria")
    list_display_links = ("nome_categoria",)
    list_per_page = 20
    search_fields = ("id_categoria", "nome_categoria")

@admin.register(Vinculo)
class VinculosAdmin(admin.ModelAdmin):
    list_display = ("id_vinculo", "servidor", "cargo", "departamento", "data_inicio", "data_fim")
    list_display_links = ("data_inicio", "data_fim")
    list_per_page = 20
    search_fields = ("id_vinculo", "data_inicio", "data_fim")

@admin.register(Ponto)
class PontosAdmin(admin.ModelAdmin):
    list_display = ("id_ponto", "servidor", "tipo_ponto", "data_hora", "latitude", "longitude")
    list_display_links = ("tipo_ponto",)
    list_per_page = 20
    search_fields = ("id_ponto", "data_hora", "tipo")