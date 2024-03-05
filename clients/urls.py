from rest_framework.routers import DefaultRouter
from clients.controller import (
    ClientViewSet,
)

routers = DefaultRouter()
routers.register("", ClientViewSet, basename="client")
urlpatterns = routers.urls
