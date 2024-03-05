from rest_framework.routers import DefaultRouter
from foods.controller import (
    CategoriesViewSet,
)

routers = DefaultRouter()
routers.register("", CategoriesViewSet, basename="categories")
urlpatterns = routers.urls
