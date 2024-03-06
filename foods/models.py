import datetime

from django.db import models

from django_resized import ResizedImageField

from utils.models import UUIDModel


def food_directory_path(instance, filename):
    name = str(datetime.datetime.now().timestamp()).split(".")[0]
    return f"food/{name}.png"


class SubMenu(UUIDModel):
    name = models.CharField(max_length=100, verbose_name="Название")
    name_en = models.CharField(max_length=100, verbose_name="Название на англ")
    deleted = models.BooleanField(default=False, editable=False)
    number = models.IntegerField()

    def __str__(self):
        return f"[{self.name}]"

    class Meta:
        ordering = ["number"]


class Categories(UUIDModel):
    name = models.CharField(max_length=100, verbose_name="Название")
    name_en = models.CharField(max_length=100, verbose_name="Название на англ")
    deleted = models.BooleanField(default=False, editable=False)
    number = models.IntegerField()
    sub_menu = models.ForeignKey(SubMenu, on_delete=models.CASCADE, related_name="categories", null=True)

    def __str__(self):
        return f"[{self.name}]"

    class Meta:
        ordering = ["number"]


class Foods(UUIDModel):
    name = models.CharField(max_length=100, verbose_name="Название")
    name_en = models.CharField(max_length=100, verbose_name="Название на англ")
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    description_en = models.TextField(verbose_name="Описание на англ", null=True, blank=True)
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    image = ResizedImageField(verbose_name="Фото", size=[500, 500], force_format="PNG", upload_to=food_directory_path)
    categories = models.ForeignKey(
        Categories, on_delete=models.DO_NOTHING, verbose_name="Категория", related_name="foods"
    )
    weight = models.IntegerField(default=0)

    def __str__(self):
        return f"({self.categories.name}) [{self.name}]"
