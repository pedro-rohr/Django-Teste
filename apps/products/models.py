from django.db import models
from categories.models import Category

# Create your models here.

class Product(models.Model):
    name = models.CharField('Nome', max_length = 50)
    description = models.TextField('Descricao', max_length = 100)
    date_fabrication = models.DateField('Data Fabricacao', auto_now = False, auto_now_add = False)
    price = models.DecimalField('Preco', max_digits = 9, decimal_places = 2, default = 0.00) # 9999999,99 = valor máximo
    is_active = models.BooleanField('Ativo', default = False)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['id']

    def __str__(self):
        return self.name