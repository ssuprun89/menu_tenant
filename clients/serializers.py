from rest_framework import serializers

from clients.models import (
    Client,
    ClientContact,
    ClientBrand,
    ClientsHours
)
from foods.models import SubMenu
from foods.serializers import SubMenuSerializer


class ClientContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientContact
        fields = ("address", "phone", "instagram", "phone", "facebook", "website", "email")


class ClientBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientBrand
        fields = ("color", "background_color", "categories_color", "font", "about")


class ClientHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientsHours
        fields = ("time_from", "time_by", "day_number")


class ClientSerializer(serializers.ModelSerializer):
    currency_symbol = serializers.CharField(source="get_currency_display")
    contact = ClientContactSerializer()
    brand = ClientBrandSerializer()
    hours = ClientHoursSerializer(many=True)
    sub_menu = serializers.SerializerMethodField()

    def get_sub_menu(self, obj):
        return SubMenuSerializer(instance=SubMenu.objects.all(), many=True).data

    class Meta:
        model = Client
        fields = ("name", "currency_symbol", "contact", "brand", "hours", "sub_menu")
