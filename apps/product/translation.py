from modeltranslation.translator import register, TranslationOptions
from .models import Category, Product


@register(Category)
class CategoryTranslationOption(TranslationOptions):
    fields = ('name',)


@register(Product)
class ActorTranslationOption(TranslationOptions):
    fields = ('title', 'description',)


