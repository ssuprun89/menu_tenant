from rest_framework import serializers

from foods.models import Categories, Foods, SubMenu


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = ["id", "name", "name_en", "description", "description_en", "price", "image", "weight"]


class CategoriesSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True)

    class Meta:
        model = Categories
        fields = ["id", "name", "name_en", "foods"]


class SubMenuSerializer(serializers.ModelSerializer):

    categories = serializers.SerializerMethodField()

    def get_categories(self, obj):
        return []

    class Meta:
        model = SubMenu
        fields = ["id", "name", "name_en", "categories", "categories"]
