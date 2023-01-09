from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=32,unique=True)
    img = models.ImageField(upload_to='cat_images', blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Recipe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    consist = models.CharField(max_length=512)
    img =models.ImageField(upload_to='res_images', blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'