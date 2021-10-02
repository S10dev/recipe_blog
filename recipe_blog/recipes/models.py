from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator


User = get_user_model()


class Recipe(models.Model):
    """Recipe structure"""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор'
        )
    title = models.CharField(max_length=40, verbose_name='Название')
    picture = models.ImageField(blank=True, null=True)
    text = models.TextField(max_length=100, blank=True, null=True)
    components = models.ManyToManyField('Component')
    tag = models.ManyToManyField('Tag')
    cooking_time = models.IntegerField(
        validators=[MinValueValidator(1, 'Value cannot be lower than 1')]
        )
    slug = models.SlugField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'recipes'


class Component(models.Model):
    """Component structure"""
    title = models.CharField(max_length=50)
    dimension = models.CharField(
        max_length=10,
        choices=[
            ('gram', 'г'),
            ('piece', 'шт'),
            ('ml', 'мл')
            ]
        )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'components'


class Component_quantity(models.Model):
    """Table linking quantity with recipe and component together"""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    compotent = models.ForeignKey(Component, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'quantity_and_recipe_linking_table'


class Tag(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tags_for_recipe'
