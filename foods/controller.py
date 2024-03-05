from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from foods.serializers import CategoriesSerializer
from foods.models import Categories


class CategoriesViewSet(GenericViewSet, mixins.ListModelMixin):
    serializer_class = CategoriesSerializer

    def get_queryset(self):
        return Categories.objects.filter(sub_menu=self.request.query_params.get("sub_menu"))


