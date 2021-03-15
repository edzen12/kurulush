from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ['name']


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ['title']
