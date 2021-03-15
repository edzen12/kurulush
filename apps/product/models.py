from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(verbose_name="Категории", max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']
    
    class Meta:
        verbose_name_plural = "Категории"
        ordering = ["-id"]
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = TreeForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    title = models.CharField("Заголовок", max_length=255)
    image = models.ImageField("Фото", upload_to="uploads", blank=True, null=True)
    description = models.TextField("Описание")
    created = models.DateTimeField("Дата", auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["-id"]

