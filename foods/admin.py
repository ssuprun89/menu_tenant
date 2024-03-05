from django.contrib import admin

# Register your models here.
from foods.models import Categories, Foods, SubMenu

admin.site.register(Categories)
admin.site.register(SubMenu)
admin.site.register(Foods)
