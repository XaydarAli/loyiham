from django.contrib import admin
from .models import   Category,Product,Cart,Client
from import_export.admin import ImportExportModelAdmin


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ("id","name","description","price")
    list_display_links = ("name","price")
    search_fields = ("name","description")
    ordering = ("id",)

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ("id","name","slug","description","quantity","price")
    list_display_links = ("id","name","slug","description")
    prepopulated_fields = {'slug': ('name',)}




@admin.register(Cart)
class CartAdmin(ImportExportModelAdmin):
    list_display = ("id","product_name","quantity","price")
    list_display_links = ("product_name","price")
    search_fields = ("product_name","total")
    ordering = ("id",)


@admin.register(Client)
class ClientAdmin(ImportExportModelAdmin):
    list_display = ("id","full_name","age","profession")
    list_display_links = ("full_name","age")
    search_fields = ("full_name","profession")
    ordering = ("full_name",)
