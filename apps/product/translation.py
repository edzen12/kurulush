from modeltranslation.translator import register, TranslationOptions
from apps.product.models import Category, Product
from apps.news.models import News
from apps.gallery.models import Gallery


@register(Category)
class CategoryTranslationOption(TranslationOptions):
    fields = ('name',)


@register(Product)
class ProductTranslationOption(TranslationOptions):
    fields = ('title', 'description',)


@register(News)
class NewsTranslationOption(TranslationOptions):
    fields = ('title', 'description',)


@register(Gallery)
class GalleryTranslationOption(TranslationOptions):
    fields = ('title',)