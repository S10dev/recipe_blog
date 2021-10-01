from django.contrib import admin
from .models import Recipe, Component, Component_quantity, Tag

# Register your models here.

admin.site.register(Recipe, )
admin.site.register(Component, )
admin.site.register(Component_quantity, )
admin.site.register(Tag, )
